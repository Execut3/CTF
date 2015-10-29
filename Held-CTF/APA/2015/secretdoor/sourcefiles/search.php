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
		<form action="" method="post">
			<label> Please name your product here, let us search and find it for you! </label>
			<input type="text" name="product_name" class="form-control" placeholder="Product Name here..." required autofocus>
			<p></p>
			<button class="btn btn-md btn-primary btn-block" type="submit">Search 4 Product</button>
		</form>

		<?php  
			include("connect.php");
			// error_reporting(0);

			if(!isset($_SESSION['username']))  
			{  
				header("Location: login.php");//redirect to login page to secure the welcome page without login access.  
			} 

			if($_SESSION['id']==1298)
			{
				// take the variables
				if(isset($_POST['product_name']))
				{
					$product_name=$_POST['product_name'];

					// connectivity
					// $product_name = strip_tags( trim( $_POST['product_name'] ) );
					$product_name = blacklist($product_name);
					//echo $product_name;
					@$sql="SELECT product, price, available FROM products WHERE product LIKE '%$product_name%'";
					$result=mysql_query($sql);
					$row = mysql_fetch_array($result);
					if($row)
					{
						echo 'Product Name:'. $row['product'];
						echo "<br>";
						echo 'Price:' .$row['price'];
						echo "<br>";
						echo 'Is available:' .$row['available'];
						echo "<p></p><p></p>";
					}
					else	
					{
						// print_r(mysql_error());
						echo 'NOT FOUND';
					}
				}	
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
				//if (!$conn) {
				//	die("Connection failed: " . mysqli_connect_error());
				//}
				
				// check get method
				if(isset($_POST['product_name']))
				{
					$product_name=$_POST['product_name'];
					$product_name = strip_tags( trim( $_POST['product_name'] ) );
					$product_name = mysql_real_escape_string($product_name);
					$sql="SELECT product, price, available FROM products WHERE product LIKE '%$product_name%'";
					$result = mysqli_query($conn, $sql);
					if (mysqli_num_rows($result) > 0) {
						// output data of each row
						while($row = mysqli_fetch_assoc($result)) {
							echo 'Product Name:'. $row['product'];
							echo "<br>";
							echo 'Price:' .$row['price'];
							echo "<br>";
							echo 'Is available:' .$row['available'];
							echo "<p></p><p></p>";
						}
					} else {
						// Add a false trace on time-based sqli just for honey them
						echo "Not Found";
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

	<?php
	function blacklist($id)
	{
		$id= preg_replace('/or/i',"", $id);			
		$id= preg_replace('/and/i',"", $id);		
		$id= preg_replace('/load_file/i',"", $id);		
		$id= preg_replace('/union/i',"", $id);		
		$id= preg_replace('/order/i',"", $id);		
		$id= preg_replace('/select/i',"", $id);		
		//$id= preg_replace('/[\/\*]/',"", $id);		
		//$id= preg_replace('/[--]/',"", $id);		
		//$id= preg_replace('/[#]/',"", $id);			
		// $id= preg_replace('/[\s]/',"", $id);		
		//$id= preg_replace('/[\/\\\\]/',"", $id);		
		while (preg_match('/flag/', $id))
		{
			$id= preg_replace('/flag/',"", $id);
		}
		return $id;
	}
	?>

</body>

</html>