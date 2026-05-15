<?php
$courseShortName = $_POST['course_short_name'] ?? '';

$courseShortName = trim($courseShortName);

if (!preg_match('/^[a-zA-Z0-9\s\-]{1,50}$/', $courseShortName)) {
    die("Invalid course short name.");
}

$safeCourseShortName = htmlspecialchars(
    $courseShortName,
    ENT_QUOTES,
    'UTF-8'
);

echo "<td>" . $safeCourseShortName . "</td>";
?>

#Fix explanation

#This fix uses:

#Input validation
#Only letters, numbers, spaces, and hyphens are allowed.
#Length restriction
#The course short name must be between 1 and 50 characters.
#Output encoding
#htmlspecialchars() converts special HTML characters into safe HTML entities.
#PHP documentation explains that characters with special meaning in HTML should be converted to entities.