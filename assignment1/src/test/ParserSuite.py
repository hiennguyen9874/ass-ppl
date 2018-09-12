import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        with a , b : i n t e g e r ; c : array [ 1 . . 2 ] of r e a l ; do
d = c [ a ] + b ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))