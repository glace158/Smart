window.addEventListener("keydown", function(){
    var driveRail = document.querySelectorAll('.drive .cont span');
    driveRail.forEach(function(el){
        var num = Number(el.children[0].innerText);
        if(num == 0) el.className = 'normal';
        else if(num > 0) el.className = 'positive';
        else if(num < 0) el.className = 'negative';
    })
});

var gas_val = [90,89,88,96,93,94,91,94];
var count = 0;
function get_gas_sensor(){
    /*let ad = fetch("/gas")
    .then(response=> {console.log(response); return response.json()})
    .then(data=>{
	let gas_value = data;
    let result = document.querySelector("#gas");
	result.innerHTML = gas_value;
      });*/
      
    let result = document.querySelector("#gas");
	result.innerHTML = gas_val[count];
    if(gas_val.length > count){
        count++;
    }
    else{
        count = 0;
    }
    
    }
  
function get_dht_sensor(num){
    /*
    fetch("/DHT11/" + num)
    .then(response=> {console.log(response); return response.json()})
    .then(data=>{
	let dht_value = data;
    let result = document.querySelector("#dht" + num);
	result.innerHTML = dht_value;
      });*/
    
    let result = document.querySelector("#dht" + num);
	result.innerHTML = 25;
    }
    
