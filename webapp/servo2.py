import pigpio

pi = pigpio.pi()

def servo_pos(pwm, degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
    
    duty = 600 + 10 * degree
    pi.set_servo_pulsewidth(pwm, duty)