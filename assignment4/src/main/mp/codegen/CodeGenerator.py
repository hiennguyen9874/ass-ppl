'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
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
        
class SubBody(): # cho statement
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access(): # cho expression
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val): # bien co value la chi muc
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val): # hang
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

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            e = SubBody(frame, glenv)
            for x in consdecl.param:
                e = self.visit(x, e)
                glenv = e.sym

        e = SubBody(frame, glenv)
        for x in consdecl.local:
            e = self.visit(x, e)
            glenv = e.sym

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # if type(returnType) is VoidType:
        #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        ## Them global declarations vao self.env
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x,e)
            else:
                self.env.insert(0, Symbol(x.name.name, MType(list(map(lambda y: y.varType, x.param)) , x.returnType), CName(self.className)))
        ## visit toi funcdecl
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG() ## ket thuc mot class
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
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
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
            return SubBody(None, [Symbol(name, MType(list(), mtype), CName(self.className))] + subctxt.sym)
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            return SubBody(frame, [Symbol(name, MType(list(), mtype), Index(idx))] + subctxt.sym)

    # Statement
    # o.frame: Frame
    # o.sym: List[Symbol]
    def visitAssign(self, ast, o):
        #ast: CallStmt
        #o: Any
        #ast.lhs: Expr
        #ast.exp: Expr
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        rc, rt = self.visit(ast.exp, Access(frame, nenv, False, True))
        lc, lt = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if type(rt) != type(lt):
            rc += self.emit.emitI2F(frame)
        self.emit.printout(rc + lc)

    def visitIf(self, ast, o):
        #o: any
        #ast.expr: Expr
        #ast.thenStmt: list(Stmt)
        #ast.elseStmt: list(Stmt)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        expr, typ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        list(map(lambda x: self.visit(x, SubBody(frame, nenv)), ast.thenStmt))
        self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1,frame))
        if ast.elseStmt is not None:
            list(map(lambda x: self.visit(x, SubBody(frame, nenv)), ast.elseStmt))
        self.emit.printout(self.emit.emitLABEL(label2,frame))

    def visitWhile(self, ast, o):
        #o: any
        #ast.sl: list(Stmt)
        #ast.exp: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        frame.enterLoop()
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(label1,frame))
        expr, typ = self.visit(ast.exp, Access(frame, nenv, False, True))
        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(label2, frame))
        list(map(lambda x: self.visit(x, SubBody(frame, nenv)), ast.sl))
        self.emit.printout(self.emit.emitGOTO(label1, frame))
        self.emit.printout(self.emit.emitLABEL(label2,frame))
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
        frame.enterLoop()
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        
        pass
    
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
        self.emit.printout(self.emit.emitGOTO(1, frame))

    def visitWith(self, ast, o):
        #o:any
        #ast.decl: list(VarDecl)
        #ast.stmt: list(Stmt)
        pass

    def visitCallStmt(self, ast, o):
        #o: Any
        #ast.method: Id
        #ast.param: list(Expr)

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())

        # for x in ast.param:
        #     str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
        #     in_ = (in_[0] + str1, in_[1].append(typ1))

        for i in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[i], Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1].append(typ1))

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    # Expression
    #frame: Frame
    #sym: List[Symbol]
    #isLeft: Boolean
    #isFirst: Boolean
    def visitBinaryOp(self, ast, o):
        #o: any
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #ast.left:Expr
        #ast.right:Expr

        ctxt = o
        frame = ctxt.frame
        leftOprandstr, typL = self.visit(ast.left, o)
        rightOperandstr, typR = self.visit(ast.right, o)

        if type(typL) == type(typR):
            if type(typL) is BoolType:
                if ast.op == 'and':
                    return leftOprandstr + rightOperandstr + self.emit.emitANDOP(frame), BoolType()                    
            if type(typL) is IntType:
                if ast.op in ['+', '-']:
                    return leftOprandstr + rightOperandstr + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
                elif ast.op == '*':
                    return leftOprandstr + rightOperandstr + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                elif ast.op == 'div':
                    return leftOprandstr + rightOperandstr + self.emit.emitDIV(frame), IntType()
                elif ast.op == 'mod':
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
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP(ast.op, FloatType(), frame), BoolType()
                elif ast.op == '<>':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('!=', FloatType(), frame), BoolType()
                elif ast.op == '=':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('==', FloatType(), frame), BoolType()
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
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP(ast.op, FloatType(), frame), BoolType()
                elif ast.op == '<>':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('!=', FloatType(), frame), BoolType()
                elif ast.op == '=':
                    return leftOprandstr + rightOperandstr + self.emit.emitREOP('==', FloatType(), frame), BoolType()

    def visitUnaryOp(self, ast, o):
        #o:any
        #ast.op: string
        #ast.body: Exprs
        
        ctxt = o
        frame = ctxt.frame
        body, typ = self.visit(ast.body, o)
        if ast.op == 'not' and type(typ) is BoolType:
            return self.emit.emitNOT(BoolType(), frame), BoolType()
        elif ast.op == '-' and type(typ) is IntType:
            return self.emit.emitNEGOP(IntType(), frame), IntType()
        elif ast.op == '-' and type(typ) is FloatType:
            return self.emit.emitNEGOP(FloatType(), frame), FloatType()

    def visitCallExpr(self, ast, o):
        #o:any
        #ast.method: Id
        #ast.param: list(Expr)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype
        
        in_ = ("", list())

        for i in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[i], Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1].append(typ1))
        
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), sym.mtype.rettype

    # LHS
    def visitId(self, ast, o):
        #o:any
        #ast.name: string
        sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype.rettype, o.frame), sym.mtype.rettype
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype.rettype, sym.value.value, o.frame), sym.mtype.rettype
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype.rettype, o.frame), sym.mtype.rettype
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype.rettype, sym.value.value, o.frame), sym.mtype.rettype

    def visitArrayCell(self, ast, o):
        #o:any
        #ast.arr:Expr
        #ast.idx:Expr
        pass

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
        return self.emit.emitPUSHCONST("true" if ast.value is True else "false", IntType(), frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        #o:any
        #ast.value:string
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
