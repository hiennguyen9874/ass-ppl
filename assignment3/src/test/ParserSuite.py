import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: procedure main() begin end """
        input = """
        var a: integer;
        procedure main();
        var b: array [1 .. 10] of integer;
            x: integer;
        begin
            a := foo();
            a := b [10] := f()[ 3 ] := x := 1 ;
        end
        function foo(): integer;
        var a: boolean;
        begin
            while a do
                begin
                    break;
                end
            a := true;
            return 200;
        end
        function f(): array [1 .. 10] of integer;
        var a: array [1 .. 10] of integer;
        begin
            return a;
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