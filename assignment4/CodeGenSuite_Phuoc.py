import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):

    def test_int(self):
        input = """
        procedure main();
        var a:integer;
        begin
        a := 1;
        putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_03(self):
        input = """
        procedure main();
        begin
        putFloat(100.02);
        end
        """
        expect = "100.02"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_04(self):
        input = """
        procedure main();
        begin
        putFloat(1.4315E7);
        end
        """
        expect = "1.4315E7"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_05(self):
        input = """
        procedure main();
        begin
        putFloat(121.5E5);
        end
        """
        expect = "1.215E7"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_06(self):
        input = """
        procedure main();
        begin
            if (true)
                then putInt(1);
                else putInt(2);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_07(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := 4;
            putFloatLn(foo(a));
        end
        function foo(a:integer):real;
        var foo:integer;
        begin
            foo := 5;
            return foo + a;
        end 
        """
        expect = """9.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_08(self):
        input = """
        procedure main();
        begin
            putIntLn(000);
        end
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_09(self):
        input = """        
        procedure main();
        begin
            putFloatLn(1.0);
        end"""
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_10(self):
        input = """
        procedure main();
        begin
            putFloatLn(10.5);
        end
        """
        expect = "10.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_11(self):
        input = """
        procedure main();
        begin
            putFloatLn(100.14);
        end
        """
        expect = "100.14\n"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_12(self):
        input = """
        procedure main();
        begin
            putBoolLn(true);
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_13(self):
        input = """
        procedure main();
        begin
            putStringLn("programming");
        end
        """
        expect = "programming\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
        input = """
        var a:integer;
        var b:real;
        procedure main();
        begin
            a := 10;
            b := 1.0;
            putInt(a);
        end
        var c:boolean;
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    # def test_15(self):
    #     input =  """
    #     var a:array[1 .. 5] of integer;
    #     procedure main();
    #     begin
    #         putInt(10);
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))
        
    # def test_16(self):
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     begin
    #         putInt(10);
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))

    # def test_17(self):
    #     """Program => Test global variable and function whose return type is voidtype."""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     begin
    #         putInt(10);
    #     end
        
    #     procedure pvoid();
    #     begin
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))

    # def test_18(self):
    #     """Program => Main function: declared variable primitive type"""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     var a:integer;
    #         b:real;
    #     begin
    #         putInt(10);
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))


    # def test_19(self):
    #     """Program => Main function: It's declared variable primitive and array type"""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
    #     begin
    #         putInt(10);
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))

    # def test_20(self):
    #     """Program => funcVoid function: It's declared variable primitive type in parameter and body"""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
    #     begin
    #         putInt(10);
    #     end
        
    #     procedure pvoid();
    #     var c:integer;
    #         c, e, f:real;
    #     begin
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))
        
    # def test_21(self):
    #     """Program => funcVoid function: It's declared variable primitive and array type in parameter and body"""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         frr:array[1 .. 4] of real;
    #         arr:array[1 .. 5] of integer;
    #     procedure main();
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
    #     begin
    #         putInt(10);
    #     end
        
    #     procedure pvoid();
    #     var c:integer;
    #         c, e, f:real;
    #         funcFrr:array[1 .. 10] of real;
    #     begin
    #     end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))

    # def test_22(self):
    #     """Program => manipulate data in Main function: simple assign the IntLiteral value to global variable IntType."""
    #     input = """
    #     var a:integer;
    #         arr:array[1 .. 5] of integer;
        
    #     procedure main();
    #     begin
    #         a := 1;
    #         putIntLn(a);
    #     end
    #     """
    #     expect = "1\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))

    # def test_23(self):
    #     """Program => manipulate data in Main function: simple assign the FloatLiteral value to global variable FloatType."""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
        
    #     procedure main();
    #     begin
    #         b := 10.5;
    #         putFloatLn(b);
    #     end
    #     """
    #     expect = "10.5\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))

    # def test_24(self):
    #     """Program => manipulate data in Main function: simple assign the BoolLiteral value to global variable BoolType."""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
    #         isTrue:boolean;
    #     procedure main();
    #     begin
    #         isTrue := false;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))

    # def test_25(self):
    #     """Program => manipulate data in Main function: simple assign the StringLiteral value to global variable StringType."""
    #     input = """
    #     var a:integer;
    #         b:real;
    #         arr:array[1 .. 5] of integer;
    #         isTrue:boolean;
    #     procedure main();
    #     begin
    #         putStringLn("testString");
    #     end
    #     """
    #     expect = "testString\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))
     

    def test_30(self):
        """Program => manipulate data in Main function: simple assign the IntLiteral value to local variable IntType."""
        input = """
        var a, b:integer;
        procedure main();
        var iNum:integer;
        begin
            iNum := 9;
            putInt(iNum);
        end
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,530))
        
    def test_31(self):
        """Program => manipulate data in Main function: simple assign the FloatLiteral value to local variable FloatType."""
        input = """
        var a, b:integer;
        procedure main();
        var fNum:real;
        begin
            fNum := 9.15;
            putFloat(fNum);
        end
        """
        expect = "9.15"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_32(self):#
        """Program => manipulate data in Main function: simple assign the BoolLiteral value to local variable BoolType."""
        input = """
        var a, b:integer;
        procedure main();
        var isTrue:boolean;
        begin
            isTrue := true;
            putBool(isTrue);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,532))

        
    def test_36(self): #
        """Program => manipulate data in Main function: Assign the int value to local variable FloatType (have coercion)."""
        input = """
        var a, b:integer;
        procedure main();
        var fNum:real;
        begin
            fNum := 19;
            putFloat(fNum);
        end
        """
        expect = "19.0"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_37(self):#
        """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type: IntType"""
        input = """
        var a, b:integer;
        procedure main();
        var iNum:integer;
        begin
            a := -1;
            iNum := a;
            putInt(iNum);
        end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_38(self):
        """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type - FloatType"""
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
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_40(self):
        """Program => manipulate data in Main function: Assign var to var (global & local), coercion int to float"""
        input = """
        var fNum:real;
        procedure main();
        var iNum:integer;
        begin
            iNum := 14;
            fNum := iNum;
            putFloat(fNum);
        end
        """
        expect = "14.0"
        self.assertTrue(TestCodeGen.test(input,expect,540))
        
    def test_41(self):
        """Program => manipulate data in Main function: Assign recur 2 times: true and false"""
        input = """
        var fNum:real;
        procedure main();
        var isT, isTrue:boolean;
        begin
            isT := false;
            isTrue := true;
            isT := isTrue;
            putBool(isT);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,541))


    # def test_59(self):
    #     """Program => manipulate data in Main function: Operator are < ; operand is IntLiteral"""
    #     input = """
    #     var arr:array[1 .. 4] of real;
    #     procedure main();
    #     var a, b:integer;
    #         isTrue:boolean;
    #     begin
    #         a := 10;
    #         b := 11;
    #         isTrue := a > b ;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,559))

    # def test_60(self):
    #     """Program => manipulate data in Main function: Operator are <= ; operand is FloatLiteral"""
    #     input = """
    #     var arr:array[1 .. 4] of real;
    #     procedure main();
    #     var a:real;
    #         b:integer;
    #         isTrue:boolean;
    #     begin
    #         a := 11.0;
    #         b := 11;
    #         isTrue := a <= b ;
    #         putBoolLn(isTrue);
    #     end"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,560))
   


    def test_73(self):
        """Program => manipulate data in Main function: Combine operator: +,/,%,<,>,<=,>="""
        input = """
        var a,b,c:integer;
            fa,fb,fc:real;
        procedure main();
        var isTrue:boolean;
        begin
            a := 1;
            b := a + 1;
            c := b mod 1;
            fa := (a + b) div (c + a);
            fb := (fa + a) / (c + b);
            fc := fa * fb / c;
            isTrue := fa <= fb;
            putBoolLn(isTrue);
        end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,573))
        

    def test_76(self):
        """Program => manipulate data in Main function: if no else stmt"""
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
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
        """Program => manipulate data in Main function: return stmt"""
        input = """
        procedure main();
        var a:real;
        begin
            a := ax(2);
            putFloat(a);
        end
        
        function ax(a:integer):real;
        begin
            if a=2
                then return 1.2;
                else return 2.0;
        end
        """
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_78(self):
        """Program => manipulate data in Main function: return void stmt"""
        input = """
        procedure main();
        begin
            foo(10);
        end
        
        procedure foo(a:integer);
        begin
            if a > 1
                then return;
                else
                    begin
                        a := a + 2;
                        return;
                    end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
        """Program => manipulate data in Main function:another return void stmt and print Int"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 1;
            test(a);
        end
        
        procedure test(a:integer);
        begin
            putInt(a);
        end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_80(self):
        """Program => manipulate data in Main function: if-else stmt simple!(enter thenStmt)"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 1
                then a := 10;
                else a := 11;
            putInt(a);
        end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,580))
        
    def test_81(self):
        """Program => manipulate data in Main function: if-else stmt simple!(enter elseStmt)"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5
                then a := 10;
                else a := 11;
            putInt(a);
        end
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_82(self):
        """Program => manipulate data in Main function: if no else stmt inner if-else stmt"""
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
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_83(self):
        """Program => manipulate data in Main function: if-else stmt inner if-else stmt"""
        input = """
        procedure main();
        var a:integer;
        begin
            a := 2;
            if a > 5 then
                if a mod 2=0 then
                    a := a * 2;
                else
                begin
                end
            else begin
                a := 11;
                if a mod 3 <> 0 then
                    a := a * 3 div 2;
            end
            putInt(a);
        end
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_84(self):
        """Program => manipulate data in Main function: dowhile stmt simple!"""
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
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_85(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It has continue stmt!"""
        input = """
        procedure main();
        var a, iSum:integer;
        begin
            a := 0;
            iSum := 0;
            while a < 20 do
            begin
                a := a + 1;
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
    def test_86(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It has break stmt!"""
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
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_87(self):
        """Program => manipulate data in Main function: dowhile stmt simple - It have continue stmt & break stmt!"""
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
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "81"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_88(self):
        """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt!"""
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
                    iSum := iSum + b;
                end
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "1750"
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_89(self):
        """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt complex: It have break and continue stmt!"""
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
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_90(self):
        """Program => manipulate data in Main function: for stmt simple"""
        input = """
        procedure main();
        var a:integer;
        begin
            for a := 0 to 10 do
            begin
                putInt(a);
                break;
            end
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,590))
        
    def test_91(self):
        """Program => manipulate data in Main function: for stmt simple: It has continue stmt"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if a mod 2=0 then continue;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_92(self):
        """Program => manipulate data in Main function: for stmt simple: It has break stmt"""
        input = """
        procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                if iSum > 27 then break;
                iSum := iSum + a;
            end
            putInt(iSum);
        end
        """
        expect = "28"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_93(self):
        """Program => manipulate data in Main function: for stmt simple: It have continue stmt and break stmt"""
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
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_94(self):
        """Program => manipulate data in Main function: for stmt innner for stmt: It have continue stmt and break stmt"""
        input = """procedure main();
        var a, b, iSum:integer;
        begin
            iSum := 0;
            for a := 0 to 9 do
            begin
                for b := 0 to a - 1 do
                begin
                    if a + b > 17 then break;
                    if b mod 2=0 then continue;
                    iSum := iSum + b;
                end
                if iSum > 27 then break;
                if a mod 3 <> 0 then continue;
                iSum := iSum + a;
            end
            putIntLn(iSum);
        end
        """
        expect = "37\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_95(self):
        """Program => manipulate data in Main function: block inner main block"""
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
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_96(self):
        """Program => manipulate data in Main function: block inner block"""
        input = """
        var i, j:integer;
        procedure main();
        var a, b, iSum:integer;
        begin
            i := 10;
            with i:real; do
            begin
                i := 14.3;
                with i:integer; do
                begin
                    i := 19;
                    putInt(i);
                end
                putFloat(i);
            end
            putInt(i);
        end
        """
        expect = "1914.310" 
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_97(self):
        """Program => Funcall is stmt in main function"""
        input = """
        var a:integer;
        procedure main();
        var b:integer;
            c:real;
        begin
            b := 5;
            c := foo(b);
            putFloat(c);
        end
        
        function foo(a:integer):integer;
        begin
            return a * a;
        end
        """
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input,expect,597))



    def test_101(self):
        """Program => return stmt in if-else stmt in function call"""
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
        self.assertTrue(TestCodeGen.test(input,expect,601))