
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

    def toListSym(self, listDecl, listSym, kind, listGlobal = None, list_func=None):
        # Ham chuyen mot list Declare -> list Symbol
        # list_func: danh sach cac function/procedure trong Program
        if listGlobal is None:
            for x in listDecl:
                sym = self.convertToSymbol(x)
                res = self.lookup(sym.name.lower(), listSym, lambda y: y.name.lower())
                if res is None:
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
        else:
            for x in listDecl:
                sym = self.convertToSymbol(x)
                res = self.lookup(sym.name.lower(), listSym, lambda y: y.name.lower())
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
        self.checkNoEntryPoint(list_global)
        lst = [x for x in ast.decl]
        for x in ast.decl:
            list_func = self.visit(x, (list_global + c, list_func))
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
        # variable:Id
        #varType: Type
        return c[1]

    def visitFuncDecl(self, ast, c):
        #name: Id
        #param: list(VarDecl)
        # returnType: Type => VoidType for Procedure
        # local:list(VarDecl)
        #body: list(Stmt)
        lst = []
        self.toListSym(ast.param, lst, Parameter)
        self.toListSym(ast.local, lst, None)
        func_list = c[1]
        isReturn = False
        isBreak = False
        for x in ast.body:
            ret = self.visit(x, (lst + c[0], func_list, False, ast, isReturn, lst, isBreak))
            func_list = ret[0]
            isReturn = ret[1]
            isBreak = ret[2]
        if not isReturn and not type(ast.returnType) is VoidType:
            raise FunctionNotReturn(ast.name.name)
        return func_list

    # in c
    # c[0] -> Environment
    # c[1] -> Danh sach ham chua duoc goi
    # c[2] -> True neu stmt nay nam trong mot vong lap
    # c[3] -> Kieu tra ve cua function/procedure
    # c[4] -> True neu da goi return
    # c[5] -> local environment
    # c[6] -> True neu ham da goi break/continue
    ## return:
    # ret[0] -> Danh sach ham chua duoc goi
    # ret[1] -> True neu da goi ham return
    # ret[2] -> True neu da goi ham break/continue
    def visitAssign(self, ast, c):
        # lhs:Expr
        # exp:Expr  
        ret = self.visit(ast.lhs, (c[0], c[1], c[3]))
        lhs = ret[0]
        func_list = ret[1]
        if type(lhs) == StringType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) == ArrayType:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.exp, (c[0], func_list, c[3]))
        exp = ret[0]
        func_list = ret[1]
        if type(exp) == type(lhs):
            pass
        elif type(lhs) == FloatType and type(exp) == IntType:
            pass
        else:
            raise TypeMismatchInStatement(ast)
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [func_list, c[4], c[6]]

    def visitIf(self, ast, c):
        # expr:Expr
        # thenStmt:list(Stmt)
        # elseStmt:list(Stmt)
        ret = self.visit(ast.expr, (c[0], c[1], c[3]))
        expr = ret[0]
        func_list = ret[1]
        if not type(expr) is BoolType:
            raise TypeMismatchInStatement(ast)
        # visit Stmt for thenStmt
        isReturn = False
        isBreak = False
        for x in ast.thenStmt:
            ret = self.visit(x, (c[0], func_list, c[2], c[3], isReturn, c[5], isBreak))
            func_list = ret[0]
            isReturn = ret[1]
            isBreak = ret[2]
        # visit stmt for elseStmt
        isReturn1 = False
        isBreak1 = False
        for x in ast.elseStmt:
            ret = self.visit(x, (c[0], func_list, c[2], c[3], isReturn1, c[5], isBreak1))
            func_list = ret[0]
            isReturn1 = ret[1]
            isBreak1 = ret[2]
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [func_list, isReturn and isReturn1, isBreak and isBreak1]

    def visitWhile(self, ast, c):
        # sl:list(Stmt)
        #exp: Expr
        ret = self.visit(ast.exp, (c[0], c[1], c[3]))
        exp = ret[0]
        func_list = ret[1]
        if not type(exp) is BoolType:
            raise TypeMismatchInStatement(ast)
        isBreak = c[6]
        for x in ast.sl:
            ret = self.visit(x, (c[0], func_list, True, c[3], False, c[5], isBreak))
            func_list = ret[0]
            isBreak = ret[2]
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [func_list, c[4], False]

    def visitFor(self, ast, c):
        # id:Id
        # expr1,expr2:Expr
        # loop:list(Stmt)
        # up:Boolean #True => increase; False => decrease
        ret = self.visit(ast.id, (c[5], c[1], c[3]))
        id = ret[0]
        func_list = ret[1]
        if not type(id) is IntType:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr1, (c[0], func_list, c[3]))
        expr1 = ret[0]
        func_list = ret[1]
        if not type(expr1) is IntType:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr2, (c[0], func_list, c[3]))
        expr2 = ret[0]
        func_list = ret[1]
        if not type(expr2) is IntType:
            raise TypeMismatchInStatement(ast)
        isReturn = c[4]
        isBreak = c[6]
        for x in ast.loop:
            ret = self.visit(x, (c[0], func_list, True, c[3], False, c[5], isBreak))
            func_list = ret[0]
            isBreak = ret[2]
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [func_list, isReturn, False]

    def visitBreak(self, ast, c):
        if c[2] is False:
            raise BreakNotInLoop()
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [c[1], c[4], True]

    def visitContinue(self, ast, c):
        if c[2] is False:
            raise ContinueNotInLoop()
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [c[1], c[4], True]

    def visitReturn(self, ast, c):
        # expr:Expr
        if ast.expr:
            ret = self.visit(ast.expr, (c[0], c[1], c[3]))
            expr = ret[0]
            func_list = ret[1]
            if type(c[3].returnType) is VoidType:
                raise TypeMismatchInStatement(ast)
            if not self.checkType(c[3].returnType, expr):
                raise TypeMismatchInStatement(ast)
            if c[4] or c[6]:
                raise UnreachableStatement(ast)
            return [func_list, True, c[6]]
        else:
            if not type(c[3].returnType) is VoidType:
                raise TypeMismatchInStatement(ast)
            if c[4] or c[6]:
                raise UnreachableStatement(ast)
            return [c[1], True, c[6]]

    def visitWith(self, ast, c):
        # decl:list(VarDecl)
        # stmt:list(Stmt)
        lst = []
        self.toListSym(ast.decl, lst, None)
        func_list = c[1]
        isReturn = c[4]
        isBreak = c[6]
        for x in ast.stmt:
            ret = self.visit(x, (lst + c[0], func_list, c[2], c[3], isReturn, lst, isBreak))
            func_list = ret[0]
            isReturn = ret[1]
            isBreak = ret[2]
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        return [func_list, isReturn, isBreak]

    def visitCallStmt(self, ast, c):
        # method:Id
        # param:list(Expr)
        at = []
        func_list = c[1]
        for x in ast.param:
            ret = self.visit(x, (c[0], func_list, c[3]))
            at.append(ret[0])
            func_list = ret[1]
        res = self.lookup(ast.method.name.lower(), c[0], lambda x: x.name.lower())
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        else:
            for i in range(len(res.mtype.partype)):
                if not self.checkType(res.mtype.partype[i], at[i]):
                    raise TypeMismatchInStatement(ast)
        if c[4] or c[6]:
            raise UnreachableStatement(ast)
        func_list_ret = []
        if not ast.method.name.lower() == c[3].name.name.lower():
            for x in func_list:
                if not ast.method.name.lower() == x.name.lower():
                    func_list_ret.append(x)
            return [func_list_ret, c[4], c[6]]
        return [func_list, c[4], c[6]]

    # Expression
    # In c
    # c[0] -> Environment
    # c[1] -> Danh sach ham chua duoc goi
    # Return
    # ret[0] -> Kieu tra ve cua Expression
    # ret[1] -> Danh sach ham chua duoc goi
    def visitBinaryOp(self, ast, c):
        # op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        # left:Expr
        # right:Expr
        ret = self.visit(ast.left, (c[0], c[1], c[2]))
        left = ret[0]
        func_list = ret[1]
        ret = self.visit(ast.right, (c[0], func_list, c[2]))
        right = ret[0]
        func_list = ret[1]

        if type(left) == type(right):
            if type(left) is BoolType and ast.op in ['and', 'andthen', 'or', 'orelse']:
                return [BoolType(), func_list]
            elif type(left) is IntType:
                if ast.op in ['+', '-', '*', 'div', 'mod']:
                    return [IntType(), func_list]
                elif ast.op in ['<', '<=', '>', '>=', '<>', '=']:
                    return [BoolType(), func_list]
                elif ast.op == '/':
                    return [FloatType(), func_list]
            elif type(left) is FloatType:
                if ast.op in ['+', '-', '*', '/']:
                    return [FloatType(), func_list]
                elif ast.op in ['=', '<>', '<', '<=', '>', '>=']:
                    return [BoolType(), func_list]
            else:
                raise TypeMismatchInExpression(ast)
        else:
            if type(left) is IntType and type(right) is FloatType:
                return [FloatType(), func_list]
            elif type(left) is FloatType and type(right) is IntType:
                return [FloatType(), func_list]
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        # op:string
        # body:Expr
        ret = self.visit(ast.body, (c[0], c[1], c[2]))
        expr = ret[0]
        func_list = ret[1]
        if ast.op == '-' and type(expr) is BoolType:
            return [BoolType(), func_list]
        elif ast.op == '-' and type(expr) is IntType:
            return [IntType(). func_list]
        elif ast.op == '-' and type(expr) is FloatType:
            return [FloatType(), func_list]
        else:
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        # method:Id
        # param:list(Expr)
        at = []
        func_list = c[1]
        for x in ast.param:
            ret = self.visit(x, (c[0], func_list, c[2]))
            at.append(ret[0])
            func_list = ret[1]
        res = self.lookup(ast.method.name.lower(), c[0], lambda x: x.name.lower())
        if res is None or not type(res.mtype) is MType or type(res.mtype.rettype) is VoidType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(res.mtype.partype)):
                if not self.checkType(res.mtype.partype[i], at[i]):
                    raise TypeMismatchInExpression(ast)
        func_list_ret = []
        if not ast.method.name.lower() == c[2].name.name.lower():
            for x in func_list:
                if not ast.method.name.lower() == x.name.lower():
                    func_list_ret.append(x)
            return [res.mtype.rettype, func_list_ret]
        else:
            return [res.mtype.rettype, func_list]

    # LHS
    def visitId(self, ast, c):
        # name:string
        res = self.lookup(ast.name.lower(), c[0], lambda x: x.name.lower())
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        elif type(res.mtype) is MType:
            raise Undeclared(Identifier(), ast.name)
        else:
            return [res.mtype, c[1]]

    def visitArrayCell(self, ast, c):
        # arr:Expr
        # idx:Expr
        ret = self.visit(ast.arr, (c[0], c[1], c[2]))
        arr = ret[0]
        func_list = ret[1]
        if not type(arr) is ArrayType:
            raise TypeMismatchInExpression(ast)
        ret = self.visit(ast.idx, (c[0], func_list, c[2]))
        idx = ret[0]
        func_list = ret[1]
        if not type(idx) is IntType:
            raise TypeMismatchInExpression(ast)
        return [arr.eleType, func_list]

    def visitIntLiteral(self, ast, c):
        # value:int
        return [IntType(), c[1]]

    def visitFloatLiteral(self, ast, c):
        # value:float
        return [FloatType(), c[1]]

    def visitBooleanLiteral(self, ast, c):
        # value:boolean
        return [BoolType(), c[1]]

    def visitStringLiteral(self, ast, c):
        # value:string
        return [StringType(), c[1]]
