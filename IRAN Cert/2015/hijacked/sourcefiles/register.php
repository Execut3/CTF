<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="sql-injection.gif">
    <title>APA-IUTcert CTF</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/signin.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">
      <form class="form-signin" action="" name="loginform" method="post">
        <h2 class="form-signin-heading text-center">Please Register</h2>
        <label for="inputUsername" class="sr-only">Username</label>
        <input type="text" name="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus>
		<label for="inputEmail" class="sr-only">Email</label>
        <input type="email" name="email" id="inputEmail" class="form-control" placeholder="Email" required>
		<label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
		<label>Already have profile, <a href="login.php">Login here</a></label>
      </form>
	  
		  
		<?php
		include("connect.php");
		include("private/create_session.php");
		
		//Starting a session, if session is set, so redirect user
		session_start();  
		if(isset($_SESSION['username']) && isset($_SESSION['mysession']) && isset($_SESSION['is_admin']))  
		{  
			header("Location: welcome.php");//redirect to login page to secure the welcome page without login access.  
		}    
		// take the variables
		if(isset($_POST['username']) && isset($_POST['password']) && isset($_POST['email']))
		{
			// $username = strip_tags( trim( $_POST['username'] ) );
			$username = mysql_real_escape_string($_POST['username']);
			$password = mysql_real_escape_string($_POST['password']);
			$email = mysql_real_escape_string($_POST['email']);
			$mysession = new_session($username, $password);
			
			$sql="INSERT INTO users ".
				 "(email, username, password, mysession, is_admin) ".
				 "VALUES ".
				 "('{$email}', '{$username}', '{$password}', '{$mysession}', '0')";
			if(@mysql_query($sql))
			{
				$_SESSION['username']=$username;
				$_SESSION['mysession']=$mysession;
				$_SESSION['password']=$password;
				$_SESSION['is_admin']=$is_admin;
				setcookie("CTF_Session", $row['mysession'], time() + (86400 * 30), '/', null, null, true);
				header('Location: welcome.php');
			}
			else 
			{
				echo 'username or email exist... sorry!';
				foreach ( $_COOKIE as $key => $value )
				{
					setcookie( $key, $value, $past, '/' );
				}
			}
		}
		?>
	  	  
    </div>
  </body>
</html>
