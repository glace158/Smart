import time
import serial
import servo2
from queue import Queue


class Radar:
    
    def __init__(self, radar_servo, tik, mindegree, maxdegree):
        self.radar_servo = servo2.Servo(radar_servo)
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
        
    def get_distance(self):
        YCTa = 0
        YCTb = 0
        YCT1 = 0
        
        while True:
            first = self.ser.read(1)
            if(first == b'\xff'):
                buffer_RTT = []
            
            for i in range(8):
                buffer_RTT.append(self.ser.read(1))
                time.sleep(0.002)
            
            if(buffer_RTT[0]==b'\xff'):
                if(buffer_RTT[1]== b'\xff'):
                    YCTa=buffer_RTT[2]
                    YCTb=buffer_RTT[3]
                    YCT1=(YCTa[0]<<8) + YCTb[0]
                    print("D: ", YCT1)
                    break
        return YCT1

    def move_radar(self):
        data = {}
        while True:
            while (self.degree >= self.mindegree and self.degree <= self.maxdegree):
                self.degree += self.tik
                self.radar_servo.servo_pos(self.degree)
                distance = round(self.get_distance() * 0.01, 2)
                data[self.degree] = distance
            
            self.tik *= -1
            self.degree = self.maxdegree if self.tik < 0 else self.mindegree
            print(data.items())
            self.q.put(data)
            data.clear()
            
    def get_q(self):
        print(self.q.qsize())
        while (self.q.qsize() > 1):
            self.q.get()
            
        return self.q.get()
