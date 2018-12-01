import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id(mean),[VarDecl(Id(size),IntType)],FloatType,[VarDecl(Id(i),IntType),VarDecl(Id(s),IntType),VarDecl(Id(x),ArrayType(1,3,IntType))],[AssignStmt(ArrayCell(Id(x),IntLiteral(3)),IntLiteral(1)),AssignStmt(ArrayCell(Id(x),IntLiteral(1)),IntLiteral(3)),AssignStmt(ArrayCell(Id(x),IntLiteral(2)),IntLiteral(5)),AssignStmt(Id(s),IntLiteral(0)),For(Id(i)IntLiteral(1),Id(size),True,[AssignStmt(Id(s),BinaryOp(+,Id(s),ArrayCell(Id(x),Id(i))))]),Return(Some(BinaryOp(/,BinaryOp(+,Id(s),FloatLiteral(0.0)),Id(size))))]),FuncDecl(Id(main),[],VoidType(),[],[CallStmt(Id(putFloat),[CallExpr(Id(mean),[IntLiteral(3)])]),Return(None)])]))
        self.assertTrue(TestAST.test(input,expect,302))
   