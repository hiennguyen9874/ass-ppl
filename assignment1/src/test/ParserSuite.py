import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """
        proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    x := 1;
                    c := a[12] ;
                   END
                   """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))