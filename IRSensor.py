import RPi.GPIO as GPIO
import ServoMotor
import time
import firebase_setup
import Constants

ledPin = 12 # define ledPin
sensorPin = 37 # define sensorPin

def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode
   #  ServoMotor.setup()

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

def loop():
      try:  
        #   setup()
          irSensorValue = collection.document(Constants.DOCUMENT_WINDOW)
          motion = GPIO.input(sensorPin)
          print(motion)
          ServoMotor.loop(45)
          if motion:
             ServoMotor.loop(0)
             irSensorValue.update({'window':"Window Open"})
          else:
             ServoMotor.loop(120)        
             irSensorValue.update({'window':"Window close"})
          time.sleep(1)
      except KeyboardInterrupt:
           GPIO.cleanup()
      except Exception as e:
        print("Exception occurred: ", str(e))

             
       
