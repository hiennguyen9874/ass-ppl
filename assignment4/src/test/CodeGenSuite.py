import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putInt"),[BinaryOp('+',IntLiteral(5),IntLiteral(1))])])])
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[FloatLiteral(5.0)])])])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_float1_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloatLn"),[FloatLiteral(7.0)])])])
        expect = "7.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,503))
        
    def test_float_int_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "7.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))
        
    def test_int_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('+',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "7.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))    
        
    def test_float_int_ast1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('-',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))
        
    def test_int_float_ast1(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('-',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))
        
    def test_int_float_ast2(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('*',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
        
    def test_float_int_ast2(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('*',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))    
    
    def test_int_float_ast3(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('/',IntLiteral(5),FloatLiteral(2.0))])])])
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_float_int_ast3(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[BinaryOp('/',FloatLiteral(5.0),IntLiteral(2))])])])
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_boolean(self):
        input = """
        procedure main(); begin putBool(true); end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_boolean1(self):
        input = """
        procedure main(); begin putBoolLn(true); end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_boolean2(self):
        input = """
        procedure main(); begin putBool(false); end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_boolean3(self):
        input = """
        procedure main(); begin putBoolLn(false); end
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_string(self):
        input = """
        procedure main(); begin putString("ahihi"); end
        """
        expect = "ahihi"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_string1(self):
        input = """
        procedure main(); begin putStringLn("ahihi"); end
        """
        expect = "ahihi\n"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_int1(self):
        input = """
        procedure main(); begin putInt(400000); end
        """
        expect = "400000"
        self.assertTrue(TestCodeGen.test(input,expect,518))

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
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_if(self):
        input = """
        procedure main();
        var i: real;
            begin
                if False then i:=1; else i:=2;
                putFloat(i);
            end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_while(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,521))