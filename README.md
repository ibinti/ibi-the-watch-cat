# ibi-the-watch-cat

Safety Monitor Watch AI Robot

I'm excited to share my Safety Monitor Watch AI Robot project. This project focuses on developing an AI robot using Adruino, Raspberry Pi and AI model trained on Colab.

It's currently in the idea stage, and I'm exploring various aspects of its design and functionality.

Currently, there is a significant gap between the ideal and the expected. The project goal is to minimize it.

<div align="center">
  <img src="ibi-the-watch-cat-ideal.png" alt="ideal ibi" width="350" style="display: inline-block; margin: 0 15px;">
  <img src="ibi-the-watch-cat-expected.png" alt="expected ibi" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>

I'm thinking through things like:

    Key features: What specific tasks will it perform?

    Navigation: How will it move independently?

    Sensors: What technologies will it use to perceive its environment?

I'm looking forward to refining these ideas as the project progresses!

```
duties -
monitor humidity
monitor temperature
watch plant grow
watch youtube - move the physical mouse with servos etc and watch the display screen
...
```
```
hardware -
arduino
raspberry pi
camera
mic
sensors - temp, humidity, etc
relay
servo motor
qi transmitter and receiver
nickel-metal hydride (NiMH)
...etc
```
```
software -
raspberry pi os
Ubuntu
python
pytorch
rain open_clip
knowledge distillation to tinyvit
onnx
docker
fastapi
ssh tunnel
.net9 maui blazor hybrid web with mudblazor
colab
vps
...etc
```
<br>
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
2025.0713
<br>
real-time heartbeat

2025.0717
<br>
arduino on pi usb port
<br>
pyfirmata on pi controls arduino onboard led on/off/blink

youtube video demo

[![blinking youtube](https://img.youtube.com/vi/j8u58aLM6-E/hqdefault.jpg)](https://youtube.com/shorts/j8u58aLM6-E?feature=share)
<br>
<br>
2025.0719

todo: UPS with NiMH charger and relays... NC -> discharging, NO -> charging
<div align="center">
  <img src="ups_parts0.png" alt="ups parts" width="350" style="display: inline-block; margin: 0 15px;">
</div>

<br>

2025.0720
<br>
todo: meetup
...
