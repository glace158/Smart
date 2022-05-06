var done = false;
var camstate = 0;
var armcamstate = false;
var armcamnum = 0;
window.onload = function(){
	done = true;
	camstate = 1;
	setInterval(radar_controll, 1500);
	fetch("/start");
	console.log("Load.. done");
}

$(function(){
	onloadcam();
	$('.select-area select').on('change', function(){
		onloadcam($(this).val(), $(this).attr('data-select'));
	});
});

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

function onloadcam(num, layout){
	var time = new Date().getTime();
	var src;
	src = "/video_feed/" + num + "/" + camstate + "?time" + time;
	$('.' + layout).attr('src', src);
}
  
window.addEventListener("keydown", (e) => {
	if(servo_keys.includes(e.key.toLowerCase())){
		armcamstate = true;
	}
	else{
		armcamstate =false;
	}
});
