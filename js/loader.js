function randVal (min,max){
    return Math.floor(Math.random()*(max-min+1)+min);
}

function randColor(){
// generates random color string
    vec="0123456789abcdef";
    color="#";
    for(i=0;i<6;i++){
       color+=vec[randVal(0,vec.length-1)];
    }
    return color;
}

function start(event){
  // alert("Click/Drag finger on Canvas to generate random explosion");
  
 // chkBasic=document.getElementById("chkBasic");
 // selectAngle=document.getElementById("selectAngle");
  // chkBasic.onclick=function(){
   //    selectAngle.style.display=((chkBasic.checked)? "inline-block":"none");
   //}
    canvas=document.getElementById("myCanvas");
    ctx=canvas.getContext("2d");
    canvas.width=window.innerWidth*1;
    canvas.height=window.innerHeight*0.50;
    // create Explosion instance (the code for this can be found here: https://cdn.rawgit.com/bureyburey/Explosion/master/explosion.js)
    exp=new Explosion(ctx);
    // the explosion.js is a modified version for a code i found online, please refer to the HTML page for link
    
    var touchActive=false;
    x=event.clientX;
    y=event.clientY;
    addExplosion(x,y);
   function addExplosion(x,y){
      // create explosion at random position on the canvas and a random color
      // create explosion is a method inside every Explosion instance
      // createExplosion(x,y,color)
      
   //   basic=chkBasic.checked;
    //  deltaAngle=parseInt(selectAngle.value);
      //document.write(deltaAngle);
   //   if(document.getElementById("chkRand").checked){
   //       if(basic){
   ///         exp.createBasicExplosion(x,y,randColor(),deltaAngle);
   //     }else
            exp.createExplosion(x,y,randColor());
    //  }else{
     //     if(basic){
            //    exp.createBasicExplosion(x,y,"#AC12F2",deltaAngle);
             //   exp.createBasicExplosion(x,y,"#FF1245",deltaAngle);
             //   exp.createBasicExplosion(x,y,"#45127F",deltaAngle);
             //   exp.createBasicExplosion(x,y,"red",deltaAngle);

       //   }else{
             //     exp.createBasicExplosion(x,y,"#AC12F2");
              //  exp.createBasicExplosion(x,y,"#FF1245");
              //  exp.createBasicExplosion(x,y,"#45127F");
              //  exp.createBasicExplosion(x,y,"red");
         // }

      
       
   }
  
  var handlerStart=function(evt){
     touchActive=true;
     handlerMove(x,y);
  }
  var handlerEnd=function(evt){
     touchActive=false; 
  }
  
  var handlerMove=function (x,y) {
  // adds explosion when dragging finger on he screen on the location that is touched
        if(!touchActive){
            return;
        }
        evt.preventDefault();
        var pos=canvas.getBoundingClientRect();
        if(evt.touches){
            var touch=evt.touches[0];
        }
        // find the (x, y) coordinate of the touch
        //var xTouch = (evt.clientX-pos.left) || (touch.clientX-pos.left);
        //var yTouch = (evt.clientY-pos.top) || (touch.clientY-pos.top);
        
        //addExplosion(xTouch,yTouch);
        addExplosion(x,y);
    }
  
  // attach event listener for canvas click (touch/mouse click)
  canvas.onmousemove=function(event){
      addExplosion(event.clientX,event.clientY);
  }
  // attach event listeners for touch click and touch drag (continous explosion generation)
   canvas.addEventListener("touchstart",handlerStart,false);
   canvas.addEventListener("touchend",handlerEnd,false); canvas.addEventListener("touchmove",handlerMove,false);

    function draw(){
       // clear the canvas
        ctx.clearRect(0,0,canvas.width,canvas.height);
        // update the explosions, 33 is the frame speed (lower=slower;higher=faster)
        exp.update(33);
        ctx.fillStyle="white";
       // ctx.fillText("# Particles: "+exp.particles.length, 10, 10);
    }
    setInterval(draw,33);
    
}
window.onload=start;