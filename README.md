# smart

##Need library
###1)flask
####install: 
'''
$ sudo apt-get install python3-flask
'''
###2)pigpio
####install:
'''
$ wget https://github.com/joan2937/pigpio/archive/master.zip
$ unzip master.zip
$ cd pigpio-master
$ make
$ sudo make install
'''
####if you can't install it
'''
$ sudo apt install python-setuptools python3-setuptools
'''
####you need to run deamon before use pigpio
'''
$ sudo pigpiod
'''
####kill deamon
'''
$ sudo killall pipiod
'''
###3)TensorFlow Lite
####install:
'''
$ git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
$ mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/ tflite1
$ cd tfilte1
$ bash get_pi_requirements.sh
$ wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
$ unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model
'''
####How to run:
'''
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
'''
