import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        var i:integer;
        procedure foo(a, b: integer; c: real);
        var ret: array [1 .. 2] of integer;
        begin
            foo1(1,2,3.2);
            if (i > 1) then foo(1,2,3);
            else return;
        end
        procedure foo1(a,b: integer; c:real);
        begin
            return;
        end
        function f():integer;
        begin
            foo1(1,2,3.2);
            if (i > 1) then begin foo(1,2,3); return; end
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
        expect = "[]"
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

    def test_callStmt_is_function(self):
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

    def test_return_procedure(self):
        input = """
        function foo():integer;
        begin
            return 1;
        end
        procedure main();
        begin
            return;
        end
        """
        expect = "Unreachable Function: foo"
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