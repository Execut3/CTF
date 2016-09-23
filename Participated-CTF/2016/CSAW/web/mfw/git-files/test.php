<?php
$page = "../templates/home', '..') === true; //" ;
$file = "templates/" . $page . ".php";
echo $file;
echo assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");
// assert("file_exists('$file')") or die("That file doesn't exist!");
?>