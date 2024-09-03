%{
#include <stdio.h>
#include <ctype.h>
%}

%%
"int"           { printf("KEYWORD: int\n"); }
"char"          { printf("KEYWORD: char\n"); }
"float"         { printf("KEYWORD: float\n"); }
"double"        { printf("KEYWORD: double\n"); }
"void"          { printf("KEYWORD: void\n"); }
"if"            { printf("KEYWORD: if\n"); }
"else"          { printf("KEYWORD: else\n"); }
"while"         { printf("KEYWORD: while\n"); }
"for"           { printf("KEYWORD: for\n"); }
"do"            { printf("KEYWORD: do\n"); }
"return"        { printf("KEYWORD: return\n"); }
"break"         { printf("KEYWORD: break\n"); }
"continue"      { printf("KEYWORD: continue\n"); }
"case"          { printf("KEYWORD: case\n"); }
"switch"          { printf("KEYWORD: switch\n"); }
"default"          { printf("KEYWORD: default\n"); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("IDENTIFIER: %s\n", yytext); }

"=="            { printf("RELATIONAL OPERATOR: ==\n"); }
"!="            { printf("RELATIONAL OPERATOR: !=\n"); }
"<="            { printf("RELATIONAL OPERATOR: <=\n"); }
">="            { printf("RELATIONAL OPERATOR: >=\n"); }

"&&"            { printf("LOGICAL OPERATOR: &&\n"); }
"||"            { printf("LOGICAL OPERATOR: ||\n"); }

"++"            { printf("ARITHMETIC OPERATOR: ++\n"); }
"--"            { printf("ARITHMETIC OPERATOR: --\n"); }
"+"             { printf("ARITHMETIC OPERATOR: +\n"); }
"-"             { printf("ARITHMETIC OPERATOR: -\n"); }
"*"             { printf("ARITHMETIC OPERATOR: *\n"); }
"/"             { printf("ARITHMETIC OPERATOR: /\n"); }

"<"             { printf("RELATIONAL OPERATOR: <\n"); }
">"             { printf("RELATIONAL OPERATOR: >\n"); }

"="             { printf("ASSIGNMENT OPERATOR: =\n"); }

"&"             { printf("BITWISE OPERATOR: &\n"); }
"|"             { printf("BITWISE OPERATOR: |\n"); }
"^"             { printf("BITWISE OPERATOR: ^\n"); }
"~"             { printf("BITWISE OPERATOR: ~\n"); }
"!"             { printf("LOGICAL OPERATOR: !\n"); }
"<<"            { printf("BITWISE OPERATOR: <<\n"); }
">>"            { printf("BITWISE OPERATOR: >>\n"); }

"+="            { printf("ARITHMETIC ASSIGNMENT OPERATOR: +=\n"); }
"-="            { printf("ARITHMETIC ASSIGNMENT OPERATOR: -=\n"); }
"*="            { printf("ARITHMETIC ASSIGNMENT OPERATOR: *=\n"); }
"/="            { printf("ARITHMETIC ASSIGNMENT OPERATOR: /=\n"); }
"%="            { printf("ARITHMETIC ASSIGNMENT OPERATOR: %%=\n"); }

"&="            { printf("BITWISE ASSIGNMENT OPERATOR: &=\n"); }
"|="            { printf("BITWISE ASSIGNMENT OPERATOR: |=\n"); }
"^="            { printf("BITWISE ASSIGNMENT OPERATOR: ^=\n"); }
"<<="           { printf("BITWISE ASSIGNMENT OPERATOR: <<=\n"); }
">>="           { printf("BITWISE ASSIGNMENT OPERATOR: >>=\n"); }


[0-9]+          { printf("NUMBER: %s\n", yytext); }
[0-9]+"."[0-9]+ { printf("NUMBER: %s\n", yytext); }

"("             { printf("SYMBOL: (\n"); }
")"             { printf("SYMBOL: )\n"); }
"{"             { printf("SYMBOL: {\n"); }
"}"             { printf("SYMBOL: }\n"); }
"["             { printf("SYMBOL: [\n"); }
"]"             { printf("SYMBOL: ]\n"); }
";"             { printf("SYMBOL: ;\n"); }
","             { printf("SYMBOL: ,\n"); }
"."             { printf("SYMBOL: .\n"); }
"->"            { printf("SYMBOL: ->\n"); }

[ \t\n]         ;


%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error opening file");
            return 1;
        }
        yyin = file; // Use yyin to point to the input file
    }
    yylex();
    return 0;
}
