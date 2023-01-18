## Challenge

Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw:guest)


## Solution

`fd` should be value of `1`, so it will call `read`.

```bash
fd@pwnable:~$ ./fd 
pass argv[1] a number
fd@pwnable:~$ ./fd 32
learn about Linux file IO
fd@pwnable:~$ ./fd 4661
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```
