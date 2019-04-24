import RPi.GPIO as GPIO
import time



m31=19
m32=26


GPIO.setmode(GPIO.BCM)
GPIO.setup(m31, GPIO.OUT)
GPIO.setup(m32, GPIO.OUT)

GPIO.output(m31 , 0)
GPIO.output(m32 , 1)

