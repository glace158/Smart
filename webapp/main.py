from flask import Flask, render_template, session, request, Response
from flask_socketio import SocketIO, send, emit
import motor
import servo2
import radar
import cv2
from queue import Queue
import RPi.GPIO as GPIO
from threading import Thread
import asyncio
import time


app = Flask(__name__)
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)

#motor pin
en = [2, 17, 10, 0]
ina = [3, 27, 9, 5]
inb = [4, 22, 11, 6]

motors = []

for i in range(4):
    motors.append( motor.set_motor(en[i], ina[i], inb[i]) )

#radar servo
radar_servo = 12
radar_degree = 90
tik = -1
#servo pin
servos = []

servos.append((14, 15)) 
servos.append((18, 23))
##########
try:

    cameras = []
    cameras.append(cv2.VideoCapture(0))
    cameras.append(cv2.VideoCapture(2))
    
    cameras[0].set(3, 80)
    cameras[0].set(4, 40)
    print(cameras[0].get(3))
    print(cameras[0].get(4))
    
except:
    print("camera fail")

q1 = Queue()
q2 = Queue()
prev_time1 = 0
prev_time2 = 0
fps = 12
def gen_frames(camera, queue, prev_time):  
    
    while True:
        success, frame = camera.read()
            
        current_time = time.time() - prev_time
        if (not success):
            break
        elif(success is True) and (current_time > 1./ fps):
            prev_time = time.time()
            ret, buffer = cv2.imencode('.png', frame)
            frame = buffer.tobytes()
#             print("frame")
            queue.put(b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
            #yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed/<int:num>')
def video_feed(num):
    print("cam",num)
    return Response( q1.get() , mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response( q1.get() , mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/video_feed2')
def video_feed2():
    return Response( q2.get(), mimetype='multipart/x-mixed-replace; boundary=frame') 
#####

@app.route('/')
def main():
    thread1 = Thread(target=gen_frames, args=(cameras[0], q1,prev_time1,))
    thread2 = Thread(target=gen_frames, args=(cameras[1], q2,prev_time2,))
    thread1.daemon = True
    thread2.daemon = True
    thread1.start()
    thread2.start()
    return render_template('index.html')

@app.route('/motor/<num>/<speed>')
def mymoter(num, speed):
    try:
        motor.set_motor_contorl(motors[int(num)], ina[int(num)], inb[int(num)], int(speed))
        return "ok"
    except:
        return "fail"  

@app.route('/servo/<num>/<degree>')
def myservo(num, degree):
    try:
        print("servo", num, ": ",degree)
        if(type(servos[int(num)]) == type(())):
            servo2.servo_pos(servos[int(num)][0], int(degree), 0, 180)
            servo2.servo_pos(servos[int(num)][1], 180 - int(degree), 0,180)
            return "ok"
        
        servo2.servo_pos(servos[int(num)], int(degree), 0, 180)
        return "ok"
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

def addnum(num1):
    return num1 + 1

if __name__ == '__main__':

    socketio.run(app, host='0.0.0.0', port=8080)#, debug=True)
    GPIO.cleanup()