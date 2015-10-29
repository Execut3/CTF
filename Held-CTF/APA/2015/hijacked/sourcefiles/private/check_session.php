<?php
	session_start();
	
	if(!isset($_SESSION['username']) || !isset($_SESSION['mysession']) || !isset($_SESSION['password']) || !isset($_SESSION['is_admin'])) 
	{
		header("Location: login.php");
	}
	else
	{
		$mysession = $_SESSION['mysession'];
		if(isset($_COOKIE['CTF_Session']) && $_COOKIE['CTF_Session']===$_SESSION['mysession'])
		{
			if(!$_SESSION['is_admin'])
			{
				echo "<!-- welcome not-admin-user : ".$_SESSION['username']." -->";
			}
			else	// if user is admin
			{
				// Here user has a valid session. Here we check if CTF_Session is valid and if user is admin or not
				$ctf_session = $_COOKIE['CTF_Session'];
				if(!preg_match("/[^A-Za-z0-9]/", $ctf_session))
				{
					// valid here
					$username = $_SESSION['username'];
					$password = $_SESSION['password'];
					$mysession = $_SESSION['mysession'];
					if($ctf_session === $mysession)
					{
						// Connect to database and do furture validations here
						// Validating user with database
						include("connect.php");
						// $username = mysql_real_escape_string($username);
						$mysession = mysql_real_escape_string($mysession);
						// $password = mysql_real_escape_string($password);
						$result = mysql_query("select * from users where username=($username) and mysession='$mysession' limit 0,1");
						$row = mysql_fetch_array($result);
						if($row)
						{
							// Getting flag and showing it to the user.
							@$sql = "select * from flag limit 0,1";
							$result = mysql_query($sql);
							$flag_row = mysql_fetch_array($result);
							if($flag_row)
							{
								$flag = $flag_row['flag'];
								echo "<script>alert('Congratz boy. flag: ".$flag."');</script>";
							}
							else
							{
								echo "<script>alert('Something is wrong with our portal. please contact us as fast as possible');</script>";
							}
						}
						
					}
					else
					{
						echo "<script>alert('You really think its that easy... Really!!!!!');</script>";
					}
				}
				else
				{
					echo "<script>alert('Buddy, Are you trying SQLI me. just come on!!!!');</script>";
				}
			}
		}
		else
		{
			echo "<script>alert('Your doing something that i dont like');</script>";
		}
		setcookie("CTF_Session", $mysession, time() + (86400 * 30), '/', null, null, true);
		
		
	}		
// ?>