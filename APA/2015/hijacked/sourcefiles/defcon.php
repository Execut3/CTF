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
		<?php
			function clear($address){
				$fn = str_replace('../', '', $address);
				$fn = str_replace('salt','', $fn);
				$fn = str_replace('random','khkhkhkh', $fn);
				return $fn;
			}
			$text = '';
			if(count($_GET)>0)
			{
				if(isset($_GET['file']))
				{
					$file = 'defcon/'.clear($_GET['file']);
					if(substr_count($file, '.') <= 3)
						{
						$text = file_get_contents($file);
						if(empty($text))
							{
								$label = 'about defcon';
								$text = file_get_contents('defcon/about.txt');
							}
						}
					else
						{
							$label = 'about defcon';
							$text = file_get_contents('defcon/about.txt');
						}	
				}
				else
				{
					$label = 'what the ....!';
					$text = 'usage: ?file';
				}
			}
			else
			{
				$label = 'about defcon';
				$text = file_get_contents('defcon/about.txt');
			}
		?>
		
		<h2><?php echo $label; ?></h2>
		<?php
			echo "<!-- opened file : ".$file." -->";
		?>
		<p>
		
		<?php
		echo $text;
		?>
		
		</p>

	

	
	</div>
	

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

	
	
	<!-- Designed by : J0hnTHEh4ck3r -->
	
	
	
</body>

</html>