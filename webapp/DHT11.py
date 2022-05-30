import time
import board
import adafruit_dht
import psutil
  

        # We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
        
class DHT11Sensor:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11(pin)
        
    def readtemp(self):
        temp = 0
        try:
            temp = self.sensor.temperature
        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:
            self.sensor.exit()
            raise error
        return temp
    
#obj0 = DHT11Sensor(13)
#obj1 = DHT11Sensor(20)

#print(obj0.readtemp())
#print(obj1.readtemp())