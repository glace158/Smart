from flask import Flask, request, render_template
import motor
import servo2
import cv2
import RPi.GPIO as GPIO
app = Flask(__name__)

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
servos.append(24)
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
        servo2.servo_pos(servos[int(num)], int(degree))
        return "ok"
    except:
        return "fail"

if __name__== '__main__':
    try:
        app.run(host='0.0.0.0', port='8080')
        GPIO.cleanup()
    except KeyboardInerrupt:
        GPIO.cleanup()