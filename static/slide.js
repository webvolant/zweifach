window.index = 0;
window.Count= 3;

window.images = new Array();
window.images[0] = "url(p1.jpg)";
window.images[1] = "url(p2.jpg)";
window.images[2] = "url(p3.jpg)"

setInterval(function(){
 $("div.main").fadeOut(500, function () {
   $("div.main").css("backgroundImage", window.images[window.index ]);
   $("div.main").fadeIn(500);
   if(window.index < window.Count-1) 
     window.index ++;
   else window.index = 0;
 });
}, 1500);