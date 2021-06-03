<?php
$path="chatfile2.txt";
if(!unlink($path)){
  echo "You have an error";
} else {
  header("Location: indexexpt.php?deletesuccess");
}
 
