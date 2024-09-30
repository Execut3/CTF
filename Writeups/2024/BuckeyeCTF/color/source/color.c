#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char FAVORITE_COLOR[0x20];
char FLAG[0x28];

void parse_answer(char *dst, char *src) {
    int i = 0;
    while (src[i] != '\n') i++;
    memcpy(dst, src, i);
}

int main() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    memset(FAVORITE_COLOR, 0, 0x20);
    char *envFlag = getenv("FLAG");
    if (envFlag) {
        strcpy(FLAG, envFlag);
    } else {
        strcpy(FLAG, "bctf{fake_flag}");
    }

    char buf[0x60];
    printf("What's your favorite color? ");
    fgets(buf, 0x60, stdin);
    parse_answer(FAVORITE_COLOR, buf);

    printf("%s!?!? Mid af color\n", FAVORITE_COLOR);

    return 0;
}
