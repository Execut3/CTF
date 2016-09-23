<?php
  $user = 'Injection1';
  $password = 'injection1';
  $db = 'Injection1';
  $host = 'localhost';

  $link = mysql_connect("$host", $user, $password);
  // Check connection
  if ($link == false) {
    die("Connection failed, please contact PACTF and let them know.");
  }
  $select = mysql_select_db($db, $link);
  $uname = $_POST["username"];
  $pswd = $_POST["password"];

  $query = 'SELECT * FROM Injection1 WHERE username="'.$uname.'" AND password="'.$pswd.'";';
  $result = mysql_query($query);
  if (mysql_num_rows($result) === 1) {
    $row = mysql_fetch_array($result);
    echo "<h1>Welcome!</h1>";
    if ($row["username"] === "admin") {
      echo '<p>Your flag is: '.$row["flag"].'</p>';
    }
    else {
      echo "<p>Hey! You aren't admin! Get outta here!</p>";
    }
  }
  else {
    echo "<h1>Login Failed</h1>";
    echo "<p>Get outta here!</p>";
  }
?>
