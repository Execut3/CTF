<?php
include('header.php');		
//error_reporting(E_ALL);
//ini_set('display_errors', '1');

?>
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
		include('title_section.php');
	 ?>

	<div class="container">
		<h2>Upload something</h2>
		<p>
			Here i created a module that will get your zip file, parse it and tell you how many files does exist in it.
		</p>
		
		<form method="post" action="" enctype="multipart/form-data">
			<input type="file" name='upload_file'>
			<input type="submit">
		</form>
		
		<?php
		
			$UPLOADS = '/var/www/site/uploads/';
			
			if (!empty($_FILES['upload_file'])) {
			 // First scan all directories and delete files with more that 10 seconds created-time
				$paths = scandir($UPLOADS);
				$now = time();
				foreach($paths as $path) {
					if ($path == '.') {
						continue;
					}
					$mtime = filemtime($UPLOADS . $path);
					if ($now - $mtime > 2) {
						shell_exec('rm -rf ' . $UPLOADS . $path);
						//echo $UPLOADS . $path . '-';
					}
				}

			    // Upload all files for this session to this unique folder
				//$path = $UPLOADS . substr(str_shuffle(str_repeat('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', mt_rand(1,20))),1,20) . '/';
				$path = $UPLOADS . session_id();
				echo "<p>Creating a directory for your files: $path</p>";
				
				if (!mkdir($path, 0777, true)) {
					die('There was an error when creating directory for your files.');
				}

				$zip = $path . uniqid('zip');
				echo "<p>Assign a unique ID to your uploaded file. Copying....</p>";

				//echo ($_FILES['upload_file']['tmp_name']) . "-";
				if (move_uploaded_file($_FILES['upload_file']['tmp_name'], $zip)) {
					shell_exec('unzip -j -n ' . $zip . ' -d ' . $path);
					unlink($zip);
					echo "<p>Unziping files</p>";

				$files_in_uploaded_path = scandir($path);
				$count = 0;
				echo "<ul>";
				foreach($files_in_uploaded_path as $pp) {
				 if ($pp === '.' or $pp === '..') continue;
				 $count += 1;
				 echo "<li>".$path.$pp."</li>";
				};
				echo "</ul>";
				echo "<p>Total $count files found. Removing other files</p>";

				shell_exec('find ' . $path.'/ -name ".*" -delete');

				}
				else {
					echo 'Error while uploading file. Please try again.';
				}
			}
		?>
				
	</div>
	
	<!-- source /source.php -->
	

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>
	
</body>

</html>
