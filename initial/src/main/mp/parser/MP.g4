grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

INTLIT: [0-9]+;

FLOATLIT: INTLIT '.' INTLIT? EP? | '.' INTLIT EP? | INTLIT EP;

fragment EP: [eE] [+-]? INTLIT;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;