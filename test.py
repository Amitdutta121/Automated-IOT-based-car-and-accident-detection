from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time
import socket
#create flask server
app = Flask(__name__)

#select motor driver pin
m11=2
m12=3
m21=14
m22=15


m31=19
m32=26

#initially everything is set to LOW
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)

GPIO.setup(m31, GPIO.OUT)
GPIO.setup(m32, GPIO.OUT)

GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
GPIO.output(m31, 0)
GPIO.output(m32, 0)


#creating snippet to acces with javascript
a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"

   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
   GPIO.output(m31, 0)
   GPIO.output(m32, 0)

   return  'true'

@app.route('/butt')
def butt():
   data1="BUTT"
   GPIO.output(m31 , 0)
   GPIO.output(m32 , 1)
   return  'true'


if __name__ == "__main__":    
 import socket
 #getting the local ip address
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8", 80))
 ipaddr = s.getsockname()[0] 
 s.close()
 print ("Start")
#run the loacl server
 app.run(host=ipaddr,port=5010)
