import RPi.GPIO as GPIO

class Motor:
    def __init__(self, EN, INA):#, INB):
        self.ina = INA
        #self.inb = INB
        
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        #GPIO.setup(INB, GPIO.OUT)
        
        self.pwm = GPIO.PWM(EN, 100)
        self.pwm.start(0)
            
        #print(self.ina, self.inb, self.pwm)
        

    def motor_speed(self, speed):
        print(speed)
        self.pwm.ChangeDutyCycle(abs(speed))  
    
        if speed == 0:
            GPIO.output(self.ina, 0)
            #GPIO.output(self.inb, 0)
        elif speed < 0:
            GPIO.output(self.ina, 0)
            #GPIO.output(self.inb, 1)
        elif speed > 0:
            GPIO.output(self.ina, 1)
            #GPIO.output(self.inb, 0)
    
    @staticmethod
    def dual_speed(motor, speed):
        print(motor, speed)
        print(type(motor))
        #motor[0].motor_speed(speed)
        #motor[1].motor_speed(speed)