from flask import Flask, render_template, session, request, Response
#from flask_socketio import SocketIO, send, emit
import motor2
import servo2
import radar2
import camera
import RPi.GPIO as GPIO
from threading import Thread
import webcam_ORG
import time

app = Flask(__name__)
#socketio = SocketIO(app)
time.sleep(5)
GPIO.setmode(GPIO.BCM)
startpin = 12
GPIO.setup(startpin, GPIO.OUT)

#motor
motors = []
motors.append((motor2.Motor(2, 3), motor2.Motor(4,17)))
motors.append((motor2.Motor(27,22), motor2.Motor(10,9)))
motors.append(motor2.Motor(21, 20, 16))
    

#radar
radar1 = radar2.Radar(16, 10, 30, 150)

#servo 
servos = []
servos.append(servo2.Servo(14))#grip 0/60 init 0
servos.append(servo2.Servo(15))#wrist 0/140 -1 init 90
servos.append(servo2.Servo(18))#wristroll 0/180 init 90
servos.append(servo2.Servo(23,24))#elbow 16/144 init 16
servos.append(servo2.Servo(25,8))#shoulder 16/160 init 16
#camera
cameras = []
cameras.append(camera.Camera(0, 12))
cameras.append(webcam_ORG.DetectCam(4, 12))
cameras.append(camera.Camera(2, 12))

print("--------------------------")
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/start')
def mystart():
    try:
        thread1 = Thread(target=cameras[0].gen_frames, args=())
        thread2 = Thread(target=cameras[1].gen_frames, args=())   
        thread1.daemon = True
        thread2.daemon = True
        thread1.start()
        print("Thread1_Start.. done")
        
        thread2.start()
        print("Thread2_Start.. done")
        
        thread3 = Thread(target=radar1.move_radar, args=())
        thread3.daemon = True
        thread3.start()
        print("Thread3_Start.. done") 
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
        return "ok"
    except:
        return "fail"  

#servo
@app.route('/servo/<num>/<degree>')
def myservo(num, degree):
    try:
        print("Servo", num, ": ",degree)
        servos[int(num)].servo_pos(int(degree))
        return "ok"
    except:
        return "fail"

#radar
@app.route('/radar')
def myradar():
    try:
        return radar1.get_q()
    except:
        return "fail"

if __name__ == '__main__':
    try:
        GPIO.output(startpin, True)
        app.run(host='0.0.0.0', port=8080)#, debug=True)
        GPIO.output(startpin, False)
    except:
        GPIO.cleanup()