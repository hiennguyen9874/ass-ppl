import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_Type_Mismatch_In_Statement_Return7(self):
        input = """
        procedure main();
        var
            i: integer;
            r: real;
            s: string;
            b: boolean;
        begin
            for i:=1 to 10 do return 1;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main(); 
        begin
            putIntLn();
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"), [], [], [
            CallStmt(Id("foo"), [])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], [], [CallStmt(Id("putIntLn"), [])])])
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input, expect, 403))

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
        self.assertTrue(TestChecker.test(input, expect, 404))

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
        self.assertTrue(TestChecker.test(input, expect, 405))

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
        self.assertTrue(TestChecker.test(input, expect, 406))

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
        self.assertTrue(TestChecker.test(input, expect, 407))

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
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 408))

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
        self.assertTrue(TestChecker.test(input, expect, 409))

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
        self.assertTrue(TestChecker.test(input, expect, 410))

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
                for a := 1.1 to 10 do foo(1);
                for b := 1 to 10 do foo(1);
                for c := 1 to 10 do foo(1);
        end
        """
        expect = "Type Mismatch In Statement: For(Id(a)FloatLiteral(1.1),IntLiteral(10),True,[CallStmt(Id(foo),[IntLiteral(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 411))

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
        self.assertTrue(TestChecker.test(input, expect, 412))

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
        self.assertTrue(TestChecker.test(input, expect, 413))

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
        self.assertTrue(TestChecker.test(input, expect, 414))

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
        self.assertTrue(TestChecker.test(input, expect, 415))

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
        self.assertTrue(TestChecker.test(input, expect, 416))

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
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_unreachable_function(self):
        input = Program([FuncDecl(Id("main"), [], [], [Return()], VoidType()),
                         FuncDecl(Id("foo"), [], [VarDecl(Id("a"), ArrayType(1, 10, IntType()))], [Return(Id("a"))], ArrayType(1, 10, IntType()))])
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclare_function(self):
        input = """
        function foo(): integer;
        var foo: real;
        begin
            foo := foo();
            return 1;
        end
        procedure main();
        var i:integer;
        begin
            i:=foo();
            return;
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_unreachable_function1(self):
        input = """
        function foo(): integer;
        var i: real;
        begin
            i := foo();
            return 1;
        end
        procedure main();
        var i:integer;
        begin
            return;
        end
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_redeclare_variable(self):
        input = """
        procedure main();
        var i:integer;
            i:real;
        begin
            return;
        end
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_redeclare_function1(self):
        input = """
        function foo(): integer;
        var i: real;
        begin
            return 1;
        end
        function foo(): real;
        var i: real;
        begin
            return 1;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_redeclare_function2(self):
        input = """
        function getInt(): real;
        var i: real;
        begin
            return 1;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_redeclare_function3(self):
        input = """
        function putInt(): real;
        var i: real;
        begin
            return 1;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_redeclare_function4(self):
        input = """
        function putLn(): real;
        var i: real;
        begin
            return 1;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Function: putLn"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_redeclare_Procedure(self):
        input = """
        Procedure putLn();
        begin
            putString("\\n");
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            return;
        end
        """
        expect = "Redeclared Procedure: putLn"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_redeclare_Parameter(self):
        input = """
        Procedure foo(i:integer;i:real);
        begin
            return;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            foo(i,j);
            return;
        end
        """
        expect = "Redeclared Parameter: i"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_redeclare_Parameter1(self):
        input = """
        Procedure foo(i:integer;j:real);
        var i:integer;
        begin
            return;
        end
        procedure main();
        var i:integer;
            j:real;
        begin
            foo(i,j);
            return;
        end
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_Undeclare_Identifier(self):
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            j := i := k := 1;
            return;
        end
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_Undeclare_Function(self):
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            j := foo();
            return;
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_Undeclare_Procedure(self):
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            foo();
            return;
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_Type_Mismatch_In_Statement_If(self):
        """ The type of a conditional expression in an if statement must be boolean. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            if i then return; else j := j + 1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: If(Id(i),[Return(None)],[AssignStmt(Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_Type_Mismatch_In_Statement_If1(self):
        """ The type of <identifier> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for j := 1 to 10 do j :=i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(j)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_Type_Mismatch_In_Statement_If2(self):
        """ The type of <expression 2> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for i := 1 to i < 10 do j := i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_Type_Mismatch_In_Statement_If3(self):
        """ The type of <expression 1> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for i := 1.2 to 10 do j := i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i)FloatLiteral(1.2),IntLiteral(10),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_Undeclared_If(self):
        """ The <identifier> must be a local integer variable. """
        input = """
        var i:real;
        procedure main();
        var j:integer;
        begin
            for i := 1 to 10 do j := i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_Type_Mismatch_In_Statement_while(self):
        """ The type of condition expression in while statement must be boolean. """
        input = """
        var i:integer;
        procedure main();
        var j:integer;
        begin
            while j do return;
            return;
        end
        """
        expect = "Type Mismatch In Statement: While(Id(j),[Return(None)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_Type_Mismatch_In_Statement_assignment(self):
        """ Left-hand side (LHS) can be in any type except string and array type. """
        input = """
        var i:integer;
        procedure main();
        var j:integer;
            str: string;
        begin
            str := "Hello";
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(str),StringLiteral(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_Type_Mismatch_In_Statement_assignment1(self):
        """ Left-hand side (LHS) can be in any type except string and array type. """
        input = """
        var i:integer;
        procedure main();
        var j:integer;
            str: string;
            arr: array [1 .. 10] of integer;
            arr1: array [1 .. 10] of integer;
        begin
            arr := arr1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr),Id(arr1))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_Type_Mismatch_In_Statement_assignment2(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var j: integer;
            i: real;
        begin
            j:=i;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(j),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_Type_Mismatch_In_Statement_assignment3(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            i:=b;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_Type_Mismatch_In_Statement_assignment4(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            b:=i;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_Type_Mismatch_In_Statement_assignment5(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            i:=s;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_Type_Mismatch_In_Statement_assignment6(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            f:=b;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(f),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_Type_Mismatch_In_Statement_assignment7(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            b:=f;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(f))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_Type_Mismatch_In_Statement_assignment8(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            s:=f;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(s),Id(f))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_Type_Mismatch_In_Statement_assignment9(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            s:=f;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(s),Id(f))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_Type_Mismatch_In_Statement_assignment10(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            f:=s;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(f),Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_Type_Mismatch_In_Statement_assignment11(self):
        """ Just the integer can coerce to the float. """
        input = """
        procedure main();
        var i: integer;
            f: real;
            b: boolean;
            s: string;
        begin
            b:=s;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_Type_Mismatch_In_Statement_Return(self):
        """ The return statement of a procedure must be without any expression. """
        input = """
        procedure main();
        var i: integer;
        begin
            return i;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(i)))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_Type_Mismatch_In_Statement_Return1(self):
        """ The return statement of a function must be with an expression whose type can be coerced
        to the return type of the enclosed function. """
        input = """
        function foo(): integer;
        begin
            return;
        end
        procedure main();
        var i: integer;
        begin
            i:= foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_Type_Mismatch_In_Statement_Return2(self):
        """ The return statement of a function must be with an expression whose type can be coerced
        to the return type of the enclosed function. """
        input = """
        function foo(): integer;
        begin
            return 1.2;
        end
        procedure main();
        var i: real;
        begin
            i := foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_Type_Mismatch_In_Statement_Return3(self):
        input = """
        function foo(): array [1 .. 10] of integer;
        var ret: array [1 .. 9] of integer;
        begin
            return ret;
        end
        procedure main();
        var i: array [1 .. 10] of integer;
        begin
            i := foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(ret)))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_redeclare_function5(self):
        input = """
        var main: integer;
        procedure main();
        begin
        end
        """
        expect = "Redeclared Procedure: main"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_Type_Mismatch_In_Statement_Return4(self):
        input = """
        function foo(): array [1 .. 10] of integer;
        var ret: array [2 .. 10] of integer;
        begin
            return ret;
        end
        procedure main();
        var i: array [1 .. 10] of integer;
        begin
            i := foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(ret)))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_Type_Mismatch_In_Statement_Return5(self):
        input = """
        function foo(): array [1 .. 10] of integer;
        var ret: array [1 .. 10] of real;
        begin
            return ret;
        end
        procedure main();
        var i: array [1 .. 10] of integer;
        begin
            i := foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(ret)))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_Type_Mismatch_In_Statement_Return6(self):
        input = """
        function foo(): array [1 .. 10] of real;
        var ret: array [1 .. 10] of integer;
        begin
            return ret;
        end
        procedure main();
        var i: array [1 .. 10] of real;
        begin
            i := foo();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(ret)))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_Type_Mismatch_In_Statement_Function_Call1(self):
        input = """
        procedure foo(x:integer;y:real);
        var arr: array [1 .. 10] of integer;
            i: integer;
            b: boolean;
            f: real;
            str: string;
        begin
            return;
        end
        procedure main();
        var arr: array [1 .. 10] of integer;
            i: integer;
            b: boolean;
            f: real;
            str: string;
        begin
            foo(i, i);
            foo(f, i);
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(f),Id(i)])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_Type_Mismatch_In_Statement_Function_Call2(self):
        input = """
        procedure foo(x:integer;y:real; ar: array [1 .. 10] of integer);
        var arr: array [1 .. 10] of real;
            i: integer;
            b: boolean;
            f: real;
            str: string;
        begin
            return;
        end
        procedure main();
        var arr: array [1 .. 10] of real;
            i: integer;
            b: boolean;
            f: real;
            str: string;
        begin
            foo(f, i, arr);
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(f),Id(i),Id(arr)])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_combine_ReturnContinue(self):
        input = """
        Procedure main();
        begin
            foo();
        end
        Procedure foo();
        begin
            while true do
            begin
                if true then return;
                else continue;
                foo();
            end
        end
        """
        expect = "Unreachable statement: CallStmt(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_Type_Mismatch_In_Expression(self):
        input = """
        function foo(i:integer): array [1 .. 10] of integer;
        var arr: array [1 .. 10] of integer;
        begin
            return arr;
        end
        Procedure main();
        var x:integer;
            a:array [1 .. 10] of integer;
            b:array [1 .. 10] of real;
        begin
            foo(2)[3+x] := a[b[2]] + 3;
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_Type_Mismatch_In_Expression1(self):
        input = """
        Procedure main();
        var x:integer;
            a:array [1 .. 10] of integer;
            b:array [1 .. 10] of real;
        begin
            x[1] := a[1];
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_Type_Mismatch_In_Expression2(self):
        input = """
        Procedure main();
        var x:integer;
            a:array [1 .. 10] of integer;
            b:array [1 .. 10] of real;
        begin
            b[1] := a[1.2];
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_Type_Mismatch_In_Expression3(self):
        input = """
        Procedure main();
        var a:boolean;
            b:boolean;
            c:boolean;
            i:integer;
        begin
            a := not b and c;
            a := b and i;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(b),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_Type_Mismatch_In_Expression4(self):
        input = """
        Procedure main();
        var a:boolean;
            b:boolean;
            c:boolean;
            i:integer;
        begin
            a := not b and c and then a or else a or True;
            a := b and i;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(b),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_Type_Mismatch_In_Expression5(self):
        input = """
        Procedure main();
        var a: integer;
            b: integer;
            c: integer;
            d: integer;
            e: integer;
        begin
            a := a + (d >= e);
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),BinaryOp(>=,Id(d),Id(e)))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_Type_Mismatch_In_Expression6(self):
        input = """
        Procedure main();
        var a: integer;
            b: integer;
            f: real;
        begin
            a := a/b + f;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),Id(b)),Id(f)))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_Type_Mismatch_In_Expression7(self):
        input = """
        Procedure main();
        var a: string;
            b: string;
            c: string;
        begin
            a := a/b + f;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),Id(b)),Id(f)))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_Type_Mismatch_In_Expression8(self):
        input = """
        Function foo(i: integer; j: real): real;
        begin
            return i + j * j;
        end
        Procedure main();
        var a: string;
            b: string;
            c: string;
        begin
            a := a/b + f;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),Id(b)),Id(f)))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_Type_Mismatch_In_Expression9(self):
        input = """
        Procedure main();
        var a: integer;
            b: integer;
            c: integer;
        begin
            while false do
            begin
                a := b;
                return;
                c := a;
            end
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_Type_Mismatch_In_Expression10(self):
        input = """
        function foo(): integer;
        var a:integer;
        begin
            if a > 0
            then return a;
        end
        Procedure main();
        var a: integer;
            b: integer;
            c: integer;
        begin
            b:= foo();
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_Type_Mismatch_In_Statement_While(self):
        input = """
        function foo(): integer;
        var a:integer;
        begin
            while a do return 1;
        end
        Procedure main();
        var a: integer;
            b: integer;
            c: integer;
        begin
            b:= foo();
        end
        """
        expect = "Type Mismatch In Statement: While(Id(a),[Return(Some(IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_Type_Mismatch_In_Statement_For(self):
        """ The type of <identifier> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for j := 1 to 10 do j :=i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(j)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_Type_Mismatch_In_Statement_For1(self):
        """ The type of <expression 2> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for i := 1 to j do j := i+j;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i)IntLiteral(1),Id(j),True,[AssignStmt(Id(j),BinaryOp(+,Id(i),Id(j)))])"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_Type_Mismatch_In_Statement_For2(self):
        """ The type of <expression 1> in a for statement must be integer. """
        input = """
        procedure main();
        var i:integer;
            j:real;
        begin
            for i:=1 to 10 do 
                begin
                    for j:=1 to 10 do
                            j:=j+1.1;
                end
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(j)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(j),BinaryOp(+,Id(j),FloatLiteral(1.1)))])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_Type_Mismatch_In_Statement_Function_Call7(self):
        input = """
        function foo(f: real): real;
        var arr: array [1 .. 10] of real;
            b: boolean;
            str: string;
        begin
            return arr[2];
        end
        procedure main();
        var arr: array [1 .. 10] of real;
            i: integer;
            b: boolean;
            f: real;
            str: string;
        begin
            f := foo(i);
            f := foo(str);
            return;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(str)])"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_Type_Mismatch_In_Expression11(self):
        input = """
        procedure main();
        var b: boolean;
        begin
            b:= -b;
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_function_not_return1(self):
        input = """
        function foo(): integer;
        var int : integer;
        begin
            if False then return int;
        end
        Procedure main();
        var int : integer;
        begin
            int := foo();
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_function_not_return2(self):
        input = """
        function foo(): integer;
        var int : integer;
        begin
            if False then int:=int+1; else return int;
        end
        Procedure main();
        var int : integer;
        begin
            int := foo();
        end
        """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_break_not_in_loop(self):
        input = """
        Procedure main();
        var int : integer;
        begin
            while true do
            begin
                if true then
                    break;
                else
                    continue;
            end
            break;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_break_not_in_loop1(self):
        input = """
        Procedure main();
        var int : integer;
        begin
            while true do
            begin
                while true do
                begin
                    break;
                end
            end
            continue;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_break_not_in_loop2(self):
        input = """
        function foo():integer;
        begin
            return 1;
        end
        Procedure main();
        var int : integer;
        begin
            while true do
            begin
                while true do
                begin
                    break;
                end
            end
            foo();
            continue;
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_break_not_in_loop3(self):
        input = """
        var a,b: integer; m,n,x: real;
        function main():integer;
        begin
            return a;
        end
        procedure main();
        begin
            if true then
                x:=9.6;
            else 
                x:=6.9;
        end
        """
        expect = "Redeclared Procedure: main"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_redeclare_variable1(self):
        input = """
        var b,c,a : integer ;
        var a: integer;

        procedure main(); begin
            return;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_undeclare_variable(self):
        input = """
            var b: integer;
            procedure main();
            begin
                putIntLn(a);
            end
            function a():real;
            begin
            end
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_undeclare_variable1(self):
        input = """
            var  d:real;
            var  e:boolean;
            procedure main(b, a : integer;  m:array[1 .. 3] of integer); 
            begin 
	            for a := 1 to 10 do 
                begin 
                    return;
	            end
            end
            procedure foo(b, a : integer);
            begin
            end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_function_not_return3(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                while true do
                begin
                    return i;
                end
            end
            procedure main();
            var i:integer;
            begin
                i:= foo();
            end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_function_not_return4(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                for i:=1 to 10 do 
                begin
                    return 1;
                end
            end
            procedure main();
            var i:integer;
            begin
                i:= foo();
            end
            """
        expect = "Function fooNot Return "
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_break_not_in_loop4(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                with i:integer; do
                    begin
                        return i;
                    end
            end
            procedure main();
            var i:integer;
            begin
                i:= foo();
                break;
            end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_no_entry_point(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                with i:integer; do
                    begin
                        return i;
                    end
            end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_no_entry_point1(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                with i:integer; do
                    begin
                        return i;
                    end
            end
            procedure main(i:integer);
            begin
                return;
            end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_no_entry_point1(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                with i:integer; do
                    begin
                        return i;
                    end
            end
            procedure main(i:integer);
            begin
                return;
            end
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_function_not_return5(self):
        input = """
            function foo():integer;
            var i:integer;
            begin
                if True then
                    return i;
                else
                    i:=i+1;
                while True do
                begin
                    i := i - 1;
                end
                return i;
            end
            procedure main();
            var i: integer;
            begin   
                i := foo(1);
            end
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_undeclare_function1(self):
        input = """
            procedure foo();
            begin
            end
            procedure main();
            var i: integer;
            begin   
                i := foo();
            end
            """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_unreachable_procedure(self):
        input = """
            procedure foo();
            begin
                while true do
                begin
                    foo();
                    return;
                end
            end
            procedure main();
            var i: integer;
            begin
            end
            """
        expect = "Unreachable Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_unreachable_procedure1(self):
        input = """
            procedure main();
            var a: integer;
            begin
                a := - -(a - -1);
            end
            procedure foo();
            begin
                while true do
                begin
                    foo();
                    return;
                end
            end
            """
        expect = "Unreachable Procedure: foo"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_undeclared_identifier(self):
        input = """
        var a:integer;
        procedure funcA();
        var b:integer; 
        begin 
            a := 7;
            b := a;
        end
        function sum(b:integer):integer; 
        var d:integer;
        begin 
            
            d := 7;
            return a + b + d;
        end
        procedure main(); 
        var m:array[1 .. 10] of integer;
        begin 

            m[1] := sum(3);
            funcA();
            a := 1 + n[1];
            return ;
        end
            """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input, expect, 496))


    def test_undeclared_identifier1(self):
        input = """
            var a:integer;
            var b:real;
            var m:array[1 .. 10] of integer;
            procedure main(); begin 
                b := m[1] + -1;
                b := b * (1.0 + 1);
                b := not (m[1] = 1);
                return ;
            end
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),UnaryOp(not,BinaryOp(=,ArrayCell(Id(m),IntLiteral(1)),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_Type_Mismatch_In_Statement_CallStmt(self):
        input = """
            procedure foo(a:array [1 .. 2] of real);
            begin
            end
            procedure goo(x:array [1 .. 2] of real);
                var 
                    y: array [2 .. 3] of real;
                    z: array [1 .. 2] of integer;
                begin
                    foo(x);
                    foo(y);
                    foo(z);
                end
            procedure main();
                var 
                    y: array [1 .. 2] of real;
                begin
                    goo(y);
                end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_Type_Mismatch_In_Statement1(self):
        input = """
            function foo(): real;
                begin
                    if True then return 2.3;
                    else return 2;
                end
            function goo(b: array [1 .. 2] of integer): array [2 .. 3] of real;
                var
                    a: array [2 .. 3] of real;
                begin
                    if True then return a;
                    else return b;
                    a[2] := foo();
                end
            procedure main();
                var 
                    y: array [1 .. 2] of integer;
                begin
                    goo(y);
                end
            """
        expect = "Type Mismatch In Statement: Return(Some(Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 499))