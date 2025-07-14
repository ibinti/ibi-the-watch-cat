# ibi-the-watch-cat

Autonomous Safety Monitor Watch AI Robot

I'm excited to share my Autonomous Safety Monitor Watch AI Robot project. This self-explanatory project focuses on developing a mobile AI robot capable of independent safety surveillance.

It's currently in the idea stage, and I'm exploring various aspects of its design and functionality.

At the moment, there exists a significant gap between the ideal ibi vs the expected ibi. Current project goal is to minimize the existing gap.

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
watch smoke
watch humidity
watch temperature
watch gas leak
watch water leak
watch pot 
watch door
watch window
watch neighbour cats
watch neighbour dogs
watch squarrel
watch silver fish
watch spider
watch youtube?
...
```
```
hardware -
arduino
raspberry pi
camera
mic
sensors - smoke, temp, humidity, etc 
motor
wheel
gear box
qi transmitter and receiver pair
nickel-metal hydride and lithium-ion rechargeable battery - charging and level monitoring circuit
...etc
```
```
software -
raspberry pi os
ubuntu
python
pytorch
train open_clip with adapter layer
knowledge distillation to tinyclip or tinyvit
onnx
docker
fastapi
ollama
ssh tunnel
.net maui blazor hybrid web app with mudblazor
kaggle
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

real-time ibi heartbeat works

<br>
2025.0719

2025.0720
<br>
todo: try run tinyclip and tinyvit with onnx on pi 4
...
