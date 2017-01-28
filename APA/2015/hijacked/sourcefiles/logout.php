<?php  
session_start();
session_destroy();  
//Deleting all the existing Cookies
$past = time() - 3600;
foreach ( $_COOKIE as $key => $value )
{
    setcookie( $key, $value, $past, '/' );
}
header("Location: login.php");//use for the redirection to some page  
?>