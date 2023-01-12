#Dumped!

**Category:** Forensics
**Points:** 100

**Description:**

In Windows Task Manager, I right clicked a process and selected "Create dump file". I'll give you the dump, but in return, give me the flag!

##Solution:

We are given RunMe.DMP.xz file. 
it's archived with xz command. Running

```
$unxz RunMe.DMP.xz
```

Will give us RunMe.DMP file:

```
$file RunMe.DMP
RunMe.DMP: MDMP crash report data
```
Simply just running "strings" command and filtering on "CTF" will give us the flag:

```
$strings RunMe.DMP | grep CTF
SharifCTF{4d7328869acb371ede596d73ce0a9af8}
```

The flag is ```4d7328869acb371ede596d73ce0a9af8```