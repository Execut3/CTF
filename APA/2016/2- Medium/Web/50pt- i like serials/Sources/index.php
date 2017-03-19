<html>
	<head>
		<title>Simple PHP! authenticator</title>
	</head>
	<body>
		
		<h3>I wrote a simple php website and i used a awesome authentication process (which i made.. don't laugh) for it.<h3>
		<h4>Can you as a pentester check it for me and verify it has no bug. If it's vulnerable, please read flag.php as a POC</h4>
		<!-- I disabled admin authentication for now, and i also put the source in index.phps -->
		
		<form method="POST" action="">
			<label>Your username: </label>
			<input type="text" name="username" />
			<br>
			<label>Your password:</label>
			<input type="password" name="password" />
			<br>
			<input type="submit" name="action" value="Login to portal" />
		</form>

		<?php
            error_reporting(0);
			include 'flag.php';
		
			class profile
			{
				public $username;
				private $password;
				
				public function __construct($username, $password)
				{
					$this->username=$username;
					$this->password=$password;
				}
			}
			
			
			$user = serialize(new profile('admin', 'admin'));
			
			$cookie_= "";
			for ($i=0; $i<strlen($user); $i++)
				$cookie_.=chr(ord($user[$i])^0x03);
		
		
		if(isset($_POST['username']) && isset($_POST['password']))
			{
				$user_profile = new profile($_POST['username'], $_POST['password']);
				if($_POST['username']=="admin")
					die("Sorry, but the admin account is disabled for now... Coma back later.");
				$serialized = serialize($user_profile);
				$cookie_= "";
				for ($i=0; $i<strlen($serialized); $i++)
					$cookie_.=chr(ord($serialized[$i])^0x03);
				setcookie("custom_cookie", $cookie_, time() + (8000 * 30), "/");
			}
		else if(isset($_COOKIE['custom_cookie']))
			{
				$cookie_ = $_COOKIE['custom_cookie'];
				$serialized = "";
				for ($i=0; $i<strlen($cookie_); $i++)
					$serialized.=chr(ord($cookie_[$i])^0x03);
				$profile = unserialize($serialized);
				if($profile->username=="admin")
					echo 'Welcome, flag is '. flag;
				else
					echo "Not authorized, dear user: ".$profile->username;
			}

		?>

	</body>
</html>
