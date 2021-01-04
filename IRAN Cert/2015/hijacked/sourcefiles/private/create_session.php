<?php

include("stuff/rand.php");
include("stuff/salt.php");

function khkh($string)
{
	$h = '';
	for($i=0; $i<strlen($string); $i++)
	{
		$hd = dechex(ord($string[$i]));
		$h .= substr('0',$hd,-2);
		$h .= $hd;
	}
	return strtoupper($h);
}

function dede($string)
{
	$d = '';
	for($i=0; $i<strlen($string)-1;$i+=2)
	{
		$d .= chr(hexdec($string[$i].$string[$i+1]));
	}
	return $d;
}

function new_session($username, $password)
{
	do
	{
		$random_var = get_random();
	} while (preg_match("/[^a-f0-4]/", $random_var));
	$clear = $username.$password.$random_var;
	$salt = get_salt();
	$result = '';
	for($i=0;$i<strlen($clear);$i++)
	{
		for($j=0;$j<strlen($salt);$j++,$i++)
		{
			$result .= $clear{$i} ^ $salt{$j};
		}
	}
	$result = khkh($result);
	$session = strtolower($result);
	return $session;
}

?>