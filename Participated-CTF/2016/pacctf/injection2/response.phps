<?php
  $user = 'Injection2';
  $password = 'injection2';
  $db = 'Injection2';
  $host = 'localhost';

  $link = mysql_connect("$host", $user, $password);
  // Check connection
  if ($link == false) {
    die("Connection failed, please contact PACTF and let them know.");
  }
  $select = mysql_select_db($db, $link);
  if ($select == false) {
    die("wtf");
  }
  // Nobody will be able to inject into our code now!
  mysql_query('SET SQL_MODE="NO_BACKSLASH_ESCAPES"');
  $uname = mysql_real_escape_string($_POST["username"]);
  $pswd = mysql_real_escape_string($_POST["password"]);

  $query = 'SELECT * FROM Injection2 WHERE username="'.$uname.'" AND password="'.$pswd.'";';
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
