import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_var_1(self):
        input = """
        var a,b: real;
            c: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_function_2(self):
        input = """
        function inc(y:real):real;
             var x:boolean;
            begin
                y := x+1;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_procedure_3(self):
        input = """
        procedure main();
            begin
                return;
                foo(x);
                goo(yy);
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_procedure_4(self):
        input = """
        procedure main();
            begin
                for i:=1 to n do
                    foo(x);
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):
        input = """
        procedure main();
            begin
                while i>1 do
                    break;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_simple_program6(self):
        input = """
        function main() : real;
            begin
               continue;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_function_7(self):
        input = """
        function main() : real;
            begin
               retunr 5;
            end
        """
        expect = "Error on line 4 col 22: 5"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_function_8(self):
        input = """
        function main() : real;
            begin
               return 5 ;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program9(self):
        input = """
            begin end
        """
        expect = "Error on line 2 col 12: begin"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program10(self):
        input = """
            procedure findMin(x, y, z: integer;m: integer);
                (* Finds the minimum of the 3 values *)
                begin
                    if x < y then m := x; else m := y;
                    if z <m then
                        m := z;
                end { end of procedure findMin }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_simple_program11(self):
        input = """
           var num, f: integer;
            function fact(x: integer): integer; (* calculates factorial of x - x! *)
                begin
                    if x=0 then
                        fact := 1;
                    else
                    fact := x * fact(x+1); (* recursive call *)
                end { end of function fact}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_var_12(self):
        input = """
            var num : integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_assstm_procedure_13(self):
        input = """
            procedure main();
                begin
                 b := (a+5);
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_with_14(self):
        input = """
            procedure main();
                begin
                    with a: integer ;do d = c[a] + b; do w
                end
        """
        expect = "Error on line 4 col 52: ;"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_with_15(self):
        input = """
            procedure main();
                begin
                    with a,b: integer ;c: array [1 .. 2] of real; 
                    do d := c[a] + b;
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_doublewith_16(self):
        input = """
            var c: integer;
            procedure main();
                begin
                    with a: integer; do with b : real do a = 1;
                end
        """
        expect = "Error on line 5 col 54: do"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_simple_notvar_17(self):
        input = """
        var a:integer;
        procedure main();
            a,d:integer;
             b,c real;
        begin
        end
        """
        expect = "Error on line 4 col 12: a"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_lhs_ass_18(self):
        input = """
        procedure main();
	        begin
	            a := b[2]  := foo();
	        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_simple_call_19(self):
        input = """
        procedure main();
	        begin
	            foo();
	        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_compuond_20(self):
        input = """
            procedure main();
                begin
                    var c: integer;
                    a := a + b;
                end
        """
        expect = "Error on line 4 col 20: var"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_procedure_21(self):
        input = """
        procedure main();
        begin
            foo(5,foo(),a[3+a]);
            foo(5,a;b)
        end
        """
        expect = "Error on line 5 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_procedure_22(self):
        input = """
        procedure main();
        begin
            with a,c:REAl;b,d,y:INTeger;m:BOOLean; do with a:integer; do a := 1;
            with a:integer; do with b:integer do a := 1;
        end
        """
        expect = "Error on line 5 col 46: do"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_procedure_23(self):
        input = """
        procedure main();
        begin
            if a=1 then a:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_procedure_24(self):
        input = """
        procedure main();
        begin
            while a=1
            do
            foo()[2]:=a:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_procedure_25(self):
        input = """
        procedure main();
        var x,y:real;
            a,b,c:array [1 .. 2] integer;
        begin
            break;
        end
        """
        expect = "Error on line 4 col 33: integer"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_procedure_226(self):
        input = """
        procedure main();
        begin
            continue
        end
        """
        expect = "Error on line 5 col 8: end"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_procedure_227(self):
        input = """
        procedure main();
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_procedure_228(self):
        input = """
        function foo():real;
        begin
        if a=true then a:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_procedure_229(self):
        input = """
        procedure main(); 
            begin
            for a := 1 to 3 do with a:integer; do for a := 1 downto 1 do a := a + 1;
            for a := 1 to 10 do for b :=1 to 10 do a:= 1;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_for_30(self):
        input = """
        pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        x:=foo(10);
                    end
                   END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_break_31(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_continue_32(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (a=1) do continuE ;
                   END
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_return_33(self):
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (a=1) do reTuRn ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_return_34(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (a=1) do return foo(a+1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_compound_35(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    while (1=1) do begin eND
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_call_36(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_call_37(self):
        input = """function foo(c: real): integer;
                   begin
                    foo(3,a+1,a<>1,a[1]);
                    return 1;
                   end
                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_call_38(self):
        input = """function foo(c: real): real;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo2();
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_call_39(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_call_40(self):
        input = """
        function foo(c: real): integer;
                   BEGIN
                    textbackground(brown); {background colour}
                    return func(a(1,2));
                   END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_multi_40(self):
        input = """
                procedure test1() ;
                begin
	               if a=1 then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
	               end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_multi_41(self):
        input = """
                procedure test2() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   begin
                   eND
               else c := 1;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_multi_43(self):
        input = """
                var i: integer ;
                function f(): integer ;
                begin
	               return 200;
                end
                procedure main() ;
                var
	               main: integer ;
                begin
	               main := f() ;
                end
                var g: real ;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_multi_44(self):
        input = """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_multi_45(self):
        input = """
                Var
                    Num1, Num2, Sum : Integer;
                Procedure concaheo(a, c:Real);
                Begin
                    Sum := Num1 + Num2; {phep cong}
                    Write(Sum);
                    Readln();
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_multi_46(self):
        input = """
                Var name, surname: String;
                Procedure Main();
                Begin
	               write("Nhap ten cua ban:");
	               readln(name);
	               writeln("Ten day du cua ban la : ",name);
	               readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_multi_47(self):
        input = """
                Var PD, Dname, Cmodel : String;
                CostPD, TCostPD, Distance : Real;
                {real is a decimal (described later on)}
                Procedure main();
                Begin
                	textbackground(brown); {background colour}
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_multi_48(self):
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 return ;
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_multi_49(self):
        input = """
                procedure main() ;
                beGin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_multi_50(self):
        input = """
                procedure main() ;
                var a: array[0 .. m-1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n - 2 do
                        temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                    print(a);
                eND
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_multi_51(self):
        input = """
                function real_array(a: array[0 .. m-1] of real;n:integer):real;
                var i:integer;s:real;
                begin
                    s:=0.;
                    for i:=n-1 downto 0 do s:=s+a[i];
                    return s;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_multi_52(self):
        input = """
                Procedure foo(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("So luong phan tu:");
                Readln( N);
                For i:=0 to N do
                    a:=a+1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_multi_53(self):
        input = """
                Function Tong():real;
                Var S,i :Integer;
                Begin
                	S:=0;
                	For i:=0 to N do
                	If(A[i] mod 5=0) then
                	S := S+A[i];
                	return S;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_multi_54(self):
        input = """
                Function foo(N:Integer) :Integer;
                Var i:Integer;
                Begin
                 For i:=2 to N-1 do
                  If(N mod i = 0) then
                    return 0;
                  Else
                    return 1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_multi_55(self):
        input = """
                Function foo():integer;
                Var Count : Integer;
                Begin
                 Count := Count+1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_multi_56(self):
        input = """
                Procedure foo();
                Var i:Integer;
                Begin
                 For i:=0 to N do
                    a:=1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_multi_57(self):
        input = """
                Procedure thay();
                Var i,k:Integer;
                Begin
                 
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_multi_58(self):
        input = """
                Function a(N:Integer ) : Boolean;
                begin 
                    a:=1;
                    if a=1 then a:=2;
                    return 1;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_multi_59(self):
        input = """
                Function foo ( A:array[0 .. 10] of REAL) : Boolean;
                Var flag : Boolean;
                 i :Integer;
                begin
                    return 0;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_multi_60(self):
        input = """
                Function foo():real;
                Var flag :boolean;
                i :Integer;
                Begin
                    a:=a+1;
                    b:=b*a;
                    c:=a+b*a;
                    if a=a then return;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_multi_61(self):
        input = """
                Procedure Chen();
                Var i :Integer;
                Begin
                 For i:=N downto k+ 1 do
                  A[i] := A[i-1];
                 A[k] := X;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_multi_62(self):
        input = """
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_multi_63(self):
        input = """
                function fibo(x: integer): integer;
                var f1,f2: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  return fibo(x-2)+ fibo(x-1);
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_multi_64(self):
        input = """
                function ok(i : integer):boolean;
                var k : integer;
                begin
                 ok := true;
                 for k := 2 to i div 2 do
                  if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    ok := false;
                    exit();
                   end
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_multi_65(self):
        input = """
                Procedure Daoso(n: integer);
                Begin
                 Assign(f,fo);
                 Close(f);
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_multi_66(self):
        input = """
                Function UCLN(m,n:integer):integer;
                Begin
                 If(m=n) then RETURN m ;
                 else
                  If (m>n) then return UCLN(m-n,n);
                  else return UCLN(m,n-m);
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_multi_67(self):
        input = """
                Var r,dt,cv:real;
                pROCEDURE main() ;
                Begin
                 Clrscr();
                 Readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_multi_68(self):
        input = """
                pROCEDURE main() ;
                Var a,b,x:real;
                Begin
                Clrscr();
                a:=1;
                b:=a;
                c:=a*a*a*a+b*b*b*b+c*c*c*c;
                Readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_multi_69(self):
        input = """
                Var a,b,c,s,p: real;
                pROCEDURE main() ;
                Begin
                Clrscr();
                printf("Ass kho qua thay oi!");
                Readln();
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_multi_70(self):
        input = """
                Procedure foo(a:integer;b:real)
                begin
                if (a=b and b mod a = 2 )
                    then 
                    return;
                End
                """
        expect = "Error on line 3 col 16: begin"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_multi_71(self):
        input = """
              (
              var i: integer;
              )()
              """
        expect = "Error on line 2 col 14: ("
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_multi_72(self):
        input = """
               var i: integer;
               )()
               """
        expect = "Error on line 3 col 15: )"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_multi_73(self):
        input = """
        procedure main(); 
            begin
            foo(5,foo(),a[3+a]);
            foo(5,a;b);
            end
               """
        expect = "Error on line 5 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_simple_74(self):
        input = """
        procedurE foo (b : real) ;
            begin
             1[1] := 1;
             (1>=0)[2] := 2+a[1]+c+("abc"< 0);
             ahihi(1)[m+1] := 3;
             (1+a[1]+(1<0))[10] := 4;
            End
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_simple_75(self):
        input = """
        procedure TGList(Item: integer);
        begin
            SetLength(Items, Length(Items) + 1);  
            Items[Length(Items) - 1] := Item;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_hello_world_76(self):
        input = """
        Program Lesson1_Program1;
        Begin
            Write('Hello World. Prepare to learn PASCAL!!');
            Readln;
        End
        """
        expect = "Error on line 2 col 8: Program"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_hello_world_77(self):
        input = """
        Var       
            Num1, Num2, Sum : Integer;

        Begin {no semicolon}
            Write('Input number 1:'); 
            Readln(Num1);
            Writeln('Input number 2:');
            Readln(Num2);
            Sum := Num1 + Num2; {addition} 
            Writeln(Sum);
            Readln;
        End
        """
        expect = "Error on line 5 col 8: Begin"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_all_278(self):
        input = """
        Var n,i,x : integer;
        a: array [1 .. 2] of integer;
        procedure foo();
        begin
        clrscr();
        write("Nhap so phan tu: ");
        readln(n);
        for i:=1 to n do
        begin
            write("Phan tu thu ',i,'= ");
            readln(a[i]);
        end
        writeln("Cac so chinh phuong co trong mang:");
        for i:=1 to n do
        begin
            x:=trunc(sqrt(a[i]));
            if sqr(x)=a[i] then
            write(a[i]=4);
        end
        readln();
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_var_79(self):
        input = """
            var a, b, c: integer;
                e,f: real;
                i: boolean;
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_var_80(self):
        input = """
           var a , b , c : integer ;
                d : array [ 1 .. 5 ] of integer ;
                e , f : real ;
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_var_81(self):
        input = """
           var
                age, weekdays : integer;
                taxrate, net_income: real;
                choice, isready: boolean;
                initials, grade: string;
                name, surname : string;
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_var_82(self):
        input = """
           var a,b:integer;
           var c,d : string;
           var arr:array [1 .. 5] of boolean;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_var_83(self):
        input = """
           var  a,b: int;
                c,d : double;
        
        """
        expect = "Error on line 2 col 21: int"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_var_84(self):
        input = """
           var  _arr: array [1+y .. 2*x] of string; 
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_var_85(self):
        input = """
           var a,b; integer;
           c: array [1 .. 5] of iteger;
        
        """
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_var_86(self):
        input = """
           var a : array [1 .. 10 ] of real; {array real 10 member} 
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_var_87(self):
        input = """
           (*khai bao mot array string va 2 bien integer*)
           var  a_1,b_1:integer;
                arr_string: array [1 .. 12] oF String;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_var_88(self):
        input = """
           var  A_rot_1: reAl;
           var  B_rot_1:reaL;
        //        B_rot_2:integer
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_funtion_89(self):
        input = """
            function ReadString(message: String): String;
                var temp: String;
                begin
                    Write(message );
                    ReadLn(temp);
                    result := temp; //result is the value returned
                end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_funtion_90(self):
        input = """
            function CircleArea(radius: real): real;
                var area: Real;
                begin
                    area := PI * radius * radius;
                    result := area;
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_funtion_91(self):
        input = """
            FuncTion foo(): string;
            // khong khai bao
                begin
                begin
                end
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_funtion_92(self):
        input = """
           function Highest(v1, v2, v3: Integer): Integer;
                begin
                    if ((v1 > v2) and (v1 > v3)) then
                    begin
                        result := v1;
                    end 
                    else if v2 > v3 then
                    begin
                        result := v2;
                    end
                    else
                    begin
                        result := v3;
                    end
                end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_funtion_93(self):
        input = """
           Function foo(a:real;a:real;c:real):real;
           // khai bao
           var _ysh: real;
           
        
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_funtion_94(self):
        input = """
           Function foo(a:real,a:real):real;
           //khai bao
           var _ysh: real;
        
        """
        expect = "Error on line 2 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_funtion_95(self):
        input = """
           funcTion 12add (a,b:integer):integer;
           var c:interger;
           begin 
                c= a+b;
            end
        
        """
        expect = "Error on line 2 col 20: 12"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_funtion_96(self):
        input = """
             FuncTion foo(): string;
            // khong khai bao
                begin
                begin
                end
        
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_funtion_97(self):
        input = """
           
            Function main():integer;
                begin
                    if ((v1 > v2) and (v1 > v3)) then
                    begin
                        result := v1;
                    end 
                end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_funtion_98(self):
        input = """
           function sphere(radius: real): array [1 .. 20] of real;
                {$ifdef CPUx86_64}
                
                {$asmMode intel}
                var
                    r: real;
                begin end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_funtion_99(self):
        input = """
        FuncTion foo(): string;
        BEGIN
        clrscr();
        write("Nhap so phan tu: ");
        readln(n);
        for i:=1 to n do
        begin
            write("Phan tu thu ',i,'= ");
            readln(a[i]);
        end
        writeln("Cac so chinh phuong co trong mang:");
        for i:=1 to n do
        begin
            x:=trunc(sqrt(a[i]));
            if sqr(x)=a[i] then
            write(a[4]);
        end
        readln();
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test_funtion_100(self):
        input = """
        Function kt(n:integer):boolean;
        var i,d:integer;
        begin
        kt:=false;
        d:=0;
        For i:=1 to n do
            if n mod i=0 then inc(d);
        if d=2 then kt:=true;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
