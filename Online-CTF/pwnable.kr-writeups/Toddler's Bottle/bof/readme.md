## Challenge

Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw:guest)

## Solution

```bash
$ checksec --file=bof
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   70) Symbols	  No	0		1		bof
```
