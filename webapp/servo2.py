import pigpio
from enum import Enum
import time

pi = pigpio.pi()
 
class Mode(Enum):
    SINGLE = 1
    DUAL = 2

class Servo:
    
    def __init__(self, pwm, min=0, max=180):
        if ( type(pwm) is int ):
            self.mode = Mode.SINGLE
        elif( type(pwm) == type(()) ):
            self.mode = Mode.DUAL
        self.pwm = pwm
        self.min = min
        self.max = max
        
        print("----------Servo----------")
        print("Mode: ", self.mode)
        print("PWM: ", self.pwm)
        print("Degree: ", self.min, "~", self.max)    
    
    def servo_pos(self, degree):
        if degree > self.max:
            degree = self.max
        elif degree < self.min:
            degree = self.min
        
        duty = 600 + 10 * degree
        if( self.mode == Mode.SINGLE):
            pi.set_servo_pulsewidth(self.pwm, duty)
            
        elif( self.mode == Mode.DUAL):
            pi.set_servo_pulsewidth(self.pwm[0], duty)
            
            duty = 600 + 10 * ((self.max + self.min) - degree)
            pi.set_servo_pulsewidth(self.pwm[1], duty)
