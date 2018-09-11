# Generated from d:\Nam3\PPL\Ass1\assignment1\src\main\mp\parser\MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
                     "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT_1", "COMMENT_2", "COMMENT_3", 
                      "IDENT", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
                      "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
                      "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                      "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                      "NOT", "AND", "OR", "DIV", "MOD", "ADD", "SUB", "MUL", 
                      "DIVI", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", 
                      "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DOTDOT", 
                      "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    COMMENT_1=2
    COMMENT_2=3
    COMMENT_3=4
    IDENT=5
    BREAK=6
    CONTINUE=7
    FOR=8
    TO=9
    DOWNTO=10
    DO=11
    IF=12
    THEN=13
    ELSE=14
    RETURN=15
    WHILE=16
    BEGIN=17
    END=18
    FUNCTION=19
    PROCEDURE=20
    VAR=21
    TRUE=22
    FALSE=23
    ARRAY=24
    OF=25
    REAL=26
    BOOLEAN=27
    INTEGER=28
    STRING=29
    NOT=30
    AND=31
    OR=32
    DIV=33
    MOD=34
    ADD=35
    SUB=36
    MUL=37
    DIVI=38
    NOT_EQUAL=39
    EQUAL=40
    LT=41
    GT=42
    LE=43
    GE=44
    LSB=45
    RSB=46
    COLON=47
    LB=48
    RB=49
    SEMI=50
    DOTDOT=51
    COMMA=52
    INTLIT=53
    FLOATLIT=54
    BOOLLIT=55
    STRINGLIT=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MPParser.RULE_program




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





