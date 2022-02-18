window.addEventListener("keydown", checkKeydown, false);
window.addEventListener("keyup", checkKeyup, false);

var degree_arr = [0,0,0,0,0,0];
var moter_keys = [['q', 'a', 'z'], ['w', 's', 'x']];
var servo_keys = ['p','o', 'i', 'u', 'y', 't'];
var key_dic = {};

key_dic = servo_key_setting(servo_keys, key_dic);
key_dic = moter_key_setting(moter_keys, key_dic, 100);
console.log(key_dic);


function checkKeydown(e){
	set_key(e.key)
}

function checkKeyup(e){

}

function servo_key_setting(arr, dic){
	for(var key of arr){
		dic[key.toUpperCase()] = 's' + arr.indexOf(key) + " " + "true";
		dic[key.toLowerCase()] = 's' + arr.indexOf(key) + " " + "false";
	}
	return dic;
}

function moter_key_setting(arr, dic, maxvalue){  
	for (var keys of arr){
	  for(var key of keys){
		let partition = parseInt(maxvalue / keys.length);
		let value = keys.length == keys.indexOf(key) + 1 ? maxvalue : partition * (keys.indexOf(key) + 1);
		dic[key.toUpperCase()] = 'm' + arr.indexOf(keys) + " " + value;
		dic[key.toLowerCase()] = 'm' + arr.indexOf(keys) + " " + -value;
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
}

function set_speed(motor_num, speed){
	set_control("motor", motor_num, speed);
}

function set_degree(servo_num, state){
	let value = 2;
	
	degree_arr[servo_num] = state == "true" ? 
	(degree_arr[servo_num] >= 180 ? 180 : degree_arr[servo_num] + value ):
	(degree_arr[servo_num] <= 0 ? 0 : degree_arr[servo_num] - value);
	
	set_control("servo", servo_num, degree_arr[servo_num]);
}

function set_control(type, pwm, speed){
	fetch("/" + type + "/" + pwm + "/" + speed);
}
