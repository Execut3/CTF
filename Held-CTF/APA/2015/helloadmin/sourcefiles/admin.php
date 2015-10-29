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
		
		if(strcmp(1,$is_admin)!==0)
		{
			echo "Your Not Admin";
		}
		else
		{
			echo "hello ".$_SESSION['username'];
			$mycookie = '"'.$mycookie.'"';
			$sql="SELECT * FROM users WHERE mycookie=$mycookie LIMIT 0,1";
			$result=mysql_query($sql);
			$row = mysql_fetch_array($result);
			if($row)
			{
				if($row['is_admin']==1)
				{
					$sql1="SELECT flag FROM flag LIMIT 0,1";
					$result1=mysql_query($sql1);
					$row1 = mysql_fetch_array($result1);
					if($row1)
					{
						echo "...Congratz body... flag is ".$row1['flag'];
					}
				}
			}
			else 
			{
				print_r(mysql_error());
			}
		}	
	?>
</body>
</html>