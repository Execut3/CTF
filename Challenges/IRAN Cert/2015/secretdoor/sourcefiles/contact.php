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
			include("connect.php");
			error_reporting(0);

			if(!isset($_SESSION['username']))  
			{  
				header("Location: login.php");//redirect to login page to secure the welcome page without login access.  
			} 
		?>
		
		<div class="container">
			<h3>You can contact PNT company by this email blahblah@blah.blah</h3>
			<!-- you can contact PNT by this mail, but i will contact them using sql@i --> 
		</div>
		

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>