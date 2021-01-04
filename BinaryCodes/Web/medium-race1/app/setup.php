<?php
//including the Mysql connect parameters.
include("connect.php");

$con = mysqli_connect($host,$dbuser,$dbpass);
if (!$con)
  {
  die('[*]...................Could not connect to DB, check the creds in db-creds.inc: ' . mysql_error());
  }

//purging Old Database	
	$sql="DROP DATABASE IF EXISTS race1";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Old database 'race1' purged if exists"; echo "<br><br>\n";}
	else 
		{echo "[*]...................Error purging database: " . mysql_error(); echo "<br><br>\n";}

//Creating new database security
	$sql="CREATE database `race1` CHARACTER SET `gbk` ";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Creating New database 'lfi' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating database: " . mysql_error();echo "<br><br>\n";}

//creating table users
$sql="CREATE TABLE race1.users (id int(8) NOT NULL AUTO_INCREMENT, username varchar(10) NOT NULL, password varchar(20) NOT NULL, PRIMARY KEY (id))";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Creating New Table 'USERS' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating Table: " . mysql_error();echo "<br><br>\n";}
	
//inserting user-items
$sql="INSERT INTO race1.users (id, username, password) VALUES 
        ('1', 'admin', 'wc7pELQ7f8Sed')";

	if (mysqli_query($con, $sql))
		{echo "[*]...................Inserted data correctly into table 'USERS'";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}


$sql="CREATE TABLE race1.privileges (userid int(8) NOT NULL AUTO_INCREMENT, is_admin varchar(1) DEFAULT '0', PRIMARY KEY (userid))";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Creating New Table 'PRIVILEGES' successfully";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error creating Table: " . mysql_error();echo "<br><br>\n";}
	
//inserting user-items
$sql="INSERT INTO race1.privileges (userid, is_admin) VALUES 
        ('1', '1')";

	if (mysqli_query($con, $sql))
		{echo "[*]...................Inserted data correctly into table 'PRIVILEGES'";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}

$sql="CREATE TABLE race1.flag (id int(8) NOT NULL AUTO_INCREMENT, flag varchar(111), PRIMARY KEY (id))";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Inserted data correctly into table 'flag'";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}
        
$sql="INSERT INTO race1.flag (flag) VALUES  ('flag_c4b42180c54db9cbd97da95a1e469801')";
	if (mysqli_query($con, $sql))
		{echo "[*]...................Inserted data correctly into table 'flag'";echo "<br><br>\n";}
	else 
		{echo "[*]...................Error inserting data: " . mysql_error();echo "<br><br>\n";}

?>
