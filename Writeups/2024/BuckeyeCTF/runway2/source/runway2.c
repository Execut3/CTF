#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fcntl.h>
#include <sys/sendfile.h>

int win(int check, int mate) {
    if (check == 0xc0ffee && mate == 0x007ab1e) {
        printf("You win! Here is your shell:\n");
        fflush(stdout);

        system("/bin/sh");
    } else {
        printf("No way!");
        fflush(stdout);
    }
}

int get_answer() {
    char answer[16];

    fgets(answer, 0x40, stdin);

    return strtol(answer, NULL, 10);
}

int calculate_answer(int op1, int op2, int op) {
    switch (op)
    {
        case 0:
            return (op1 + op2);
        case 1:
            return (op1 - op2);
        case 2:
            return (op1 * op2);
        case 3:
            return (op1 / op2);
        default:
            exit(-1);
    }
}

int main() {
    int op1;
    int op2;
    int op;
    char operands[5] = "+-*/";
    int input;
    int answer;

    srand(time(0));

    printf("Pop quiz!\n");
    fflush(stdout);

    op1 = rand() % 30;
    op2 = rand() % 30;
    op = rand() % 4;

    printf("What is %d %c %d?\n", op1, op[operands], op2);
    fflush(stdout);

    input = get_answer();
    answer = calculate_answer(op1, op2, op);

    if (input == answer) {
        printf("Good job! No flag though :)\n");
    } else {
        printf("I don't think you're trying very hard.\n");
    }

    return 0;
}