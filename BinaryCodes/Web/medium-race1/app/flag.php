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
		include('header.php');
		include('title_section.php');
	 ?>
	<div class="container">
        <?php        
            if ($_SESSION['is_admin'] === '1' ) {
				include("connect.php");
                $sql = "SELECT flag from flag;";
				$result = mysqli_query($con, $sql);
				$row = $result->fetch_assoc();
				//echo($row['flag']);
				//echo 'fds';
            } else {
            echo "<h2> I belive only admin can see the flag!";
            }
        ?>
    </div>
	

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>


</body>

</html>