<?php
$dbuser = 'race1';
$dbpass = 'race1@mysqlTYUVNM';
$dbname = 'race1';
$host = 'localhost';
@error_reporting(1);

$con = mysqli_connect($host,$dbuser,$dbpass);

if (!$con)
{
    
    echo "Failed to connect to MySQL ";
}
mysqli_select_db($con, $dbname) or die ( "Unable to connect to the database: $dbname");
?>




 
