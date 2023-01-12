<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>HelloAdminLoginPage</title>
</head>

<body>
	<?php
		include("connect.php");

		session_start();  
		if(!isset($_SESSION['username']) || !isset($_SESSION['password']) || !isset($_SESSION['isadmin']))  
		{  
			header("Location: logout.php");
		}    
		$mycookie = $_COOKIE['MyCookie'];
		$is_admin = $_COOKIE['Admin'];
		if($_COOKIE['Admin']==0)
		{
			echo "hello ".$_SESSION['username'];
		}
		elseif($_COOKIE['Admin']==1)
		{
			header("Location: admin.php");
		}
		else
		{
			echo "What!---";
		}	
	?>
</body>
</html>