import cv2
from queue import Queue
import time

class Camera:
    def __init__(self, cam_num, fps, state=True):
        self.cam = cv2.VideoCapture(cam_num, cv2.CAP_V4L)
        self.q = Queue()
        self.fps = fps
        self.prev_time = 0
        self.state = state
        self.cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.cam.set(3, 80)
        self.cam.set(4, 40)
        print("cam", cam_num, self.cam.get(3))
        print("cam", cam_num, self.cam.get(4))
        
    def gen_frames(self):  
        while True:
            success, frame = self.cam.read()
            current_time = time.time() - self.prev_time
            if (not success):
                break
            elif(success is True) and (current_time > 1./ self.fps and self.state):
                self.prev_time = time.time()
                ret, buffer = cv2.imencode('.png', frame)
                frame = buffer.tobytes()
                self.q.put(b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
                #yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
            elif (not self.state):
                self.clear_q()
        
    def set_state(self, state):
        self.state = state
    
    def clear_q(self):
        while(not self.q.empty()):
            self.q.get()
        print("q_empty")
        
        
    def get_q(self):
        return self.q.get()
