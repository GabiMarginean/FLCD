%{
#include <stdio.h>
#include <stdlib.h>
#define YYDEBUG 1

#define TIP_INT 1
#define TIP_REAL 2
#define TIP_CAR 3

double stiva[20];
int sp;

void push(double x)
{ stiva[sp++]=x; }

double pop()
{ return stiva[--sp]; }

%}

%union {
  	int l_val;
	char *p_val;
}

%token BEGINN
%token CONST
%token DO
%token ELSE
%token END
%token IF
%token PRINT
%token PROGRAM
%token READ
%token THEN
%token VAR
%token WHILE
%token DECL
%token WHILST
%token RELATION
%token VERIF
%token BEGIN
%token RET
%token FOR
%token TYPE


%token ID
%token <p_val> CONST_INT
%token <p_val> CONST_REAL
%token <p_val> CONST_CAR
%token CONST_SIR

%token CHAR
%token INTEGER
%token REAL

%token ATRIB
%token NE
%token LE
%token GE

%left '+' '-'
%left DIV MOD '*' '/'
%left OR
%left AND
%left NOT

%%
prog:	'~' bloc '~'
		;
bloc:	decllist stmt
		| decllist
		| stmt
		;
decllist: declaration
		| declaration ',' decllist
		;
declaration: DECL ID TYPE
		| DECL ID TYPE ":=" expr
		| DECL ID TYPE '[]'
		| 'dtype' ID ":" decllist END
		;

assignstmt: ID ':=' expr
		| ID ":+" expr 
		| ID ":-" expr 
		| ID "++"
		| ID "--"
		;

stmtlist: stmt
		| stmt ';' stmtlist
		;
stmt:	simplstmt
		| structstmt
		;
simplstmt: assignstmt
		| PRINT idlist
		| PRINT expr
		| READ idlist
		;

idlist: ID 
		| ID ',' idlist 
		;
structstmt:	cmpdstmt 
		| ifstmt 
		| whilestmt
		;
cmpdstmt: BEGIN stmtlist END
		;
ifstmt: VERIF compcond THEN stmt
		| VERIF compcond THEN stmt ELSE stmt
		;
whilestmt: WHILST compcond DO stmt
		;
forstmt: FOR declaration ',' compcond ',' assignstmt DO
		| FOR assignstmt ',' compcond ',' assignstmt DO
		;
retstmt: RET
		| RET expr
		;

expr: expr '+' term 
		| expr '-' term 
		| term
		;
term: term '*' factor
		| term '/' factor
		| term '%' factor
		| factor
		;

factor: '(' expr ')'
	 | ID
	 ;

compcond: condition 
		| condition AND compcond
		| condition OR compcond
		;
condition: expr RELATION expr
		| NOT condition
		;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}

