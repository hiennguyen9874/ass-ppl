from AST import *
from MPParser import MPParser
from MPVisitor import MPVisitor


class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        lstdecl = []
        for x in ctx.declaration():
            decl = self.visit(x)
            if type(decl) == type([]):
                lstdecl = lstdecl + decl
            else:
                lstdecl.append(decl)
        return Program(lstdecl)

    def visitDeclaration(self, ctx: MPParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVardec(self, ctx: MPParser.VardecContext):
        lisvardecl = []
        for x in ctx.onevardec():
            lisvardecl += self.visit(x)
        return lisvardecl

    def visitOnevardec(self, ctx: MPParser.OnevardecContext):
        varType = self.visit(ctx.functiontype())
        return [VarDecl(Id(x.getText()), varType) for x in ctx.IDENT()]

    def visitArraytype(self, ctx: MPParser.ArraytypeContext):
        str = ctx.getText()
        str0 = ctx.INTLIT(0).getText()
        str1 = ctx.INTLIT(1).getText()
        if ctx.SUBOP(0) and ctx.SUBOP(1):
            str0 = '-' + str0
            str1 = '-' + str1
        elif ctx.SUBOP(0) and str[6] == '-':
            str0 = '-' + str0
        elif ctx.SUBOP(0):
            str1 = '-' + ctx.INTLIT(1).getText()
        lower = int(str0)
        upper = int(str1)
        eleType = self.visit(ctx.primitivetype())
        return ArrayType(lower, upper, eleType)

    def visitPrimitivetype(self, ctx: MPParser.PrimitivetypeContext):
        if ctx.REAL():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.INTEGER():
            return IntType()
        elif ctx.STRING():
            return StringType()

    def visitFundec(self, ctx: MPParser.FundecContext):
        param = []
        local = []
        if ctx.paralist() and ctx.vardec():
            param = self.visit(ctx.paralist())
            local = self.visit(ctx.vardec())
        elif ctx.paralist():
            param = self.visit(ctx.paralist())
        elif ctx.vardec():
            local = self.visit(ctx.vardec())
        cpstmt = self.visit(ctx.compoundstate())
        returntype = self.visit(ctx.functiontype())
        return FuncDecl(Id(ctx.IDENT().getText()), param, local, cpstmt, returntype)

    def visitParalist(self, ctx: MPParser.ParalistContext):
        listvariable = []
        for x in ctx.paradec():
            listvariable += self.visit(x)
        return listvariable

    def visitParadec(self, ctx: MPParser.ParadecContext):
        return [VarDecl(Id(x.getText()), self.visit(ctx.functiontype())) for x in ctx.IDENT()]

    def visitFunctiontype(self, ctx: MPParser.FunctiontypeContext):
        return self.visit(ctx.getChild(0))

    def visitProdec(self, ctx: MPParser.ProdecContext):
        param = []
        local = []
        if ctx.paralist() and ctx.vardec():
            param = self.visit(ctx.paralist())
            local = self.visit(ctx.vardec())
        elif ctx.paralist() and not(ctx.vardec()):
            param = self.visit(ctx.paralist())
        elif not(ctx.paralist()) and ctx.vardec():
            local = self.visit(ctx.vardec())
        cpstmt = self.visit(ctx.compoundstate())
        return FuncDecl(Id(ctx.IDENT().getText()), param, local, cpstmt)

    def visitStatement(self, ctx: MPParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitIfstate(self, ctx: MPParser.IfstateContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.statement(0))
        if ctx.statement(1):
            elseStmt = self.visit(ctx.statement(1))
            return [If(expr, thenStmt, elseStmt)]
        else:
            return [If(expr, thenStmt)]

    def visitWhilestate(self, ctx: MPParser.WhilestateContext):
        expr = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        return [While(expr, stmt)]

    def visitForstate(self, ctx: MPParser.ForstateContext):
        id = Id(ctx.IDENT().getText())
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        loop = self.visit(ctx.statement())
        return [For(id, expr1, expr2, True, loop)] if ctx.TO() else [For(id, expr1, expr2, False, loop)]

    def visitBreakstate(self, ctx: MPParser.BreakstateContext):
        return [Break()]

    def visitContiSate(self, ctx: MPParser.ContiSateContext):
        return [Continue()]

    def visitReturnstate(self, ctx: MPParser.ReturnstateContext):
        if ctx.expression():
            expr = self.visit(ctx.expression())
            return [Return(expr)]
        else:
            return [Return()]

    def visitCompoundstate(self, ctx: MPParser.CompoundstateContext):
        lststmt = []
        for x in ctx.statement():
            lststmt += self.visit(x)
        return lststmt

    def visitCallstate(self, ctx: MPParser.CallstateContext):
        method = Id(ctx.IDENT().getText())
        param = []
        if ctx.expressionList():
            param = self.visit(ctx.expressionList())
        return [CallStmt(method, param)]

    def visitAssignstate(self, ctx: MPParser.AssignstateContext):
        lhs = [self.visit(x) for x in ctx.lhs()]
        expr = self.visit(ctx.expression())
        i = len(lhs) - 1
        listlhs = []
        listlhs.append(Assign(lhs[i], expr))
        while i > 0:
            listlhs.append(Assign(lhs[i-1], lhs[i]))
            i = i-1
        return listlhs

    def visitWithstate(self, ctx: MPParser.WithstateContext):
        decl = []
        for x in ctx.onevardec():
            decl += self.visit(x)
        stmt = self.visit(ctx.statement())      
        return [With(decl, stmt)]

    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visit(ctx.getChild(0))

    def visitScalarvar(self, ctx: MPParser.ScalarvarContext):
        return Id(ctx.IDENT().getText())

    def visitExpression(self, ctx: MPParser.ExpressionContext):
        op = ""
        if ctx.AND() and ctx.THEN():
            op = "andthen"
            left = self.visit(ctx.expression())
            right = self.visit(ctx.expression1())
            return BinaryOp(op, left, right)
        elif ctx.OR() and ctx.ELSE():
            op = "orelse"
            left = self.visit(ctx.expression())
            right = self.visit(ctx.expression1())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression1())

    def visitExpression1(self, ctx: MPParser.Expression1Context):
        op = ""
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            op = ctx.NOT_EQUAL().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.LE():
            op = ctx.LE().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.GE():
            op = ctx.GE().getText()
        else:
            return self.visit(ctx.expression2(0))
        left = self.visit(ctx.expression2(0))
        right = self.visit(ctx.expression2(1))
        return BinaryOp(op, left, right)

    def visitExpression2(self, ctx: MPParser.Expression2Context):
        op = ""
        if ctx.ADDOP():
            op = ctx.ADDOP().getText()
        elif ctx.SUBOP():
            op = ctx.SUBOP().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        else:
            return self.visit(ctx.expression3())
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)

    def visitExpression3(self, ctx: MPParser.Expression3Context):
        op = ""
        if ctx.DIVOP():
            op = ctx.DIVOP().getText()
        elif ctx.MULOP():
            op = ctx.MULOP().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        elif ctx.AND():
            op = ctx.AND().getText()
        else:
            return self.visit(ctx.expression4())
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)

    def visitExpression4(self, ctx: MPParser.Expression4Context):
        op = ""
        if ctx.SUBOP():
            op = ctx.SUBOP().getText()
        elif ctx.NOT():
            op = ctx.NOT().getText()
        else:
            return self.visit(ctx.expression5())
        body = self.visit(ctx.expression4())
        return UnaryOp(op, body)

    def visitExpression5(self, ctx: MPParser.Expression5Context):
        if ctx.LSB() and ctx.RSB():
            arr = self.visit(ctx.expression5())
            idx = self.visit(ctx.expression())
            return ArrayCell(arr, idx)
        else:
            return self.visit(ctx.operands())

    def visitOperands(self, ctx: MPParser.OperandsContext):
        if ctx.LB() and ctx.RB():
            return self.visit(ctx.expression())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.funCall():
            return self.visit(ctx.funCall())
        elif ctx.IDENT():
            return Id(ctx.IDENT().getText())

    def visitLiteral(self, ctx: MPParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))

    def visitFunCall(self, ctx: MPParser.FunCallContext):
        id = Id(ctx.IDENT().getText())
        if ctx.expressionList():
            param = self.visit(ctx.expressionList())
            return CallExpr(id, param)
        else:
            return CallExpr(id, [])

    def visitExpressionList(self, ctx: MPParser.ExpressionListContext):
        return [self.visit(x) for x in ctx.expression()]

    def visitBoollit(self, ctx: MPParser.BoollitContext):
        str1 = ctx.getText()
        if len(str1) == 4:
            return BooleanLiteral(True)
        elif len(str1) == 5:
            return BooleanLiteral(False)

    def visitIndexexpr(self, ctx: MPParser.IndexexprContext):
        arr = self.visit(ctx.expression(0))
        idx = self.visit(ctx.expression(1))
        return ArrayCell(arr, idx)