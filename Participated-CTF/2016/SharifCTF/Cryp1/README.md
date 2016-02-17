#Rail Fence Cipher

**Category:** Cryptography
**Points:** 50

**Description:**

Decrypt and find the flag.

##Solution

In this challenge we are given below cipher:

```
AaY  rpyfneJBeaaX0n ,ZZcs uXeeSVJ sh2tioaZ}slrg, ciE-anfGt. eCIyss TzprttFliora{GcouhQIadctm0ltt FYluuezTyorZ 
```

As the name of challenge represent, The encryption is related to rail-fence cipher.
To solve this challenge, I used an online decoder website: "http://www.geocachingtoolbox.com/index.php?page=railFenceCipher"

Putting the number of rails to 24, will give us the below result:

```
A fence is a.yzFrcQclFuy oeYttIoalps ncloses an area, Sharifesri{uamtlzrZTu 0dhGot CGEgZ2VuZXJpYyB0ZXJt},-tITt
```

And we see a part of a message clear: 'A fence is a' & 'sharif'

searching for the clear-text "A fence is a" will lead us to a wikipedia link : "https://en.wikipedia.org/wiki/Fence"

```
A fence is a structure that encloses an area,...
```

Now we have part of the clear-message. if we look at the decrypted text categorized in 24 rails, We will see text below:

```
A.............................................a.............................................Y................
. ........................................... .r...........................................p.y...............
..f.........................................n...e.........................................J...B..............
...e.......................................a.....a.......................................X.....0.............
....n..................................... .......,.....................................Z.......Z............
.....c...................................s......... ...................................u.........X...........
......e.................................e...........S.................................V...........J..........
....... ...............................s.............h...............................2.............t.........
........i.............................o...............a.............................Z...............}........
.........s...........................l.................r...........................g.................,.......
.......... .........................c...................i.........................E...................-......
...........a.......................n.....................f.......................G.....................t.....
.................................. .......................e.....................C.......................I....
.............y...................s.........................s................... .........................T...
..............z.................p...........................r.................t...........................t..
...............F...............l.............................i...............o.............................r.
................a.............{...............................G.............c...............................o
.................u...........h.................................Q...........I.................................
..................a.........d...................................c.........t..................................
...................m.......0.....................................l.......t...................................
....................t..... .......................................F.....Y....................................
.....................l...u.........................................u...e.....................................
......................z.T...........................................y.o......................................
.......................r.............................................Z.......................................
```

The first 12 rows of the decrypted message are correct, But in the 13th row we should fix the message by making the text clear. In other hand
we have part of the crypted-message in clear. So we know after text:```A fence is a ```, We should have " structure". So in the
first column of 13th row, we should replace 'y' with ' '. and in the second column we should replace ' '  with 'e' and so on.

Looking at the decrypted message we can see that by removing first character -> '.' in the 13th column & shifting all furture character to left, we will fix 13th column
and the clear-text will be look like this:

```
A fence is a spl{uamtlzrTu 0dhGirsencloses an area, SharifC tocQclFuyZoeYttIortTIGEgZ2VuZXJpYyB0ZXJt},-tyzFa
```

We should go throught all other rows and fix them to match the cleartext recieved from wikipedia link.
For example in 14th row we should remove 's' to shift character to left. We keep removing characters to recover clear-text recieved from wikipedia.
(remember to add a ' ' at the end of decrypted message after removing each character.)

After removing all the additional characters, We will have something like this:

```
AaY  rpyfneJBeaaX0n ,ZZcs uXeeSVJ sh2tioaZ}slrg. ciE anfGt eCIys TzttFlra{GuhQIctm0t FYuezTrZ
```

Putting number of rails to "21" we will see the clear message as this:

```
A---------------------------------------a---------------------------------------Y------------
- ------------------------------------- -r-------------------------------------p-y-----------
--f-----------------------------------n---e-----------------------------------J---B----------
---e---------------------------------a-----a---------------------------------X-----0---------
----n------------------------------- -------,-------------------------------Z-------Z--------
-----c-----------------------------s--------- -----------------------------u---------X-------
------e---------------------------e-----------S---------------------------V-----------J------
------- -------------------------s-------------h-------------------------2-------------t-----
--------i-----------------------o---------------a-----------------------Z---------------}----
---------s---------------------l-----------------r---------------------g-----------------.---
---------- -------------------c-------------------i-------------------E------------------- --
-----------a-----------------n---------------------f-----------------G---------------------t-
------------ ---------------e-----------------------C---------------I-----------------------y
-------------s------------- -------------------------T-------------z-------------------------
--------------t-----------t---------------------------F-----------l--------------------------
---------------r---------a-----------------------------{---------G---------------------------
----------------u-------h-------------------------------Q-------I----------------------------
-----------------c-----t---------------------------------m-----0-----------------------------
------------------t--- -----------------------------------F---Y------------------------------
-------------------u-e-------------------------------------z-T-------------------------------
--------------------r---------------------------------------Z--------------------------------

A fence is a structure that encloses an area, SharifCTF{QmFzZTY0IGlzIGEgZ2VuZXJpYyB0ZXJt}. ty
```

The flag is ```QmFzZTY0IGlzIGEgZ2VuZXJpYyB0ZXJt```.