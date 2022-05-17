var done = false;
var camstate = 0;
var armcamstate = false;
var armcamnum = 2;
var cam = [0,1,2];


function camset(){
		let result = document.querySelector('#cam_test');
		if(result.innerText == "on"){
			var time = new Date().getTime();
				result.innerHTML = "off";
				camstate = 0;
			}
		else if(result.innerText == "off"){
				result.innerHTML = "on";
				camstate = 1;
			}
	}

function onloadcam(num){
	let e = document.getElementById("select0" + num);
	cam[num] = e.selectedIndex;
	//console.log("cam[0]:",cam[0],"cam[1]:",cam[1],"cam[2]:",cam[2]);
	
	var time = new Date().getTime();
	if(done && armcamstate && num == 1){
			let arm = document.getElementById("select02");
			cam[2] = arm.selectedIndex;
			document.getElementById("cam1").src="/video_feed/" + cam[2] + "/" + camstate + "?time" + time;
		}
	else if(done){
			document.getElementById("cam" + num).src="/video_feed/" + cam[num]+ "/" + camstate + "?time" + time;
		}
  }



window.addEventListener("keydown", (e) => {
	if(servo_keys.includes(e.key.toLowerCase())){
		armcamstate = true;
	}
	else{
		armcamstate =false;
	}
});
    
