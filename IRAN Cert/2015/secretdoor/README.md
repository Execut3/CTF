#SecretDoor

**Category:** Web
**Points:** 50

**Description:**

There's this crazy friend of mine that recently got into web designing using php and sql. he also created a page for a company. but he said that he can access to anyfile in anyplace whenever he wants, when he is logged in his account. can you find the backdoor in this page that can access to files in another directories. and I almost forgot, his name is 'john'. it's not it's login name, but sure you can find it. and remember your job is to read me the /home/flag.txt file!!!

##SecretDoor-Solution:

not ready yet.

**But if you're eager to know, here is a little hint:**

It is a combination of Blind/Union SQL Injection, Directory traversal vulnerability. First a sql-injection in first page (blind sqli).

```
username:	john")) or 1 limit 0,1 #
password:	<anything>
```

And we will be redirected to ```welcome.php```. As the description said, There is a secret door that is accessible only when we are login as john. so we should find a way to login as john.

In the login page there is no way to bypass it and then read values in database, because there is a length-filter on inputs of username/password. if lenght of username|password is more than 23, there will be no sql-fetch.
So we should find another way in. what if we work with ```limit 0,1```. It means, What if we find the id of john and set query on that id. for example if id of john is '7', we can use:

```
john")) or 1 limit 7,1 #
```

Finding ID for john
--

As the description said, his name is john. Also there is a url for seeing our profile: ```/profile.php?id=1```
Also we can see other users profile by changing the value of ```id```. But the problem is there are a lot of IDs on the database. so we should run a script to find the id of john.

But there is a better solution, fire up burp, send a request to ```/profile.php?id=1```, now capture it using burp, send it to intruder, set a variable on ```id```, now use a range of 1-2000, and at last grep on the name 'john'.
Now Start intruder.

by this method we can find the id of 'john', now it's time to login as john:

```
john")) or 1 limit 1298,1 #
```

Now if we look out on our profile we see that we are logged in as 'john'.

Finding a way to read ```/home/flag.txt```
--

Now that we are login as john, we can check for vulnerable fields and parameters. looks like search.php is vulnerable now (to sql injection).
Ok! so we can read ```/home/flag.txt``` using sql ```read_file``` command.

But this field has a simple waf filtering going on. here is a php-code for filtering section:

```php
<?php
	function blacklist($id)
	{
	$id= preg_replace('/or/i',"", $id);			
	$id= preg_replace('/and/i',"", $id);		
	$id= preg_replace('/load_file/i',"", $id);		
	$id= preg_replace('/union/i',"", $id);		
	$id= preg_replace('/order/i',"", $id);		
	$id= preg_replace('/select/i',"", $id);
	while (preg_match('/flag/', $id))
		{
			$id= preg_replace('/flag/',"", $id);
		}
	return $id;
	}
?>
```

We can bypass this filtering easily by just using method like this: ```oorr``` will become ```or``` and etc.
 
SO the query in search.php, should be like this:

```
-1%' oorr 1=2 uniunionon selselectect 1,(seselectlect loaload_filed_file('/home/flag.txt')),3#
```

But this doesn't work. We should find a way to read it. we can achieve this by hexing the '/home/flag.txt'. So the last query will look like this:

```
-1%' oorr 1=2 uniunionon selselectect 1,(seselectlect loaload_filed_file(0x2f686f6d652f666c61672e747874)),3#
```

And we will see the flag: **SQLI_is_M0R3_Than_AweS0M3**


