window.addEventListener("keydown", checkKeydown, false);
window.addEventListener("keyup", checkKeyup, false);

var degree_arr = [0,90,90,16,16];
var moter_keys = [['z', 'a', 'q'], ['x', 's', 'w'],['t','g','b']];
var servo_keys = ['p','o', 'i', 'u', 'y'];
var fire_key = "m";
var armid = ["#Grip", "#Wrist", "#Wrist_Roll", "#Elbow", "#Shoulder", "#Waist"]
var driveid = ["#L_Speed", "#R_Speed"]
var key_dic = {};
var tik = 2;

key_dic = servo_key_setting(servo_keys, key_dic);
key_dic = moter_key_setting(moter_keys, key_dic, 100 );
console.log(key_dic);
console.log(degree_arr);

function checkKeydown(e){
	set_key(e.key)
	console.log(e.key);
}

function checkKeyup(e){
	if(key == fire_key)
	{
		set_extinguisher(0);
	}
}

function servo_key_setting(keyarr, dic){
	for(var key of keyarr){
		dic[key.toUpperCase()] = 's' + keyarr.indexOf(key) + " " + "true";
		dic[key.toLowerCase()] = 's' + keyarr.indexOf(key) + " " + "false";
		//init
		set_control("servo", keyarr.indexOf(key), degree_arr[keyarr.indexOf(key)]);
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
	else if(key == fire_key)
	{
		set_extinguisher(1);
	}
}

function set_extinguisher(state){
	fetch("/extinguisher/" + state);
}

function set_speed(motor_num, speed){
	set_control("motor", motor_num, speed);
	let result = document.querySelector(driveid[motor_num]);
	val = String(speed);
	result.innerHTML = val;
}

function set_degree(servo_num, state){
	
	degree_arr[servo_num] = state == "true" ? 
	(degree_arr[servo_num] >= 180 ? 180 : degree_arr[servo_num] + tik ):
	(degree_arr[servo_num] <= 0 ? 0 : degree_arr[servo_num] - tik);
	let result = document.querySelector(armid[servo_num]);
	    key = armid[servo_num].replace("#", ""),
		val = String(degree_arr[servo_num]);
		
	result.innerHTML = key+":  "+ parseInt(val);
	set_control("servo", servo_num, degree_arr[servo_num]);
	  
}

function set_servospeed(){
    var x = document.getElementById('a').value;
    tik = (x-0)*(5-0)/(100-0)+0;
}

function set_control(type, pwm, speed){
	fetch("/" + type + "/" + pwm + "/" + speed);
}
