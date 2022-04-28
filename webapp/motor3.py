import RPi.GPIO as GPIO

class Motor2:
    def __init__(self, EN, INA, INB):
        self.ina = INA
        self.inb = INB
        
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        GPIO.setup(INB, GPIO.OUT)
        
        self.pwm = GPIO.PWM(EN, 100)
        self.pwm.start(0)
        
        print("----------Motor----------")
        print("PWM: ", self.pwm)
        print("INA: ", self.ina)
        print("INB: ", self.inb)
        

    def motor_speed(self, speed):
        self.pwm.ChangeDutyCycle(abs(speed))  
    
        if speed == 0:
            GPIO.output(self.ina, 0)
            GPIO.output(self.inb, 0)
        elif speed < 0:
            GPIO.output(self.ina, 0)
            GPIO.output(self.inb, 1)
        elif speed > 0:
            GPIO.output(self.ina, 1)
            GPIO.output(self.inb, 0)
