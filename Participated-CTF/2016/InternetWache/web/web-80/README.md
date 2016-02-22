#0ldsk00lBlog

**Category:** Web
**Points:** 80

**Description:**

I stumbled across this kinda oldskool blog. I bet it is unhackable, I mean, there's only static HTML.

##0ldsk00lBlog-Solution:

For this challenge the only thing that we can see is a static page with a bunch of html tags.
Nothing useful. except that in the contents, There is a little hint about GIT.

```html

<html>
<head>
	<title>0ldsk00l</title>
</head>
<body>

	<h1>Welcome to my 0ldsk00l blog.</h1>
	<p>
		Now this is some oldskool classic shit. Writing your blog manually without all this crappy bling-bling CSS / JS stuff.
	</p>

	<h2>2016</h2>
	<p>
		It's 2016 now and I need to somehow keep track of my changes to this document as it grows and grows. All people are talking about a tool called 'Git'. I think I might give this a try.
	</p>

	<h2>1990-2015</h2>
	<p>
		Hmm, looks like totally forgot about this page. I should start blogging more often.
	</p>

	<h2>1990</h2>
	<p>
		I proudly present to you the very first browser for the World Wide Web. Feel free to use it to view my awesome blog.
	</p>

	<h2>1989</h2>
	<p>
		So, yeah, I decided to invent the World Wide Web and now I'm sitting here and writing this. 
	</p>
</body>
</html>
```

So lets check it out.

https://0ldsk00lblog.ctf.internetwache.org/.git/HEAD

and it gives us the response ```ref: refs/heads/master``` which is a big hint that tells us that
the project is controlled with GIT.

But how we can download it's content and search for the flag. There is a simple way to do it. I used
this tool for ripping this git repo: https://github.com/kost/dvcs-ripper

and by running command below, i downloaded all of the git files:

```bash
$./rip-git.pl -v -u https://0ldsk00lblog.ctf.internetwache.org/.git

[i] Downloading git files from https://0ldsk00lblog.ctf.internetwache.org/.git
[i] Auto-detecting 404 as 200 with 3 requests
[i] Getting correct 404 responses
[i] Using session name: tHWacUFs
[d] found COMMIT_EDITMSG
[d] found config
[d] found description
[d] found HEAD
[d] found index
[!] Not found for packed-refs: 404 Not Found
[!] Not found for objects/info/alternates: 404 Not Found
[!] Not found for info/grafts: 404 Not Found
[d] found logs/HEAD
[d] found objects/14/d58c53d0e70c92a3a0a5d22c6a1c06c4a2d296
[d] found objects/db/a52097aba3af2b30ccbc589912ae67dcf5d77b
[d] found objects/26/858023dc18a164af9b9f847cbfb23919489ab2
[d] found objects/8c/46583a968da7955c13559693b3b8c5e5d5f510
[d] found refs/heads/master
[i] Running git fsck to check for missing items
Checking object directories: 100% (256/256), done.
Checking objects: 100% (135/135), done.
[d] found objects/19/49446afea12e0937044fdabe8cc101c87f7c54
[d] found objects/25/a3f35784188ac1c9bf48a94e5a9c815bcb598c
[d] found objects/33/a5c0876603d7a6f9729637f36030bbabb2afa3
[d] found objects/3b/e70be50c04bab8cd5d115da10c3a9c784d6bae
[d] found objects/95/a5396e62ca5c9577f761ebe969f52d3b6a9235
[i] Got items with git fsck: 5, Items fetched: 5
[i] Running git fsck to check for missing items
Checking object directories: 100% (256/256), done.
Checking objects: 100% (135/135), done.
[d] found objects/55/08adb31bf48ae5fe437bdeba60f83982356934
[d] found objects/91/f09a7948e02d891d3a39c058a634a8752aba20
[d] found objects/75/03402e4d48be951cddda34aae6e01905bb5c98
[i] Got items with git fsck: 3, Items fetched: 3
[i] Running git fsck to check for missing items
Checking object directories: 100% (256/256), done.
Checking objects: 100% (135/135), done.
[i] Got items with git fsck: 0, Items fetched: 0
[!] No more items to fetch. That's it!
```

From now on is simple. We should search file/folders for the flag. The flag is in the objects
that are created by git. So we need to find a way to read this objects.
I wrote a simple python code to surf in .git/objects folder and read all the files in that directory
and if it found the flag, will print it in terminal. Here is my code:

```python
import zlib # A compression / decompression library
import glob, os

directory = './.git/objects'
os.chdir(directory)


def read_git_object(filename):
    compressed_contents = open(filename, 'rb').read()
    return zlib.decompress(compressed_contents)

result = []

for folder_name in glob.glob("*"):
    for file_name in glob.glob(folder_name+'/*'):
        try:
            filename = os.path.join(directory, file_name)
            data = read_git_object(filename)
            result.append(data)
        except:
            pass

flag = ''
for r in result:
    if 'IW{' in r:
        index = r.find('IW{')
        while True:
            flag += r[index]
            if r[index] == '}':
                break
            index += 1
            
    if flag:
        break
print 'flag is : %s'%flag
```

Running this command will give us the flag:

```bash
$python solver.py
flag is : IW{G1T_1S_4W3SOME}
```

And the flag is **IW{G1T_1S_4W3SOME}**

