<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>PNT Company</title>
    <link href="./css/bootstrap.min.css" rel="stylesheet">
    <link href="css/heroic-features.css" rel="stylesheet">

</head>

<body>
	
	<?php
	session_start();
	?>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="welcome.php">PNT Company</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
						<a href="contact.php">Contact</a>
                    </li>
                    <li>
						<a href="search.php">Search</a>
                    </li>
                </ul>
				<ul class="nav navbar-nav pull-right">
					<li class="pull-right">
						<a href="profile.php?id=<?php echo $_SESSION['id'] ?>">your-profile</a>
					</li>
					<li class="pull-right">
                        <a href="logout.php">Logout</a>
                    </li>
				</ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container" style="margin-top:100px">

        <?php
		if(!isset($_SESSION['username']))  
			{  
				header("Location: login.php");//redirect to login page to secure the welcome page without login access.  
			}
		else
		{
			$servername = "localhost";
			$username = "sqli";
			$password = "sqlipass";
			$dbname = "sqli";
			// Create connection
			$conn = mysqli_connect($servername, $username, $password, $dbname);
			// Check connection
			// if (!$conn) {
				// die("Connection failed: " . mysqli_connect_error());
			// }
			// check get method
			if(isset($_GET['id']))
			{
				$id = $_GET['id'];
				$id = addslashes($_GET['id']);
				// $id = mysql_real_escape_string($id);
				$sql = "SELECT username,email FROM users WHERE id=$id LIMIT 0,1";
				$result = mysqli_query($conn, $sql);
				if (mysqli_num_rows($result) > 0) {
					// output data of each row
					while($row = mysqli_fetch_assoc($result)) {
						echo "<h2>Username: ".$row['username']."</h2>";
						echo "<h2>Email: ".$row['email']."</h2>";
					}
				} else {
					echo "User not found!";
					echo "<!-- khkhkhkh -->";
				}
			}
		}
		?>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>