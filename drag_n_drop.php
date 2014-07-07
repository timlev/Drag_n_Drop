<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="drag_n_drop_theme.css" />
        <title>My Site</title>
        <?php
            require('maketable.php');
            import_lesson($csvfile="Lessons/people_places_things.csv", $delimiter=',');
            echo '<script> var words_remaining=' . $words_remaining . '</script>'
        ?>
        <script>
            var score = 0;
            
            function allowDrop(ev) {
                ev.preventDefault();
            }

            function drag(ev) {
                appStatus("Dragging the "+ev.target.getAttribute('id'));
                ev.dataTransfer.setData("Text", ev.target.id);
                ev.dataTransfer.dropEffect='move';
            }

            function drop(ev) {
                ev.preventDefault();
                var data = ev.dataTransfer.getData("Text");
                ev.target.appendChild(document.getElementById(data));
                var element = ev.dataTransfer.getData("Text");
                appStatus("Dropped "+element+" into the "+ev.target.getAttribute('id'));
                if (ev.target.getAttribute('id').split(",")[0] != element.split(",")[0]){
                    document.getElementById(ev.target.getAttribute('id')).style.color = "red";
                }
                else if (ev.target.getAttribute('id').split(",")[0] == element.split(",")[0]){
                    document.getElementById(ev.target.getAttribute('id')).style.color = "green";
                    document.getElementById(element).style.color = "green";
                    document.getElementById(element).removeAttribute("draggable");
                    document.getElementById(ev.target.getAttribute('id')).removeAttribute("ondrop");
                    document.getElementById(ev.target.getAttribute('id')).removeAttribute("ondragover");
                    score += 1;
                    words_remaining -= 1;
                    appStatus("Current score: " + score + " Words remaining: " + words_remaining);
                    if (words_remaining == 0){
                        document.getElementById("menu_link").innerHTML = "Finished!<br>Current score: " + score + " Words remaining: " + words_remaining
                    }
                }
                else {
                    document.getElementById(ev.target.getAttribute('id')).style.color = "black";
                }
            }


            function appStatus(msg){
                document.getElementById('app_status').innerHTML = msg;
            }
        </script>

    </head>
    
    <body>
    <div id="menu_link"></div>
    <table>
        <tr>
            <?= makeheaderbox() ?>
        </tr>
        <?= makeblanktable() ?>
    </table>
    <?= makechoicetable() ?>
    
    <h3 id="app_status">App status area ready...</h3>


    </body>

</html>
