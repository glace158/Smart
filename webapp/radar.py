import time
import serial

ser = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

YCTa = 0
YCTb = 0
YCT1 = 0

def get_distance():
    while True:
        first = ser.read(1)
        #print(first == b'\xff')
        if(first == b'\xff'):
            buffer_RTT = []
            
            for i in range(8):
                buffer_RTT.append(ser.read(1))
                time.sleep(0.002)
            #print(buffer_RTT)
            if(buffer_RTT[0]==b'\xff'):
                if(buffer_RTT[1]== b'\xff'):
                    YCTa=buffer_RTT[2]
                    YCTb=buffer_RTT[3]
                    YCT1=(YCTa[0]<<8) + YCTb[0]
                    print("D: ", YCT1)
                    break
        
            
    return YCT1
