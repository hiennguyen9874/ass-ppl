/*
 Studen name: Nguyễn XUân Hiến Studen Id: 1652192
 */
grammar MP;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Parser
program: (declaration)+ EOF;

declaration: varDec | funDec | proDec;

// Variable declaration

varDec: VAR onevarDec+;

onevarDec: IDENT (COMMA IDENT)* COLON functionType SEMI;

functionType:
	primitiveType
	| arrayType; // [1 .. 4] -> dung ; [1..5] -> sai

arrayType:
	ARRAY (LSB expression DOTDOT expression RSB)? OF primitiveType;

primitiveType: REAL | BOOLEAN | INTEGER | STRING;

// Function declaration

funDec:
	FUNCTION IDENT LB paraList RB COLON functionType SEMI varDec? compoundState;

paraList: (paradec (SEMI paradec)*)?;

paradec: IDENT (COMMA IDENT)* COLON functionType;

// Procedure  declaration

proDec:
	PROCEDURE IDENT LB paraList RB SEMI varDec? compoundState;


// Statement
statement:
	assignState
	| ifState
	| whileState
	| forState
	| breakState
	| contiSate
	| returnState
	| compoundState
	| callState
	| expressionStatement
	| withState;

assignState: lsh (ASSIGNOP lsh)* ASSIGNOP expression SEMI;

lsh: scalarvar | indenxexp;

scalarvar: IDENT;

indenxexp: expression LSB expression RSB;

ifState: IF expression THEN statement (ELSE statement)?;

whileState: WHILE expression DO statement;

forState:
	FOR IDENT ASSIGNOP expression (TO | DOWNTO) expression DO statement;

breakState: BREAK SEMI;

contiSate: CONTINUE SEMI;

returnState: RETURN expression? SEMI;

withState: WITH onevarDec+ DO statement;

callState: IDENT LB IDENT (COMMA expression)* RB SEMI;

compoundState: BEGIN statement*? END;

expressionStatement: expression SEMI;

// Expression
expression:
	primary
	| expression '[' expression ']'
	| <assoc = right> (SUBOP | NOT) expression
	| expression (DIVOP | MULOP | DIV | MOD | AND) expression
	| expression (ADDOP | SUBOP | OR) expression
	| expression (EQUAL | NOT_EQUAL | LT | LE | GT | GE) expression
	| expression (AND THEN | OR ELSE) expression;

primary: LB expression RB | literal | funCall | IDENT;

literal: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT;

funCall: IDENT LB expressionList? RB;

expressionList: expression (COMMA expression)*;



// "ABC"="abc"

fragment A: ('a' | 'A');

fragment B: ('b' | 'B');

fragment C: ('c' | 'C');

fragment D: ('d' | 'D');

fragment E: ('e' | 'E');

fragment F: ('f' | 'F');

fragment G: ('g' | 'G');

fragment H: ('h' | 'H');

fragment I: ('i' | 'I');

fragment J: ('j' | 'J');

fragment K: ('k' | 'K');

fragment L: ('l' | 'L');

fragment M: ('m' | 'M');

fragment N: ('n' | 'N');

fragment O: ('o' | 'O');

fragment P: ('p' | 'P');

fragment Q: ('q' | 'Q');

fragment R: ('r' | 'R');

fragment S: ('s' | 'S');

fragment T: ('t' | 'T');

fragment U: ('u' | 'U');

fragment V: ('v' | 'V');

fragment W: ('w' | 'W');

fragment X: ('x' | 'X');

fragment Y: ('y' | 'Y');

fragment Z: ('z' | 'Z');

// Keywords

BREAK: B R E A K;

CONTINUE: C O N T I N U E;

FOR: F O R;

TO: T O;

DOWNTO: D O W N T O;

DO: D O;

IF: I F;

THEN: T H E N;

ELSE: E L S E;

RETURN: R E T U R N;

WHILE: W H I L E;

BEGIN: B E G I N;

END: E N D;

FUNCTION: F U N C T I O N;

PROCEDURE: P R O C E D U R E;

VAR: V A R;

TRUE: T R U E;

FALSE: F A L S E;

ARRAY: A R R A Y;

OF: O F;

REAL: R E A L;

BOOLEAN: B O O L E A N;

INTEGER: I N T E G E R;

STRING: S T R I N G;

NOT: N O T;

AND: A N D;

OR: O R;

DIV: D I V;

MOD: M O D;

WITH: W I T H;

// Operators

ASSIGNOP: ':=';

ADDOP: '+';

SUBOP: '-';

MULOP: '*';

DIVOP: '/';

NOT_EQUAL: '<>';

EQUAL: '=';

LT: '<';

GT: '>';

LE: '<=';

GE: '>=';


// Separators

LSB: '[';

RSB: ']';

COLON: ':';

LB: '(';

RB: ')';

SEMI: ';';

DOTDOT: '..';

COMMA: ',';

// Lexer Comment

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

COMMENT_1: '(*' .*? '*)' -> skip;

COMMENT_2: '{' .*? '}' -> skip;

COMMENT_3: '//' ~[\r\n]* -> skip;

// Identifiers

IDENT: [_a-zA-Z][_a-zA-Z0-9]*;

// Literals

INTLIT: [0-9]+;

FLOATLIT: (INTLIT '.' INTLIT? | '.' INTLIT | INTLIT) ExponentPart?;

fragment ExponentPart: [eE] [-]? INTLIT;

BOOLLIT: TRUE | FALSE;

STRINGLIT:
	'"' STRINGCHAR* '"' {
	self.text=self.text[1:-1]
};

fragment STRINGCHAR: ~["\\\n\r] | EscapeSequence;

fragment EscapeSequence: '\\' [btnfr"'\\];

ILLEGAL_ESCAPE:
	'"' STRINGCHAR* '\\' ~[btnfr"'\\] {
	raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING:
	'"' STRINGCHAR* {
	raise UncloseString(self.text[1:])
};
ERROR_CHAR:
	.{
	raise ErrorToken(self.text)
};