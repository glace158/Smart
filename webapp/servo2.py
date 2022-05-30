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

#servos = []
#servos.append(Servo(14, 0, 60))#grip 0/60 init 0
#servos.append(Servo(15, 0, 140))#wrist 0/140 -1 init 90
#servos.append(Servo(18))#wristroll 0/180 init 90
#servos.append(Servo((23,24), 16,144))#elbow 16/144 init 16
#servos.append(Servo((25,8),16,160))#shoulder 16/160 init 16

#servos[0].servo_pos(0)
#time.sleep(3)
#servos[1].servo_pos(100)
#time.sleep(3)