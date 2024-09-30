#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/sendfile.h>

int win() {
    printf("You win! Here is your shell:\n");
    fflush(stdout);

    system("/bin/sh");
}

int echo(int amount) {
    char message[32];

    fgets(message, amount, stdin);

    printf(message);
    fflush(stdout);
}

int main() {
    printf("Is it just me, or is there an echo in here?\n");
    fflush(stdout);

    echo(31);
    echo(100);

    return 0;
}