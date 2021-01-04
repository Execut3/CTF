<?php
$flag = "flag_php";

if (isset($_GET['num'])) {
     if (is_numeric($_GET['num'])){
          if (strlen($_GET['num']) < 7){
               if ($_GET['num'] > 999999)
                    echo "flag_f9609f2362ffa1f5f89261f59237e97b";
          }
     }
} else {
     highlight_file("source.php");
}

?>
