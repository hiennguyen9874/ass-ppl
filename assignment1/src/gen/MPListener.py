# Generated from D:/Nam3/PPL/Ass1/assignment1/src/main/mp/parser\MP.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete listener for a parse tree produced by MPParser.
class MPListener(ParseTreeListener):

    # Enter a parse tree produced by MPParser#program.
    def enterProgram(self, ctx:MPParser.ProgramContext):
        pass

    # Exit a parse tree produced by MPParser#program.
    def exitProgram(self, ctx:MPParser.ProgramContext):
        pass


    # Enter a parse tree produced by MPParser#declaration.
    def enterDeclaration(self, ctx:MPParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MPParser#declaration.
    def exitDeclaration(self, ctx:MPParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MPParser#varDec.
    def enterVarDec(self, ctx:MPParser.VarDecContext):
        pass

    # Exit a parse tree produced by MPParser#varDec.
    def exitVarDec(self, ctx:MPParser.VarDecContext):
        pass


    # Enter a parse tree produced by MPParser#onevarDec.
    def enterOnevarDec(self, ctx:MPParser.OnevarDecContext):
        pass

    # Exit a parse tree produced by MPParser#onevarDec.
    def exitOnevarDec(self, ctx:MPParser.OnevarDecContext):
        pass


    # Enter a parse tree produced by MPParser#functionType.
    def enterFunctionType(self, ctx:MPParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by MPParser#functionType.
    def exitFunctionType(self, ctx:MPParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by MPParser#arrayType.
    def enterArrayType(self, ctx:MPParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MPParser#arrayType.
    def exitArrayType(self, ctx:MPParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MPParser#primitiveType.
    def enterPrimitiveType(self, ctx:MPParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by MPParser#primitiveType.
    def exitPrimitiveType(self, ctx:MPParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by MPParser#funDec.
    def enterFunDec(self, ctx:MPParser.FunDecContext):
        pass

    # Exit a parse tree produced by MPParser#funDec.
    def exitFunDec(self, ctx:MPParser.FunDecContext):
        pass


    # Enter a parse tree produced by MPParser#paraList.
    def enterParaList(self, ctx:MPParser.ParaListContext):
        pass

    # Exit a parse tree produced by MPParser#paraList.
    def exitParaList(self, ctx:MPParser.ParaListContext):
        pass


    # Enter a parse tree produced by MPParser#paradec.
    def enterParadec(self, ctx:MPParser.ParadecContext):
        pass

    # Exit a parse tree produced by MPParser#paradec.
    def exitParadec(self, ctx:MPParser.ParadecContext):
        pass


    # Enter a parse tree produced by MPParser#proDec.
    def enterProDec(self, ctx:MPParser.ProDecContext):
        pass

    # Exit a parse tree produced by MPParser#proDec.
    def exitProDec(self, ctx:MPParser.ProDecContext):
        pass


    # Enter a parse tree produced by MPParser#statement.
    def enterStatement(self, ctx:MPParser.StatementContext):
        pass

    # Exit a parse tree produced by MPParser#statement.
    def exitStatement(self, ctx:MPParser.StatementContext):
        pass


    # Enter a parse tree produced by MPParser#lsh.
    def enterLsh(self, ctx:MPParser.LshContext):
        pass

    # Exit a parse tree produced by MPParser#lsh.
    def exitLsh(self, ctx:MPParser.LshContext):
        pass


    # Enter a parse tree produced by MPParser#scalarvar.
    def enterScalarvar(self, ctx:MPParser.ScalarvarContext):
        pass

    # Exit a parse tree produced by MPParser#scalarvar.
    def exitScalarvar(self, ctx:MPParser.ScalarvarContext):
        pass


    # Enter a parse tree produced by MPParser#ifState.
    def enterIfState(self, ctx:MPParser.IfStateContext):
        pass

    # Exit a parse tree produced by MPParser#ifState.
    def exitIfState(self, ctx:MPParser.IfStateContext):
        pass


    # Enter a parse tree produced by MPParser#whileState.
    def enterWhileState(self, ctx:MPParser.WhileStateContext):
        pass

    # Exit a parse tree produced by MPParser#whileState.
    def exitWhileState(self, ctx:MPParser.WhileStateContext):
        pass


    # Enter a parse tree produced by MPParser#forState.
    def enterForState(self, ctx:MPParser.ForStateContext):
        pass

    # Exit a parse tree produced by MPParser#forState.
    def exitForState(self, ctx:MPParser.ForStateContext):
        pass


    # Enter a parse tree produced by MPParser#breakState.
    def enterBreakState(self, ctx:MPParser.BreakStateContext):
        pass

    # Exit a parse tree produced by MPParser#breakState.
    def exitBreakState(self, ctx:MPParser.BreakStateContext):
        pass


    # Enter a parse tree produced by MPParser#contiSate.
    def enterContiSate(self, ctx:MPParser.ContiSateContext):
        pass

    # Exit a parse tree produced by MPParser#contiSate.
    def exitContiSate(self, ctx:MPParser.ContiSateContext):
        pass


    # Enter a parse tree produced by MPParser#returnState.
    def enterReturnState(self, ctx:MPParser.ReturnStateContext):
        pass

    # Exit a parse tree produced by MPParser#returnState.
    def exitReturnState(self, ctx:MPParser.ReturnStateContext):
        pass


    # Enter a parse tree produced by MPParser#withState.
    def enterWithState(self, ctx:MPParser.WithStateContext):
        pass

    # Exit a parse tree produced by MPParser#withState.
    def exitWithState(self, ctx:MPParser.WithStateContext):
        pass


    # Enter a parse tree produced by MPParser#callState.
    def enterCallState(self, ctx:MPParser.CallStateContext):
        pass

    # Exit a parse tree produced by MPParser#callState.
    def exitCallState(self, ctx:MPParser.CallStateContext):
        pass


    # Enter a parse tree produced by MPParser#compoundState.
    def enterCompoundState(self, ctx:MPParser.CompoundStateContext):
        pass

    # Exit a parse tree produced by MPParser#compoundState.
    def exitCompoundState(self, ctx:MPParser.CompoundStateContext):
        pass


    # Enter a parse tree produced by MPParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MPParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MPParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MPParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MPParser#assignState.
    def enterAssignState(self, ctx:MPParser.AssignStateContext):
        pass

    # Exit a parse tree produced by MPParser#assignState.
    def exitAssignState(self, ctx:MPParser.AssignStateContext):
        pass


    # Enter a parse tree produced by MPParser#expression.
    def enterExpression(self, ctx:MPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MPParser#expression.
    def exitExpression(self, ctx:MPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MPParser#indenxexp.
    def enterIndenxexp(self, ctx:MPParser.IndenxexpContext):
        pass

    # Exit a parse tree produced by MPParser#indenxexp.
    def exitIndenxexp(self, ctx:MPParser.IndenxexpContext):
        pass


    # Enter a parse tree produced by MPParser#operands.
    def enterOperands(self, ctx:MPParser.OperandsContext):
        pass

    # Exit a parse tree produced by MPParser#operands.
    def exitOperands(self, ctx:MPParser.OperandsContext):
        pass


    # Enter a parse tree produced by MPParser#literal.
    def enterLiteral(self, ctx:MPParser.LiteralContext):
        pass

    # Exit a parse tree produced by MPParser#literal.
    def exitLiteral(self, ctx:MPParser.LiteralContext):
        pass


    # Enter a parse tree produced by MPParser#funCall.
    def enterFunCall(self, ctx:MPParser.FunCallContext):
        pass

    # Exit a parse tree produced by MPParser#funCall.
    def exitFunCall(self, ctx:MPParser.FunCallContext):
        pass


    # Enter a parse tree produced by MPParser#expressionList.
    def enterExpressionList(self, ctx:MPParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MPParser#expressionList.
    def exitExpressionList(self, ctx:MPParser.ExpressionListContext):
        pass


