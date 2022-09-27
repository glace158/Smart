import time
import pyaudio
import wave
from threading import Thread

class Mic:
    def __init__(self, state=True):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000
        self.CHUNK = 512
        self.RECORD_SECONDS = 0.01
        self.audio1 = pyaudio.PyAudio()
        print("-----------Mic-----------")
        
    
    def start(self):
        thread = Thread(target=self.genHeader, args=())
        thread.daemon = True
        thread.start()
        return self
    
    def genHeader(self, sampleRate, bitsPerSample, channels):
        datasize = 2000*10**6
        o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
        o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
        o += bytes("WAVE",'ascii')                                              # (4byte) File type
        o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
        o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
        o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
        o += (channels).to_bytes(2,'little')                                    # (2byte)
        o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
        o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
        o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
        o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
        o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
        o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
        return o
    
    def sound(self):

        CHUNK = 512
        sampleRate = 48000
        bitsPerSample = 16
        channels = 1
        self.wav_header = self.genHeader(sampleRate, bitsPerSample, channels)

        self.stream = self.audio1.open(format=self.FORMAT, channels=self.CHANNELS,
                        rate=self.RATE, input=True,input_device_index=1,
                        frames_per_buffer=self.CHUNK)
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = self.wav_header + self.stream.read(self.CHUNK)
               first_run = False
           else:
               data = self.stream.read(self.CHUNK)
           yield(data)
    
    
    def loading(self):
        return (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + self.loadimg + b'\r\n')
    
    def set_state(self, state):
        self.state = state

