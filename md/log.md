# log.md

2025.1003

enabled uart1,2,3 on pi0.

```
sudo vi /boot/firmware/config.txt
[all]
enable_uart=1
dtoverlay=uart2,txpin=0,rxpin=1
dtoverlay=uart3,txpin=2,rxpin=3
```

uart1 for pico-0, uart2 for pico-1, uart3 for esp32


2025.0926

ordered aliexpress: Raspberry Pi Pico and ESP32 WROOM-32 


2025.0925

gone: one arduino nano

gone: one esp32-c3 super mini


2025.0921

esp32-c3 super mini works for wifi and ble keyboard and ble mouse, all at the same time.
wifi did not work when plugged into breadboard, while ble still worked. weirdo. both wifi and ble use 2.4GHz, anyway. maybe signal strength due to faraday cage effect or whatever...
wasted a few days wondering why wifi does not work now, when first time testing worked. at last i know why.

2025.0916

esp32-c3 super mini works for ble hid keyboard and ble hid mouse simultaneously
use vs code with platformio extension, and ESP32-BLE-Combo lib from github

2025.0903

pi0 power also does not recognize full power either. maybe due to thin breakout dupont lines are not enough to drive full current. when sdcard reader was plugged in, low voltage warning showed up. measured the power supply voltage, it is 5.1V as it should be. so the issue is the dupont cables from power supply to pi0 5V pin. i may need to physically modify the gpio header connector to accomodate proper 5V and gnd pin connection.  

x11 -> no good, stick to wayland labwc

pi1 vcc was wrong (it was vcc for cooling fan from display, this caused low voltage warning and pre-mature shutdown, now pi1 power behaviour should resemble pi0), use usb-c for sure

2025.0902

pi0 mouse control cmds => uno output d2-d10 => pro micro input_pullup d2-d10 => pi1 mouse being controlled by pi0 code

soldered pro micro pins. thought i fried it. there is a active low rst (reset) pin. this will allow uploading the sketch when not uploading normally

2025.0901

"pro micro" is not official arduino product. it is made by other company. 
official arduino is just "micro"

2025.0831

accidental buck converter ups. can sustain pi0 and pi1 for 1 hour. full recharging 2~3 days 
to avoid indefitely trickle charging, do discharge excercise at least every 3 days. like regular excercise if ibi is a real cat

<br>
2025.0828

kiosk runs for two hours with 8x1.2V nimh + buck conveter 

<br>
2025.0827

arduino pro micro hid mouse

pyautogui desktop capture and mouse position and mouse click

<br>
2025.0826

buck converter

sg90 360 degree

<br>
2025.0825

usb port name to nano/uno

<br>
2025.0819

3 dof pi cam, used three sg90 to create a mechanism for Pitch -> Yaw -> Roll

<br>
2025.0816

chicken detected

<br>
2025.0809

blazor united servers at osaka, toronto and colab receive messages sent from pi signalrcore at vancouver

<br>
2025.0728

two eyes
<div align="center">
  <img src="../png/two-eyes-2025-0728-1004-16.png" alt="two eyes" width="640" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0726
<br>
proof of concept moving pad with two servos for vertical and horizonal directions
<br>
use cardboard, masking tape and zip tie. arduino needs longer usb cable extension to reach mouse on computer table
<br>
there is no particular reason to keep the mouse upright normal position. keep the mouse in upside down and let the bottom laser diode light visible and simply cover a moving paper pad. use two paint roller like structure for moving pad control. this seems to be more effective and easier... use two more servos for mouse left and right click, and two more for scrolling, and last one for shutter or hopping

total 7 sg90 servos

<div align="center">
  <img src="../png/idea-moving-pad.png" alt="idea-moving-pad" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0724
<br>
added pi4 camera. sensor readings on webcam view, light blue is measured w/ pi4, yellow w/ arduino
<br>
tip: install picamera2 and opencv using `apt install` system wide instead of `pip install` in venv, and then create venv w/ ` python3 -m venv --system-site-packages venv` this is not an ideal, but due to compatibility issues such as python version and numpy==1.24.2, best workaround so far.

<div align="center">
  <img src="../png/ibi-the-watch-cat-2025-0724-1658-54.png" alt="ibi-the-watch-cat-2025-0724-1658-54" width="1280" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0721
<br>
10 Pcs 9G SG90 Micro Servo Motors arrived! so tiny and cute, i love it.

<div align="center">
  <img src="../png/servos.png" alt="servos" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0720
<br>
AM2302 (DHT22) Digital Temperature and Humidity Sensor on Pi 4

Real-time sensor reading is shown at Live Stats (https://ibinti.com/ibi-the-watch-cat)

<div align="center">
  <img src="../png/dht22.png" alt="dht22" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0719
<br>
NiMH charger and relays... NC -> discharging, NO -> charging

<div align="center">
  <img src="../png/ups_parts0.png" alt="ups parts" width="350" style="display: inline-block; margin: 0 15px;">
  <img src="../png/UPS-NiMH.png" alt="wiring diagram" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>
2025.0717
<br>
arduino on pi usb port
<br>
pyfirmata on pi controls arduino onboard led on/off/blink

youtube video demo

[![blinking youtube](https://img.youtube.com/vi/j8u58aLM6-E/hqdefault.jpg)](https://youtube.com/shorts/j8u58aLM6-E?feature=share)
<br>

2025.0713
<br>
real-time heartbeat

2025.0712

arduino and raspberry pi 4 in the body box. run pi with ac-power adaptor.
let it to connect wifi and push heartbeat to ibinti.com/ibi-the-watch-cat
<br>
set up ssh tunnel and real vnc viewer<br>
```bash
ssh -L 5900:20.25.07.12:5900 ibi@20.25.07.12
VNC Server: localhost
ibi pushes heartbeat
```
<br>
