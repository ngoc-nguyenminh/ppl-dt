grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.STRING:

        return result
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}


options{
	language=Python3;
}

/*-------------grammar---------------*/
//result.text = result.text[1:len(result.text)-1]

program:  decls+ EOF;

/*Declarations*/
decls
    : vardecl
    | funcdecl
    | constdecl
    ;

funcdecl
    :FUN ID LP paramlist? RP body
    ;

paramlist
    :  param (CM param)*
    ;

param
    : ID dimension?
    ;

body
    : LB stm_list RB
    ;

mytype
    : INTLIT
    | FLOATLIT
    | BOOLIT
    | STRINGLIT
    | array
    | json
    ;


typname
    : NUMBER
    | STRING
    | BOOLEAN
    | JSON
    | ARRAY
    ;

array
    : LSB (mytype (CM mytype)* )? RSB
    ;

json
    : LB (keyval CM)* keyval  RB
    ;

keyval
    : ID CL mytype
    ;

/*Expressions*/
expression
    : exp0 (STRADD | STREQ) exp0
    | exp0
    ;
exp0
    : exp1 (EQ | NEQ | GT | LT | GEQ | LEQ ) exp1
    | exp1
    ;

exp1
    : exp1 (AND | OR) exp2
    | exp2
    ;

exp2
    : exp2 (ADD | NEG  ) exp3
    | exp3
    ;

exp3
    : exp3 (MUL |  DIV |  MOD) exp4
    | exp4
    ;

exp4
    : NOT exp4
    | exp5
    ;

exp5
    : NEG exp5
    | exp6
    ;

exp6
    : exp6 post_flix_json_exp
    | exp6 post_flix_array_exp
    | operand
    ;

operand
    : mytype
    | call
    | LP expression RP
    | ID
    | CONSTID
    ;

index_exp
    : expression /*post_flix_array_exp*/ ;

json_exp
    : expression /*post_flix_json_exp*/ ;

post_flix_array_exp
    : LSB expression (CM expression)* RSB
    ;

post_flix_json_exp
    : LB STRINGLIT RB
    ;

/*Statements*/
statement
    : assign SM
    | callstm
    | ifstm
    | forinstm
    | foronstm
    | whilestm
    | brk SM
    | cont SM
    | ret SM
    ;

stm_list : (vardecl | statement | constdecl)*;

constdecl
    : CONST constmodule (CM constmodule)* SM;

constmodule
    : CONSTID dimension? (CL typname)? ASSIGN expression
    ;

vardecl
    : LET varmodule (CM varmodule)* SM
    ;

varmodule
    : ID dimension? (CL typname)? (ASSIGN expression)?
    ;

dimension
    : LSB (INTLIT (CM INTLIT)*)? RSB
    ;

assign
    : lhs ASSIGN expression
    ;

lhs
    : index_exp
    | json_exp
    | ID
    ;

call
    : CALL LP ID CM LSB exp_list? RSB RP
    ;

callstm
    : CALL LP ID CM LSB exp_list? RSB RP SM
    ;

exp_list
    : expression(CM (expression))*
    ;

ret
    : RET (expression)?
    ;

ifstm
//    :IF expression THEN stm_list (ELIF expression THEN stm_list)* (ELSE stm_list)? ENDIF DOT
    :if_module (elif_module)* (else_module)?
    ;

if_module: IF LP expression RP LB stm_list RB;
elif_module: ELIF LP expression RP LB stm_list RB;
else_module: ELSE LB stm_list RB;


forinstm
    : FOR ID IN expression LB stm_list RB
    ;

foronstm
    : FOR ID OF expression LB stm_list RB
    ;

whilestm
    : WHILE LP expression RP LB stm_list RB
    ;

brk: BREAK ;

cont: CONT;

/*-----------Fragments------------------*/
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment EXPONENT: [eE] [+-]? DIGIT+;

/*------------Tokens-----------------*/
/*Keywords*/
LET:'Let';
CONST: 'Constant';
ASSIGN: '=';

NUMBER: 'Number';
BOOLEAN: 'Boolean';
STRING: 'String';
JSON: 'JSON';
ARRAY: 'Array';

FUN: 'Function';
RET: 'Return';

IF: 'If';
ELIF: 'Elif';
ELSE: 'Else';
BREAK: 'Break';
CONT: 'Continue';
CALL: 'Call';

FOR: 'For';
WHILE: 'While';
OF: 'Of';
IN: 'In';
//DO: 'Do';

/*Operators*/
ADD: '+';
STRADD: '+.';
NEG: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: '!';
AND: '&&';
OR: '||';

EQ: '==';
STREQ: '==.';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';

/*----------Symbols---------*/
CM: ',';
DOT: '.';
CL: ':';
SM: ';';
LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
LP: '(';
RP: ')';


COMMENT: '##' ('#' ~'#' | ~'#')* '##' -> skip;
WS : [ \t\n\r]+ -> skip ; // skip spaces, tabs, newlines

/*Literals*/
INTLIT: '0' | [1-9] DIGIT*;
FLOATLIT: ('0' | [1-9] DIGIT*) ( '.' | (('.' DIGIT* EXPONENT?) | EXPONENT));

BOOLIT
    : 'True'
    | 'False'
    ;

STRINGLIT: '"' ('\\' [bfnrt'\\] | ~[\\\r\n"'] | '\'"')* '"'
{self.text = self.text[1:len(self.text)-1]}
;

ID: [a-z][_a-zA-Z0-9]*;
CONSTID: '$'[a-z][_a-zA-Z0-9]*;

ERROR_CHAR:[@#$%^~`?];
UNCLOSE_STRING: '"' ('\\' [bfnrt'\\] | ~[\\\r\n"'] | '\'"')*

;
ILLEGAL_ESCAPE: '"' ~["]*
{for i in range(len(self.text)):
    check = (self.text[i] == "\\") or (self.text[i+1] in "\'\"\t\f\r\n")
    if check == True:
        self.text = self.text[1:i+2]
        break
}
;
UNTERMINATED_COMMENT: '##' ('#' (~'#' | EOF)  | ~'#')*;
