from flask import Flask, render_template, session, request, Response
#from flask_socketio import SocketIO, send, emit
import motor2
import servo2
import radar2
import camera
import gas_sensor
import DHT11
import RPi.GPIO as GPIO
from threading import Thread
import webcam_ORG
import time
import cv2
app = Flask(__name__)
time.sleep(5)
GPIO.setmode(GPIO.BCM)
startpin = 12
GPIO.setup(startpin, GPIO.OUT)

#gassensor
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 19
mq2_dpin = 26
mq2_apin = 0

gas = gas_sensor.GasSensor(SPICLK, SPIMISO, SPIMOSI, SPICS, mq2_dpin, mq2_apin)

#motor
motors = []
motors.append((motor2.Motor(2, 3), motor2.Motor(4,17)))
motors.append((motor2.Motor(27,22), motor2.Motor(5,6)))
motors.append(motor2.Motor(26,19,20))
    

#radar
radar1 = radar2.Radar(7, 10, 30, 150)#.start()

#servo
servos = []
servos.append(servo2.Servo(14, 0, 60, 0))#grip 0/60 init 0
servos.append(servo2.Servo(15, 0, 140, 90))#wrist 0/140 -1 init 90
servos.append(servo2.Servo(18, 0, 180, 90))#wristroll 0/180 init 90
servos.append(servo2.Servo((23,24), 16,144, 90))#elbow 16/144 init 16
servos.append(servo2.Servo((25,8), 16,160, 16))#shoulder 16/160 init 16

#fire
fire_servo = servo2.Servo(13, 0, 180)

#camera
cameras = []
cameras.append(webcam_ORG.DetectCam(2, 12).start())
cameras.append(camera.Camera(4, 12).start())
cameras.append(camera.Camera(0, 12).start())

#dht11
dht11 = []
dht11.append(DHT11.DHT11Sensor(26))
dht11.append(DHT11.DHT11Sensor(20))

print("--------------------------")
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/start')
def mystart():
    try:
        thread4 = Thread(target=radar1.move_radar, args=())
        thread4.daemon = True
        thread4.start()
        print("Thread4_Start.. done") 
        return "ok"
    except:
        return "fail"

#camera
@app.route('/video_feed/<num>/<state>')
def video_feed(num, state):
    num = int(num)
    if(int(state) == 1):
        cameras[num].set_state(True)
        cameras[num].clear_q()
        return Response( cameras[num].get_q() , mimetype='multipart/x-mixed-replace; boundary=frame')
    cameras[num].set_state(False)
    return Response( cameras[num].loading() , mimetype='multipart/x-mixed-replace; boundary=frame')

#motor
@app.route('/motor/<num>/<speed>')
def mymoter(num, speed):
    try:
        print("Motor", num, ": ", speed)
        if ( type(motors[int(num)]) != type(()) ):
            motors[int(num)].motor_speed(int(speed))
        else:
            motors[int(num)][0].motor_speed(int(speed))
            motors[int(num)][1].motor_speed(int(speed))
        return speed
    except:
        return "fail"  

#servo
@app.route('/servo/<num>/<tik>')
def myservo(num, tik):
    try:
        
        return str(servos[int(num)].servo_pos(int(tik)))
    except:
        return "fail"

#radar
@app.route('/radar')
def myradar():
    try:
        return radar1.get_q()
    except:
        return "fail"
#gas
@app.route('/gas')
def mygas():
    try:
        return str(gas.readadc())
    except:
        return "fail"
    
#DHT11
@app.route('/DHT11/<num>')
def myDHT11(num):
    try:
        return str(dht11[int(num)].readtemp())
    except:
        return "fail"

#extinguisher
@app.route('/extinguisher/<state>')
def myextinguisher(state):
    try:
        if(int(state) == 0):
            fire_servo.servo_pos(180)
        else:
            fire_servo.servo_pos(0)
        return "ok"
    except:
        return "fail"

if __name__ == '__main__':
    try:
        GPIO.output(startpin, True)
        app.run(host='0.0.0.0', port=8080)#, debug=True)
        GPIO.output(startpin, False)
    except:
        GPIO.cleanup()
        