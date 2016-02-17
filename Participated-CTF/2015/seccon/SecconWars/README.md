#Seccon Wars

**Category:** Steganography
**Points:** 100

**Description:**

In this challenge, we are given a url: 'https://youtu.be/8SFsln4VyEk'

Looking at video shows that there a qrcode of black color in center of video. But it's not easy to detect it.
We need to find a way to get this qrcode, cause obviosly the flag is in it.

Looking at video file shows that bunch of texts with yellow color are moving in the screen and whenever they cross the qrcode, we can detect some part of qrcode with them.

A simple way is to just take snapshots of screen and put them all together.

###Method:
VLC player has an option to get screenshot of each video's frame.
For enabling it:

```Tools -> Preferences -> Show Settings : all -> Vidoe -> enable : scene video filter ```

And under Scene Filter : 1- add a path 2- set period of frames, i used 12: means after 12 frames shown, take a snapshot

And just by playing video, you will get snapshots of the video while playing.
after that I used photoshop to put them all together and i set each png (layer) to screen mode for combining them all.

Here is the result:

![Image of 1]
(./images/steg-1.jpg)

By cropping it and make a little change in brightness, here is the result:

![Image of 2]
(./images/steg-2.jpg)

Now just use any program to decode this picture. i used this online site: https://zxing.org/w/decode

And we will be rewarded with a flag:

### SECCON{TH3F0RC3AVVAK3N53P7}

