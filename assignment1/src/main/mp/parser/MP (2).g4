/*
 Student name: Nguyễn Xuân Hiến
 Student Id: 1652192
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

declaration: vardec | fundec | prodec;

// Variable declaration

vardec: VAR onevardec+;

onevardec: IDENT (COMMA IDENT)* COLON functiontype SEMI;

arraytype:
	ARRAY LSB SUBOP? INTLIT DOTDOT SUBOP? INTLIT RSB OF primitivetype;

primitivetype: REAL | BOOLEAN | INTEGER | STRING;

// Function declaration

fundec:
	FUNCTION IDENT LB paralist? RB COLON functiontype SEMI vardec? compoundstate;

paralist: paradec (SEMI paradec)*;

paradec: IDENT (COMMA IDENT)* COLON functiontype;

functiontype:
	primitivetype
	| arraytype; // [1 .. 4] -> dung ; [1..5] -> sai

// Procedure  declaration

prodec:
	PROCEDURE IDENT LB paralist? RB SEMI vardec? compoundstate;

// statement
statement:
	ifstate
	| whilestate
	| forstate
	| breakstate
	| contiSate
	| returnstate
	| compoundstate
	| callstate
	| assignstate
	| withstate;

ifstate: IF expression THEN statement (ELSE statement)?;

whilestate: WHILE expression DO statement;

forstate:
	FOR IDENT ASSIGNOP expression (TO | DOWNTO) expression DO statement;

breakstate: BREAK SEMI;

contiSate: CONTINUE SEMI;

returnstate: RETURN expression? SEMI;

compoundstate: BEGIN statement* END;

callstate: IDENT LB expressionList? RB SEMI;

assignstate: lhs (ASSIGNOP lhs)* ASSIGNOP expression SEMI;

withstate: WITH onevardec+ DO statement;

lhs: scalarvar | indexexpr;

scalarvar: IDENT;

// Expression
expression: expression ( AND THEN | OR ELSE ) expression1 | expression1;

expression1: expression2 (EQUAL | NOT_EQUAL | LT | LE | GT | GE) expression2 | expression2;

expression2: expression2 (ADDOP | SUBOP | OR) expression3 | expression3;

expression3: expression3 (DIVOP | MULOP | DIV | MOD | AND) expression4 | expression4;

expression4: (SUBOP | NOT) expression4 | expression5;

expression5: expression5 LSB expression RSB | operands;

operands: LB expression RB | literal | funCall | IDENT;

literal: INTLIT  | boollit | STRINGLIT | FLOATLIT ;

funCall: IDENT LB expressionList? RB;

expressionList: expression (COMMA expression)*;	

boollit: TRUE | FALSE;

indexexpr:	expression LSB expression RSB;

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

FLOATLIT: (INTLIT '.' INTLIT? | '.' INTLIT ) ExponentPart? | INTLIT ExponentPart;

fragment ExponentPart: E [-]? INTLIT;

STRINGLIT:
	'"' STRINGCHAR* '"' {
	self.text=self.text[1:-1]
};

fragment STRINGCHAR: ~["\\\n\r] | EscapeSequence;

fragment EscapeSequence: '\\' [btnfr"'\\];

// Error
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