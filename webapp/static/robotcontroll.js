window.addEventListener("keydown", checkKeydown, false);
window.addEventListener("keyup", checkKeyup, false);

//var degree_arr = [0,90,90,16,16];
var moter_keys = [['z', 'a', 'q'], ['x', 's', 'w'],['t','g','b','r','f']];
var servo_keys = ['p','o', 'i', 'u', 'y','k', 'j', 'h'];
var fire_key = ["m", "n"];
var armid = ["#Grip", "#Wrist", "#Wrist_Roll", "#Elbow", "#Shoulder", "#Waist"]
var driveid = ["#L_Speed", "#R_Speed"]
var key_dic = {};
var tik = 2;

key_dic = servo_key_setting(servo_keys, key_dic);
key_dic = moter_key_setting(moter_keys, key_dic, 100 );
console.log(key_dic);
//console.log(degree_arr);

function checkKeydown(e){
	set_key(e.key)
	console.log(e.key);
}

function checkKeyup(e){
}

function servo_key_setting(keyarr, dic){
	for(var key of keyarr){
		dic[key.toUpperCase()] = 's' + keyarr.indexOf(key) + " " + "true";
		dic[key.toLowerCase()] = 's' + keyarr.indexOf(key) + " " + "false";
		//init
		set_control("servo", keyarr.indexOf(key), 0);
	}
	return dic;
}

function moter_key_setting(arr, dic, maxvalue){  
	for (var keys of arr){
	  for(var key of keys){
		let partition = parseInt(maxvalue / keys.length);
		let value = keys.length == keys.indexOf(key) + 1 ? maxvalue : partition * (keys.indexOf(key) + 1);
		dic[key.toUpperCase()] = 'm' + arr.indexOf(keys) + " " + (value).toString();
		dic[key.toLowerCase()] = 'm' + arr.indexOf(keys) + " " + (-value).toString();
	  }
	  dic[arr.indexOf(keys)] = 'm' + arr.indexOf(keys) + " " + '0';
	}
	return dic;
}

function set_key(key){
	if(key in key_dic){
		let mrs = key_dic[key].split(' ');

		if(mrs[0][0] == "m"){
			set_speed(mrs[0][1], mrs[1]);
		}
		else{
			set_degree(mrs[0][1], mrs[1]);
		}
	}
	else if(key == fire_key[0])
	{
		set_extinguisher(1);
	}
	else if(key == fire_key[1]){
		set_extinguisher(0);
	}
}

function set_extinguisher(state){
	fetch("/extinguisher/" + state);
}

function set_speed(motor_num, speed){
	set_control("motor", motor_num, speed);
	if(motor_num != 2){
		let result = document.querySelector(driveid[motor_num]);
		val = String(speed);
		result.innerHTML = val;
	}
}

function set_degree(servo_num, state){
	let val = state == "true" ? tik : tik * -1;
	set_control("servo", servo_num, val);
}

function set_servospeed(){
    var x = document.getElementById('a').value;
    tik = (x-0)*(5-0)/(100-0)+0;
}

function set_control(type, pwm, speed){
	fetch("/" + type + "/" + pwm + "/" + speed)
	.then(response=> {console.log(response); return response.json()})
    .then(data=>{
		if(type == "servo"){
			
			let result = document.querySelector(armid[pwm]);
			key = armid[pwm].replace("#", ""),

			result.innerHTML = key+":  "+ parseInt(data);
		}
      });
}
