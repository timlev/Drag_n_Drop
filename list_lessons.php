<?php
echo '<style>h1 {background-color: #abcdef;
    border: solid black 3pt; 
    border-radius: 25px;
    font-size: 2em;
    text-align: center;
    font-family:Arial;
    text-shadow: 0px 1px 1px #fff;
    //background-image: -webkit-gradient(linear, left top, left bottom, from(#ccc), to(#999));
    max-width: 200px;
}
</style>';
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
