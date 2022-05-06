window.addEventListener("keydown", function(){
    var driveRail = document.querySelectorAll('.drive .cont span');
    driveRail.forEach(function(el){
        var num = Number(el.children[0].innerText);
        if(num == 0) el.className = 'normal';
        else if(num > 0) el.className = 'positive';
        else if(num < 0) el.className = 'negative';
    })
});

function camset1(){
		let result = document.querySelector('#cam_test1');
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

function camset2(){
		let result = document.querySelector('#cam_test2');
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

