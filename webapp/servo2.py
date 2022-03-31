import pigpio
import time
pi = pigpio.pi()

def servo_pos(pwm, degree , min, max):
    if degree > max:
        degree = max
    elif degree < min:
        degree = min
    
    duty = 600 + 10 * degree
    pi.set_servo_pulsewidth(pwm, duty)