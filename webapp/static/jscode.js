window.addEventListener("keydown", checkKeydown, false);
window.addEventListener("keyup", checkKeyup, false);

var degree_arr = [0,0,0,0,0,0];

var key_dic = 
{'P': "s0 true", 'p': "s0 false", 
'O': "s1 true", 'o': "s1 false", 
'I': "s2 true", 'i': "s2 false",
'U': "s3 true", 'u': "s3 false",
'Y': "s4 true", 'y': "s4 false",
'Q': "m0 100", 'A': "m0 66", 'Z': "m0 33", '1': "m0 0",
'q': "m0 -100", 'a': "m0 -66", 'z': "m0 -33",
'W': "m1 100", 'S': "m1 66", 'X': "m1 33", '2': "m1 0",
'w': "m1 -100", 's': "m1 -66", 'x': "m1 -33",
'D': "s5 true", 'd': "s5 false"
};

function checkKeydown(e){
	set_key(e.key)
}

function checkKeyup(e){

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
