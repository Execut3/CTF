#Command-line Quiz

**Category:** Unknown
**Points:** 100

**Description:** 

telnet caitsith.pwn.seccon.jp

User:root

Password:seccon

The goal is to find the flag word by “somehow” reading all *.txt files.

**Write-up:**

In this challenge we should read flag.txt, but we don't have premission to read it, so we should solve 5 stages before we can access to it. Each of these Stages are described in a document file.
Output of commands that i used to solve this challenge, are displayed below:

```bash
Execut3@kali:~$ telnet caitsith.pwn.seccon.jp
Trying 153.120.171.19...
Connected to caitsith.pwn.seccon.jp.
Escape character is '^]'.

CaitSith login: root
Password:

$ ls
bin         etc         init        linuxrc     sbin        stage2.txt  stage4.txt  tmp
dev         flags.txt   lib         proc        stage1.txt  stage3.txt  stage5.txt  usr
$ cat flags.txt
cat: can't open 'flags.txt': Operation not permitted
$ cat stage1.txt
What command do you use when you want to read only top lines of a text file?

Set your answer to environment variable named stage1 and execute a shell.

  $ stage1=$your_answer_here sh

If your answer is what I meant, you will be able to access stage2.txt file.
$
$ stage1=head sh
$ cat stage2.txt
What command do you use when you want to read only bottom lines of a text file?

Set your answer to environment variable named stage2 and execute a shell.

  $ stage2=$your_answer_here sh

If your answer is what I meant, you will be able to access stage3.txt file.
$
$ stage2=tail sh
$ cat stage3.txt
What command do you use when you want to pick up lines that match specific patterns?

Set your answer to environment variable named stage3 and execute a shell.

  $ stage3=$your_answer_here sh

If your answer is what I meant, you will be able to access stage4.txt file.
$
$ stage3=grep sh
$ cat stage4.txt
What command do you use when you want to process a text file?

Set your answer to environment variable named stage4 and execute a shell.

  $ stage4=$your_answer_here sh

If your answer is what I meant, you will be able to access stage5.txt file.
$
$ stage4=awk sh
$ cat stage5.txt
OK. You reached the final stage. The flag word is in flags.txt file.

flags.txt can be read by only one specific program which is available
in this server. The program for reading flags.txt is one of commands
you can use for processing a text file. Please find it. Good luck. ;-)
$
$ sed -n 1p flags.txt
OK. You have read all .txt files. The flag word is shown below.
$ sed -n 2,3p flags.txt

SECCON{CaitSith@AQUA}
```

And the flag is ```SECCON{CaitSith@AQUA}```.
