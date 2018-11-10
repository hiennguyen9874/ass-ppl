import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: procedure main() begin end """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         putIntLn(4);
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) procedure main( begin end"""
    #     input = """procedure main( begin end"""
    #     expect = "Error on line 1 col 16: begin"
    #     self.assertTrue(TestParser.test(input,expect,203))