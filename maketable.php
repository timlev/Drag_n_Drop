<?php
    function maketable()
    {
        print("My table");
    }
    global $categories;

    function import_lesson($csvfile='',$del='|')
    {
        //Make sure file exists
        if (!file_exists($csvfile) || !is_readable($csvfile)){
            echo "Problem openning file.";
            return FALSE;
        }
        global $categories;
        $categories = array();
        $cat_contents = array();
        

        $handle = fopen($csvfile,"r");

        $contents = array();
        while(! feof($handle))
         {
            $row = fgetcsv($handle, 0, $delimiter=$del);
            if ($row != ""){
                $contents[] = $row;
            }
            
         }
         fclose($handle);
         $headers = $contents[0];
         unset($contents[0]);
         #print_r($headers);
         
         $num_cats = count($headers);
         global $words_remaining;
         $words_remaining = 0;
         foreach ($contents as $row){
            for ($i = 0; $i < $num_cats; $i++){
                if ($row[$i] != ""){
                    $categories[$headers[$i]][] = ($row[$i]);
                    $words_remaining += 1;
                }
            }
         }
        #print_r($categories);
    }
    
    function makeheaderbox()
    {
        global $categories;
        foreach ($categories as $cat => $words){
            print '<td><div id="header">' . $cat . '</div></td>';
        }
    }
    
    function makeblanktable()
    {
        #Get number of rows needed
        global $categories;
        $num_words = [];
        foreach ($categories as $cat => $words){
            $num_words[] = count($words);
        }
        $max_words = max($num_words);
        
        #Get number of categories needed
        $num_cats = count($categories);
        
        for ($r=0; $r<$max_words;$r++){
            print '<tr>';
            foreach ($categories as $c => $words){
                #Object name = category number
                echo '<td><div name="' . $c . ',' . $r .'" id="droppable" class="destination"></div></td>';
            }
            print '</tr>';
        }
    }
    
    
    function makechoicetable(){
        
        global $categories;
        $mixed_words = array();
        echo '<table>';
        foreach ($categories as $cat => $words){
            //Add all words to $mixed_words
            foreach ($words as $word){
                $mixed_words[] = array($word, $cat);
            }
        }
        //Shuffle words
        shuffle($mixed_words);

        //Print table rows for choices
        foreach ($mixed_words as $word){
            #print_r($word[0]);
            echo '<div name="' . $word[1] . ',' . $word[0] . '" id="draggable" class="source">' . $word[0] .'</div>';
        }

    
        print '</table>';
    }
?>
