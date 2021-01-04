<?php

	error_reporting(0);
	session_start();
	
	if(!isset($_SESSION['score']))
	{
		$_SESSION['score'] = 0;
		
	}
	
	if($_POST['answer'] !== $_SESSION['solution'] OR $_SESSION['solution']=='')
	{	    
		unset($_SESSION['solution']);
		header('Location:index.php');	    
	}
	else
	{    
		$_SESSION['score'] = $_SESSION['score'] + 1;
		$_SESSION['result'] = $_SESSION['score'];
		unset($_SESSION['solution']);
		header('Location:index.php');
	}

?>
