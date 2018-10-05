import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test_simple_function(self):
        input = """function foo ():REAL; begin
            getIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("getIntLn"),[IntLiteral(4)])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_function_with_param(self):
        input = """function foo(a,b:real):REAL; begin
            getIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[],[CallStmt(Id("getIntLn"),[IntLiteral(4)])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_function_without_parameter(self):
        input = """
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test_vardecl_integer(self):
        input = """
        var a, b, c: integer;
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_assign_id_intlit(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := 2;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("x"),IntLiteral(2))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    
    def test_assign_id_float(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := 2.1e2;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("x"),FloatLiteral(210.0))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_assign_id_string(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := "abc";
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("x"),StringLiteral("abc"))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_assign_id_array(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            x := a[1];
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("x"),ArrayCell(Id("a"),IntLiteral(1)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    
    def test_assign_id_boolean(self):
        input = """
        function foo ():INTEGER; 
        begin
            x := true;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("x"),BooleanLiteral(True))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test_vardecl_array(self):
        input = """
        Var a: Array [1 .. 5] of INTEGER;
        """
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,5,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_vardecl_string(self):
        input = """
        Var a,b,c:string;
        """
        expect = str(Program([VarDecl(Id("a"),StringType()),VarDecl(Id("b"),StringType()),VarDecl(Id("c"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    
    def test_if_statement(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then x := y := .5e3;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("=",Id("a"),IntLiteral(9)),[Assign(Id("y"),FloatLiteral(500.0)),Assign(Id("x"),Id("y"))],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_nested_if_statement(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then 
                if a<6 then
                    x := y := .5e3;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("=",Id("a"),IntLiteral(9)),[If(BinaryOp("<",Id("a"),IntLiteral(6)),[Assign(Id("y"),FloatLiteral(500.0)),Assign(Id("x"),Id("y"))],[])],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_if_else_statement(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then 
                x := y := .5e3;
            else x:=5;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("=",Id("a"),IntLiteral(9)),[Assign(Id("y"),FloatLiteral(500.0)),Assign(Id("x"),Id("y"))],[Assign(Id("x"),IntLiteral(5))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_nested_if_else_statement(self):
        input = """
        function foo ():BOOLEAN; 
        begin
            if a = 9 then 
                if a<6 then
                    x := y := .5e3;
                else x:=2;
            else
                x:=4;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("=",Id("a"),IntLiteral(9)),[If(BinaryOp("<",Id("a"),IntLiteral(6)),[Assign(Id("y"),FloatLiteral(500.0)),Assign(Id("x"),Id("y"))],[Assign(Id("x"),IntLiteral(2))])],[Assign(Id("x"),IntLiteral(4))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test_while_statement(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            a := 0;
            while (a < 10) AND (x <> 0.) do
            begin 
                a := a + 1;
            end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("a"),IntLiteral(0)),While(BinaryOp("AND",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("<>",Id("x"),FloatLiteral(0.0))),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test_while_statement_with_if(self):
        input = """
        function foo ():BOOLEAN; 
        var x,y: real; a,b,c: INTEGER;
        begin
            a := 0;
            while (a < 10) AND (x <> 0.) do
                if a = 2 then
                a := a + 1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[Assign(Id("a"),IntLiteral(0)),While(BinaryOp("AND",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("<>",Id("x"),FloatLiteral(0.0))),[If(BinaryOp("=",Id("a"),IntLiteral(2)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],[])])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_for_statement(self):
        input = """
        procedure foo(); 
        begin
            for i := 1 to 10 do
                a := a+1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[For(Id("i"),IntLiteral(1),IntLiteral(10),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_for_statement_with_if(self):
        input = """
        procedure foo(); 
        begin
            sum := 0;
            for count := 1 to 100 do
            begin
                sum := sum + count;
                if sum = 38 then return;
            end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("sum"),IntLiteral(0)),For(Id("count"),IntLiteral(1),IntLiteral(100),True,[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("count"))),If(BinaryOp("=",Id("sum"),IntLiteral(38)),[Return(None)],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_statement_return_expr(self):
        input = """
                Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                    Count := 0;
                    For i:=1 to N do
                    If ( A[i] = X ) then
                        Count := Count + 1;
                    return Count;
                End
                """
        expect = str(Program([FuncDecl(Id("CountX"),[VarDecl(Id("A"),ArrayType(0,100,IntType())),VarDecl(Id("N"),IntType()),VarDecl(Id("X"),IntType())],[VarDecl(Id("i"),IntType()),VarDecl(Id("Count"),IntType())],[Assign(Id("Count"),IntLiteral(0)),For(Id("i"),IntLiteral(1),Id("N"),True,[If(BinaryOp("=",ArrayCell(Id("A"),Id("i")),Id("X")),[Assign(Id("Count"),BinaryOp("+",Id("Count"),IntLiteral(1)))],[])]),Return(Id("Count"))],IntType())]))

        self.assertTrue(TestAST.test(input,expect,320))

    def test_statement_idx_expr_in_if(self):
        input = """
                Procedure replace (A:array[0 .. 100] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                    For i:=0 to N do
                    If(A[i] = x) then { x ==> y }
                        A[i] := y;
                    return;
                End
                """
        expect = str(Program([FuncDecl(Id("replace"),[VarDecl(Id("A"),ArrayType(0,100,IntType())),VarDecl(Id("N"),IntType()),VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())],[VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(0),Id("N"),True,[If(BinaryOp("=",ArrayCell(Id("A"),Id("i")),Id("x")),[Assign(ArrayCell(Id("A"),Id("i")),Id("y"))],[])]),Return(None)],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,321))