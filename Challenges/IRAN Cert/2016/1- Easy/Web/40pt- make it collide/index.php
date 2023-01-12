<!DOCTYPE html>
<html>
<head>
	<title>You should provide two strings that could make a collision, can you do that? (I don't think so!)</title>
</head>
<body>

<pre>
if (isset($_GET['pass1']) and isset($_GET['pass2'])) {
    if ($_GET['pass1'] != $_GET['pass2'])
    	if (md5($_GET['pass1']) === md5($_GET['pass2']))
        	die('Nice job, Flag is '.$flag);
    else
        print 'Sorry, You didn\'t make a collision';
}
</pre>

</body>
</html>

<?php
error_reporting(0);
$flag='APA{First_l00k_for_7h3_bug5}';
if (isset($_GET['pass1']) and isset($_GET['pass2'])) {
    if ($_GET['pass1'] != $_GET['pass2'])
    	if (md5($_GET['pass1']) === md5($_GET['pass2']))
        	die('Nice job, Flag is '.$flag);
    else
        print 'Sorry, You didn\'t make a collision';
}
?>