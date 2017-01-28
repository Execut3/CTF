<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>APA-IUTcert</title>
    <link href="./css/bootstrap.min.css" rel="stylesheet">
    <link href="css/heroic-features.css" rel="stylesheet">

</head>

<body>
	
	<?php
		include('stuff/header.php');
		include('private/check_session.php');
	?>
	<!-- Page Content -->
    <div class="container">
        <!-- Jumbotron Header -->
        <header class="jumbotron hero-spacer">
            <h2 class="text-center">APA-IUTcert CAPTURE the FLAG</h2>
			<h4 class="text-center">A challenge for experts</h4>
        </header>
    </div>
	<div class="container">	
		<form action="" method="post">
			<label> If you like this site. please help us out by your comments. </label>
			<input type="text" name="comment" class="form-control" placeholder="Your Comment here..." required autofocus>
			<p></p>
			<button class="btn btn-md btn-primary btn-block" type="submit">Send your comment to us!</button>
		</form>

		<?php  
		if(isset($_POST['comment']))
		{
			$comment=$_POST['comment'];
			echo '<p>Thanks for your help</p>';
			echo '<p>Your comment: "'.$comment.'" recieved successfully.';
		}	
			
		?>
	</div>
	

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

	
	
	<!-- Designed by : J0hnTHEh4ck3r -->
	
	
	
</body>

</html>