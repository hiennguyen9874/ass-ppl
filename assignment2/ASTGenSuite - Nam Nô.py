import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
        end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_var_declare(self):
        input = """var a,b: integer;
                    c:real;"""
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_declare1(self):
        input = """var a: array[1 .. 3] of integer;"""
        expect = str(Program([VarDecl(Id('a'),ArrayType(1,3,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_var_main(self):
        input = """var a: boolean;
                    procedure main(); 
                    begin 
                        print(a);
                    end"""
        expect = str(Program([VarDecl(Id("a"),BoolType()),FuncDecl(Id("main"),[],[],[CallStmt(Id("print"),[Id("a")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_var_main1(self):
        input = """var a: boolean;
                    var b: array[2 .. 6] of real;
                    procedure main(); 
                    begin 
                        //b[2] := 1.;
                        print(a);
                    end"""
        expect = str(Program([VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),ArrayType(2,6,FloatType())),FuncDecl(Id("main"),[],[],[CallStmt(Id("print"),[Id("a")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_function(self):
        input = """function a(x,y:real):real;
            begin
                return 2.1;
            end
            """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[],[Return(FloatLiteral(2.1))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_function1(self):
        input = """function a():array[1 .. 4] of integer;
            var a,b:real;
            begin
                return 2.1;
            end
            """
        expect = str(Program([FuncDecl(Id("a"),[],[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[Return(FloatLiteral(2.1))],ArrayType(1,4,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_function2(self):
        input = """function a(y:array[2 .. 5] of integer):integer;
            var a,b:real;
            begin
                return 2.1;
            end
            """
        expect = str(Program([FuncDecl(Id("a"),[VarDecl(Id("y"),ArrayType(2,5,IntType()))],[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[Return(FloatLiteral(2.1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_procedure(self):
        input = """procedure a();
            var a,b:real;
            begin
                return;
            end
            """
        expect = str(Program([FuncDecl(Id("a"),[],[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[Return()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_procedure1(self):
        input = """procedure a(x,y:real;z:boolean);
            var a,b:real;
            begin
                f();
            end
            """
        expect = str(Program([FuncDecl(Id("a"),
            [VarDecl(Id("x"),FloatType()),
            VarDecl(Id("y"),FloatType()),
            VarDecl(Id("z"),BoolType())],
            [VarDecl(Id("a"),FloatType()),
            VarDecl(Id("b"),FloatType())],
            [CallStmt(Id("f"),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_if_stmt(self):
        input = """procedure main(); 
            begin 
                if a>2 then foo();
            end"""
        expect = str(Program([FuncDecl(Id("main"),
            [],[],
            [If(BinaryOp(">",Id("a"),IntLiteral(2)),[CallStmt(Id("foo"),[])],[])],
            VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_if_stmt1(self):
        input = """procedure main(); 
            begin 
                if (a>2) and (b=4) then a:=2;b:=3;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("and",BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(4))),[Assign(Id("a"),IntLiteral(2))],[]),Assign(Id("b"),IntLiteral(3))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_if_stmt2(self):
        input = """procedure main(); 
            begin 
                if a>2 then a:=2; else a:=4; foo();
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(2)),[Assign(Id("a"),IntLiteral(2))],[Assign(Id("a"),IntLiteral(4))]),CallStmt(Id("foo"),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_if_stmt3(self):
        input = """procedure main(); 
            begin 
                if a>2 then if a>4 then a:=4;else a:=2;foo(1,a);
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(2)),[If(BinaryOp(">",Id("a"),IntLiteral(4)),[Assign(Id("a"),IntLiteral(4))],[Assign(Id("a"),IntLiteral(2))])],[]),CallStmt(Id("foo"),[IntLiteral(1),Id("a")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_if_stmt(self):
        input = """procedure main(); 
            begin 
                if f(a,2)<2 then a:=2;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("<",CallExpr(Id("f"),[Id("a"),IntLiteral(2)]),IntLiteral(2)),[Assign(Id("a"),IntLiteral(2))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_assignment_stmt(self):
        input = """procedure main(); 
            begin 
                a:=2;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),IntLiteral(2))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_assignment_stmt1(self):
        input = """procedure main(); 
            begin 
                a:=b:=2;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("b"),IntLiteral(2)),Assign(Id("a"),Id("b"))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_assignment_stmt2(self):
        input = """procedure main(); 
            begin 
                a := b[10]:= foo()[3]:= x := 1 ;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_for_stmt(self):
        input = """procedure main(); 
            begin 
                for a:=1 to 10 do break;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),IntLiteral(10),True,[Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_for_stmt1(self):
        input = """procedure main(); 
            begin 
                for a:=1 to a(x,y) do foo();c:=7;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),CallExpr(Id("a"),[Id("x"),Id("y")]),True,[CallStmt(Id("foo"),[])]),Assign(Id("c"),IntLiteral(7))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_for_stmt2(self):
        """Simple program: int main() {} """
        input = """procedure main(); 
            begin 
                for a:=1 to 2+3 do if a mod 3 then foo(); g(a);
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),BinaryOp("+",IntLiteral(2),IntLiteral(3)),True,[If(BinaryOp("mod",Id("a"),IntLiteral(3)),[CallStmt(Id("foo"),[])],[])]),CallStmt(Id("g"),[Id("a")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_for_stmt3(self):
        input = """procedure main(); 
            begin 
                for a:=(6+x)*y to f(2)[2] do b:=foo();
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(6),Id("x")),Id("y")),ArrayCell(CallExpr(Id("f"),[IntLiteral(2)]),IntLiteral(2)),True,[Assign(Id("b"),CallExpr(Id("foo"),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_while_stmt(self):
        """Simple program: int main() {} """
        input = """procedure main(); 
            begin 
                while 1 do foo();
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[CallStmt(Id("foo"),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_while_stmt1(self):
        input = """
        var a: integer;
        procedure main(); 
            begin 
                while a>3 do foo(a);a:=a+1;
            end"""
        expect = str(Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],[],[While(BinaryOp(">",Id("a"),IntLiteral(3)),[CallStmt(Id("foo"),[Id("a")])]),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_while_stmt2(self):
        input = """procedure main(); 
            begin 
                while true do x:=1; while a(x) do foo(x);x:=x+1;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BooleanLiteral("true"),[Assign(Id("x"),IntLiteral(1))]),While(CallExpr(Id("a"),[Id("x")]),[CallStmt(Id("foo"),[Id("x")])]),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_while_stmt3(self):
        input = """procedure main(); 
            begin 
                while a=b do foo();a := b[10]:= foo()[3]:= x := 1 ;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_while_break(self):
        input = """procedure main(); 
            begin 
                while a=b do 
                foo();
                a := b[10]:= foo()[3]:= x := 1 ;
                if a=5 then break;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10))),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Break()],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_while_continue(self):
        input = """procedure main(); 
            //var a,b:integer;
            begin 
                while a=b do 
                foo();
                a := b[10]:= foo()[3]:= x := 1 ;
                if a=5 then break;
                g(a)[1]:=2;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10))),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Break()],[]),Assign(ArrayCell(CallExpr(Id("g"),[Id("a")]),IntLiteral(1)),IntLiteral(2))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_function3(self):
        input = """
            var a,b: integer;
            function f():integer; 
            begin 
                while a=b do 
                foo();
                a := b[10]:= foo()[3]:= x := 1 ;
                if a=5 then break;
                return a;
            end"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("f"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10))),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Break()],[]),Return(Id("a"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_compound(self):
        input = """procedure main(); 
        begin
        print("Nam dep trai");
        begin
        foo();
        end
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("print"),[StringLiteral("Nam dep trai")]),CallStmt(Id("foo"),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_arr_decl(self):
        input = """var i:array [-3 .. -2] of integer;
        procedure main();
        begin
        end
        var j,x:array [-1 .. -2] of string;"""
        expect = str(Program([VarDecl(Id("i"),ArrayType(-3,-2,IntType())),FuncDecl(Id("main"),[],[],[],VoidType()),VarDecl(Id(("j")),ArrayType(-1,-2,StringType())),VarDecl(Id("x"),ArrayType(-1,-2,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,332))


    def test_if_stmt4(self):
        input = """procedure main(); 
        begin
        if a > 3 then if a < 6 then a := 1; 
        else a := 3; else a := 6;
        end """
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(3)),[If(BinaryOp("<",Id("a"),IntLiteral(6)),[Assign(Id("a"),IntLiteral(1))],[Assign(Id("a"),IntLiteral(3))])],[Assign(Id("a"),IntLiteral(6))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_var_main2(self):
        input = """procedure main(a:INTEGER;b:real;c:real;d:boolean;e:boolean;f:boolean);
        var b:rEAL;c:boolean;d:boolean;e,f,h:array[1 .. 2] of real;
        begin
        end"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id(("a")),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),BoolType()),VarDecl(Id("e"),BoolType()),VarDecl(Id("f"),BoolType())],[VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),BoolType()),VarDecl(Id("e"),ArrayType(1,2,FloatType())),VarDecl(Id("f"),ArrayType(1,2,FloatType())),VarDecl(Id("h"),ArrayType(1,2,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_with(self):
        input = """procedure main(); 
        begin 
        with a:real;b,c:boolean;d:INTEGER; do begin
        with a:integer; do begin foo(); end
        with b:real;c,d:integer; do begin end
        end
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),IntType())],[With([VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[])]),With([VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_op(self):
        input = """procedure main(); 
        begin
        a := a > b or else not c >= d;
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("a"),BinaryOp("orelse",BinaryOp(">",Id("a"),Id("b")),BinaryOp(">=",UnaryOp("not",Id("c")),Id("d"))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_for_stmt4(self):
        input = """procedure main(); 
        begin
        for a := 4 downto 10 do begin end
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(4),IntLiteral(10),False,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))

#     def test_all(self):
#         input = """function foo(n:integer;x:array[1 .. 10] of integer):array [1 .. 10] of integer;
# var b:array[1 .. 10] of integer;
# begin
#     with i:integer; do 
#         if n > 0 then
#             for i := n downto a[n] do begin
#                 b[i] := a[i] + x[i];
#                 if i = a[x[i]] then
#                     return x;
#                 else
#                     continue;
#             end
#         else
#             for i := 1 to n mod a[n] do begin
#                 b[i] := a[i] and then x[i] or else b[i];
#                 if a[x[i]] then
#                     return x;
#                 else
#                     break;
#             end
#     return foo(foo(x),a[x[n]]);
# end
# procedure main(); 
# var i:integer;
# begin
#     i := getIntLn();
#     foo(a,i);
#     with i:integer; do
#         for i := 1 to 10 do
#             putIntLn(a[i]);
# end
# var a:array[1 .. 10] of integer;"""
#         expect = str(Program([FuncDecl(Id("main"),[],[],[For("a",IntLiteral(4),IntLiteral(10),False,[])],VoidType())]))
#         self.assertTrue(TestAST.test(input,expect,338))