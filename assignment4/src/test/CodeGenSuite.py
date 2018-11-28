import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
#     def test_int(self):
#         input = """
#         procedure main(); 
#         begin 
#             putInt(100); 
#         end
#         """
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,500))
    
#     def test_int_ast(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putInt"),[BinaryOp('+',IntLiteral(5),IntLiteral(1))])])])
#         expect = "6"
#         self.assertTrue(TestCodeGen.test(input,expect,501))
        
#     def test_float_ast(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[FloatLiteral(5.0)])])])
#         expect = "5.0"
#         self.assertTrue(TestCodeGen.test(input,expect,502))
        
#     def test_float1_ast(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloatLn"),[FloatLiteral(7.0)])])])
#         expect = "7.0\n"
#         self.assertTrue(TestCodeGen.test(input,expect,503))
        
#     def test_float_int_ast(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(5.0),IntLiteral(2))])])])
#         expect = "7.0"
#         self.assertTrue(TestCodeGen.test(input,expect,504))
        
#     def test_int_float_ast(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('+',IntLiteral(5),FloatLiteral(2.0))])])])
#         expect = "7.0"
#         self.assertTrue(TestCodeGen.test(input,expect,505))    
        
#     def test_float_int_ast1(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('-',FloatLiteral(5.0),IntLiteral(2))])])])
#         expect = "3.0"
#         self.assertTrue(TestCodeGen.test(input,expect,506))
        
#     def test_int_float_ast1(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('-',IntLiteral(5),FloatLiteral(2.0))])])])
#         expect = "3.0"
#         self.assertTrue(TestCodeGen.test(input,expect,507))
        
#     def test_int_float_ast2(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('*',IntLiteral(5),FloatLiteral(2.0))])])])
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,508))
        
#     def test_float_int_ast2(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('*',FloatLiteral(5.0),IntLiteral(2))])])])
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,509))    
    
#     def test_int_float_ast3(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('/',IntLiteral(5),FloatLiteral(2.0))])])])
#         expect = "2.5"
#         self.assertTrue(TestCodeGen.test(input,expect,510))
    
#     def test_float_int_ast3(self):
#         input = Program([
#             FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp('/',FloatLiteral(5.0),IntLiteral(2))])])])
#         expect = "2.5"
#         self.assertTrue(TestCodeGen.test(input,expect,511))

#     def test_boolean(self):
#         input = """
#         procedure main(); begin putBool(true); end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,512))

#     def test_boolean1(self):
#         input = """
#         procedure main(); begin putBoolLn(true); end
#         """
#         expect = "true\n"
#         self.assertTrue(TestCodeGen.test(input,expect,513))

#     def test_boolean2(self):
#         input = """
#         procedure main(); begin putBool(false); end
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,514))

#     def test_boolean3(self):
#         input = """
#         procedure main(); begin putBoolLn(false); end
#         """
#         expect = "false\n"
#         self.assertTrue(TestCodeGen.test(input,expect,515))

#     def test_string(self):
#         input = """
#         procedure main(); begin putString("ahihi"); end
#         """
#         expect = "ahihi"
#         self.assertTrue(TestCodeGen.test(input,expect,516))

#     def test_string1(self):
#         input = """
#         procedure main(); begin putStringLn("ahihi"); end
#         """
#         expect = "ahihi\n"
#         self.assertTrue(TestCodeGen.test(input,expect,517))
    
#     def test_int1(self):
#         input = """
#         procedure main(); begin putInt(400000); end
#         """
#         expect = "400000"
#         self.assertTrue(TestCodeGen.test(input,expect,518))

#     def test_float(self):
#         input = """
#         function foo(i: integer): real;
#         begin
#             return i;
#         end
#         procedure main();
#         var i: real;
#             begin
#                 i := foo(1);
#                 putFloat(i);
#             end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input,expect,519))

#     def test_if(self):
#         input = """
#         procedure main();
#         var i: real;
#             begin
#                 if False then i:=1; else i:=2;
#                 putFloat(i);
#             end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,520))

#     def test_for(self):
#         input = """
#         procedure main();
#             var i: integer;
#             begin
#                 for i := 10 downto 0 do 
#                     begin
#                         putInt(i);
#                     end
#                 putLn();
#             end
#         """
#         expect = "109876543210\n"
#         self.assertTrue(TestCodeGen.test(input,expect,521))

#     def test_for1(self):
#         input = """
#         procedure main();
#             var i: integer;
#             begin
#                 for i := 0 to 10 do 
#                     begin
#                         putInt(i);
#                     end
#                 putLn();
#             end
#         """
#         expect = "012345678910\n"
#         self.assertTrue(TestCodeGen.test(input,expect,522))

#     def test_break_for(self):
#         input = """
#         procedure main();
#             var i: integer;
#             begin
#                 for i := 0 to 10 do 
#                     begin
#                         putInt(i);
#                         break;
#                     end
#                 putLn();
#             end
#         """
#         expect = "0\n"
#         self.assertTrue(TestCodeGen.test(input,expect,523))

#     def test_while(self):
#         input = """
#         procedure main();
#             var i: integer;
#             begin
#                 i := 1;
#                 putInt(0);
#                 while i <= 10 do
#                 begin
#                     putString(" ");
#                     putInt(i);
#                     i := i + 1;
#                 end
#                 putLn();
#             end
#         """
#         expect = "0 1 2 3 4 5 6 7 8 9 10\n"
#         self.assertTrue(TestCodeGen.test(input,expect,524))

#     def test_break_while(self):
#         input = """
#         procedure main();
#             var i: integer;
#             begin
#                 i := 1;
#                 putInt(0);
#                 while i <= 10 do
#                 begin
#                     putString(" ");
#                     putInt(i);
#                     break;
#                     i := i + 1;
#                 end
#                 putLn();
#             end
#         """
#         expect = "0 1\n"
#         self.assertTrue(TestCodeGen.test(input,expect,525))

#     def test_with(self):
#         input = """
#             procedure main();
#                 begin
#                     putStringLn("bat dau with");
#                     with a, b: integer; do
#                         begin
#                             a := 1;
#                             b := 2;
#                             putInt(a+b); 
#                         end
#                     putStringLn("ket thuc with");
#                 end
#         """
#         expect = "bat dau with\n3ket thuc with\n"
#         self.assertTrue(TestCodeGen.test(input,expect,526))

#     def test_and_then(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(false and then false);
#                 end
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,527))

#     def test_and_then1(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(true and then false);
#                 end
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,528))

#     def test_or_else(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(false or else false);
#                 end
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,529))

#     def test_or_else1(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(true or else false);
#                 end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,530))
    
#     def test_binaryOp_bool(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(true and true);
#                 end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,531))
    
#     def test_unaryOp_bool(self):
#         input = """
#             procedure main();
#                 begin
#                     putBool(not true);
#                 end
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,532))

#     def test_unary_int(self):
#         input = """
#             procedure main();
#                 begin
#                     putInt(-1);
#                 end
#         """
#         expect = "-1"
#         self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_unary_float(self):
        input = """
            procedure main();
                begin
                    putInt(500);
                end
        """
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,534))