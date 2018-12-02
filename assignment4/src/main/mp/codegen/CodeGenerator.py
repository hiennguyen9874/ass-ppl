'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *   Nguyễn Xuân Hiến - 1652192
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType(list(), VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
        
    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class MyClass():
    def __init__(self, sym, isGlobalArray, lstDeclArray):
        #sym: List[Symbol]
        #isGlobalArray: Boolean
        #lstDeclArray: List[VarDecl]

        self.sym = sym
        self.isGlobalArray = isGlobalArray
        self.lstDeclArray = lstDeclArray

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def genMETHOD(self, consdecl, o:MyClass, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        
        isGlobalArray = o.isGlobalArray
        lstDeclArray = o.lstDeclArray

        if isGlobalArray:
            # Constructor cho khai bao bien global la array
            returnType = VoidType()
            methodName = "<clinit>"
            intype = list()
            mtype = MType(intype, returnType)
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True, frame))
            frame.enterScope(True)
            for x in lstDeclArray:
                lexeme = self.className + "." + x.variable.name
                self.emit.printout(self.emit.emitINITARRAY(lexeme, x.varType, frame))
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            # if frame.getStackSize() != 0:
            #     print(methodName)
            frame.exitScope()
        else:
            isInit = consdecl.returnType is None
            isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
            returnType = VoidType() if isInit else consdecl.returnType
            methodName = "<init>" if isInit else consdecl.name.name
            intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))
            mtype = MType(intype, returnType)
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
            frame.enterScope(True)
            glenv = o.sym
            # Generate code for parameter declarations
            if isInit:
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
            elif isMain:
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
                glenv.insert(0, Symbol("args", ArrayPointerType(StringType()), Index(idx)))
            else:
                # Sinh ma cho parameter declarations
                e = SubBody(frame, glenv)
                for x in consdecl.param:
                    e = self.visit(x, e)
                    glenv = e.sym
            if not isInit:
                # Sinh ma cho local declarations
                e = SubBody(frame, glenv)
                for x in consdecl.local:
                    e = self.visit(x, e)
                    glenv = e.sym
                    if type(x.varType) is ArrayType:
                        idx = glenv[0].value.value
                        self.emit.printout(self.emit.emitINITARRAY(idx, x.varType, frame))
            e = SubBody(frame, glenv)
            body = consdecl.body
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            # Generate code for statements
            if isInit:
                self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            list(map(lambda x: self.visit(x, e), body))
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            # if frame.getStackSize() != 0:
            #     print(methodName)
            frame.exitScope()

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        ## List cac bien array trong global
        lstArray = list()

        ## Them global declarations vao self.env
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x,e)
                self.env = e.sym
                if type(x.varType) is ArrayType:
                    lstArray.append(x)
            else:
                self.env.insert(0, Symbol(x.name.name, MType(list(map(lambda y: y.varType, x.param)) , x.returnType), CName(self.className)))
        
        ## visit toi funcdecl
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x, e)

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), MyClass(c, False, list()), Frame("<init>", VoidType))

        # Constructor cho array
        if len(lstArray) > 0:
            self.genMETHOD(FuncDecl(Id("<clinit>"), list(), list(), list(), None), MyClass(c, True, lstArray), Frame("<clinit>", VoidType))

        self.emit.emitEPILOG()
        return c

    # Declaration
    def visitFuncDecl(self, ast, o):
        #o: SubBody
        #ast.name: Id
        #ast.param: list(VarDecl)
        #ast.returnType: Type => VoidType for Procedure
        #ast.local: list(VarDecl)
        #ast.body: list(Stmt)

        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, MyClass(subctxt.sym, False, list()), frame)
        # return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
        return SubBody(None, subctxt.sym)
    
    def visitVarDecl(self, ast, o):
        #ast: VarDecl
        #o: SubBody
        #ast.variable: Id
        #ast.varType: Type

        subctxt = o
        frame = subctxt.frame
        mtype = ast.varType
        name = ast.variable.name

        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, False, ""))
            return SubBody(None, [Symbol(name, mtype, CName(self.className))] + subctxt.sym)
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            return SubBody(frame, [Symbol(name, mtype, Index(idx))] + subctxt.sym)

    # Statement
    # o.frame: Frame
    # o.sym: List[Symbol]
    def visitAssign(self, ast, o):
        #o: Any
        #ast.lhs: Expr
        #ast.exp: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        if type(ast.lhs) is ArrayCell:
            # gan mot gia tri cho mot index expression.
            lc, lt = self.visit(ast.lhs, Access(frame, nenv, True, True))
            self.emit.printout(lc)
            rc, rt = self.visit(ast.exp, Access(frame, nenv, False, True))
            self.emit.printout(rc)
            if type(lt) != type(rt):
                self.emit.printout(self.emit.emitI2F(frame))
            self.emit.printout(self.emit.emitASTORE(lt, frame))          
        else:
            # gan mot gia tri cho mot bien
            rc, rt = self.visit(ast.exp, Access(frame, nenv, False, True))
            lc, lt = self.visit(ast.lhs, Access(frame, nenv, True, True))
            if type(rt) is IntType and type(lt) is FloatType:
                rc += self.emit.emitI2F(frame)
            self.emit.printout(rc + lc)

    def visitIf(self, ast, o):
        #o:any
        #ast.expr:Expr
        #ast.thenStmt:list(Stmt)
        #ast.elseStmt:list(Stmt)
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # Kiem tra dieu kien
        expr, _ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        # label sai
        label1 = frame.getNewLabel()
        # label dung
        label2 = None
        if len(ast.elseStmt) != 0:
            label2 = frame.getNewLabel()
        # Neu dieu kien sai thi nhay toi label1
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        list(map(lambda x: self.visit(x, o), ast.thenStmt))
        if len(ast.elseStmt) != 0:
            self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1,frame))
        if len(ast.elseStmt) != 0:
            list(map(lambda x: self.visit(x, o), ast.elseStmt))
            self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitWhile(self, ast, o):
        #o: any
        #ast.sl: list(Stmt)
        #ast.exp: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        frame.enterLoop()

        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(labelContinue,frame))
        expr, _ = self.visit(ast.exp, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))
        list(map(lambda x: self.visit(x, o), ast.sl))

        self.emit.printout(self.emit.emitGOTO(labelContinue, frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak,frame))

        frame.exitLoop()
    
    def visitFor(self, ast, o):
        #o:any
        #ast.id: Id
        #ast.expr1,expr2: Expr
        #ast.loop: list(Stmt)
        #ast.up: Boolean #True => increase; False => decrease

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        label1 = frame.getNewLabel()

        frame.enterLoop()
        accessT = Access(frame, nenv, True, True)
        accessF = Access(frame, nenv, False, True)
        # Gan gia tri expr1 cho id
        expr1, _ = self.visit(ast.expr1, accessF)
        id1, _ = self.visit(ast.id, accessT)
        self.emit.printout(expr1)
        self.emit.printout(id1)
        # In ra label 1
        self.emit.printout(self.emit.emitLABEL(label1, frame))

        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()

        if ast.up is True:
            id1, _ = self.visit(ast.id, accessF)
            self.emit.printout(id1)
            expr2, _ = self.visit(ast.expr2, accessF)
            self.emit.printout(expr2)
            self.emit.printout(self.emit.emitIFICMPGT(labelBreak, frame))
        else:
            id1, _ = self.visit(ast.id, accessF)
            self.emit.printout(id1)
            expr2, _ = self.visit(ast.expr2, accessF)
            self.emit.printout(expr2)
            self.emit.printout(self.emit.emitIFICMPLT(labelBreak, frame))

        list(map(lambda x: self.visit(x, o), ast.loop))
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))

        if ast.up is True:
            # i + 1 dat len stack
            expr, _ = self.visit(BinaryOp('+', ast.id, IntLiteral(1)), accessF)
            # Gan gia tri tren stack vao Id
            id2, _ = self.visit(ast.id, accessT)
            self.emit.printout(expr)
            self.emit.printout(id2)
        else:
            # i - 1 dat len stack
            expr, _ = self.visit(BinaryOp('-',ast.id,IntLiteral(1)), accessF)
            # Gan gia tri tren stack vao id
            id2, _ = self.visit(ast.id, accessT)
            self.emit.printout(expr)
            self.emit.printout(id2)
        # quay lai label1
        self.emit.printout(self.emit.emitGOTO(label1, frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()
    
    def visitBreak(self, ast, o):
        #o:any

        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        #o:any
        
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitReturn(self, ast, o):
        #o:any
        #ast.expr: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        if ast.expr is not None:
            str1, typ1 = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(frame.returnType) is FloatType:
                str1 += self.emit.emitI2F(frame)
            self.emit.printout(str1)
        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))

    def visitWith(self, ast, o):
        #o:any
        #ast.decl: list(VarDecl)
        #ast.stmt: list(Stmt)

        ctxt = o
        frame = ctxt.frame
        glenv = ctxt.sym

        frame.enterScope(False)
        e = SubBody(frame, glenv)
        for x in ast.decl:
            e = self.visit(x, e)
            glenv = e.sym
        e = SubBody(frame, glenv)
        body = ast.stmt
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, e), body))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitCallStmt(self, ast, o):
        #o: Any
        #ast.method: Id
        #ast.param: list(Expr)

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype

        access = Access(frame, nenv, False, True)
        for i in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[i], access)
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(frame)
            self.emit.printout(str1)
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    # Expression
    #o.frame: Frame
    #o.sym: List[Symbol]
    #o.isLeft: Boolean
    #o.isFirst: Boolean
    def visitBinaryOp(self, ast, o):
        #o: any
        #ast.op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #ast.left:Expr
        #ast.right:Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        leftOprandstr, typL = self.visit(ast.left, Access(frame, nenv, False, True))
        rightOperandstr, typR = self.visit(ast.right, Access(frame, nenv, False, True))

        if type(typL) == type(typR):
            if type(typL) is BoolType:
                if ast.op.lower() == 'and':
                    return leftOprandstr + rightOperandstr + self.emit.emitANDOP(frame), BoolType()   
                elif ast.op.lower() == 'or':
                    return leftOprandstr + rightOperandstr + self.emit.emitOROP(frame), BoolType()
                elif ast.op.lower() == 'andthen':
                    # right, typR1 = self.visit(BooleanLiteral(False), o)
                    # lst = leftOprandstr + right + self.emit.emitREOP('==', IntType(), frame)
                    lst = list()
                    label1 = frame.getNewLabel()
                    label2 = frame.getNewLabel()
                    lst.append(leftOprandstr)
                    lst.append(self.emit.emitIFFALSE(label1, frame))
                    lst.append(rightOperandstr)
                    lst.append(self.emit.emitIFFALSE(label1, frame))
                    lst.append(self.emit.emitPUSHICONST("true", frame))
                    lst.append(self.emit.emitGOTO(label2,frame))
                    lst.append(self.emit.emitLABEL(label1,frame))
                    lst.append(self.emit.emitPUSHICONST("false", frame))
                    lst.append(self.emit.emitLABEL(label2,frame))
                    frame.pop()
                    return ''.join(lst), BoolType()
                elif ast.op.lower() == 'orelse':
                    # right, typR1 = self.visit(BooleanLiteral(True), o)
                    # lst = leftOprandstr + right + self.emit.emitREOP('==', IntType(), frame)
                    lst = list()
                    label1 = frame.getNewLabel()
                    label2 = frame.getNewLabel()
                    lst.append(leftOprandstr)
                    lst.append(self.emit.emitIFTRUE(label1, frame))
                    lst.append(rightOperandstr)
                    lst.append(self.emit.emitIFTRUE(label1, frame))
                    lst.append(self.emit.emitPUSHICONST("false", frame))
                    lst.append(self.emit.emitGOTO(label2,frame))
                    lst.append(self.emit.emitLABEL(label1,frame))
                    lst.append(self.emit.emitPUSHICONST("true", frame))
                    lst.append(self.emit.emitLABEL(label2,frame))
                    frame.pop()
                    return ''.join(lst), BoolType()
            elif type(typL) is IntType:
                if ast.op in ['+', '-']:
                    return leftOprandstr + rightOperandstr + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
                elif ast.op == '*':
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                elif ast.op.lower() == 'div':
                    return leftOprandstr + rightOperandstr + self.emit.emitDIV(frame), IntType()
                elif ast.op.lower() == 'mod':
                    return leftOprandstr + rightOperandstr + self.emit.emitMOD(frame), IntType()
                elif ast.op in ['<', '<=', '>', '>=']:
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP(ast.op, IntType(), frame), BoolType()
                elif ast.op == '<>':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('!=', IntType(), frame), BoolType()
                elif ast.op == '=':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('==', IntType(), frame), BoolType()
                elif ast.op == '/':
                    leftOprandstr += self.emit.emitI2F(frame)
                    rightOperandstr += self.emit.emitI2F(frame)
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
            elif type(typL) is FloatType:
                if ast.op in ['+', '-']:
                    return leftOprandstr + rightOperandstr + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op == '*':
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op == '/':
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['<', '<=', '>', '>=']:
                    return self.emit.emitFREOP(ast.op, leftOprandstr, rightOperandstr, frame), BoolType()
                elif ast.op == '<>':
                    return self.emit.emitFREOP('!=', leftOprandstr, rightOperandstr, frame), BoolType()
                elif ast.op == '=':
                    return self.emit.emitFREOP('==', leftOprandstr, rightOperandstr, frame), BoolType()
        else:
            if ast.op in ['+', '-']:
                if type(typL) is FloatType and type(typR) is IntType:
                    return leftOprandstr + rightOperandstr + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif type(typL) is IntType and type(typR) is FloatType:
                    return leftOprandstr + self.emit.emitI2F(frame) + rightOperandstr + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
            elif ast.op == '*':
                if type(typL) is FloatType and type(typR) is IntType:
                    return leftOprandstr + rightOperandstr + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif type(typL) is IntType and type(typR) is FloatType:
                    return leftOprandstr + self.emit.emitI2F(frame) + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
            else:
                if type(typL) is IntType: 
                    leftOprandstr += self.emit.emitI2F(frame)
                if type(typR) is IntType: 
                    rightOperandstr += self.emit.emitI2F(frame)
                if ast.op == '/':
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['<', '<=', '>', '>=']:
                    return self.emit.emitFREOP(ast.op, leftOprandstr, rightOperandstr, frame), BoolType()
                elif ast.op == '<>':
                    return self.emit.emitFREOP('!=', leftOprandstr, rightOperandstr, frame), BoolType()
                elif ast.op == '=':
                    return self.emit.emitFREOP('==', leftOprandstr, rightOperandstr, frame), BoolType()

    def visitUnaryOp(self, ast, o):
        #o:any
        #ast.op: string
        #ast.body: Exprs
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        body, typ = self.visit(ast.body, Access(frame, nenv, False, True))
        if ast.op.lower() == 'not' and type(typ) is BoolType:
            return body + self.emit.emitNOT(IntType(), frame), BoolType()
        elif ast.op == '-' and type(typ) is IntType:
            return body + self.emit.emitNEGOP(IntType(), frame), IntType()
        elif ast.op == '-' and type(typ) is FloatType:
            return body + self.emit.emitNEGOP(FloatType(), frame), FloatType()

    def visitCallExpr(self, ast, o):
        #o:any
        #ast.method: Id
        #ast.param: list(Expr)
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        
        lst = list()
        access = Access(frame, nenv, False, True)
        for i in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[i], access)
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(frame)
            lst.append(str1)
        lst.append(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
        return ''.join(lst), sym.mtype.rettype

    # LHS
    def visitId(self, ast, o):
        #o:any
        #ast.name: string
        
        sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
        
        typ = sym.mtype

        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitWRITEVAR(sym.name, typ, sym.value.value, o.frame), typ
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitREADVAR(sym.name, typ, sym.value.value, o.frame), typ

    def visitArrayCell(self, ast, o):
        #o:any
        #ast.arr:Expr
        #ast.idx:Expr
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        lst = list()
        arr, typeArr = self.visit(ast.arr, Access(frame, nenv, False, True))
        idx, typeIdx = self.visit(ast.idx, Access(frame, nenv, False, True))
        
        typ = typeArr.eleType
        lst.append(arr)
        lst.append(idx)
        lst.append(self.emit.emitPUSHICONST(typeArr.lower, frame))
        lst.append(self.emit.emitADDOP('-', IntType(), frame))
        if not o.isLeft:
            lst.append(self.emit.emitALOAD(typ, frame))
        return ''.join(lst), typ

    # Literal
    def visitIntLiteral(self, ast, o):
        #o: Any
        #ast.value:int

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, IntType(), frame), IntType()
    
    def visitFloatLiteral(self, ast, o):
        #o:any
        #ast.value:float
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        #o:any
        #ast.value:boolean
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value).lower(), IntType(), frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        #o:any
        #ast.value:string
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
