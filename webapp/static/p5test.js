var angle = 30;
var minangle = 30;
var maxangle = 150;
var distance = 0;
var num = 1;

var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

socket.on('connect',function(ret){
		console.log("connected");
	});


function emitradar(){
    socket.emit('testSocket',{num});
    
    socket.on('test',function(data){
    distance = data.distance * 0.01;
    angle = data.angle;
  });
} 

const timer= ms => new Promise(res=>setTimeout(res,ms))

async function load(){
  while(true){
    radar_controll();
    await timer(80);
    }
  }
  
//setInterval(radar_controll, 0);

function radar_controll(){
    var ad = fetch("/radar")
    .then(response=> {console.log(response); return response.text()})
    .then(data=>{
	console.log(data);
	const arr = data.split(" ");
	distance = parseFloat(arr[0]);
	angle = parseInt(arr[1]);
	console.log(distance);
	console.log(angle);
      });
    
  }

var xframe = 500;
var yframe = xframe / 2;

function setup() {
  createCanvas(xframe, yframe);
  background(0);
}

let maxdis = 5;
let state = -1;

function draw() {
  /*
  if(angle > maxangle || angle < minangle){
       state *= -1;
     }
  angle += state;
  */

  fillbackground();
  drawtext();
  //drawLine();
  drawobject();
}

function fillbackground(){
  let fadeangle = 1;
  if((angle < maxangle && angle > (maxangle - fadeangle)) || (angle > minangle && angle < ( minangle + fadeangle) ) ){
      
    noStroke();
    fill(0,8)
    rect(0,0, xframe, yframe)  
   }
}

function drawtext(){
  
  stroke(255);
  strokeWeight(0);
  textSize(xframe / 40);
  fill(0)
  rect(xframe / 100, yframe/ 35, xframe / 5, yframe / 8);
  fill(255)
  text("Distance: " + distance + "m" , xframe / 100, yframe/ 15);
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
  stroke(0);
  strokeWeight(xframe * 0.005);
  translate(xframe/2, yframe);  
  let pixs_distance = (yframe * 0.94) / maxdis * (distance);
  stroke(128,128,128);
  line(0,0,(pixs_distance *cos(radians(angle))),-pixs_distance *sin(radians(angle)));
  stroke(180,0,0);
  ellipse(pixs_distance*cos(radians(angle)),-pixs_distance*sin(radians(angle)), 2);

}

function drawLine() { 
  push()
  strokeWeight(xframe * 0.005);
  stroke(0,255,0, 20);
  translate(xframe/2, yframe);  
  line(0,0,((yframe * 0.94) *cos(radians(angle))),-(yframe * 0.94) *sin(radians(angle)));
  pop();
}
