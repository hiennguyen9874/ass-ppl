import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_all(self):
        input = """
        var i:integer;
        procedure foo(a, b: integer; c: real);
        var ret: array [1 .. 2] of integer;
            i:integer;
        begin
            foo1(1,2,3.2);
            if (True and then False) then foo(1,2,3);
            else return;
            for i:=1 to 10 do
            begin
                i := i + 1;
            end
        end
        procedure foo1(a,b: integer; c:real);
        begin
            return;
        end
        function f():integer;
        begin
            foo1(1,2,3.2);
            if (i > 1) then 
            begin 
                foo(1,2,3); 
                return;
            end
            else return 1;
        end
        procedure main();
        var
            main: integer;
            foo: integer;
            ret: array [1 .. 2] of integer;
        begin
            main := f();
            putIntLn(main);
            with
                i:integer;
                main:integer;
                f:integer;
            do begin
                putLn();
                main := f := i := 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            end
            putIntLn(main);
            return;
        end
        var g:integer;
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main(); 
        begin
            putIntLn();
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putIntLn"),[])])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_undeclared_function(self):
        input = """
        function foo():integer;
        begin
            return 1;
        end
        procedure main();
        begin
            foo();
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_undeclared_procedure(self):
        input = """
        procedure foo();
        begin
            return;
        end
        procedure main();
        begin
            return;
        end
        """
        expect = "Unreachable Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_global1(self):
        input = """
        function f(i:integer ; j:real):integer;
        var a:integer;
            b:boolean;
            c:string;
            d:integer;
        begin
            with a,b:real; c:array [1 .. 2] of real; do
                begin
                    a := c[d] +b;
                    putIntLn(a);
                    return a;
                end
        end
        procedure main();
        var i: integer;
        begin
            i := f(1,2.3);
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_global2(self):
        input = """
        procedure Main32( c: real);
            var Main32: real;      
            begin 
                    if true then Main32(1);   
            end
        procedure Main();
        begin 
        end
        """
        expect = "Undeclared Procedure: Main32"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_function_not_return(self):
        input = """
        function foo():integer;
        var a:integer;
        begin
            while 1>0 do
            begin
                return 1;
            end
            a:=a+1;
        end
        procedure Main();
        var a:integer;
        begin 
            a:= foo();
        end
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_unreachable_stmt1(self):
        input = """
        function f():integer;
        var x,y:integer;
        begin
            if(x>y) then
                    return x;
            else  return y;
            x:=y;
        end
        procedure Main();
        var a:integer;
        begin 
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_unreachable_stmt2(self):
        input = """
        function f():integer;
        var x,y:integer;
        begin
                with
                    x:integer;
                    y:real;
            do begin
                    return 100;
            end
            x:= x+1;
        end
        procedure Main();
        var a:integer;
        begin 
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_for_stmt(self):
        input = """
        var a: integer;
        procedure main();
        begin
                foo(5);
        end
        procedure foo(b: integer);
        var c: integer;
        begin
                for a := 1 to 10 do foo(1);
                for b := 1 to 10 do foo(1);
                for c := 1 to 10 do foo(1);
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_break_stmt1(self):
        input = """
        var a: integer;
        procedure main();
        begin
            a := f();
        end
        function f():integer;
                var x,y:integer;
                begin
                    while(x < y) do
                    begin
                        if (x = 5)then begin
                            x := 6;
                            break;
                        end
                        else begin
                            x:=5;
                            break;
                        end
                        x := y;
                    end
                    return x;
                end
        """
        expect = "Unreachable statement: AssignStmt(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_break_stmt2(self):
        input = """
        var a: integer;
        procedure main();
        begin
            a := foo();
        end
        function foo(): integer;
        var a: boolean;
        begin
            while a do
                begin
                    break;
                    a := True;
                end
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(a),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_return_stmt2(self):
        input = """
        var a: integer;
        procedure main();
        begin
            a := foo();
        end
        function foo(): integer;
        var a: boolean;
        begin
            if (1>0) then
            return;
            else
            return 1;
        end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_return_stmt3(self):
        input = """
        var a: integer;
        procedure main();
        begin
            a := foo();
        end
        function foo(): integer;
        var a: boolean;
        begin
            if (1>0) then
            return 1;
            else
            return 1;
            main();
        end
        """
        expect = "Unreachable statement: CallStmt(Id(main),[])"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_unreachable_statement2(self):
        input = """
        var a: integer;
        procedure main();
        var b: array [1 .. 10] of integer;
            x: integer;
        begin
            a := foo();
            a := b [10] := f()[ 3 ] := x := 1 ;
        end
        function foo(): integer;
        var a: boolean;
        begin
            while a do
                begin
                    break;
                end
            return 200;
            a := true;
        end
        function f(): array [1 .. 10] of integer;
        var a: array [1 .. 10] of integer;
        begin
            return a;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(a),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_return_array(self):
        input = """
        procedure main();
        begin
            return;
        end
        function foo(): array [1 .. 10] of integer;
        var a: array [1 .. 9] of integer;
        begin
            return a;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_unreachable_function(self):
        input = Program([FuncDecl(Id("main"),[],[],[Return()],VoidType()),
        FuncDecl(Id("foo"),[],[VarDecl(Id("a"),ArrayType(1,10,IntType()))],[Return(Id("a"))],ArrayType(1,10,IntType()))])
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,418))
