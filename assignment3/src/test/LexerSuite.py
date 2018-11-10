import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lơercase_identifier(self):
        """test identifiers"""
        input = """
        Procedure main();
        var a: array [ -1 .. 100 ] of Real;
            i: integer;
        begin
            while (-i div i>=i+i) and (i+i*i<=i+i*i-i/i) do
                while i do
                    return;
        end
        """
        self.assertTrue(TestLexer.test(input,"abc,<EOF>",101))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))