%{
  #include <stdio.h>
  #include <stdlib.h>
  #include <math.h>   // for pow()

  int op = 0, i;
  float a, b;
  void digi(const char *text); // pass yytext as argument
%}

DIGIT   [0-9]+(\.[0-9]+)?     // Fixed regex
ADD     \+
SUB     -
MUL     \*
DIV     /
POW     \^
NEWLINE \n

%%
{DIGIT}    { digi(yytext); }
{ADD}      { op = 1; }
{SUB}      { op = 2; }
{MUL}      { op = 3; }
{DIV}      { op = 4; }
{POW}      { op = 5; }
{NEWLINE}  { printf("\nThe Answer: %f\n\n", a); }
.|\n       ; // ignore other characters
%%

void digi(const char *text) {
  if(op == 0){
    a = atof(text);
  } else {
    b = atof(text);
    switch(op){
      case 1: a = a + b; break;
      case 2: a = a - b; break;
      case 3: a = a * b; break;
      case 4: a = a / b; break;
      case 5: a = pow(a, b); break;
    }
    op = 0;
  }
}

int main(){
  printf("Enter an arithmetic expression:\n");
  yylex();
  return 0;
}

int yywrap(){
  return 1;
}
