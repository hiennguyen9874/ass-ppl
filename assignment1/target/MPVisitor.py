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


    # Visit a parse tree produced by MPParser#varDec.
    def visitVarDec(self, ctx:MPParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#onevarDec.
    def visitOnevarDec(self, ctx:MPParser.OnevarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#functionType.
    def visitFunctionType(self, ctx:MPParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayType.
    def visitArrayType(self, ctx:MPParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitiveType.
    def visitPrimitiveType(self, ctx:MPParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funDec.
    def visitFunDec(self, ctx:MPParser.FunDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paraList.
    def visitParaList(self, ctx:MPParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paradec.
    def visitParadec(self, ctx:MPParser.ParadecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proDec.
    def visitProDec(self, ctx:MPParser.ProDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
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


    # Visit a parse tree produced by MPParser#compoundState.
    def visitCompoundState(self, ctx:MPParser.CompoundStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MPParser.ExpressionStatementContext):
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


    # Visit a parse tree produced by MPParser#funCall.
    def visitFunCall(self, ctx:MPParser.FunCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressionList.
    def visitExpressionList(self, ctx:MPParser.ExpressionListContext):
        return self.visitChildren(ctx)



del MPParser