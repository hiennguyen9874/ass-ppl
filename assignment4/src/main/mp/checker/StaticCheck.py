
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [Symbol("getInt", MType([], IntType())),
                   Symbol("putInt", MType([IntType()], VoidType())),
                   Symbol("putIntLn", MType([IntType()], VoidType())),
                   Symbol("getFloat", MType([], FloatType())),
                   Symbol("putFloat", MType([FloatType()], VoidType())),
                   Symbol("putFloatLn", MType([FloatType()], VoidType())),
                   Symbol("putBool", MType([BoolType()], VoidType())),
                   Symbol("putBoolLn", MType([BoolType()], VoidType())),
                   Symbol("putString", MType([StringType()], VoidType())),
                   Symbol("putStringLn", MType([StringType()], VoidType())),
                   Symbol("putLn", MType([], VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def convertToSymbol(self, decl):
        # Ham chuyen tu mot Declare -> mot symbol
        if type(decl) == VarDecl:
            return Symbol(decl.variable.name, decl.varType)
        elif type(decl) == FuncDecl:
            return Symbol(decl.name.name, MType([i.varType for i in decl.param], decl.returnType))

    def toListSym(self, listDecl, listSym, kind, listGlobal=None, list_func=None):
        # Ham chuyen mot list Declare -> list Symbol
        # list_func: danh sach cac function/procedure trong Program
        for x in listDecl:
            sym = self.convertToSymbol(x)
            res = self.lookup(sym.name.lower(), listSym, lambda y: y.name.lower())
            res1 = None
            if listGlobal:
                res1 = self.lookup(sym.name.lower(), listGlobal, lambda y: y.name.lower())
            if res is None and res1 is None:
                listSym.insert(0, sym)
                if not list_func is None and type(sym.mtype) is MType:
                    list_func.insert(0, sym)
            elif type(sym.mtype) is MType:
                if type(sym.mtype.rettype) is VoidType:
                    raise Redeclared(Procedure(), sym.name)
                else:
                    raise Redeclared(Function(), sym.name)
            elif kind == Parameter:
                raise Redeclared(Parameter(), sym.name)
            else:
                raise Redeclared(Variable(), sym.name)

    def checkNoEntryPoint(self, listSym):
        # Ham kiem tra xem co ham main trong chuong trinh hay khong?
        # String.lower() -> chuyen chu hoa ve chu thuong
        isMain = False
        sym = Symbol("main", MType([], VoidType()))
        for x in listSym:
            if x.name.lower() == sym.name.lower() and x.mtype.partype == [] and type(x.mtype.rettype) == VoidType:
                isMain = True
                break
        if isMain == False:
            raise NoEntryPoint()

    def checkType(self, left, right):
        # ham kiem tra kieu co the gan
        # chi co the gan int cho float
        if type(left) == type(right):
            if type(left) is ArrayType:
                if type(left.eleType) == type(right.eleType) and left.lower == right.lower and left.upper == right.upper:
                    return True
                else:
                    return False
            else:
                return True
        elif type(left) == FloatType and type(right) == IntType:
            return True
        else:
            return False

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        # decl:list(Decl)
        list_func = []
        list_global = []
        self.toListSym(ast.decl, list_global, None, c, list_func)
        self.checkNoEntryPoint(list_func)
        for x in ast.decl:
            self.visit(x, (list_global + c, list_func))
        sym = Symbol("main", MType([], VoidType()))
        for x in list_func:
            if not x.name.lower() == sym.name.lower() or not x.mtype.partype == sym.mtype.partype or not type(x.mtype.rettype) == type(sym.mtype.rettype):
                if type(x.mtype.rettype) is VoidType:
                    raise Unreachable(Procedure(), x.name)
                else:
                    raise Unreachable(Function(), x.name)
        return []

    # Decl
    def visitVarDecl(self, ast, c):
        # variable: Id
        # varType: Type
        return

    def visitFuncDecl(self, ast, c):
        # name: Id
        # param: list(VarDecl)
        # returnType: Type => VoidType for Procedure
        # local: list(VarDecl)
        # body: list(Stmt)
        lst = []
        self.toListSym(ast.param, lst, Parameter)
        self.toListSym(ast.local, lst, None)
        isReturn = False
        isBreak = False
        for x in ast.body:
            [isReturn, isBreak] = self.visit(x, (lst + c[0], c[1], False, ast, isReturn, isBreak))
        if not isReturn and not type(ast.returnType) is VoidType:
            raise FunctionNotReturn(ast.name.name)

    # in c
    # c[0]: list -> Environment
    # c[1]: list -> Danh sach ham chua duoc goi
    # c[2]: boolean -> True neu stmt nay nam trong mot vong lap
    # c[3]: AST -> Kieu tra ve cua function/procedure
    # c[4]: boolean -> True neu da goi return
    # c[5]: boolean -> True neu ham da goi break/continue
    # return:
    # ret[0] -> True neu da goi ham return
    # ret[1] -> True neu da goi ham break/continue
    def visitAssign(self, ast, c):
        # lhs: Expr
        # exp: Expr
        lhs = self.visit(ast.lhs, (c[0], c[1], c[3]))
        exp = self.visit(ast.exp, (c[0], c[1], c[3]))
        if type(lhs) is StringType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if not type(exp) == type(lhs) and not (type(lhs) is FloatType and type(exp) is IntType):
            raise TypeMismatchInStatement(ast)
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [False, False]

    def visitIf(self, ast, c):
        # expr: Expr
        # thenStmt: list(Stmt)
        # elseStmt: list(Stmt)
        expr = self.visit(ast.expr, (c[0], c[1], c[3]))
        # visit Stmt for thenStmt
        isReturn = False
        isBreak = False
        for x in ast.thenStmt:
            [isReturn, isBreak] = self.visit(x, (c[0], c[1], c[2], c[3], isReturn, isBreak))
        # visit stmt for elseStmt
        isReturn1 = False
        isBreak1 = False
        for x in ast.elseStmt:
            [isReturn1, isBreak1] = self.visit(x, (c[0], c[1], c[2], c[3], isReturn1, isBreak1))
        if not type(expr) is BoolType:
            raise TypeMismatchInStatement(ast)
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [isReturn and isReturn1, (isBreak and isBreak1) or (isBreak and isReturn1) or (isReturn and isBreak1)]

    def visitWhile(self, ast, c):
        # sl: list(Stmt)
        # exp: Expr
        exp = self.visit(ast.exp, (c[0], c[1], c[3]))
        isReturn = False
        isBreak = False
        for x in ast.sl:
            [isReturn, isBreak] = self.visit(x, (c[0], c[1], True, c[3], isReturn, isBreak))
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [False, False]

    def visitFor(self, ast, c):
        # id: Id
        # expr1,expr2: Expr
        # loop: list(Stmt)
        # up: Boolean #True => increase; False => decrease
        iD = self.visit(ast.id, (c[0], c[1], c[3]))
        expr1 = self.visit(ast.expr1, (c[0], c[1], c[3]))
        expr2 = self.visit(ast.expr2, (c[0], c[1], c[3]))
        isReturn = False
        isBreak = False
        for x in ast.loop:
            [isReturn, isBreak] = self.visit(x, (c[0], c[1], True, c[3], isReturn, isBreak))
        if type(iD) is not IntType or type(expr1) is not IntType or type(expr2) is not IntType:
            raise TypeMismatchInStatement(ast)
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [False, False]

    def visitBreak(self, ast, c):
        if c[2] is False:
            raise BreakNotInLoop()
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [False, True]

    def visitContinue(self, ast, c):
        if c[2] is False:
            raise ContinueNotInLoop()
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [False, True]

    def visitReturn(self, ast, c):
        # expr: Expr
        if ast.expr:
            expr = self.visit(ast.expr, (c[0], c[1], c[3]))
            if type(c[3].returnType) is VoidType or not self.checkType(c[3].returnType, expr):
                raise TypeMismatchInStatement(ast)
            if c[4] or c[5]:
                raise UnreachableStatement(ast)
            return [True, False]
        else:
            if not type(c[3].returnType) is VoidType:
                raise TypeMismatchInStatement(ast)
            if c[4] or c[5]:
                raise UnreachableStatement(ast)
            return [True, False]

    def visitWith(self, ast, c):
        # decl: list(VarDecl)
        # stmt: list(Stmt)
        lst = []
        self.toListSym(ast.decl, lst, None)
        isReturn = False
        isBreak = False
        for x in ast.stmt:
            [isReturn, isBreak] = self.visit(x, (lst + c[0], c[1], c[2], c[3], isReturn, isBreak))
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        return [isReturn, isBreak]

    def visitCallStmt(self, ast, c):
        # method: Id
        # param: list(Expr)
        at = [self.visit(x, (c[0], c[1], c[3])) for x in ast.param]

        res = self.lookup(ast.method.name.lower(),c[0], lambda x: x.name.lower())
        if res is None or type(res.mtype) is not MType or type(res.mtype.rettype) is not VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        else:
            for i in range(len(res.mtype.partype)):
                if not self.checkType(res.mtype.partype[i], at[i]):
                    raise TypeMismatchInStatement(ast)
        if c[4] or c[5]:
            raise UnreachableStatement(ast)
        if not ast.method.name.lower() == c[3].name.name.lower():
            name = ast.method.name.lower()
            for x in c[1]:
                if name == x.name.lower():
                    c[1].remove(x)
        return [False, False]

    # Expression
    # c[0]: list -> Environment
    # c[1]: list -> Danh sach ham chua duoc goi
    # c[2]: AST -> Kieu tra ve cua function/procedure
    # Return: type -> Kieu tra ve cua Expression
    def visitBinaryOp(self, ast, c):
        # op: string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        # left: Expr
        # right: Expr
        left = self.visit(ast.left, (c[0], c[1], c[2]))
        right = self.visit(ast.right, (c[0], c[1], c[2]))
        if type(left) == type(right):
            if type(left) is BoolType and ast.op.lower() in ['and', 'andthen', 'or', 'orelse']:
                return BoolType()
            elif type(left) is IntType:
                if ast.op.lower() in ['+', '-', '*', 'div', 'mod']:
                    return IntType()
                elif ast.op in ['<', '<=', '>', '>=', '<>', '=']:
                    return BoolType()
                elif ast.op == '/':
                    return FloatType()
            elif type(left) is FloatType:
                if ast.op in ['+', '-', '*', '/']:
                    return FloatType()
                elif ast.op in ['=', '<>', '<', '<=', '>', '>=']:
                    return BoolType()
            raise TypeMismatchInExpression(ast)
        else:
            lst = [IntType, FloatType]
            if type(left) in lst and type(right) in lst:
                if ast.op in ['+', '-', '*', '/']:
                    return FloatType()
                elif ast.op in ['=', '<>', '<', '<=', '>', '>=']:
                    return BoolType()
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        # op: string
        # body: Expr
        expr = self.visit(ast.body, (c[0], c[1], c[2]))
        if ast.op == 'not' and type(expr) is BoolType:
            return BoolType()
        elif ast.op == '-' and type(expr) is IntType:
            return IntType()
        elif ast.op == '-' and type(expr) is FloatType:
            return FloatType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        # method: Id
        # param: list(Expr)
        at = [self.visit(x, (c[0], c[1], c[2])) for x in ast.param]
        res = self.lookup(ast.method.name.lower(),
                          c[0], lambda x: x.name.lower())
        if res is None or not type(res.mtype) is MType or type(res.mtype.rettype) is VoidType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(res.mtype.partype)):
                if not self.checkType(res.mtype.partype[i], at[i]):
                    raise TypeMismatchInExpression(ast)
        if not ast.method.name.lower() == c[2].name.name.lower():
            for x in c[1]:
                if ast.method.name.lower() == x.name.lower():
                    c[1].remove(x)
        return res.mtype.rettype

    # LHS
    def visitId(self, ast, c):
        # name: string
        res = self.lookup(ast.name.lower(), c[0], lambda x: x.name.lower())
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        elif type(res.mtype) is MType:
            raise Undeclared(Identifier(), ast.name)
        else:
            return res.mtype

    def visitArrayCell(self, ast, c):
        # arr: Expr
        # idx: Expr
        arr = self.visit(ast.arr, (c[0], c[1], c[2]))
        idx = self.visit(ast.idx, (c[0], c[1], c[2]))
        if not type(arr) is ArrayType or not type(idx) is IntType:
            raise TypeMismatchInExpression(ast)
        return arr.eleType

    def visitIntLiteral(self, ast, c):
        # value: int
        return IntType()

    def visitFloatLiteral(self, ast, c):
        # value: float
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        # value: boolean
        return BoolType()

    def visitStringLiteral(self, ast, c):
        # value: string
        return StringType()
