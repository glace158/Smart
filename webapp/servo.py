import RPi.GPIO as GPIO 

SERVO_MAX_DUTY    = 10
SERVO_MIN_DUTY    = 3

GPIO.setmode(GPIO.BCM)
 

def set_servo(pin):
    GPIO.setup(pin, GPIO.OUT)
    
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    return pwm

def servo_pos(pwm, degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
        
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    pwm.ChangeDutyCycle(duty)

