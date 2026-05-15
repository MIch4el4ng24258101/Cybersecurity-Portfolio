<?php
$courseShortName = $_POST['course_short_name'];

echo "<td>" . $courseShortName . "</td>";
?>

#Why it is vulnerable

#The user input is printed directly into the HTML page. 
#If an attacker enters JavaScript instead of normal text, the browser may execute it. 
#OWASP recommends output encoding so user input is treated as text, not code.