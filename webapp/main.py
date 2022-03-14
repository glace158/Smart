from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit
import motor
import servo2
import RPi.GPIO as GPIO

app = Flask(__name__)
app.secret_key = "pswd"
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)

#motor pin
en = [2, 17, 10, 0]
ina = [3, 27, 9, 5]
inb = [4, 22, 11, 6]

motors = []

for i in range(4):
    motors.append( motor.set_motor(en[i], ina[i], inb[i]) )

#servo pin
servos = []

servos.append(14) 
servos.append(15)
servos.append(18)
servos.append(23)
servos.append((24,8))
servos.append(25)

@app.route('/')
def hello():
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
        if(type(servos[int(num)]) == type(())):
            servo2.servo_pos(servos[int(num)][0], int(degree))
            servo2.servo_pos(servos[int(num)][1], 180 - int(degree))
            return "ok"
        
        servo2.servo_pos(servos[int(num)], int(degree))
        return "ok"
    except:
        return "fail"

@socketio.on('testSocket',namespace='/test')
def testEvent(data):
    print(data)
    num = data['num']
    num = addnum(num)
    emit('test', {"num": num},callback=session.get('test'))

def addnum(num1):
    return num1 + 1

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
    GPIO.cleanup()