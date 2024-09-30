#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fcntl.h>
#include <sys/sendfile.h>

int win() {
    printf("You win! Here is your shell:\n");

    system("/bin/sh");
}

int get_favorite_food() {
    char food[64];

    printf("What is your favorite food?\n");
    fflush(stdout);

    fgets(food, 100, stdin);

    printf("Hmmm..... %s...", food);
}

int main() {
    int rand_num;

    srand(time(0));
    rand_num = rand() % 100;

    get_favorite_food();

    if (rand_num <= 50) {
        printf("That sounds delicious!\n");
    } else if (rand_num <= 70) {
        printf("Eh, that sounds okay.\n");
    } else if (rand_num <= 80) {
        printf("That's my favorite food too!\n");
    } else if (rand_num <= 90) {
        printf("I've never tried that before!\n");
    } else if (rand_num <= 100) {
        printf("Ew! I would never eat that.\n");
    }

    return 0;
}