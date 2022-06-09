import RPi.GPIO as GPIO
import time

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
#SPICLK = 11
#SPIMISO = 9
#SPIMOSI = 10
#SPICS = 19
#mq2_dpin = 26
#mq2_apin = 0

GPIO.setmode(GPIO.BCM)

class GasSensor:
    #port init
    def __init__(self, SPICLK=11, SPIMISO=9, SPIMOSI=10, SPICS=19, mq2_dpin=26, mq2_apin=0):
         # set up the SPI interface pins
        self.mq2_apin = mq2_apin
        self.mq2_dpin = mq2_dpin
        self.SPICLK = SPICLK
        self.SPIMISO = SPIMISO
        self.SPIMOSI = SPIMOSI
        self.SPICS = SPICS
        GPIO.setup(self.SPIMOSI, GPIO.OUT)
        GPIO.setup(self.SPIMISO, GPIO.IN)
        GPIO.setup(self.SPICLK, GPIO.OUT)
        GPIO.setup(self.SPICS, GPIO.OUT)
        GPIO.setup(self.mq2_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
    def readadc(self):
        if ((self.mq2_apin > 7) or (self.mq2_apin < 0)):
            return -1
        GPIO.output(self.SPICS, True)

        GPIO.output(self.SPICLK, False)  # start clock low
        GPIO.output(self.SPICS, False)     # bring CS low

        commandout = self.mq2_apin
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
            if (commandout & 0x80):
                    GPIO.output(self.SPIMOSI, True)
            else:
                    GPIO.output(self.SPIMOSI, False)
            commandout <<= 1
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)
            adcout <<= 1
            if (GPIO.input(self.SPIMISO)):
                adcout |= 0x1

        GPIO.output(self.SPICS, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout