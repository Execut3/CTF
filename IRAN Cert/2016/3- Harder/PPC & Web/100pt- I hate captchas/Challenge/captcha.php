<?php

//error_reporting(E_ALL);
//ini_set('display_errors', 1);

error_reporting(0);
session_start();

if(!isset($_SESSION['time']))
{
    $t = time();    //timestamp
    $_SESSION['otime'] = $t;
    $final = $t + 60*2;
    $_SESSION['time'] = $final; 
    create_image();
}

else
{
    if(time() > $_SESSION['time'])
    {
        session_destroy(); 
    }
    else
    {
        create_image();
    }   
}


function create_image()
{

    header("Content-Type: image/png");
    $image = imagecreatetruecolor(200, 50) or die("Cannot Initialize new GD image stream");

    $background_color = imagecolorallocate($image, 255, 255, 255);
    $text_color = imagecolorallocate($image, 72, 64, 161);
    $line_color = imagecolorallocate($image, 54, 170, 171);
    $pixel_color = imagecolorallocate($image, 255, 27, 0);

    imagefilledrectangle($image, 0, 0, 200, 50, $background_color);

    for ($i = 0; $i < 6; $i++) {
        imagesetthickness($image, rand(1,3));
        imageline($image, 0, rand(0 ,255) % 100, 200, rand(0, 255) % 100, $line_color);
    }

    for ($i = 0; $i < 1000; $i++) {
        imagesetpixel($image, rand() % 200, rand() % 50, $pixel_color);
    }

    $letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $len = strlen($letters);
    $letter = $letters[rand(0, $len - 1)];
   
    $word = "";
    for ($i = 0; $i < 5; $i++) {
        $letter = $letters[rand(0, $len - 1)];
        imagestring($image, 5, 35 + ($i * 30), rand(5, 30), $letter, $text_color);
        $word .= $letter;
    }
    $_SESSION['solution'] = $word;
    imagepng($image);
    imagedestroy($image);

}


?>
