---
title: "Noughts & Crosses"
layout: post
published: true
categories: showcase future-projects
---

> For those of you who are learning (or want to learn) HTML and Javascript, Salih has planned to make a noughts-and-crosses game with you!

> You can see what it will look like when it is finished [here](/files/showcase/Future/noughts-and-crosses.html).

> Do you think you can manage it? Here's the code:

    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Noughts and Crosses</title>
    <style>
    .x{
      background-image:url(" http://icongal.com/gallery/image/37201/cancel_exit_cross_close.png");
    }
    .o{
      background-image:url(" http://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Letter_o.svg/50px-Letter_o.svg.png");
    }
    .r{
      display: block;
      height: 50px;
      width: 150px;
    }
    .s{
      border: 1px black solid;
      display: inline-block;
      width: 48px;
      height: 48px;
    }
    .winner {
    width: 150px;
    text-align: center;
    font-family: tahoma;
    background-image: url('http://i44.servimg.com/u/f44/14/74/52/91/prod_410.gif');
    }
    </style>
    </head>
    <body>
    <div id="game">
    </div>
    <script>
    var turns = 1;
    var Board = [[0,0,0],[0,0,0],[0,0,0]];
    function play(){
      str="";
      for(i=0;i<3;i++){
        str=str+'<div id="r'+i+'" class="r">';
        for(j=0;j<3;j++){
          if(Board[i][j]===0){
          str = str + '<div id="s'+i+j+'" onclick="select('+i+','+j+')" class="s"></div>';
          }else if(Board[i][j]==1){
          str = str + '<div id="s'+i+j+'" onclick="select('+i+','+j+')" class="o s"></div>';
          }else if(Board[i][j]==2){
          str = str + '<div id="s'+i+j+'" onclick="select('+i+','+j+')" class="x s"></div>';
          }
        }
        str=str+'</div>';
      }
      return str;
    }
    function select(x,y){
      if(Board[x][y]===0){
        if(turns==1){
          Board[x][y] = 1;
          turns = 2;
        }else{
          Board[x][y] = 2;
          turns = 1;
        }
    document.getElementById("game").innerHTML = play();
      winner();
      }
    }
    function winner(){
      if(turns==1){if(
        ((Board[0][0]===Board[0][1]&&Board[0][0]===Board[0][2])&&Board[0][0]!==0)||
        ((Board[1][0]===Board[1][1]&&Board[1][0]===Board[1][2])&&Board[1][0]!==0)||
        ((Board[2][0]===Board[2][1]&&Board[2][0]===Board[2][2])&&Board[2][0]!==0)||
         ((Board[0][0]===Board[1][0]&&Board[0][0]===Board[2][0])&&Board[0][0]!==0)||
         ((Board[0][1]===Board[1][1]&&Board[0][1]===Board[2][1])&&Board[0][1]!==0)||
         ((Board[0][2]===Board[1][2]&&Board[0][2]===Board[2][2])&&Board[0][2]!==0)||
         ((Board[0][0]===Board[1][1]&&Board[0][0]===Board[2][2])&&Board[0][0]!==0)||
         ((Board[0][2]===Board[1][1]&&Board[0][2]===Board[2][0])&&Board[0][2]!==0)
      ){
      Board = [[4,4,4],[4,4,4],[4,4,4]];
        document.getElementById("game").innerHTML = document.getElementById("game").innerHTML+'<div class="winner"> Crosses wins</div>';
    }}else{
      if(
        ((Board[0][0]===Board[0][1]&&Board[0][0]===Board[0][2])&&Board[0][0]!==0)||
        ((Board[1][0]===Board[1][1]&&Board[1][0]===Board[1][2])&&Board[1][0]!==0)||
        ((Board[2][0]===Board[2][1]&&Board[2][0]===Board[2][2])&&Board[2][0]!==0)||
         ((Board[0][0]===Board[1][0]&&Board[0][0]===Board[2][0])&&Board[0][0]!==0)||
         ((Board[0][1]===Board[1][1]&&Board[0][1]===Board[2][1])&&Board[0][1]!==0)||
         ((Board[0][2]===Board[1][2]&&Board[0][2]===Board[2][2])&&Board[0][2]!==0)||
         ((Board[0][0]===Board[1][1]&&Board[0][0]===Board[2][2])&&Board[0][0]!==0)||
         ((Board[0][2]===Board[1][1]&&Board[0][2]===Board[2][0])&&Board[0][2]!==0)
      ){
      Board = [[4,4,4],[4,4,4],[4,4,4]];
        document.getElementById("game").innerHTML = document.getElementById("game").innerHTML+'<div class="winner"> Noughts wins</div>';
        
    }
    }
    }
    document.getElementById("game").innerHTML = play();
    </script>
    </body>
    </html>
