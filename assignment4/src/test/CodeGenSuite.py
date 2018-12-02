import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """
        procedure main(); 
        begin 
            putInt(100);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putInt"),[BinaryOp('+',IntLiteral(5),IntLiteral(1))])])])
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
        
    def test_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.0)])])])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
        
    def test_float1_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloatLn"),[FloatLiteral(7.0)])])])
        expect = "7.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    def test_float_int_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "7.0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    def test_int_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('+',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "7.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))    
        
    def test_float_int_ast1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('-',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))
        
    def test_int_float_ast1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('-',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 507))
        
    def test_int_float_ast2(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('*',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
        
    def test_float_int_ast2(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('*',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))    
    
    def test_int_float_ast3(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('/',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test_float_int_ast3(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('/',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_boolean(self):
        input = """
        procedure main(); begin putBool(true); end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_boolean1(self):
        input = """
        procedure main(); begin putBoolLn(true); end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_boolean2(self):
        input = """
        procedure main(); begin putBool(false); end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_boolean3(self):
        input = """
        procedure main(); begin putBoolLn(false); end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_string(self):
        input = """
        procedure main(); begin putString("ahihi"); end
        """
        expect = "ahihi"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_string1(self):
        input = """
        procedure main(); begin putStringLn("ahihi"); end
        """
        expect = "ahihi\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_int1(self):
        input = """
        procedure main(); begin putInt(400000); end
        """
        expect = "400000"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_float(self):
        input = """
        function foo(i: integer): real;
        begin
            return i;
        end
        procedure main();
        var i: real;
            begin
                i := foo(1);
                putFloat(i);
            end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_if5(self):
        input = """
        procedure main();
        var i: real;
            begin
                if False then i:=1; else i:=2;
                putFloat(i);
            end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_for(self):
        input = """
        procedure main();
            var i: integer;
            begin
                for i := 10 downto 0 do 
                    begin
                        putInt(i);
                        continue;
                    end
                putLn();
            end
        """
        expect = "109876543210\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_for1(self):
        input = """
        procedure main();
            var i: integer;
            begin
                for i := 0 to 10 do 
                    begin
                        putInt(i);
                    end
                putLn();
            end
        """
        expect = "012345678910\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_break_for(self):
        input = """
        procedure main();
            var i: integer;
            begin
                for i := 0 to 10 do 
                    begin
                        putInt(i);
                        break;
                    end
                putLn();
            end
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_while(self):
        input = """
        procedure main();
            var i: integer;
            begin
                i := 1;
                putInt(0);
                while i <= 10 do
                begin
                    putString(" ");
                    putInt(i);
                    i := i + 1;
                    continue;
                end
                putLn();
            end
        """
        expect = "0 1 2 3 4 5 6 7 8 9 10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_break_while(self):
        input = """
        procedure main();
            var i: integer;
            begin
                i := 1;
                putInt(0);
                while i <= 10 do
                begin
                    putString(" ");
                    putInt(i);
                    break;
                    i := i + 1;
                end
                putLn();
            end
        """
        expect = "0 1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_with(self):
        input = """
            procedure main();
                begin
                    putStringLn("bat dau with");
                    with a, b: integer; do
                        begin
                            a := 1;
                            b := 2;
                            putInt(a+b); 
                        end
                    putStringLn("ket thuc with");
                end
        """
        expect = "bat dau with\n3ket thuc with\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_and_then(self):
        input = """
            procedure main();
                begin
                    putBool(false and then false);
                end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_and_then1(self):
        input = """
            procedure main();
                begin
                    putBool(true and then false);
                end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_or_else(self):
        input = """
            procedure main();
                begin
                    putBool(false or else false);
                end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_or_else1(self):
        input = """
            procedure main();
                begin
                    putBool(true or else false);
                end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    def test_binaryOp_bool(self):
        input = """
            procedure main();
                begin
                    putBool(true and true);
                end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test_unaryOp_bool(self):
        input = """
            procedure main();
                begin
                    putBool(not true);
                end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_unary_int(self):
        input = """
            procedure main();
                begin
                    putInt(-1);
                end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_if2(self):
        input = """
            var a:boolean; procedure main(); begin  if false then putInt(100);  putInt(10); end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_if(self):
        input = """
            procedure main();
                begin
                    putStringLn("bat dau if");
                    if True then
                        putStringLn("Dung");
                    else
                        putStringLn("Sai");
                    putStringLn("ket thuc if");
                end
        """
        expect = "bat dau if\nDung\nket thuc if\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_if1(self):
        input = """
            procedure main();
                begin
                    putStringLn("bat dau if");
                    if False then
                        putStringLn("Dung");
                    putStringLn("ket thuc if");
                end
        """
        expect = "bat dau if\nket thuc if\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_if4(self):
        input = """
            function foo():integer;
            begin
                return 1;
            end
            procedure main();
                begin
                    putInt(foo());
                end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_for2(self):
        input = """
        function foo(n: integer): integer;
        var i: integer;
            sum: integer;
        begin
            sum := 0;
            for i := 0 to n do
            begin
                sum := sum + i;
            end
            return sum;
        end
        procedure main();
            begin
                putInt(foo(10));
            end
        """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_for3(self):
        input = """
        function foo(n: integer): integer;
        var i: integer;
            sum: integer;
        begin
            return 55;
        end
        procedure main();
            begin
                putInt(foo(10));
            end
        """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_if3(self):
        input = """
        var a: integer;
        procedure main();
            var b: integer;
            begin
                a := 7;
                b := 1;
                if a > b then
                    putInt(a);
            end
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_mod(self):
        input = """
        var a: integer;
        procedure main();
            var b: integer;
            begin
                putInt(6 mod 5);
            end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_div(self):
        input = """
        procedure main();
            var b: integer;
            begin
                b := 1 + 2;
                putInt(b);
            end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_div1(self):
        input = """
        procedure main();
            begin
                b := 1 + 2;
                putInt(b);
            end
        var b: integer;
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_function(self):
        input = """
        var n: integer;
        function foo(a, b: integer): integer;
        begin
            n := 3;
            putIntLn(a);
            putInt(b);
            return a*n + b;
        end
        procedure main();
            var n: integer;
            begin
                n := foo(1,2);
                putInt(n);
            end
        """
        expect = "1\n25"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_function1(self):
        input = """
        var n: integer;
        procedure foo();
        begin
            n := 10;
        end
        procedure main();
            begin
                foo();
                putIntLn(n);
            end
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_function2(self):
        input = """
        procedure foo(a,b: integer; c:real);
        var i, i1: integer;
            f, f1: real;
            b, b1: boolean;
        begin
            b := 1 <> 2 ;
            putBool(b);
        end
        procedure main();
            begin
                foo(1,2,4.3);
            end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_online_14(self):
        input = """
        function searchArr(d: array [1 .. 5] of integer; n: integer): array [1 .. 5] of integer;
        var i: integer;
        begin
            for i := 1 to n do begin
                d[i] := i;
            end
            return d;
        end
        procedure main();
        var arr: array [1 .. 5] of integer;
        begin
            putInt(searchArr(arr, 5)[1]);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_binaryop_float(self):
        input = """
        procedure main();
        begin
            putBool( 1 <> 2.0 );
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_binaryop_float1(self):
        input = """
        procedure main();
        begin
            putBool( 1 = 2.0 );
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_binaryop_float2(self):
        input = """
        procedure main();
        begin
            putBool( 1 >= 2.0 );
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_assignment_1(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a :=(10 - 9*8) + (6 div 4);
            putInt(a);
        end
        """
        expect = "-61"
        self.assertTrue(TestCodeGen.test(input, expect, 551))
   
    def test_all(self):
        input = Program([VarDecl(Id("a"),IntType()),
        VarDecl(Id("b"),IntType()),
        VarDecl(Id("c"),IntType()),
        FuncDecl(Id("main"),[],[],
        [Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp('=',Id("a"),IntLiteral(1)),
        [With([VarDecl(Id("a"),IntType())],
        [For(Id("a"),IntLiteral(2),IntLiteral(3),True,
        [With([VarDecl(Id("b"),IntType())],
        [CallStmt(Id("putIntLn"),[Id("a")])])])])],
        [With([VarDecl(Id("a"),IntType())],
        [For(Id("a"),IntLiteral(7),IntLiteral(8),True,
        [With([VarDecl(Id("b"),IntType())],
        [CallStmt(Id("putIntLn"),[Id("a")])])])])]),
        With([VarDecl(Id("c"),IntType())],
        [CallStmt(Id("putInt"),[Id("a")])]),
        Return(None)],VoidType())])
        expect = "2\n3\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_array_1(self):
        input = """
        var m: array [1 .. 10] of integer;
        procedure main();
        begin
            m[1] := 5;
            putInt(m[1]);
        end"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    def test_array_2(self):
        input = """
        function mean(size:integer): real;
        var i,s: integer;
            x: array [1 .. 3] of integer;
        begin
            x[3] := 1;
            x[1] := 3;
            x[2] := 5;
            s := 0;
            for i := 1 to size do
                begin
                    s := s + x[i];
                end
            return (s + 0.0 ) / size;
        end
        procedure main();
        begin
            putFloat(mean(3));
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_array_3(self):
        input = """
        function searchArr(m: array [1 .. 5] of integer; a,n : integer): integer;
        var i :integer;
        begin
            for i:=1 to n do begin
                if m[i] = a then
                    return i;
            end
            return -1;
        end
        procedure main();
        var j,result: integer;
            arr: array [1 .. 5] of integer;
        begin
            for j := 1 to 5 do
            begin
                arr[j] := j + 1;
            end
            result := searchArr(arr, 3, 5);
            putInt(result);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_array_4(self):
        input = """
        var arr: array [1 .. 5] of integer;
        function searchArr(d: array [1 .. 5] of integer; a, n: integer): integer;
        var i: integer;
        begin
            for i := 1 to n do begin
                d[i] := i;
            end
            return arr[1];
        end
        procedure main();
        var j, result: integer;
        begin
            arr[1] := 5;
            arr[2] := 3;
            arr[3] := 11;
            arr[4] := 19;
            arr[5] := 20;
            result := searchArr(arr, 3, 5);
            putInt(result);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test_all1(self):
        input = """
        procedure main();
        var a, b, Sum:integer;
        begin
            Sum := 0;
            for a := 0 to 9 do
            begin
                if (a mod 2) = 0 then continue;
                    Sum := Sum + a;
            end
            putInt(Sum);
        end
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_assignment_2(self):
        input = """
        procedure main();
        var a, b:integer;
        begin
            a := b := 1;
            putInt(a*b);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_while_1(self):
        input = """
        procedure main();
        var i: integer;
        begin
            i := 0;
            while i < 10 do
            begin
                putInt(i);
                i := i + 1;
            end
        end
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_while_2(self):
        input = """
        procedure main();
        var i: integer;
        begin
            i := 0;
            while true do
            begin
                putInt(i);
                i := i + 1;
                if i > 10 then
                    break;
            end
        end
        """
        expect = "012345678910"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_for_1(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                begin
                    putInt(i);
                    putString("->");
                end
        end
        """
        expect = "0->1->2->3->4->5->6->7->8->9->10->"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_for_2(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                begin
                    putInt(i);
                    putString("->");
                    if i > 5 then
                        break;
                end
        end
        """
        expect = "0->1->2->3->4->5->6->"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_for_3(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                begin
                    putInt(i);
                    if i > 5 then
                        continue;
                    putString("->");
                end
        end
        """
        expect = "0->1->2->3->4->5->678910"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_for_4(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 10 do
                begin
                    putInt(i);
                    if i > 5 then
                        return;
                    putString("->");
                end
        end
        """
        expect = "0->1->2->3->4->5->6"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_with_1(self):
        input = """
        procedure main();
        var i: integer;
        begin
            i := 1;
            with i: integer; do
                begin
                    i := 2;
                    putIntLn(i);
                end
            putIntLn(i);
        end
        """
        expect = "2\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_with_2(self):
        input = """
        procedure main();
        var i: integer;
        begin
            i := 1;
            with i: integer; do
                begin
                    i := 2;
                    return;
                    putIntLn(i);
                end
            putIntLn(i);
        end
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_binary_op_1(self):
        input = """
        procedure main();
        begin
            putFloat(1 + 1.2);
        end
        """
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_binary_op_2(self):
        input = """
        procedure main();
        begin
            putFloat(1.2 - 1);
        end
        """
        expect = "0.20000005"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_binary_op_3(self):
        input = """
        procedure main();
        begin
            putFloat(3.5*2.2);
        end
        """
        expect = "7.7000003"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_binary_op_4(self):
        input = """
        procedure main();
        begin
            putFloat(1.2 / 2.1);
        end
        """
        expect = "0.5714286"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
        
    def test_unary_op_1(self):
        input = """
        procedure main();
        begin
            putFloat(-2.1);
        end
        """
        expect = "-2.1"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_unary_op_2(self):
        input = """
        procedure main();
        begin
            putInt(-1);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_unary_op_3(self):
        input = """
        procedure main();
        begin
            putBool(not true);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_online_15(self):
        input = """
        var arr: array [1 .. 5] of integer;
        function searchArr(d: array [1 .. 5] of integer; a, n: integer): integer;
        var i: integer;
        begin
            for i := 1 to n do begin
                d[i] := i;
            end
            return arr[1];
        end
        procedure main();
        var j, result: integer;
        begin
            arr[1] := 5;
            arr[2] := 3;
            arr[3] := 11;
            arr[4] := 19;
            arr[5] := 20;
            result := searchArr(arr, 3, 5);
            putInt(result);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_75(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := -100 to 100 do
                for i := 0 to 100 do begin end
            putInt(i);
        end
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_76(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a :=(10 - 9*8) + (6 div 4);
            putInt(a);
        end
        """
        expect = "-61"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
   
    def test_77(self):
        input = Program([VarDecl(Id("a"),IntType()),
        VarDecl(Id("b"),IntType()),
        VarDecl(Id("c"),IntType()),
        FuncDecl(Id("main"),[],[],
        [Assign(Id("a"),IntLiteral(1)),
        If(BinaryOp('=',Id("a"),IntLiteral(1)),
        [With([VarDecl(Id("a"),IntType())],
        [For(Id("a"),IntLiteral(2),IntLiteral(3),True,
        [With([VarDecl(Id("b"),IntType())],
        [CallStmt(Id("putIntLn"),[Id("a")])])])])],
        [With([VarDecl(Id("a"),IntType())],
        [For(Id("a"),IntLiteral(7),IntLiteral(8),True,
        [With([VarDecl(Id("b"),IntType())],
        [CallStmt(Id("putIntLn"),[Id("a")])])])])]),
        With([VarDecl(Id("c"),IntType())],
        [CallStmt(Id("putInt"),[Id("a")])]),
        Return(None)],VoidType())])
        expect = "2\n3\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_78(self):
        input = """
        var m: array [1 .. 10] of integer;
        procedure main();
        begin
            m[1] := 5;
            putInt(m[1]);
        end"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test_79(self):
        input = """
        function mean(size:integer): real;
        var i,s: integer;
            x: array [1 .. 3] of integer;
        begin
            x[3] := 1;
            x[1] := 3;
            x[2] := 5;
            s := 0;
            for i := 1 to size do
                begin
                    s := s + x[i];
                end
            return (s + 0.0 ) / size;
        end
        procedure main();
        begin
            putFloat(mean(3));
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_80(self):
        input = """
        function searchArr(m: array [1 .. 5] of integer; a,n : integer): integer;
        var i :integer;
        begin
            for i:=1 to n do begin
                if m[i] = a then
                    return i;
            end
            return -1;
        end
        procedure main();
        var j,result: integer;
            arr: array [1 .. 5] of integer;
        begin
            for j := 1 to 5 do
            begin
                arr[j] := j + 1;
            end
            result := searchArr(arr, 3, 5);
            putInt(result);
        end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_81(self):
        input = """
        var a, b, c: integer;
        function foo(i: integer): boolean;
        begin
            a := a + i;
            return i >= 5;
        end
        procedure main();
        var x: boolean;
        begin
            a := 0;
            putBoolLn(( (foo(1) or foo(2)) or foo(3)) or foo(7));
            putIntLn(a);
            a := 0;
            putBoolLn(( (foo(1) or else foo(2)) or else foo(3)) or else foo(4));
            putIntLn(a);
            a := 0;
            putBoolLn(( (foo(1) or foo(2)) or foo(3)) or foo(7));
            putIntLn(a);
            a := 0;
            putBoolLn(( (foo(1) or foo(2)) or else foo(5)) or else foo(7));
            putInt(a);
        end
        """
        expect = "true\n13\nfalse\n10\ntrue\n13\ntrue\n8"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_82(self):
        input = """
        function foo(): integer;
        var a, b: integer;
        begin
            a := 5;
            b := 6;
            if a > b then
                return 5;
            else
                return 6;
        end
        procedure main();
        var a,b,c: integer;
        begin
           c := foo();
           putInt(c);
        end
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_83(self):
        input = """
        function foo(): integer;
        var a, b: integer;
        begin
            a := 5;
            b := 6;
            if a < b then
                return 5;
            return 6;
        end
        procedure main();
        var a,b,c: integer;
        begin
           c := foo();
           putInt(c);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_84(self):
        input = Program([VarDecl(Id("arr"),ArrayType(1,5,IntType())),
        FuncDecl(Id("searchArr"),[VarDecl(Id("d"),ArrayType(1,5,IntType())),VarDecl(Id("a"),IntType()),
        VarDecl(Id("n"),IntType())],
        [VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(1),Id("n"),True,
        [Assign(ArrayCell(Id("d"),Id("i")),Id("i"))]),Return(ArrayCell(Id("arr"),IntLiteral(1)))],IntType()),
        FuncDecl(Id("main"),[],[VarDecl(Id("j"),IntType()),VarDecl(Id("result"),IntType())],
        [Assign(ArrayCell(Id("arr"),IntLiteral(1)),IntLiteral(5)),
        Assign(ArrayCell(Id("arr"),IntLiteral(2)),IntLiteral(3)),
        Assign(ArrayCell(Id("arr"),IntLiteral(3)),IntLiteral(11)),
        Assign(ArrayCell(Id("arr"),IntLiteral(4)),IntLiteral(19)),
        Assign(ArrayCell(Id("arr"),IntLiteral(5)),IntLiteral(20)),
        Assign(Id("result"),CallExpr(Id("searchArr"),[Id("arr"),IntLiteral(3),IntLiteral(5)])),
        CallStmt(Id("putInt"),[Id("result")]),Return(None)],VoidType())])
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_85(self):
        input = """ 
            procedure main();
            var i,j,k:integer;
            begin
                i:=0;
                j:=0;
                k:=0;
                while i <= 10.0 do
                    while j <= 10 do
                        while k <> 10 do
                        begin
                            k:= k + 2;
                            j:= j + 1;
                            i:= j + k;
                            putFloat(i);
                        end
            end"""
        expect = "3.06.09.012.015.0Time out\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_86(self):
        input = """
        procedure main();
        var a, b, res:integer;
        begin
            a := 1;
            b := 1;
            res := foo(a, b);
            putIntLn(res);
        end
        
        function foo(a:integer; b:integer):integer;
        begin
            if a=b
                then return 111;
                else return 222;
        end
        """
        expect = "111\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_87(self):
        input = """
        var i, j:integer;
        procedure main();
        var a, b, iSum:integer;
        begin
            i := 10;
            with i:real; do
            begin
                i := 11.8;
                putFloat(i);
            end
            i := 11;
            putIntLn(i);
        end
        """
        expect = "11.811\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_88(self):
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if iSum > 27 then break;
                if a mod 3=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "27"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_89(self):
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            a := b := iSum := 0;
            while a < 20 do
            begin
                b := 0;
                a := a + 1;
                while b < a do
                begin
                    b := b + 1;
                    if b > 10 then break;
                    if b mod 2=1 then continue;
                    iSum := iSum + b;
                end
                if a mod b=0 then continue;
                if a + b > 40 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "554"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_90(self):
        input = """
        procedure main();
        var a, iSum:integer;
        begin
            a := 0;
            iSum := 0;
            while a < 20 do
            begin
                a := a + 1;
                if a > 17 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "153"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_91(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            while a < 5 do
            begin
                putInt(a);
                a := a + 1;
            end
        end
        """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_92(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5 
            then
                if a mod 2=0
                then 
                    a := a * 2;
                else
                    begin
                    end
            else 
            begin
                a := 11;
                if a mod 3 <> 0 then a := a * 3;
            end
            putInt(a);
        end
        """
        expect = "33"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_93(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            if a > 1
                then a := 10;
            putIntLn(a);
        end
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_94(self):
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var a, b:integer;
            isTrue:boolean;
        begin
            a := 10;
            b := 11;
            isTrue := a > b ;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_95(self):
        input = """
        var arr:array[1 .. 4] of real;
        procedure main();
        var a:real;
            b:integer;
            isTrue:boolean;
        begin
            a := 11.0;
            b := 11;
            isTrue := a <= b ;
            putBoolLn(isTrue);
        end"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_96(self):
        input = """
        var a, b:real;
        procedure main();
        var fNum:real;
        begin
            a := 11.5;
            fNum := a;
            putFloat(fNum);
        end
        """
        expect = "11.5"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_97(self):
        input = """
        function foo(): integer;
        var a, b: integer;
        begin
            a := 5;
            b := 6;
            if a > b then
                return 5;
            else
                return 6;
        end
        procedure main();
        var a,b,c: integer;
        begin
           c := foo();
           putInt(c);
        end
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_98(self):
        input = """
        procedure main();
        var a, b, res:integer;
        begin
            a := 1;
            b := 1;
            res := foo(a, b);
            putIntLn(res);
        end
        
        function foo(a:integer; b:integer):integer;
        begin
            if a=b
                then return 111;
                else return 222;
        end
        """
        expect = "111\n"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_99(self):
        input = """
            var i : integer;
            procedure foo(i:integer);
            begin
                i := 1;
            end
            procedure main();
            begin  
                i := 2;
                foo(i);
                putInt(i);
            end
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
