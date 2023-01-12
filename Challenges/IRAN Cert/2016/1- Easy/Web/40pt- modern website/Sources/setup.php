<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>SETUP DB</title>
</head>

<body bgcolor="#000000">

<div style=" margin-top:20px;color:#FFF; font-size:24px; text-align:center"> 
Welcome&nbsp;&nbsp;&nbsp;
<font color="#FF0000"> Dhakkan </font>
<br>
</div>

<div style=" margin-top:10px;color:#FFF; font-size:23px; text-align:left">
<font size="3" color="#FFFF00">
SETTING UP THE DATABASE SCHEMA AND POPULATING DATA IN TABLES:
<br><br> 


<?php
//including the Mysql connect parameters.
include("db-creds.inc");
$con = mysql_connect($host,$dbuser,$dbpass);
if (!$con)
  {
  die('[*]...................Could not connect to DB, check the creds in db-creds.inc: ' . mysql_error());
  }
//@mysql_select_db('mysql',$con)	
	
//purging Old Database	
	$sql="DROP DATABASE IF EXISTS modern_website";
	if (mysql_query($sql))
		{echo "[*]...................Old database 'Modern website' purged if exists"; echo "<br><br>\n";}
	else 
		{echo "[*]...................Error purging database: " . mysql_error(); echo "<br><br>\n";}
//Creating new database security
	$sql="CREATE database `modern_website` CHARACTER SET `gbk` ";
	if (mysql_query($sql))
		{echo "[*]...................Creating New database 'modern_website' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating database: " . mysql_error();echo "<br><br>\n";}
//creating table users
$sql="CREATE TABLE modern_website.users (id int(3) NOT NULL AUTO_INCREMENT, username varchar(20) NOT NULL, password varchar(60) NOT NULL, PRIMARY KEY (id))";
	if (mysql_query($sql))
		{echo "[*]...................Creating New Table 'USERS' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating Table: " . mysql_error();echo "<br><br>\n";}
//creating table emails
//$sql="CREATE TABLE modern_website.emails
//		(
//		id int(3)NOT NULL AUTO_INCREMENT,
//		email_id varchar(30) NOT NULL,
//		PRIMARY KEY (id)
//		)";
//	if (mysql_query($sql))
//		{echo "[*]...................Creating New Table 'EMAILS' successfully"; echo "<br><br>\n";}
//	else 
//		{echo "[*]...................Error creating Table: " . mysql_error();echo "<br><br>\n";}
//creating table uagents
$sql="CREATE TABLE modern_website.uagents
		(
		id int(3)NOT NULL AUTO_INCREMENT,
		uagent varchar(256) NOT NULL,
		ip_address varchar(35) NOT NULL,
		username varchar(20) NOT NULL,
		PRIMARY KEY (id)
		)";
	if (mysql_query($sql))
		{echo "[*]...................Creating New Table 'UAGENTS' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating Table: " . mysql_error();echo "<br><br>\n";}

//inserting data
$sql="INSERT INTO modern_website.users (id, username, password) VALUES ('1', 'test', 'test'), ('2', 'admin', 'APACTF{N3V3R_TRU57_US3R_INPUTS_even_in_user_agents}')";
	if (mysql_query($sql))
		{echo "[*]...................Inserted data correctly into table 'USERS'";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}
//inserting data
//$sql="INSERT INTO `modern_website`.`emails` (id, email_id) VALUES ('1', 'Dumb@dhakkan.com'), ('2', 'Angel@iloveu.com'), ('3', 'Dummy@dhakkan.local'), ('4', 'secure@dhakkan.local'), ('5', 'stupid@dhakkan.local'), ('6', 'superman@dhakkan.local'), ('7', 'batman@dhakkan.local'), ('8', 'admin@dhakkan.com')";
//	if (mysql_query($sql))
//		{echo "[*]...................Inserted data correctly  into table 'EMAILS'";echo "<br><br>\n";}
//	else 
//		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}
//CREATE TABLE security.search (id int(3) NOT NULL AUTO_INCREMENT, search varchar(20) NOT NULL, PRIMARY KEY (id));
//INSERT INTO `security`.`search` (search) VALUES ( 'Dumb@dhakkan.com'), ('Angel@iloveu.com'), ('Dummy@dhakkan.local'), ( 'secure@dhakkan.local'), ( 'stupid@dhakkan.local'), ( 'superman@dhakkan.local'), ( 'batman@dhakkan.local'), ( 'admin@dhakkan.com')"; 
//including the Challenges DB creation file.
?>


</font>
</div>
</body>
</html>