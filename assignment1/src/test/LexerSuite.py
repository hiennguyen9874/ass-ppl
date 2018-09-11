import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("(* This is a block comment *)","<EOF>",101))
    def test_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("// This is a block comment","<EOF>",102))
    def test_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("{This is a block comment}","<EOF>",103))
    def test_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("(* This\nis\nnbloc\ncomment *)","<EOF>",104))
    
    