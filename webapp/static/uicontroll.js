window.addEventListener("keydown", function(){
    var driveRail = document.querySelectorAll('.drive .cont span');
    driveRail.forEach(function(el){
        var num = Number(el.children[0].innerText);
        if(num == 0) el.className = 'normal';
        else if(num > 0) el.className = 'positive';
        else if(num < 0) el.className = 'negative';
    })
});

function get_gas_sensor(){
    let ad = fetch("/gas")
    .then(response=> {console.log(response); return response.json()})
    .then(data=>{
	let gas_value = data;
    let result = document.querySelector("#gas");
	result.innerHTML = gas_value;
      });
    }
  
function get_dht_sensor(num){
    fetch("/DHT11/0")
    .then(response=> {console.log(response); return response.json()})
    .then(data=>{
	let dht_value = data;
    let result = document.querySelector("#dht0");
	result.innerHTML = dht_value;
    result = document.querySelector("#dht1");
	result.innerHTML = dht_value;
      });
    }
    
