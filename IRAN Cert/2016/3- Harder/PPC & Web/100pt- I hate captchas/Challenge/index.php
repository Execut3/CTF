<!DOCTYPE html>

<?php 
    error_reporting(0);
    session_start();
    
    if(!isset($_SESSION['result']))
        {
            $_SESSION['result'] = 0;
        }
?>

<html>
    <head>
        <title>Break me as long as i give you the FLAG</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h3>Break me as long as I give you the FLAG</h3>
        <br>
        <p>I wrote a simple captcha validation site, Just to know if you could break it or not.</p>
        <p>Have fun and try to break this captcha for 100 times in less than 2 minutes<p>
        <br>
        <form action="check.php" method="post"> 
            <img src="captcha.php" onerror=javascript:error();><br>
            Enter Code:<input type="text" name="answer" /> 
            <input type="submit" name="Submit" value="Submit" /> <br><br>        
           <?php
                echo 'Total successful breaks: '.$_SESSION['result'];
                if($_SESSION['result'] > 100)
                {  
                    echo "<h2>Nice job, Flag is APACTF{Wh0_l!k3_C4ptch4sSsSsS}</h2>";
                }
           ?> 
        </form>
    </body>
</html>
