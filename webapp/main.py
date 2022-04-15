from flask import Flask, render_template, session, request, Response
from flask_socketio import SocketIO, send, emit
import motor
import motor2
import servo2
import radar
import camera
import RPi.GPIO as GPIO
from threading import Thread
import time

app = Flask(__name__)
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)

#motor pin

motors = []
motors.append((motor2.Motor(2, 3), motor2.Motor(4,17)))
motors.append((motor2.Motor(27,22), motor2.Motor(10,9)))
    

#radar servo
radar_servo = 12
radar_degree = 90
tik = -1
#servo pin
servos = []

servos.append(servo2.Servo((14, 15)))
servos.append(servo2.Servo((18, 23)))
servos.append(servo2.Servo(24))
##########

cameras = []
cameras.append(camera.Camera(0, 12))
cameras.append(camera.Camera(2, 12))

@app.route('/video_feed1/<state>')
def video_feed1(state):
    if(int(state)):
        cameras[0].set_state(True)
        return Response( cameras[0].get_q() , mimetype='multipart/x-mixed-replace; boundary=frame')
    cameras[0].set_state(False)
    return "ok"

@app.route('/video_feed2/<state>')
def video_feed2(state):
    if(int(state)):
        cameras[1].set_state(True)
        return Response( cameras[1].get_q() , mimetype='multipart/x-mixed-replace; boundary=frame')
    cameras[1].set_state(False)
    return "ok"
#####

@app.route('/')
def main():
    thread1 = Thread(target=cameras[0].gen_frames, args=())
    thread2 = Thread(target=cameras[1].gen_frames, args=())   
    thread1.daemon = True
    thread2.daemon = True
    thread1.start()
    thread2.start()

    return render_template('index.html')

@app.route('/motor/<num>/<speed>')
def mymoter(num, speed):
    try:
        if ( type(motors[int(num)]) != type(()) ):
            motors[int(num)].motor_speed(int(speed))
        else:
            motors[int(num)][0].motor_speed(int(speed))
            motors[int(num)][1].motor_speed(int(speed))
        #motor2.dual_speed(motors[int(num)], int(speed))
        #motor.set_motor_contorl(motors[int(num)], ina[int(num)], inb[int(num)], int(speed))
        return "ok"
    except:
        return "fail"  

@app.route('/servo/<num>/<degree>')
def myservo(num, degree):
    try:
        print("servo", num, ": ",degree)
        servos[int(num)].servo_pos(int(degree))
        return "ok"
    except:
        return "fail"

@app.route('/radar')
def myradar():
    try:
        global radar_degree
        global tik
        if(radar_degree < 30 or radar_degree > 150):
            tik *= -1
    
        radar_degree += tik
        servo2.servo_pos(radar_servo, radar_degree, 30, 150)
        distance = radar.get_distance() * 0.01
        return "%d %d" % (distance, radar_degree)
    except:
        return "fail"

@socketio.on('testSocket',namespace='/test')
def testEvent(data):
    global radar_degree
    global tik
    if(radar_degree < 30 or radar_degree > 150):
        tik *= -1
    
    radar_degree += tik
    servo2.servo_pos(radar_servo, radar_degree, 30, 150)
    distance = radar.get_distance()
    emit('test', {"distance": distance, "angle": radar_degree},callback=session.get('test'))

if __name__ == '__main__':

    socketio.run(app, host='0.0.0.0', port=8080)#, debug=True)
    GPIO.cleanup()