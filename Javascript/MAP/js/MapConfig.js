

   var g_map_backgroundColor = "black";        // background to draw map on
   var g_map_borderColor = "black";            // state border color  
   var g_map_highlightBorderColor = "black";  // highlighted state border color

   var g_map_baseRGB = [255,255,255];          // state color default
   var g_map_highlightRGB = [0,100,200];       // state color when highlighted

   var g_map_infoBoxFillRGB   = [0,0,0];       // info box background color
   var g_map_infoBoxBorderRGB = [255,255,255]; // info box border color
   var g_map_infoBoxTextRGB   = [255,255,255]; // info box text color

   var g_map_useInfoBox = true;  // default to use the info box for all states
   var g_map_isIE9 = false;      // must detect IE9 for proper mouse position

   
   
   
   var g_map_stateMap = null;


   
   var g_map_canvas;
   var g_map_context;
   var g_map_renderInterval;




   function map_userSetup()
   {

    
      for ( var abbrev in g_map_stateMap )
      {
         var state = g_map_stateMap[abbrev]; 
         var nameAndAbbrev = state.myPrettyName + "  (" + state.myAbbrev + ")";

         state.setInfoBoxText(nameAndAbbrev);
         state.addInfoBoxText(""); // add a blank line
      }

      g_map_stateMap["AL"].addInfoBoxText("Population: 5,108,468");
      g_map_stateMap["AK"].addInfoBoxText("Population: 733,406");
      g_map_stateMap["AZ"].addInfoBoxText("Population: 7,431,344");
      g_map_stateMap["AR"].addInfoBoxText("Population: 3,067,732");
      g_map_stateMap["CA"].addInfoBoxText("Population: 38,965,193");
      g_map_stateMap["CO"].addInfoBoxText("Population: 5,913,324");
      g_map_stateMap["CT"].addInfoBoxText("Population: 3,617,176");
      g_map_stateMap["DC"].addInfoBoxText("Population: 678,972");
      g_map_stateMap["DE"].addInfoBoxText("Population: 1,044,321");
      g_map_stateMap["FL"].addInfoBoxText("Population: 22,975,931");
      g_map_stateMap["GA"].addInfoBoxText("Population: 11,145,304");
      g_map_stateMap["HI"].addInfoBoxText("Population: 1,430,877");
      g_map_stateMap["ID"].addInfoBoxText("Population: 1,990,456");
      g_map_stateMap["KY"].addInfoBoxText("Population: 4,540,745");
      g_map_stateMap["LA"].addInfoBoxText("Population: 4,559,475");
      g_map_stateMap["ME"].addInfoBoxText("Population: 1,402,106");
      g_map_stateMap["MD"].addInfoBoxText("Population: 6,196,525");
      g_map_stateMap["MA"].addInfoBoxText("Population: 7,020,058");
      g_map_stateMap["MI"].addInfoBoxText("Population: 10,041,241");
      g_map_stateMap["MN"].addInfoBoxText("Population: 5,761,530");
      g_map_stateMap["MS"].addInfoBoxText("Population: 2,940,452");
      g_map_stateMap["MO"].addInfoBoxText("Population: 6,215,144");
      g_map_stateMap["MT"].addInfoBoxText("Population: 1,142,746");
      g_map_stateMap["NE"].addInfoBoxText("Population: 1,988,698");
      g_map_stateMap["NV"].addInfoBoxText("Population: 3,210,931");
      g_map_stateMap["NH"].addInfoBoxText("Population: 1,405,105");
      g_map_stateMap["NJ"].addInfoBoxText("Population: 9,320,865");
      g_map_stateMap["NM"].addInfoBoxText("Population: 2,115,266");
      g_map_stateMap["NY"].addInfoBoxText("Population: 19,469,232");
      g_map_stateMap["NC"].addInfoBoxText("Population: 10,975,017");
      g_map_stateMap["ND"].addInfoBoxText("Population: 788,940");
      g_map_stateMap["OH"].addInfoBoxText("Population: 11,812,173");
      g_map_stateMap["OK"].addInfoBoxText("Population: 4,088,377");
      g_map_stateMap["OR"].addInfoBoxText("Population: 4,227,337");
      g_map_stateMap["PA"].addInfoBoxText("Population: 12,951,275");
      g_map_stateMap["RI"].addInfoBoxText("Population: 1,098,082");
      g_map_stateMap["SC"].addInfoBoxText("Population: 5,464,155");
      g_map_stateMap["SD"].addInfoBoxText("Population: 928,767");
      g_map_stateMap["TN"].addInfoBoxText("Population: 7,204,002");
      g_map_stateMap["TX"].addInfoBoxText("Population: 30,976,754");
      g_map_stateMap["UT"].addInfoBoxText("Population: 3,454,323");
      g_map_stateMap["VT"].addInfoBoxText("Population: 647,818");
      g_map_stateMap["VA"].addInfoBoxText("Population: 8,752,297");
      g_map_stateMap["WA"].addInfoBoxText("Population: 7,841,283");
      g_map_stateMap["WV"].addInfoBoxText("Population: 1,766,107");
      g_map_stateMap["WI"].addInfoBoxText("Population: 5,931,367");
      g_map_stateMap["WY"].addInfoBoxText("Population: 586,485");
      g_map_stateMap["IN"].addInfoBoxText("Population: 6,892,124");
      g_map_stateMap["IL"].addInfoBoxText("Population: 12,516,863");
      g_map_stateMap["KS"].addInfoBoxText("Population: 2,944,376");
      
      g_map_stateMap["DC"].addInfoBoxText("Capital: National Capital");
      g_map_stateMap["AL"].addInfoBoxText("Capital: Montgomery");
      g_map_stateMap["AK"].addInfoBoxText("Capital: Juneau");
      g_map_stateMap["AZ"].addInfoBoxText("Capital: Phoenix");
      g_map_stateMap["AR"].addInfoBoxText("Capital: Little Rock");
      g_map_stateMap["CA"].addInfoBoxText("Capital: Sacramento");
      g_map_stateMap["CO"].addInfoBoxText("Capital: Denver");
      g_map_stateMap["CT"].addInfoBoxText("Capital: Hartford");
      g_map_stateMap["DE"].addInfoBoxText("Capital: Dover");
      g_map_stateMap["FL"].addInfoBoxText("Capital: Tallahassee");
      g_map_stateMap["GA"].addInfoBoxText("Capital: Atlanta");
      g_map_stateMap["HI"].addInfoBoxText("Capital: Honolulu");
      g_map_stateMap["ID"].addInfoBoxText("Capital: Boise");
      g_map_stateMap["IL"].addInfoBoxText("Capital: Springfield");
      g_map_stateMap["IN"].addInfoBoxText("Capital: Indianapolis");
      g_map_stateMap["IA"].addInfoBoxText("Capital: Des Moines");
      g_map_stateMap["KS"].addInfoBoxText("Capital: Topeka");
      g_map_stateMap["KY"].addInfoBoxText("Capital: Frankfort");
      g_map_stateMap["LA"].addInfoBoxText("Capital: Baton Rouge");
      g_map_stateMap["ME"].addInfoBoxText("Capital: Augusta");
      g_map_stateMap["MD"].addInfoBoxText("Capital: Annapolis");
      g_map_stateMap["MA"].addInfoBoxText("Capital: Boston");
      g_map_stateMap["MI"].addInfoBoxText("Capital: Lansing");
      g_map_stateMap["MN"].addInfoBoxText("Capital: St. Paul");
      g_map_stateMap["MS"].addInfoBoxText("Capital: Jackson");
      g_map_stateMap["MO"].addInfoBoxText("Capital: Jefferson");
      g_map_stateMap["MT"].addInfoBoxText("Capital: Helena");
      g_map_stateMap["NE"].addInfoBoxText("Capital: Lincoln");
      g_map_stateMap["NV"].addInfoBoxText("Capital: Carson City");
      g_map_stateMap["NH"].addInfoBoxText("Capital: Concord");
      g_map_stateMap["NJ"].addInfoBoxText("Capital: Trenton");
      g_map_stateMap["NM"].addInfoBoxText("Capital: Santa Fe");
      g_map_stateMap["NY"].addInfoBoxText("Capital: Albany");
      g_map_stateMap["NC"].addInfoBoxText("Capital: Raleigh");
      g_map_stateMap["ND"].addInfoBoxText("Capital: Bismarck");
      g_map_stateMap["OH"].addInfoBoxText("Capital: Columbus");
      g_map_stateMap["OK"].addInfoBoxText("Capital: Oklahoma City");
      g_map_stateMap["OR"].addInfoBoxText("Capital: Salem");
      g_map_stateMap["PA"].addInfoBoxText("Capital: Harrisburg");
      g_map_stateMap["RI"].addInfoBoxText("Capital: Providence");
      g_map_stateMap["SC"].addInfoBoxText("Capital: Columbia");
      g_map_stateMap["SD"].addInfoBoxText("Capital: Pierre");
      g_map_stateMap["TN"].addInfoBoxText("Capital: Nashville");
      g_map_stateMap["TX"].addInfoBoxText("Capital: Austin");
      g_map_stateMap["UT"].addInfoBoxText("Capital: Salt Lake City");
      g_map_stateMap["VT"].addInfoBoxText("Capital: Montpelier");
      g_map_stateMap["VA"].addInfoBoxText("Capital: Richmond");
      g_map_stateMap["WA"].addInfoBoxText("Capital: Olympia");
      g_map_stateMap["WV"].addInfoBoxText("Capital: Charleston");
      g_map_stateMap["WI"].addInfoBoxText("Capital: Madison");
      g_map_stateMap["WY"].addInfoBoxText("Capital: Cheyenne");

      for ( var abbrev in g_map_stateMap )
      {
         var state = g_map_stateMap[abbrev]; 
         state.addInfoBoxText("");
         state.addInfoBoxText("The United States of America is the world's third largest country in size and nearly the third largest in terms of population.Along the northern border is Canada and the southern border is Mexico.");
      }

      
      return;
}


