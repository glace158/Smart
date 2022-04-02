var done = false;

window.onload = function(){
	done = true;
	camstart();
	console.log("load done");
	}

function camstart(){
		onloadcam1();
		onloadcam2();
    
		let result = document.querySelector('#cam_test');
		result.innerHTML = "on";
	}
    
function onloadcam1(){
	if(done == true){
			var time = new Date().getTime();
			console.log("frame");
			document.getElementById("cam1").src="/video_feed1?time" + time;
		}
  }

function onloadcam2(){
	if(done == true){
			var time = new Date().getTime();
			document.getElementById("cam2").src="/video_feed2?time" + time;
		}
  }
