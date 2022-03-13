<!doctype html>
<html lang="en">
<head>
   <!--Required meta tags--
   
   <!--Bootstrap CSS-->
   <link rel="stylesheet" type="text/css" href="style.css">
   <title>Live Streaming Demonstration</title>
</head>
<body>
<div class="container"> 
    <div class="col-lg-8 offset-lg-2">
        <h3 class="mt-5">Live Streaming</h3>
        <!--<img src="{{ url_for('video_feed')}}"width="100%">-->
    </div>
    <div class="list-wrap">
        <ul>
            <li>
                <p class="tit">RGB Camera</p>
                <div class="cont">
                    <img src="temp_01.jpg"/>
                </div>
            </li>
            <li>
                <p class="tit">Themal Camera</p>
                <div class="cont">
                    <img src="temp_02.jpg"/>
                </div>
            </li>
            <li>
                <p class="tit">Radar</p>
                <div class="cont">
                    <img src="temp_03.jpg"/>
                </div>
            </li>
        </ul>
        <ul class="bot">
            <li class="border info">
                <p class="tit">Info</p>
                <div class="cont">
                    <dl>
                        <dt>outside temperature</dt>
                        <dd>100C</dd>
                        <dt>inside temperature</dt>
                        <dd>30C</dd>
                        <dt>air quiality</dt>
                        <dd>50ppm</dd>
                        <dt>defog mode</dt>
                        <dd>off</dd>
                        <dt>mic</dt>
                        <dd>on</dd>
                        <dt>sound mute</dt>
                        <dd>off</dd>
                    </dl>
                </div>
            </li>
            <li class="border drive">
                <p class="tit">Drive Control</p>
                <div class="cont">
                    <span>L Speed: <em>-100</em></span>
                    <span>R Speed: <em>100</em></span>
                </div>
            </li>
            <li class="border arm">
                <p class="tit">Arm Control</p>
                <div class="cont">
                    <div class="txt-group">
                        <span class="fc-green">Grip: 20</span>
                        <span>Wrist: 50</span>
                        <span>Wrist Roll: 120</span>
                        <span class="fc-green">Elbow: 100</span>
                        <span>Shoulder: 55</span>
                        <span>Waist: 0</span>
                    </div>
                </div>
            </li>
            <li>
                <p class="tit">Arm Camera</p>
                <div class="cont">
                    <img src="temp_04.jpg"/>
                </div>
            </li>
        </ul>
    </div>
</div>
<script>
window.addEventListener('DOMContentLoaded', function(){
    var driveRail = document.querySelectorAll('.drive .cont span');
    driveRail.forEach(function(el){
        var num = Number(el.children[0].innerText);
        if(num > 0) el.className = 'positive';
        if(num < 0) el.className = 'negative';
    })
});
</script>
</body>
</html>