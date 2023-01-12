<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="sql-injection.gif">
    <title>LogIn Please</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/signin.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">
      <form class="form-signin" action="" name="loginform" method="post">
        <h2 class="form-signin-heading text-center">Please sign in</h2>
        <label for="inputUsername" class="sr-only">Username</label>
        <input type="text" name="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus>
		<label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
		<label>No profile, <a href="register.php">register here</a></label>
      </form>
		
	  
		  
		<?php
		include("connect.php");
		
		//Starting a session, if session is set, so redirect user
		session_start();  
		if(isset($_SESSION['username']) && isset($_SESSION['mysession']) && isset($_SESSION['is_admin']))  
		{  
			header("Location: welcome.php");//redirect to login page to secure the welcome page without login access.  
		}    
		// take the variables
		if(isset($_POST['username']) && isset($_POST['password']))
		{
			$username = strip_tags( trim( $_POST['username'] ) );
			$password = strip_tags( trim( $_POST['password'] ) );
			$username = mysql_real_escape_string($username);
			$password = mysql_real_escape_string($password);
			$username='"'.$username.'"';
			$password='"'.$password.'"';
			@$sql="SELECT * FROM users WHERE username=(($username)) and password=($password) LIMIT 0,1";
			$result=mysql_query($sql);
			$row = mysql_fetch_array($result);
			if($row)
			{
				$_SESSION['username']=$username;
				$_SESSION['mysession']=$row['mysession'];
				$_SESSION['password']=$row['password'];
				$_SESSION['is_admin']=$row['is_admin'];
				setcookie("CTF_Session", $row['mysession'], time() + (86400 * 30), '/', null, null, true);
				header('Location: welcome.php');
			}
			else 
			{
				// Add a false trace on time-based sqli just for honey them
				include('logout.php');
				// print_r(mysql_error());
			}
		}
		?>
	  	  
    </div>
  </body>
</html>
