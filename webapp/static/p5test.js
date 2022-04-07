var angle = 90;
var distance = 0;
var num = 0;
var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

socket.on('connect',function(ret){
		console.log("connected");
	});


$(document).on('click','#socketTest',function(){
    socket.emit('testSocket',{num});
    
    socket.on('test',function(data){
    distance = data.distance * 0.01;
    angle = data.angle;
    console.log("server told : "+ data.distance);
    console.log("server told2 : "+ data.angle);
	});
});


var xframe = 400;
var yframe = 200;

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

var xframe = 500;
var yframe = xframe / 2;

function setup() {
  createCanvas(xframe, yframe);
  background(0);
}

let maxdis = 15;

function draw() {
  noStroke();
  fill(0,8)
  rect(0,0, xframe, yframe)
  drawtext();
  drawLine();
  drawobject();
}

function drawtext(){
  
  stroke(255);
  strokeWeight(0);
  textSize(xframe / 40);
  fill(0)
  rect(xframe / 100, yframe/ 35, xframe / 7, yframe / 8);
  fill(255)
  text("Distance: " + distance.toFixed(2) , xframe / 100, yframe/ 15);
  text("Degree: " + parseInt(angle), xframe / 100, yframe/ 8);
}

function drawradar(){
  background(0);
  noFill();
  
  stroke(0, 255, 0, 80);
  textSize(xframe / 60);
  
  let linenum = 5;
  
  for(let i = 94; i > linenum; i -= 94 / linenum){
    arc(xframe / 2, yframe, xframe * (0.01 * i), yframe * 2 * (0.01 * i), PI, 0);
  }

  for(let i = 1; i <= linenum; i++){
    let dtext = maxdis / linenum * i;
    text(dtext + 'm', xframe/2, yframe - ((yframe/linenum) * i * 0.96));
  }
}

function drawobject(){
  push()
  stroke(255,0,0);
  strokeWeight(2);
  translate(xframe/2, yframe);  
  let pixs_distance = (yframe * 0.94) / maxdis * (distance);
  ellipse(pixs_distance*cos(radians(180-angle)),-pixs_distance*sin(radians(180-angle)), 2);
}

function drawLine() { 
  push()
  strokeWeight(2);
  stroke(0,255,0, 20);
  translate(xframe/2, yframe);  
  line(0,0,((yframe * 0.94) *cos(radians(180-angle))),-(yframe * 0.94) *sin(radians(180-angle)));
  pop();
}

