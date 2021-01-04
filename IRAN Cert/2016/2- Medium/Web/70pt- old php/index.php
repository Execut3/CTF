<html>
    <head>
        <title>My awesome website</title>
    </head>
    <body>
        <h2>Learning PHP is fun</h2>
        <p>I started to learn php and wrote a simple website that just replace strings in the given text.</p>
        <br>
        
        <form method="get" action="">
            <label for="current_string">Current string
            <input type="text" name="current_string">
            <br><br>
            <label for="new_string">New string
            <input type="text" name="new_string">
            <br><br>
            <label for="given_text">Main text to apply changes to
            <textarea name="given_text" rows="5"></textarea>
            <br><br>
            <input type="submit" value="Replace">
        </form>
        
        <?php
            error_reporting(0);
            $prefix = '/';
            $suffix = '/i';            
            
            extract($_GET);
            if( isset($current_string) && isset($new_string) && isset($given_text) ) {
                $pattern = $prefix . $current_string . $suffix;
                $result = preg_replace($pattern, $new_string, $given_text);
                echo '<h1> Result: </h1>';
				echo '<p>'.$result.'</p>';
            }
        ?>
        
    </body>
</html>


