import RPi.GPIO as GPIO

HIGH = 1
LOW = 0

def set_motor(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    
    pwm = GPIO.PWM(EN, 100) 
       
    pwm.start(0) 
    return pwm

def set_motor_contorl(pwm, INA, INB, speed):
    pwm.ChangeDutyCycle(abs(speed))  
    
    if speed == 0:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)
    elif speed < 0:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
    elif speed > 0:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
  

GPIO.setmode(GPIO.BCM)
