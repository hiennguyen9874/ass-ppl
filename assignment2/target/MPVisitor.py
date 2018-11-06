# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardec.
    def visitVardec(self, ctx:MPParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#onevardec.
    def visitOnevardec(self, ctx:MPParser.OnevardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraytype.
    def visitArraytype(self, ctx:MPParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitivetype.
    def visitPrimitivetype(self, ctx:MPParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#fundec.
    def visitFundec(self, ctx:MPParser.FundecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paralist.
    def visitParalist(self, ctx:MPParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paradec.
    def visitParadec(self, ctx:MPParser.ParadecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#functiontype.
    def visitFunctiontype(self, ctx:MPParser.FunctiontypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#prodec.
    def visitProdec(self, ctx:MPParser.ProdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstate.
    def visitIfstate(self, ctx:MPParser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestate.
    def visitWhilestate(self, ctx:MPParser.WhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstate.
    def visitForstate(self, ctx:MPParser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstate.
    def visitBreakstate(self, ctx:MPParser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#contiSate.
    def visitContiSate(self, ctx:MPParser.ContiSateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstate.
    def visitReturnstate(self, ctx:MPParser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstate.
    def visitCompoundstate(self, ctx:MPParser.CompoundstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstate.
    def visitCallstate(self, ctx:MPParser.CallstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstate.
    def visitAssignstate(self, ctx:MPParser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstate.
    def visitWithstate(self, ctx:MPParser.WithstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#scalarvar.
    def visitScalarvar(self, ctx:MPParser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression1.
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression2.
    def visitExpression2(self, ctx:MPParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression3.
    def visitExpression3(self, ctx:MPParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression4.
    def visitExpression4(self, ctx:MPParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression5.
    def visitExpression5(self, ctx:MPParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operands.
    def visitOperands(self, ctx:MPParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funCall.
    def visitFunCall(self, ctx:MPParser.FunCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressionList.
    def visitExpressionList(self, ctx:MPParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boollit.
    def visitBoollit(self, ctx:MPParser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexpr.
    def visitIndexexpr(self, ctx:MPParser.IndexexprContext):
        return self.visitChildren(ctx)



del MPParser