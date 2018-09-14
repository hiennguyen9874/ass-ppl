import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment_1(self):
        self.assertTrue(TestLexer.test(
            """// This is a comment""", "<EOF>", 101))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test(
            """{This is a block comment}""", "<EOF>", 102))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test(
            """(*This is a block comment*)""", "<EOF>", 103))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test(
            """// This {is} a comment""", "<EOF>", 104))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test(
            """// This (*is*) a comment""", "<EOF>", 105))

    def test_comment_6(self):
        self.assertTrue(TestLexer.test(
            """{This is // a block comment}""", "<EOF>", 106))

    def test_comment_7(self):
        self.assertTrue(TestLexer.test(
            """{This is a (* block *) comment}""", "<EOF>", 107))

    def test_comment_8(self):
        self.assertTrue(TestLexer.test(
            """(*This is a // block comment*)""", "<EOF>", 108))

    def test_comment_9(self):
        self.assertTrue(TestLexer.test(
            """(*This is {a block} comment*)""", "<EOF>", 109))

    def test_indentifiers_10(self):
        self.assertTrue(TestLexer.test("""abcd""", "abcd,<EOF>", 110))

    def test_indentifiers_11(self):
        self.assertTrue(TestLexer.test("""a1b2c3d4""", "a1b2c3d4,<EOF>", 111))

    def test_indentifiers_12(self):
        self.assertTrue(TestLexer.test("""notandor""", "notandor,<EOF>", 112))

    def test_indentifiers_13(self):
        self.assertTrue(TestLexer.test("""abcbreak""", "abcbreak,<EOF>", 113))

    def test_indentifiers_14(self):
        self.assertTrue(TestLexer.test(
            """abc+cdef""", "abc,+,cdef,<EOF>", 114))

    def test_indentifiers_15(self):
        self.assertTrue(TestLexer.test(
            """abcdef/12345""", "abcdef,/,12345,<EOF>", 115))

    def test_keywords_16(self):
        self.assertTrue(TestLexer.test(
            """breakcontinuefortodowntoifthen""", "breakcontinuefortodowntoifthen,<EOF>", 116))

    def test_keywords_17(self):
        self.assertTrue(TestLexer.test(
            """elsereturnwhilebeginendfunction""", "elsereturnwhilebeginendfunction,<EOF>", 117))

    def test_keywords_18(self):
        self.assertTrue(TestLexer.test("""producedurevartrue""",
                                       "producedurevartrue,<EOF>", 118))

    def test_operators_19(self):
        self.assertTrue(TestLexer.test("""+-*/""", "+,-,*,/,<EOF>", 119))

    def test_error_20(self):
        self.assertTrue(TestLexer.test(
            "\"123\k123\"", "Illegal Escape In String: 123\k", 120))

    def test_comment_21(self):
        self.assertTrue(TestLexer.test("{abc}", "<EOF>", 121))

    def test_float_22(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 122))

    def test_comment_23(self):
        self.assertTrue(TestLexer.test(
            "(*This is block comment*)", "<EOF>", 123))

    def test_float_24(self):
        self.assertTrue(TestLexer.test("123\n123", "123,123,<EOF>", 124))

    def test_float_25(self):
        self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 125))

    def test_indentifiers_26(self):
        self.assertTrue(TestLexer.test("123abcd123", "123,abcd123,<EOF>", 126))

    def test_comment_27(self):
        self.assertTrue(TestLexer.test(
            "(*This is a block comment*)", "<EOF>", 127))

    def test_test_float_28(self):
        self.assertTrue(TestLexer.test("123\n123", "123,123,<EOF>", 128))

    def test_indentifiers_29(self):
        self.assertTrue(TestLexer.test("name Name name1 NAME2",
                                       "name,Name,name1,NAME2,<EOF>", 129))

    def test_comment_30(self):
        self.assertTrue(TestLexer.test(
            "//This is a line comment", "<EOF>", 130))

    def test_indentifiers_31(self):
        self.assertTrue(TestLexer.test("_ _name _Name _1 name_1",
                                       "_,_name,_Name,_1,name_1,<EOF>", 131))

    def test_indentifiers_32(self):
        self.assertTrue(TestLexer.test("1Name 24name39",
                                       "1,Name,24,name39,<EOF>", 132))

    def test_float_33(self):
        self.assertTrue(TestLexer.test("1.2", "1.2,<EOF>", 133))

    def test_float_34(self):
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 134))

    def test_float_35(self):
        self.assertTrue(TestLexer.test(".1", ".1,<EOF>", 135))

    def test_float_36(self):
        self.assertTrue(TestLexer.test("1e2", "1e2,<EOF>", 136))

    def test_float_37(self):
        self.assertTrue(TestLexer.test("1.2E-2", "1.2E-2,<EOF>", 137))

    def test_float_38(self):
        self.assertTrue(TestLexer.test("0.2e-22", "0.2e-22,<EOF>", 138))

    def test_float_39(self):
        self.assertTrue(TestLexer.test(".1E2", ".1E2,<EOF>", 139))

    def test_float_40(self):
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 140))

    def test_float_41(self):
        self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 141))

    def test_float_42(self):
        self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 142))

    def test_float_43(self):
        self.assertTrue(TestLexer.test("128e-42", "128e-42,<EOF>", 143))

    def test_float_44(self):
        self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 144))

    def test_float_45(self):
        self.assertTrue(TestLexer.test("143e", "143,e,<EOF>", 145))

    def test_all_46(self):
        self.assertTrue(TestLexer.test(
            "foo(2)[3+x] := a[b[2]] +3;", "foo,(,2,),[,3,+,x,],:=,a,[,b,[,2,],],+,3,;,<EOF>", 146))

    def test_string_47(self):
        self.assertTrue(TestLexer.test("\"abc123\"", "abc123,<EOF>", 147))

    def test_float_48(self):
        self.assertTrue(TestLexer.test("1.e-12", "1.e-12,<EOF>", 148))

    def test_indentifiers_49(self):
        self.assertTrue(TestLexer.test("abcd_1234", "abcd_1234,<EOF>", 149))

    def test_indentifiers_50(self):
        self.assertTrue(TestLexer.test(
            "modnotorand", "modnotorand,<EOF>", 150))

    def test_error_51(self):
        self.assertTrue(TestLexer.test("\"abc", "Unclosed String: abc", 151))

    def test_string_52(self):
        self.assertTrue(TestLexer.test("\"ab	c\"", "ab	c,<EOF>", 152))

    def test_all_53(self):
        self.assertTrue(TestLexer.test(" if(true) x=1; ",
                                       "if,(,true,),x,=,1,;,<EOF>", 153))

    def test_comment_54(self):
        self.assertTrue(TestLexer.test("(*abcd def*)", "<EOF>", 154))

    def test_indentifiers_55(self):
        self.assertTrue(TestLexer.test("_ _name _Name _1 name_1",
                                       "_,_name,_Name,_1,name_1,<EOF>", 155))

    def test_error_56(self):
        self.assertTrue(TestLexer.test("$name #name", "Error Token $", 156))

    def test_keywords_57(self):
        self.assertTrue(TestLexer.test("boolean break continue else for float if int return void do while true false string",
                                       "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>", 157))

    def test_keywords_58(self):
        self.assertTrue(TestLexer.test(
            " boolean check; ", "boolean,check,;,<EOF>", 158))

    def test_keywords_indentifires_59(self):
        self.assertTrue(TestLexer.test("int age1, age2; ",
                                       "int,age1,,,age2,;,<EOF>", 159))

    def test_all_60(self):
        self.assertTrue(TestLexer.test(" void main(){}\n\tstring[] getName(){}",
                                       "void,main,(,),string,[,],getName,(,),<EOF>", 160))

    def test_keywords_61(self):
        self.assertTrue(TestLexer.test("return a;\nreturn;\nbeak;\ncontinue;",
                                       "return,a,;,return,;,beak,;,continue,;,<EOF>", 161))

    def test_all_62(self):
        self.assertTrue(TestLexer.test(
            "var a,b,c:integer;\nd:array [1 .. 2] of integer;", "var,a,,,b,,,c,:,integer,;,d,:,array,[,1,..,2,],of,integer,;,<EOF>", 162))

    def test_all_63(self):
        self.assertTrue(TestLexer.test("function foo(a,b,integer;c:real):array [1 .. 4] of integer;",
                                       "function,foo,(,a,,,b,,,integer,;,c,:,real,),:,array,[,1,..,4,],of,integer,;,<EOF>", 163))

    def test_operators_64(self):
        self.assertTrue(TestLexer.test("+ - * /", "+,-,*,/,<EOF>", 164))

    def test_keywords_65(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 165))

    def test_keywords_66(self):
        self.assertTrue(TestLexer.test(
            "true/false", "true,/,false,<EOF>", 166))

    def test_operators_67(self):
        self.assertTrue(TestLexer.test("""<=""", "<=,<EOF>", 167))

    def test_operators_68(self):
        self.assertTrue(TestLexer.test("20-2", "20,-,2,<EOF>", 168))

    def test_indentifiers_69(self):
        self.assertTrue(TestLexer.test(
            """
            a<===>=b
            """, "a,<=,=,=,>=,b,<EOF>", 169))

    def test_keywords_70(self):
        self.assertTrue(TestLexer.test(
            "20>>2<<3", "20,>,>,2,<,<,3,<EOF>", 170))

    def test_operators_71(self):
        self.assertTrue(TestLexer.test("5*3+a/3-b*2.2E2",
                                       "5,*,3,+,a,/,3,-,b,*,2.2E2,<EOF>", 171))

    def test_operators_72(self):
        self.assertTrue(TestLexer.test("a+b/c", "a,+,b,/,c,<EOF>", 172))

    def test_operators_73(self):
        self.assertTrue(TestLexer.test(
            "a>b<c>=5<=2", "a,>,b,<,c,>=,5,<=,2,<EOF>", 173))

    def test_separators_74(self):
        self.assertTrue(TestLexer.test(
            "( ) [ ] { } ; ,", "(,),[,],;,,,<EOF>", 174))

    def test_none_75(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 175))

    def test_keywords_76(self):
        self.assertTrue(TestLexer.test("True TRUE False FALSE",
                                       "True,TRUE,False,FALSE,<EOF>", 176))

    def test_string_77(self):
        self.assertTrue(TestLexer.test(
            " \"This is a string\" ", "This is a string,<EOF>", 177))

    def test_string_78(self):
        self.assertTrue(TestLexer.test(" "" ", "<EOF>", 178))

    def test_comment_79(self):
        self.assertTrue(TestLexer.test(
            "\"This (*is a*) string\"", "This (*is a*) string,<EOF>", 179))

    def test_integer_80(self):
        self.assertTrue(TestLexer.test(
            "0 00 24 39 123456789 000000", "0,00,24,39,123456789,000000,<EOF>", 180))

    def test_integer_81(self):
        self.assertTrue(TestLexer.test("+0 -00 +24 -39",
                                       "+,0,-,00,+,24,-,39,<EOF>", 181))

    def test_float_82(self):
        self.assertTrue(TestLexer.test(
            "123. .123 1.23", "123.,.123,1.23,<EOF>", 182))

    def test_float_83(self):
        self.assertTrue(TestLexer.test("123.e2 .123E-2 1.23e0",
                                       "123.e2,.123E-2,1.23e0,<EOF>", 183))

    def test_float_84(self):
        self.assertTrue(TestLexer.test("12.3e+2 1.23E+2",
                                       "12.3,e,+,2,1.23,E,+,2,<EOF>", 184))

    def test_float_85(self):
        self.assertTrue(TestLexer.test("e2 E-2", "e2,E,-,2,<EOF>", 185))

    def test_error_86(self):
        self.assertTrue(TestLexer.test(".e2 .E-2", "Error Token .", 186))

    def test_string_87(self):
        self.assertTrue(TestLexer.test("\"ab	c\"", "ab	c,<EOF>", 187))

    def test_unclose_string_88(self):
        self.assertTrue(TestLexer.test("\"string nay bi loi unclose string ",
                                       "Unclosed String: string nay bi loi unclose string ", 188))

    def test_all_89(self):
        self.assertTrue(TestLexer.test("begin\ny:=x+1\nend;",
                                       "begin,y,:=,x,+,1,end,;,<EOF>", 189))

    def test_string_90(self):
        self.assertTrue(TestLexer.test("\"123\f45\"", "12345,<EOF>", 190))

    def test_unclose_string_91(self):
        self.assertTrue(TestLexer.test(
            "\"123\r45\"", "Unclosed String: 123", 191))

    def test_unclose_string_92(self):
        self.assertTrue(TestLexer.test(
            "\"abc\nxyz\"", "Unclosed String: abc", 192))

    def test_all_93(self):
        self.assertTrue(TestLexer.test("var a , b , c : integer ;",
                                       "var,a,,,b,,,c,:,integer,;,<EOF>", 193))

    def test_all_94(self):
        self.assertTrue(TestLexer.test(
            "d : array [ 1 .. 5 ] of integer ;", "d,:,array,[,1,..,5,],of,integer,;,<EOF>", 194))

    def test_indentifiers_95(self):
        self.assertTrue(TestLexer.test("abcd_1234", "abcd_1234,<EOF>", 195))

    def test_operators_96(self):
        self.assertTrue(TestLexer.test("+-*/notmodorand<>=<=>=div",
                                       "+,-,*,/,notmodorand,<>,=,<=,>=,div,<EOF>", 196))

    def test_string_97(self):
        self.assertTrue(TestLexer.test(
            "\"this a string\"", "this a string,<EOF>", 197))

    def test_indentifiers_98(self):
        self.assertTrue(TestLexer.test(
            "int main()", "int,main,(,),<EOF>", 198))

    def test_indentifiers_99(self):
        self.assertTrue(TestLexer.test(
            """
            procedure main(); 
            var main:Integer;
            begin
	            main := f();
	        return ;
            end 
            """, "procedure,main,(,),;,var,main,:,Integer,;,begin,main,:=,f,(,),;,return,;,end,<EOF>", 199))

    def test_indentifiers_100(self):
        self.assertTrue(TestLexer.test(
            """
            return ireturn RETURNi RETURN 
            """, "return,ireturn,RETURNi,RETURN,<EOF>", 200))

    def test_error_500(self):
        self.assertTrue(TestLexer.test(
            """ "sfsa \b" """, "sfsa \b,<EOF>", 500))

    def test_501(self):
        self.assertTrue(TestLexer.test("//ascw_12", "<EOF>", 501))

    def test_502(self):
        self.assertTrue(TestLexer.test("""
        function main() : real; begin retunr 5; end
        """, "function,main,(,),:,real,;,begin,retunr,5,;,end,<EOF>", 502))

    def test_503(self):
        self.assertTrue(TestLexer.test("""
        if a=true then a:=1; 
        """, "if,a,=,true,then,a,:=,1,;,<EOF>", 503))

    def test_504(self):
        self.assertTrue(TestLexer.test("""aa\\\\""", "aa,Error Token \\", 504))

    def test_505(self):
        self.assertTrue(TestLexer.test(
            "{reff85}_asq//sf", "_asq,<EOF>", 505))
