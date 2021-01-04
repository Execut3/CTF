<?php
if (isset($_GET['num'])) {
     if (is_numeric($_GET['num'])){
          if (strlen($_GET['num']) < 7){
               if ($_GET['num'] > 999999)
                    echo "flag_XXX";
          }
     }
}
?>
