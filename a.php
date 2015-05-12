<?php
$temp1 = file_get_contents("temp.txt",FILE_USE_INCLUDE_PATH);
$temp2 = file_get_contents("temp2.txt",FILE_USE_INCLUDE_PATH);
$content = "Temp&eacuterature MCP9808 : ".$temp1."<br />"."Temp&eacuterature TMP36 : ".$temp2."<br />";
echo $content;
?>
