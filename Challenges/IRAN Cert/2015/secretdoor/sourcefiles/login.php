<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="icon.gif">
    <title>LogIn Please</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/signin.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">
      <form class="form-signin" action="" name="loginform" method="post">
        <h2 class="form-signin-heading text-center">Please sign in</h2>
        <label for="inputEmail" class="sr-only">Email</label>
        <input type="text" name="email" id="inputEmail" class="form-control" placeholder="Email" required autofocus>
		<label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>
	  
		  
		<?php
		include("connect.php");
		// error_reporting(0);
		
		//Starting a session, if session is set, so redirect user
		session_start();  
		if(isset($_SESSION['username']))  
		{  
			header("Location: welcome.php");//redirect to login page to secure the welcome page without login access.  
		}    
		// take the variables
		if(isset($_POST['email']) && isset($_POST['password']))
		{
			$email=$_POST['email'];
			$password=$_POST['password'];

			// connectivity
			$email = strip_tags( trim( $_POST['email'] ) );
			$len = strlen($email);
			if($len<24 && strlen($password)<10)
			{
				$email='"'.$email.'"';
				$password='"'.$password.'"'; 
				@$sql="SELECT id, email, username, password FROM users WHERE email=(($email)) and password=($password) LIMIT 0,1";
				$result=mysql_query($sql);
				$row = mysql_fetch_array($result);
				if($row)
					// and if(mysql_num_rows($result)==1)
				{
					$_SESSION['email']=$row['email'];				//here session is used and value of $user_email store in $_SESSION.
					$_SESSION['username']=$row['username'];	
					$_SESSION['id']=$row['id'];						
					header('Location: welcome.php');
				}
				else  
				{
					// print_r(mysql_error());
				}
			}		
		}
		?>
	  	  
    </div>
  </body>
</html>
