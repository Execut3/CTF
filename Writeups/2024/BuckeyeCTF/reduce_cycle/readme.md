## reduce_recycle [269 pts]

**Category:** Forensics
**Solves:** 38

## Description
I forgot the randomly generated 12-character password I used to encrypt these files.... is there anything you can do to help me get my flag back??

dogs_wearing_tools.zip
important_flags.7z

https://bctf-24-stage1.s3-us-east-2.amazonaws.com/12622b0e612e2ad5045f13d05fc490aff893fe10d811d027680a36e6e4a8f805/dogs_wearing_tools.zip

https://bctf-24-stage1.s3-us-east-2.amazonaws.com/b1952503efe0f4a6557afe79dca6509526669f21d092ac98840b7d026f568e63/important_flags.7z

### Solution

In this challenge, we are given two files

- dogs_wearing_tools.zip

- important_flags.7z

and seem to both files are encrypted with same password. so if we find the password for one, the next one is also available.

By the names it's obvious that the importat file is the `import_flags.7z` and seem that we need to find the password from `dogs_wearing_tools.zip` and then use that password to open the other one.

Let's check the zip file:

```bash
$ file dogs_wearing_tools.zip 
dogs_wearing_tools.zip: Zip archive data, at least v2.0 to extract, compression method=store

$ unzip -l dogs_wearing_tools.zip 

Archive:  dogs_wearing_tools.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
  1817550  2024-09-01 19:38   1.png
  1830967  2024-09-01 19:38   2.png
    94416  2024-09-01 19:38   3.png
  1210542  2024-09-01 19:36   4.png
---------                     -------
  4953475                     4 files

```

Let's check if we can find the encryption method used for zip:
```bash
$ 7z l dogs_wearing_tools.zip -slt

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=en_GB.UTF-8,Utf16=on,HugeFiles=on,64 bits,12 CPUs x64)

Scanning the drive for archives:
1 file, 4954033 bytes (4838 KiB)

Listing archive: dogs_wearing_tools.zip

--
Path = dogs_wearing_tools.zip
Type = zip
Physical Size = 4954033

----------
Path = 1.png
Folder = -
Size = 1817550
Packed Size = 1817562
Modified = 2024-09-02 04:08:05
Created = 
Accessed = 
Attributes = A
Encrypted = +
Comment = 
CRC = 346673B4
Method = ZipCrypto Store
Characteristics = NTFS : Encrypt
Host OS = FAT
Version = 20
Volume Index = 0
Offset = 0

Path = 2.png
Folder = -
...
```

As you can see it is using `Method = ZipCrypto Store` which is vulnerable to plain-text attack.

We know that this zip file includes 4 images in png format.
PNG files always start with the following bytes:

```hex
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D
```

Here's how to create a file with these 12 bytes:

```bash
echo -ne '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D' > png_header.bin
```

I tried to crack with `pkcrack` and didn't work:

```bash
pkcrack -C dogs_wearing_tools.zip -c 1.png -p png_header.bin -d decrypted.zip
Plaintext must be at least 13 bytes! Aborting.
```

So i tried to use another powerfull tool named `bkcrack`.

```bash
> bkcrack -C dogs_wearing_tools.zip -c 1.png -p png_header.bin 
bkcrack 1.7.0 - 2024-05-26
[19:18:13] Z reduction using 5 bytes of known plaintext
100.0 % (5 / 5)
[19:18:13] Attack on 1190986 Z values at index 6
Keys: adf73413 6f6130e7 0cfbc537
7.7 % (91746 / 1190986)
Found a solution. Stopping.
You may resume the attack with the option: --continue-attack 91746
[19:19:35] Keys
adf73413 6f6130e7 0cfbc537

```

We have found keys to crack the zip file and open it.
To do so use following command:
```bash
$ bkcrack -C dogs_wearing_tools.zip -k adf73413 6f6130e7 0cfbc537 -c 3.png -d 3.png
```
each file that we want can be recovered using this command.

After opening images we see just image of dogs and nothing useful.

Now let's try to recover the password:
```bash
$ bkcrack -k adf73413 6f6130e7 0cfbc537 -r 12 ?p
bkcrack 1.7.0 - 2024-05-26
[19:29:44] Recovering password
length 0-6...
length 7...
length 8...
length 9...
length 10...
length 11...
length 12...
Password: 2n3Ad3&ZxDvV
19.8 % (1789 / 9025)
Found a solution. Stopping.
You may resume the password recovery with the option: --continue-recovery 326e38202020
[19:30:04] Password
as bytes: 32 6e 33 41 64 33 26 5a 78 44 76 56 
as text: 2n3Ad3&ZxDvV
```

Now opeing the important flags:
```bash
$ 7z e important_flags.7z 

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=en_GB.UTF-8,Utf16=on,HugeFiles=on,64 bits,12 CPUs x64)

Scanning the drive for archives:
1 file, 186 bytes (1 KiB)

Extracting archive: important_flags.7z
--
Path = important_flags.7z
Type = 7z
Physical Size = 186
Headers Size = 138
Method = Copy 7zAES
Solid = -
Blocks = 1

    
Enter password (will not be echoed):
Everything is Ok

Size:       33
Compressed: 186
```

and get the flag:
```bash
cat flag.txt
bctf{flaghere}
```