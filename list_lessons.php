<?php
$files = scandir("./Lessons");
$lessons = [];
foreach ($files as $file)
{
    if (strpos($file, ".csv") !== false)
    {
        $lessons[] = $file;
    }
}
echo '<h1> Lessons </h1>';
echo '<ul>';
foreach ($lessons as $lesson)
{
    $link_text = str_replace(".csv","",$lesson);
    
    echo '<li><h3><a href="drag_n_drop.php?' . 'lesson=Lessons/' . $lesson . '">' . $link_text . '</a></h3></li>';
}
echo '</ul>';

?>
