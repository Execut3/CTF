<?php
	session_start();
	if(!isset($_SESSION['username'])) 
	{
		header("Location: login.php");
	}
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
                <a class="navbar-brand" href="welcome.php">Do you belive in magic! me neither...</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
					<li>
						<a href="details.php">Other-CTFs</a>
					</li>
					<li>
						<a href="upload.php">Check my file...</a>
					</li>
					<li>
						<a href="flag.php">flag!</a>
					</li>
					<li>
						<a href="logout.php">Logout</a>
					</li>
				</ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>