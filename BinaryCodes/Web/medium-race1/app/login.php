<?php
session_start();
?>

<?php
if(isset($_SESSION['username']) && isset($_SESSION['is_admin']))  
{  
	header("Location: welcome.php");//redirect to login page to secure the welcome page without login access.  
	
}

include("connect.php");

if(isset($_POST['username'])){
	$username = $_POST['username'];
	$username_escape = mysqli_real_escape_string($con, $username);
	
	$sql = "SELECT id, username, password from users where username='$username_escape';";
	$result = mysqli_query($con, $sql);
	
	$row = $result->fetch_assoc();
	
	if($username === $row['username'] and $_POST['password'] === $row['password']){
			//sleep(1);
			
			$password = $_POST['password'];
			//echo '<h1>Logged in as</h1>'.($username_escape);

			$uid = $row['id'];
			$sql = "SELECT is_admin from privileges where userid='$uid'";
			$result = mysqli_query($con, $sql);

			$row = $result->fetch_assoc();
			$_SESSION['username']=$username;
			$_SESSION['password']=$password;
			if($row['is_admin']){
				$_SESSION['is_admin']=$row['is_admin'];
			} else {
				
			}

			
			
			header('Location: welcome.php');
			
	} else {
			echo 'password or username is not correct';
	}

}

?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="sql-injection.gif">
        <title>Login pleaserewrewrewr</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/signin.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <form class="form-signin" action="login.php" name="loginform" method="POST">
                <h2 class="form-signin-heading text-center">Please sign in</h2>
                <label for="inputUsername" class="sr-only">Username</label>
                <input type="text" name="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus>
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
                <label>No profile,s <a href="register.php">register here</a></label>
            </form>


        </div>
    </body>
</html>