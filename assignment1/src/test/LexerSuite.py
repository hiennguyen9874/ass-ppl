import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        self.assertTrue(TestLexer.test("{abc}", "<EOF>", 101))

    def test_2(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 102))

    def test_3(self):
        self.assertTrue(TestLexer.test("(*This is block comment*)", "<EOF>", 103))

    def test_4(self):
        self.assertTrue(TestLexer.test("123\n123", "123,123,<EOF>", 104))

    def test_5(self):
        self.assertTrue(TestLexer.test("\"123\k123\"","Illegal Escape In String: 123\k", 105))

    def test_6(self):
        self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 106))

    def test_7(self):
        self.assertTrue(TestLexer.test("123abcd123", "123,abcd123,<EOF>", 107))

    def test_8(self):
        self.assertTrue(TestLexer.test("(*This is a block comment*)", "<EOF>", 108))

    def test_9(self):
        self.assertTrue(TestLexer.test("123\n123", "123,123,<EOF>", 109))

    def test_10(self):
        self.assertTrue(TestLexer.test("name Name name1 NAME2","name,Name,name1,NAME2,<EOF>", 110))

    def test_11(self):
        self.assertTrue(TestLexer.test("//This is a line comment", "<EOF>", 111))

    def test_12(self):
        self.assertTrue(TestLexer.test("_ _name _Name _1 name_1","_,_name,_Name,_1,name_1,<EOF>", 112))

    def test_13(self):
        self.assertTrue(TestLexer.test("1Name 24name39","1,Name,24,name39,<EOF>", 113))

    def test_14(self):
        self.assertTrue(TestLexer.test("1.2", "1.2,<EOF>", 114))

    def test_15(self):
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 115))

    def test_16(self):
        self.assertTrue(TestLexer.test(".1", ".1,<EOF>", 116))

    def test_17(self):
        self.assertTrue(TestLexer.test("1e2", "1e2,<EOF>", 117))

    def test_18(self):
        self.assertTrue(TestLexer.test("1.2E-2", "1.2E-2,<EOF>", 118))

    def test_19(self):
        self.assertTrue(TestLexer.test("0.2e-22", "0.2e-22,<EOF>", 119))

    def test_20(self):
        self.assertTrue(TestLexer.test(".1E2", ".1E2,<EOF>", 120))

    def test_21(self):
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 121))

    def test_22(self):
        self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 122))

    def test_23(self):
        self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 123))

    def test_24(self):
        self.assertTrue(TestLexer.test("128e-42", "128e-42,<EOF>", 124))

    def test_25(self):
        self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 125))

    def test_26(self):
        self.assertTrue(TestLexer.test("143e", "143,e,<EOF>", 126))

    def test_27(self):
        self.assertTrue(TestLexer.test("foo(2)[3+x] := a[b[2]] +3;", "foo,(,2,),[,3,+,x,],:=,a,[,b,[,2,],],+,3,;,<EOF>", 127))

    def test_28(self):
        self.assertTrue(TestLexer.test("\"abc123\"", "abc123,<EOF>", 128))

    def test_29(self):
        self.assertTrue(TestLexer.test("1.e-12", "1.e-12,<EOF>", 129))

    def test_30(self):
        self.assertTrue(TestLexer.test("abcd_1234", "abcd_1234,<EOF>", 130))

    def test_31(self):
        self.assertTrue(TestLexer.test("modnotorand", "modnotorand,<EOF>", 131))

    def test_32(self):
        self.assertTrue(TestLexer.test("\"abc", "Unclosed String: abc", 132))

    def test_33(self):
        self.assertTrue(TestLexer.test("\"ab	c\"", "ab	c,<EOF>", 133))

    def test_34(self):
        self.assertTrue(TestLexer.test(" if(true) x=1; ","if,(,true,),x,=,1,;,<EOF>", 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("(*abcd def*)", "<EOF>", 135))


    def test_36(self):
        self.assertTrue(TestLexer.test("_ _name _Name _1 name_1","_,_name,_Name,_1,name_1,<EOF>", 136))


    def test_37(self):
        self.assertTrue(TestLexer.test("$name #name", "Error Token $", 137))


    def test_38(self):
        self.assertTrue(TestLexer.test("boolean break continue else for float if int return void do while true false string", "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>", 138))


    def test_39(self):
        self.assertTrue(TestLexer.test(" boolean check; ","boolean,check,;,<EOF>", 139))


    def test_40(self):
        self.assertTrue(TestLexer.test("int age1, age2; ","int,age1,,,age2,;,<EOF>", 140))


    def test_41(self):
        self.assertTrue(TestLexer.test(" void main(){}\n\tstring[] getName(){}", "void,main,(,),string,[,],getName,(,),<EOF>", 141))


    def test_42(self):
        self.assertTrue(TestLexer.test("return a;\nreturn;\nbeak;\ncontinue;", "return,a,;,return,;,beak,;,continue,;,<EOF>", 142))

    def test_43(self):
        self.assertTrue(TestLexer.test("var a,b,c:integer;\nd:array [1 .. 2] of integer;","var,a,,,b,,,c,:,integer,;,d,:,array,[,1,..,2,],of,integer,;,<EOF>",143))

    def test_44(self):
        self.assertTrue(TestLexer.test("function foo(a,b,integer;c:real):array [1 .. 4] of integer;","function,foo,(,a,,,b,,,integer,;,c,:,real,),:,array,[,1,..,4,],of,integer,;,<EOF>",144))

    def test_45(self):
        self.assertTrue(TestLexer.test("+ - * /","+,-,*,/,<EOF>",145))

    def test_46(self):
        self.assertTrue(TestLexer.test("true false","true,false,<EOF>",146))

    def test_47(self):
        self.assertTrue(TestLexer.test("true/false","true,/,false,<EOF>",147))

    def test_48(self):
        self.assertTrue(TestLexer.test("20-2","20,-,2,<EOF>",148))

    def test_49(self):
        self.assertTrue(TestLexer.test("20>>2<<3","20,>,>,2,<,<,3,<EOF>",149))
        
    def test_50(self):
        self.assertTrue(TestLexer.test("5*3+a/3-b*2.2E2","5,*,3,+,a,/,3,-,b,*,2.2E2,<EOF>",150))

    def test_51(self):
        self.assertTrue(TestLexer.test("a+b/c","a,+,b,/,c,<EOF>",151))

    def test_52(self):
        self.assertTrue(TestLexer.test("a>b<c>=5<=2","a,>,b,<,c,>=,5,<=,2,<EOF>",152))

    def test_53(self):
        self.assertTrue(TestLexer.test("( ) [ ] { } ; ,","(,),[,],;,,,<EOF>",153))

    def test_53(self):
        self.assertTrue(TestLexer.test("","<EOF>",153))

    def test_54(self):
        self.assertTrue(TestLexer.test("True TRUE False FALSE","True,TRUE,False,FALSE,<EOF>",154))

    def test_55(self):
        self.assertTrue(TestLexer.test(" \"This is a string\" ","This is a string,<EOF>",155))

    def test_56(self):
        self.assertTrue(TestLexer.test(" "" ","<EOF>",156))

    def test_57(self):
        self.assertTrue(TestLexer.test("\"This (*is a*) string\"","This (*is a*) string,<EOF>",157))

    def test_58(self):
        self.assertTrue(TestLexer.test("0 00 24 39 123456789 000000","0,00,24,39,123456789,000000,<EOF>",158))

    def test_59(self):
        self.assertTrue(TestLexer.test("+0 -00 +24 -39","+,0,-,00,+,24,-,39,<EOF>",159))

    def test_60(self):
        self.assertTrue(TestLexer.test("0x24EF39","0,x24EF39,<EOF>",160))

    def test_61(self):
        self.assertTrue(TestLexer.test("123. .123 1.23","123.,.123,1.23,<EOF>",161))

    def test_62(self):
        self.assertTrue(TestLexer.test("123.e2 .123E-2 1.23e0","123.e2,.123E-2,1.23e0,<EOF>",162))

    def test_63(self):
        self.assertTrue(TestLexer.test("12.3e+2 1.23E+2","12.3,e,+,2,1.23,E,+,2,<EOF>",163))

    def test_64(self):
        self.assertTrue(TestLexer.test("e2 E-2","e2,E,-,2,<EOF>",164))

    def test_65(self):
        self.assertTrue(TestLexer.test(".e2 .E-2","Error Token .",165))

    def test_66(self):
        self.assertTrue(TestLexer.test("\"ab	c\"", "ab	c,<EOF>", 166))

    def test_67(self):
        self.assertTrue(TestLexer.test("\"string nay bi loi unclose string ","Unclosed String: string nay bi loi unclose string ",167))

    def test_68(self):
        self.assertTrue(TestLexer.test("begin\ny:=x+1\nend;","begin,y,:=,x,+,1,end,;,<EOF>",168))

