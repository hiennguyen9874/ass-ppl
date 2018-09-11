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


    # Visit a parse tree produced by MPParser#functionType.
    def visitFunctionType(self, ctx:MPParser.FunctionTypeContext):
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


    # Visit a parse tree produced by MPParser#prodec.
    def visitProdec(self, ctx:MPParser.ProdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstate.
    def visitCompoundstate(self, ctx:MPParser.CompoundstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#state.
    def visitState(self, ctx:MPParser.StateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignState.
    def visitAssignState(self, ctx:MPParser.AssignStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lsh.
    def visitLsh(self, ctx:MPParser.LshContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#scalarvar.
    def visitScalarvar(self, ctx:MPParser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indenxexp.
    def visitIndenxexp(self, ctx:MPParser.IndenxexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifState.
    def visitIfState(self, ctx:MPParser.IfStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileState.
    def visitWhileState(self, ctx:MPParser.WhileStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forState.
    def visitForState(self, ctx:MPParser.ForStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakState.
    def visitBreakState(self, ctx:MPParser.BreakStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#contiSate.
    def visitContiSate(self, ctx:MPParser.ContiSateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnState.
    def visitReturnState(self, ctx:MPParser.ReturnStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withState.
    def visitWithState(self, ctx:MPParser.WithStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callState.
    def visitCallState(self, ctx:MPParser.CallStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primary.
    def visitPrimary(self, ctx:MPParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressionList.
    def visitExpressionList(self, ctx:MPParser.ExpressionListContext):
        return self.visitChildren(ctx)



del MPParser