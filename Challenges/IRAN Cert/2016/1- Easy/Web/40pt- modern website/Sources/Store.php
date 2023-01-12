<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>APACERT CTF Competition</title>

    <link href="style.css" type="text/css" rel="stylesheet"/>
</head>

<body bgcolor="#000000">


<div style=" margin-top:10px;color:#FFF; font-size:16px; text-align:left">


    <h3 id="agent_location"></h3>

    <?php
    //echo $_SERVER['HTTP_USER_AGENT'] . "\n\n";

    $browser = get_browser(null, true);
    //echo current ($browser);


    while ($i = key($browser)) {
        if ($i == 'parent') {
            echo "<div class='error'> Some Web sites may not be displayed correctly or work correctly in '" . current($browser) . "' try using an other browser." . '<br /></div>';
        }
        next($browser);
    }
    ?>

</div>

<div style="margin-left: 20px; margin-top:20px;color:#FFF; font-size:24px;">
    Welcome to Our Modern Website
    <br/>
    Login and checkout our new products

    <div align="center"
         style=" margin-top: 20px;border:20px; background-color:grey;;width:400px; height:150px;">
        <div style="padding-top:10px; font-size:15px;">


            <!--Form to post the contents -->
            <form action="" name="form1" method="post">

                <div style="margin-top:15px; height:30px;">Username : &nbsp;&nbsp;&nbsp;
                    <input type="text" name="uname" value=""/></div>

                <div> Password : &nbsp; &nbsp;
                    <input type="text" name="passwd" value=""/></div>
                </br>
                <div style=" margin-top:9px;margin-left:90px;"><input type="submit" name="submit" value="Submit"/></div>
            </form>
        </div>
    </div>

    <div style="color:#FFF; font-size:16px; text-align:left">

        <?php
        //including the Mysql connect parameters.
        include("sql-connect.php");
        error_reporting(0);

        function check_input($value)
        {
            if (!empty($value)) {
                // truncation (see comments)
                $value = substr($value, 0, 20);
            }

            // Stripslashes if magic quotes enabled
            if (get_magic_quotes_gpc()) {
                $value = stripslashes($value);
            }

            // Quote if not a number
            if (!ctype_digit($value)) {
                $value = "'" . mysql_real_escape_string($value) . "'";
            } else {
                $value = intval($value);
            }
            return $value;
        }


        $uagent = $_SERVER['HTTP_USER_AGENT'];

        $IP = $_SERVER['REMOTE_ADDR'];

        //echo 'Your IP ADDRESS is: ' . $IP;
        //echo 'Your User Agent is: ' .$uagent;
        // take the variables
        if (isset($_POST['uname']) && isset($_POST['passwd'])) {
            $uname = check_input($_POST['uname']);
            $passwd = check_input($_POST['passwd']);

            /*
            echo 'Your Your User name:'. $uname;
            echo "<br>";
            echo 'Your Password:'. $passwd;
            echo "<br>";
            echo 'Your User Agent String:'. $uagent;
            echo "<br>";
            echo 'Your User Agent String:'. $IP;
            */

            //logging the connection parameters to a file for analysis.
            $fp = fopen('result.txt', 'a');
            fwrite($fp, 'User Agent:' . $uname . "\n");

            fclose($fp);


            $sql = "SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1";
            $result1 = mysql_query($sql);
            $row1 = mysql_fetch_array($result1);
            if ($row1) {
                $insert = "INSERT INTO `security`.`uagents` (`uagent`, `ip_address`, `username`) VALUES ('$uagent', '$IP', $uname)";
                //echo $insert;
                mysql_query($insert);
                //echo 'Your IP ADDRESS is: ' .$IP;
                //echo "<br>";
                //echo 'Your User Agent is: ' . $uagent;
                print_r(mysql_error());
                echo '<p>Successfully logged in!</p>';

            } else {
                //echo "Try again looser";
                print_r(mysql_error());
                echo '<p>Authentication failed</p>';

            }
        }
        ?>
    </div>


</body>
</html>
