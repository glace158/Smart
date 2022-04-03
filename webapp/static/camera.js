var done = false;

window.onload = function(){
	done = true;
	onloadcam1(1);
	onloadcam2(1);
	console.log("load done");
	}

function camset(){
		let result = document.querySelector('#cam_test');
		if(result.innerText == "on"){
			var time = new Date().getTime();
				onloadcam1(0);
				result.innerHTML = "off";
			}
		else if(result.innerText == "off"){
				onloadcam1(1);
				result.innerHTML = "on";
			}
	}
    
function onloadcam1(state){
	if(done == true){
			var time = new Date().getTime();
			console.log("frame");
			document.getElementById("cam1").src="/video_feed1/" + state + "?time" + time;
		}
  }

function onloadcam2(state){
	if(done == true){
			var time = new Date().getTime();
			document.getElementById("cam2").src="/video_feed2/" + state + "?time" + time;
		}
  }
