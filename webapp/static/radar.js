let angle = []
var minangle = 30;
var maxangle = 150;
let distance = []


function radar_state(){
		let result = document.querySelector('#State_test1');
		if(result.innerText == "on"){
			var time = new Date().getTime();
				result.innerHTML = "off";
			}
		else if(result.innerText == "off"){
				result.innerHTML = "on";
        setInterval(radar_controll, 1500);
        fetch("/start");
			}
	}

function radar_controll(){
    distance = [];
    var ad = fetch("/radar")
    .then(response=> {console.log(response); return response.json()})
    .then(data=>{
	
	angle = Object.keys(data);
	for(let i = 0; i<angle.length; i++){
	    distance.push( data[angle[i]] );
	  }
	newwrite = true;
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
let i = 0;
var newwrite = false;

function draw() {
  
  if(newwrite){
      drawLine();
      drawobject();
      i++;
      
      if(i > angle.length){
	newwrite = false;
	i = 0;
      } 
    }
}

function fillbackground(){
    noStroke();
    fill(0)
    rect(0,0, xframe, yframe)  
}

function drawobject(){
    push()
    stroke(0);
    strokeWeight(xframe * 0.005);
    translate(xframe/2, yframe);  
    let pixs_distance = (yframe * 0.94) / maxdis * (distance[i]);
    stroke(128,128,128);
    line(0,0,(pixs_distance *cos(radians(angle[i]))),-pixs_distance *sin(radians(angle[i])));
    stroke(0);
    ellipse(pixs_distance*cos(radians(angle[i])),-pixs_distance*sin(radians(angle[i])), 2);
}

function drawLine() { 
  push()
  strokeWeight(xframe * 0.005);
  
  translate(xframe/2, yframe);
  stroke(0);
  line(0,0,((yframe * 2) *cos(radians(angle[i]))),-(yframe * 2) *sin(radians(angle[i])));  
  stroke(70,70,70);
  line(0,0,((yframe * 0.94) *cos(radians(angle[i]))),-(yframe * 0.94) *sin(radians(angle[i])));
  pop();
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
