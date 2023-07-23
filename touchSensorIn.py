import RPi.GPIO as GPIO
import time
import sys
import Constants
import firebase_setup

GPIO.setmode(GPIO.BOARD)
touch = 11   # GPIO pin number on the board
light = 12   # GPIO pin number on the board
GPIO.setup(touch, GPIO.IN)
GPIO.setup(light, GPIO.OUT)

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)
 
def touchFunctionality():
    tocuSensorValue = collection.document(Constants.DOCUMENT_LIGHT)
    try:
        senState = GPIO.input(touch)
        if senState:
            GPIO.output(light, GPIO.HIGH)
            time.sleep(1)
            tocuSensorValue.update({'light':"light On"})
            return "Sensor is touched"
        else :
            GPIO.output(light, GPIO.LOW)
            time.sleep(0.1)
            tocuSensorValue.update({'light':"light off"})
            return "sensor not touched"
    except Exception as e:
        print("An exception occurred:", e)    
    # except KeyboardInterrupt:
    #     GPIO.cleanup()
    #     sys.exit()





# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# touch = 17
# light = 18
# GPIO.setup(touch, GPIO.IN)
# butState = 0
# butStateOld = 0
# index  = 0
# GPIO.setup(light, GPIO.OUT)

# def touchFunctionality():
#         try:
#             while True:
#                 senState = GPIO.input(touch)
#                 print(senState)
#                 if butState == 0 and butStateOld == 1:
#                    GPIO.output(light, GPIO.HIGH)
#                 butStateOld = butState
#                 # if senState:
#                 #     GPIO.output(light, GPIO.HIGH)
#                 #     time.sleep(1)
#                 # else :
#                 #     GPIO.output(light, GPIO.LOW)
#                 #     time.sleep(0.1)
#         except KeyboardInterrupt:
#                 GPIO.cleanup()            