<?php
$dbuser ='root';
$dbpass ='';
$dbname ="helloadmin";
$host = 'localhost';
@error_reporting(0);
@$con = mysql_connect($host,$dbuser,$dbpass);
// Check connection
if (!$con)
{
    echo "Failed to connect to MySQL: " . mysql_error();
}
    @mysql_select_db($dbname,$con) or die ( "Unable to connect to the database: $dbname");
?>




 
