<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>HelloAdminLoginPage</title>
</head>

<body>

	<form action="" method="POST">
		<label>username</label>
		<input type="text" name="username">
		<label>password</label>
		<input type="password" name="password">
		<input type="submit" value="Login">
	</form>

	<?php
		include("connect.php");
		
		session_start();  
		if(isset($_SESSION['username']) && isset($_SESSION['mycookie']))  
		{  
			header("Location: user.php");
		}    
		// take the variables
		if(isset($_POST['username']) && isset($_POST['password']))
		{
			$username= mysql_real_escape_string($_POST['username']);
			$password= mysql_real_escape_string($_POST['password']);
			$username='"'.$username.'"';
			$password='"'.$password.'"';
			
			@$sql="SELECT * FROM users WHERE username={$username} and password={$password} LIMIT 0,1";
			$result=mysql_query($sql);
			$row = mysql_fetch_array($result);
			if($row)
			{
				$_SESSION['username']=$row['username'];				//here session is used and value of $user_email store in $_SESSION.
				$_SESSION['password']=$row['password'];
				$_SESSION['isadmin']=$row['is_admin'];		
				setcookie("MyCookie", $row['mycookie'], time() + 86400, '/');
				setcookie("Admin", $row['is_admin'], time() + 86400, '/');
				if($row['is_admin']===1)
				{
					header('Location: admin.php');
				}
				else
				{
					header('Location: user.php');
				}
			}
			else  
			{
				echo 'Sorry';
			}
		}
	?>

</body>
</html>