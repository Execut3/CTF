<?php
error_reporting(0);
session_start();
$authorized = isset($_SESSION["authorized"]) && isset($_COOKIE["auth"]);
$userdb = array(
	"guest" => "guest",
	"admin" => "itcouldbeanything"
);
if(isset($_GET["logout"])) {
	unset($_SESSION["authorized"]);
	setcookie("auth", "");
	$authorized = False;
}
if(!$authorized && isset($_GET["login"]) && isset($_GET["pass"])) {
	if(!isset($userdb[$_GET["login"]]) || $_GET["pass"] != $userdb[$_GET["login"]]) {
		echo "Wrong credentials<br><br>";
	} else {
		$_COOKIE["auth"] = base64_encode(time().":".$_GET["login"]); 
		setcookie("auth", $_COOKIE["auth"]);
		$_SESSION["authorized"] = 1;
		$authorized = True;
	}
}
if(!$authorized) {
    echo "Very simple authentication form";
	echo "<form action='#'>Login <input type='text' name='login' value='guest'><br>";
	echo "Password <input type='pass' name='pass' value='guest'><br>";
	echo "<input type='submit' value='Login'>";
	echo "</form>";
} else {
	$auth = explode(":", base64_decode($_COOKIE["auth"]), 2);
	$time = $auth[0];
	$login = $auth[1];
	echo "Authorized as ".htmlentities($login)."<br>";
	if($login == "admin") {
		echo "Flag: APACTF{N0NeedToKnowP@sswordTh!sT!m3}<br>";
	}
	echo "<a href='?logout=1'>logout</a>";		
}
?>