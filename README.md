# smart

## Need library
### 1)flask
#### install: 
```
sudo apt-get install python3-flask
```
### 2)pigpio
#### install:
```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```
#### if you can't install it
```
sudo apt install python-setuptools python3-setuptools
```
#### you need to run deamon before use pigpio
```
sudo pigpiod
```
#### kill deamon
```
sudo killall pipiod
```
### 3)TensorFlow Lite
#### install:
```
git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/ tflite1
sudo pip3 install virtualenv
python3 -m venv tflite1-env
cd tfilte1
bash get_pi_requirements.sh
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model
```
#### TensorFlow Coral
```
// plz unplugged coral
cd tflite1
source tflite1-env/bin/activate
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install libedgetpu1-max
// check ok and yes
wget dl.google.com/coral/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite
mv mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite Sample_TFLite_model/edgetpu.tflite
// plz plugged coral and start your code 
```
#### How to run:
```
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
```
## Serial port setting
#### First open the config.txt file
```
sudo nano /boot/config.txt
```
#### Add text at endline of the config.txt file
```
dtoverlay=uart2
```
#### Reboot raspberrypi
```
sudo reboot
```
#### Check Serial port
```
ls -l /dev/ttyAMA*
```
If you check "/dev/ttyAMA1"
Success Serial port setting

## DHT11
```
sudo apt update
sudo apt full-upgrade
sudo apt install python3-pip
sudo pip3 install --upgrade setuptools
sudo reboot

sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```
