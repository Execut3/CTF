We are given a dump file named `dump`. (File is too big and is not uploaded in the git folder.)

First let's run `file` command on the file and see what we get.
```bash
$ file dump 
dump: ELF 64-bit LSB core file, x86-64, version 1 (SYSV), SVR4-style, from 'python3 wreck.py', real uid: 1000, effective uid: 1000, real gid: 1000, effective gid: 1000, execfn: '/usr/bin/python3', platform: 'x86_64'
```

a little strange file and seem to have signature on many files in it.
Now let's run `binwalk` on it and see what files are stored in it.

```bash
$ binwalk dump 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 64-bit LSB core file AMD x86-64, version 1 (SYSV)
18052         0x4684          Unix path: /usr/bin/python3.10
32768         0x8000          ELF, 64-bit LSB shared object, AMD x86-64, version 1 (SYSV)
611664        0x95550         Unix path: /usr/lib/locale/C.UTF-8.utf8/LC_CTYPE
612064        0x956E0         Unix path: /usr/lib/locale/C.utf8/LC_CTYPE
743584        0xB58A0         Unix path: /usr/lib/python3.10/lib-dynload
821272        0xC8818         Copyright string: "copyright -- copyright notice pertaining to this interpreter"
821285        0xC8825         Copyright string: "copyright notice pertaining to this interpreter"
841584        0xCD770         Unix path: /home/gsemaj/.local/lib/python3.10/site-packages/PIL/../pillow.libs/libjpeg-e44fd0cd.so.62.4.0
900032        0xDBBC0         Unix path: /home/gsemaj/.local/lib/python3.10/site-packages/PIL/../pillow.libs/
921584        0xE0FF0         Unix path: /home/gsemaj/.local/bin:/home/gsemaj/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/loc
1005216       0xF56A0         Unix path: /usr/lib/python3.10/lib-dynload/_bz2.cpython-310-x86_64-linux-gnu.so
1012624       0xF7390         Unix path: /usr/lib/python3.10/lib-dynload/_lzma.cpython-310-x86_64-linux-gnu.so
1030767       0xFBA6F         Copyright string: "Copyright CNRI, All Rights Reserved. NO WARRANTY."
^C

```

as you can see many many files exist in it. let's list the files and their positions into another file for better analyzing.

I tried to extract all files in a folder and see what usefull data i can get, But it consumed many space, so I stoped extraction and tried to analyze it without extracting all files. (Consumed over 20G for me before stop!)

let's run the `strings` and see if we can fine anything useful:

```bash
$ strings dump
....
Set the internal flag to true.
        that call wait() once the flag is true will not block at all.
    Support for flags
f_flag
f_flag
__abc_tpflags__
flag.jpg
"flag.jpg"
__flags__
sys.flags
    unless th
....
```

And we can see many junk data which are not useful. 
There was a `flag.jpg` file which got my attention.
Let's see if we can recover it from the dump file.

I looked at the `binwalk.txt` and tried to find any file named `flag.jgp`, but nothing found.
Then looked for any jpg or jpeg related files.

There was a file with following details which get my attention and is `JPEG` file:
```
2108736       0x202D40        JPEG image data, JFIF standard 1.01
```

Now lets try to fetch it from that position. using `dd` command:

```bash
$ dd if=dump of=output.jpg bs=1 skip=2108736 count=25986
```
(Note: the size of file is `2134722 − 2108736`)

and it will get us the `output.jpg` which is the flag image.