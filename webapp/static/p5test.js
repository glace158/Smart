var r = 255;
var g = 0;
var b = 0;

var num = 0;
var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

socket.on('connect',function(ret){
		console.log("connected");
	});

$(document).on('click','#socketTest',function(){
    socket.emit('testSocket',{num});
  
    socket.on('test',function(data){
    num = data.num;
    console.log("server told : "+ data.num);
	});
});

var xframe = 200;
var yframe = 100;

var degree = 0;
var distance = 0;

function setup() {
  createCanvas(xframe, yframe);
  
  background(0);
  noFill();
  strokeWeight(2);
  stroke(0, 255, 0, 80);
  textSize(xframe / 60);
  
  let linenum = 5;
  let maxdis = 15;
  
  for(let i = 94; i > linenum; i -= 94 / linenum){
    arc(xframe / 2, yframe, xframe * (0.01 * i), yframe * 2 * (0.01 * i), PI, 0);
  }
  
  for(let i = 1; i <= linenum; i++){
    let dtext = maxdis / linenum * i;
    text(dtext + 'm', xframe/2, yframe - ((yframe/linenum) * i * 0.96));
  }
}

function draw() {
  textSize(xframe / 40);
  text("Distance: ", xframe / 100, yframe/ 15);
  text("Degree: ", xframe / 100, yframe/ 8);
  fill(255);
  noStroke();
}
