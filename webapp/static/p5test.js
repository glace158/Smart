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

function setup() {
  createCanvas(100, 100);
}

function draw() {
  background(0);
  strokeWeight(100);
  stroke(r,g,b);
  point(400,300);
}
