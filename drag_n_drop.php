<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="drag_n_drop_theme.css" />
        <title>My Site</title>
        <?php
            require('maketable.php');
            import_lesson($csvfile=$_GET['lesson'], $delimiter=',');
            #import_lesson($csvfile="Lessons/people_places_things.csv", $delimiter=',');
            echo '<script> var words_remaining=' . $words_remaining . '</script>'
        ?>
    <link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.css" rel="stylesheet">
    <link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.2/css/lightness/jquery-ui-1.10.2.custom.min.css" rel="stylesheet">
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui-touch-punch/0.2.2/jquery.ui.touch-punch.min.js"></script>

        <script>
        $(document).ready(function(){
        $(function() {
          $( ".source" ).draggable({ revert: "invalid" });
          $( ".destination" ).droppable({
            drop: function( event, ui ) {
              var dragged_category = ui.draggable.attr("name").split(",")[0];
              var dropped_category = $(this).attr("name").split(",")[0];
              if (dragged_category == dropped_category){
                  ui.draggable.draggable("disable");
                  $(this).css({"background-color":"yellow"});
                  $(this).text(ui.draggable.text());
                  ui.draggable.hide();
                  score += 1;
                  words_remaining -= 1;
                  moves += 1;
                  $("#status").text("Current score: " + score + " Words remaining: " + words_remaining);
                  if (words_remaining == 0){
                     document.getElementById("menu_link").innerHTML = "Finished!<br>Current score: " + score + " Words remaining: " + words_remaining + "<br>Moves: " + moves
                  }
	          }
	          else{
	              ui.draggable.css({"color":"red"});
	              moves += 1;
	              
	          }

            }
          });
        });
        });

            var score = 0;
            var moves = 0;
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
    
    <h3 id="status">App status area ready...</h3>
    <center><h2><a href="list_lessons.php">Lesson Menu</a></h2></center>

    </body>

</html>
