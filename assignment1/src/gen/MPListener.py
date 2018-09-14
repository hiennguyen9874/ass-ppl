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


    # Enter a parse tree produced by MPParser#vardec.
    def enterVardec(self, ctx:MPParser.VardecContext):
        pass

    # Exit a parse tree produced by MPParser#vardec.
    def exitVardec(self, ctx:MPParser.VardecContext):
        pass


    # Enter a parse tree produced by MPParser#onevardec.
    def enterOnevardec(self, ctx:MPParser.OnevardecContext):
        pass

    # Exit a parse tree produced by MPParser#onevardec.
    def exitOnevardec(self, ctx:MPParser.OnevardecContext):
        pass


    # Enter a parse tree produced by MPParser#arraytype.
    def enterArraytype(self, ctx:MPParser.ArraytypeContext):
        pass

    # Exit a parse tree produced by MPParser#arraytype.
    def exitArraytype(self, ctx:MPParser.ArraytypeContext):
        pass


    # Enter a parse tree produced by MPParser#primitivetype.
    def enterPrimitivetype(self, ctx:MPParser.PrimitivetypeContext):
        pass

    # Exit a parse tree produced by MPParser#primitivetype.
    def exitPrimitivetype(self, ctx:MPParser.PrimitivetypeContext):
        pass


    # Enter a parse tree produced by MPParser#fundec.
    def enterFundec(self, ctx:MPParser.FundecContext):
        pass

    # Exit a parse tree produced by MPParser#fundec.
    def exitFundec(self, ctx:MPParser.FundecContext):
        pass


    # Enter a parse tree produced by MPParser#paralist.
    def enterParalist(self, ctx:MPParser.ParalistContext):
        pass

    # Exit a parse tree produced by MPParser#paralist.
    def exitParalist(self, ctx:MPParser.ParalistContext):
        pass


    # Enter a parse tree produced by MPParser#paradec.
    def enterParadec(self, ctx:MPParser.ParadecContext):
        pass

    # Exit a parse tree produced by MPParser#paradec.
    def exitParadec(self, ctx:MPParser.ParadecContext):
        pass


    # Enter a parse tree produced by MPParser#functiontype.
    def enterFunctiontype(self, ctx:MPParser.FunctiontypeContext):
        pass

    # Exit a parse tree produced by MPParser#functiontype.
    def exitFunctiontype(self, ctx:MPParser.FunctiontypeContext):
        pass


    # Enter a parse tree produced by MPParser#prodec.
    def enterProdec(self, ctx:MPParser.ProdecContext):
        pass

    # Exit a parse tree produced by MPParser#prodec.
    def exitProdec(self, ctx:MPParser.ProdecContext):
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


    # Enter a parse tree produced by MPParser#indexexpr.
    def enterIndexexpr(self, ctx:MPParser.IndexexprContext):
        pass

    # Exit a parse tree produced by MPParser#indexexpr.
    def exitIndexexpr(self, ctx:MPParser.IndexexprContext):
        pass


    # Enter a parse tree produced by MPParser#scalarvar.
    def enterScalarvar(self, ctx:MPParser.ScalarvarContext):
        pass

    # Exit a parse tree produced by MPParser#scalarvar.
    def exitScalarvar(self, ctx:MPParser.ScalarvarContext):
        pass


    # Enter a parse tree produced by MPParser#ifstate.
    def enterIfstate(self, ctx:MPParser.IfstateContext):
        pass

    # Exit a parse tree produced by MPParser#ifstate.
    def exitIfstate(self, ctx:MPParser.IfstateContext):
        pass


    # Enter a parse tree produced by MPParser#whilestate.
    def enterWhilestate(self, ctx:MPParser.WhilestateContext):
        pass

    # Exit a parse tree produced by MPParser#whilestate.
    def exitWhilestate(self, ctx:MPParser.WhilestateContext):
        pass


    # Enter a parse tree produced by MPParser#forstate.
    def enterForstate(self, ctx:MPParser.ForstateContext):
        pass

    # Exit a parse tree produced by MPParser#forstate.
    def exitForstate(self, ctx:MPParser.ForstateContext):
        pass


    # Enter a parse tree produced by MPParser#breakstate.
    def enterBreakstate(self, ctx:MPParser.BreakstateContext):
        pass

    # Exit a parse tree produced by MPParser#breakstate.
    def exitBreakstate(self, ctx:MPParser.BreakstateContext):
        pass


    # Enter a parse tree produced by MPParser#contiSate.
    def enterContiSate(self, ctx:MPParser.ContiSateContext):
        pass

    # Exit a parse tree produced by MPParser#contiSate.
    def exitContiSate(self, ctx:MPParser.ContiSateContext):
        pass


    # Enter a parse tree produced by MPParser#returnstate.
    def enterReturnstate(self, ctx:MPParser.ReturnstateContext):
        pass

    # Exit a parse tree produced by MPParser#returnstate.
    def exitReturnstate(self, ctx:MPParser.ReturnstateContext):
        pass


    # Enter a parse tree produced by MPParser#withstate.
    def enterWithstate(self, ctx:MPParser.WithstateContext):
        pass

    # Exit a parse tree produced by MPParser#withstate.
    def exitWithstate(self, ctx:MPParser.WithstateContext):
        pass


    # Enter a parse tree produced by MPParser#callstate.
    def enterCallstate(self, ctx:MPParser.CallstateContext):
        pass

    # Exit a parse tree produced by MPParser#callstate.
    def exitCallstate(self, ctx:MPParser.CallstateContext):
        pass


    # Enter a parse tree produced by MPParser#compoundstate.
    def enterCompoundstate(self, ctx:MPParser.CompoundstateContext):
        pass

    # Exit a parse tree produced by MPParser#compoundstate.
    def exitCompoundstate(self, ctx:MPParser.CompoundstateContext):
        pass


    # Enter a parse tree produced by MPParser#assignstate.
    def enterAssignstate(self, ctx:MPParser.AssignstateContext):
        pass

    # Exit a parse tree produced by MPParser#assignstate.
    def exitAssignstate(self, ctx:MPParser.AssignstateContext):
        pass


    # Enter a parse tree produced by MPParser#expression.
    def enterExpression(self, ctx:MPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MPParser#expression.
    def exitExpression(self, ctx:MPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MPParser#expression1.
    def enterExpression1(self, ctx:MPParser.Expression1Context):
        pass

    # Exit a parse tree produced by MPParser#expression1.
    def exitExpression1(self, ctx:MPParser.Expression1Context):
        pass


    # Enter a parse tree produced by MPParser#expression2.
    def enterExpression2(self, ctx:MPParser.Expression2Context):
        pass

    # Exit a parse tree produced by MPParser#expression2.
    def exitExpression2(self, ctx:MPParser.Expression2Context):
        pass


    # Enter a parse tree produced by MPParser#expression3.
    def enterExpression3(self, ctx:MPParser.Expression3Context):
        pass

    # Exit a parse tree produced by MPParser#expression3.
    def exitExpression3(self, ctx:MPParser.Expression3Context):
        pass


    # Enter a parse tree produced by MPParser#expression4.
    def enterExpression4(self, ctx:MPParser.Expression4Context):
        pass

    # Exit a parse tree produced by MPParser#expression4.
    def exitExpression4(self, ctx:MPParser.Expression4Context):
        pass


    # Enter a parse tree produced by MPParser#expression5.
    def enterExpression5(self, ctx:MPParser.Expression5Context):
        pass

    # Exit a parse tree produced by MPParser#expression5.
    def exitExpression5(self, ctx:MPParser.Expression5Context):
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


    # Enter a parse tree produced by MPParser#boolit.
    def enterBoolit(self, ctx:MPParser.BoolitContext):
        pass

    # Exit a parse tree produced by MPParser#boolit.
    def exitBoolit(self, ctx:MPParser.BoolitContext):
        pass


