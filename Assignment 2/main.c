#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 1024
#define MAX_WORD_LENGTH 512

int is_keyword(const char *word) {
    const char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if",
        "int", "long", "register", "return", "short", "signed", "sizeof", "static",
        "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "printf"
    };
    size_t num_keywords = sizeof(keywords) / sizeof(keywords[0]);

    for (size_t i = 0; i < num_keywords; ++i) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

int is_identifier(const char *word) {
    if (isalpha(word[0])) {
        for (size_t i = 1; i < strlen(word); ++i) {
            if (!isalnum(word[i])) {
                return 0;
            }
        }
        return 1;
    }
    return 0;
}

int is_operator(const char *word) {
    const char *operators[] = {"+", "-", "*", "/", "="};
    size_t num_operators = sizeof(operators) / sizeof(operators[0]);

    for (size_t i = 0; i < num_operators; ++i) {
        if (strcmp(word, operators[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void analyze_code(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        return;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), file)) {
        char *token = strtok(line, " \t\n;,.(){}[]<>\"\'");
        while (token) {
            int length = strlen(token);

            if (is_keyword(token)) {
                printf("Keyword: %s, Length: %d\n", token, length);
            } else if (is_identifier(token)) {
                printf("Identifier: %s, Length: %d\n", token, length);
            } else if (is_operator(token)) {
                printf("Operator: %s, Length: %d\n", token, length);
            } else {
                printf("Other: %s, Length: %d\n", token, length);
            }

            token = strtok(NULL, " \t\n;,.(){}[]<>\"\'");
        }
    }

    fclose(file);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <source_file>\n", argv[0]);
        return 1;
    }

    analyze_code(argv[1]);
    return 0;
}
