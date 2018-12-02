import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_call_without_parameter(self):
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
            putBoolLn(( (foo(1) or foo(2)) or else foo(3)) or else foo(4));
            putIntLn(a);
        end
        """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,302))
   