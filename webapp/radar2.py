import time
import serial
import pigpio
import servo2
from queue import Queue


class Radar:
    
    def __init__(self, radar_servo, tik, mindegree, maxdegree):
        self.pi = pigpio.pi()
        self.radar_servo = radar_servo
        
        self.tik = tik
        self.degree = mindegree
        self.mindegree = mindegree
        self.maxdegree = maxdegree
        self.q = Queue()
        self.ser = serial.Serial(
            port='/dev/ttyAMA1',
            baudrate=57600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
            )
        print("----------Radar----------")
        print("Pin: ", self.radar_servo)
        print("Degree: ", self.mindegree, "~", self.maxdegree)
        print("Tik: ", self.tik)

    def move_radar(self):
        while True:
            data = {}
            while (self.degree >= self.mindegree and self.degree <= self.maxdegree):
                self.degree += self.tik
                
                duty = 600 + 10 * self.degree
                self.pi.set_servo_pulsewidth(self.radar_servo, duty)
                
                YCTa = 0
                YCTb = 0
                YCT1 = 0
        
                while True:
                    first = self.ser.read(1)
                    if(first == b'\xff'):
                        buffer_RTT = []
            
                        for i in range(7):
                            buffer_RTT.append(self.ser.read(1))
            
                        if(buffer_RTT[0]==b'\xff'):
                            if(buffer_RTT[1]== b'\xff'):
                                YCTa=buffer_RTT[2]
                                YCTb=buffer_RTT[3]
                                YCT1=(YCTa[0]<<8) + YCTb[0]
                                break
                        
                distance = round(YCT1 * 0.01, 2)
                for i in range(self.degree, self.degree + self.tik, -1 if self.tik < 0 else 1):
                    data[i] = distance
                    if(i < self.mindegree or i > self.maxdegree):
                        break
            
            self.tik *= -1
            self.degree = self.maxdegree if self.tik < 0 else self.mindegree

            self.q.put(data)
            
    def get_q(self):
        while (self.q.qsize() > 1):
            self.q.get()
        
        data = self.q.get()
        print("----------Radar_Data----------")
        print(data)
        print("------------------------------")
        return data
