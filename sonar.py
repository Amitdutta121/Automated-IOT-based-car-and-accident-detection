# Libraries
import RPi.GPIO as GPIO
import time

import pyrebase

config ={
	"apiKey": "AIzaSyD6CrwdW8cBgm6S3aNF9FkWgK6aTtYsjd8",
    "authDomain": "cse341project.firebaseapp.com",
    "databaseURL": "https://cse341project.firebaseio.com",
    "projectId": "cse341project",
    "storageBucket": "cse341project.appspot.com",
    "messagingSenderId": "638349095865"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 21
GPIO_ECHO = 20

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if int(dist)<20:
                db.child("CSE341_project").update({"AGE": "Danger"})
            else:
                db.child("CSE341_project").update({"AGE": "Safe"})
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()