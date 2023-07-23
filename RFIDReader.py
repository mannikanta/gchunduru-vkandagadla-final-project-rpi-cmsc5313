import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import StepperMotor as door
import sys
import asyncio
import firebase_setup
import Constants

import touchSensorIn as lightSensor

reader = SimpleMFRC522()

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

def readCard():
        mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)
        try: 
           id, text = reader.read()
           count = 0
           print('ID:', id)
           if id == 114018660653 or id == 222867724730 or id == 'None':
                count = 0
                door.setup()
                door.loop() 
                mainDoorValue.update({'mDoorStatus':"opened"})
                time.sleep(0.1)
                mainDoorValue.update({'mDoorStatus':"closed"}) 
                asyncio.run(readSensors())
           else:
                count = count + 1
                if count == 3:
                        print("camera activated")        

        except:
            GPIO.cleanup()
            sys.exit()


async def readSensors():

    while True:
            await read_sensor_data()  
            await asyncio.sleep(1)  
    # # Create tasks for each sensor
    # print("Hi execution is in Read_sensor")
    # tasks = [
    #     read_sensor_data(), 
    # ]
    # await asyncio.gather(*tasks)

async def read_sensor_data():
                    
                          data =  lightSensor.touchFunctionality() 
                          print('Status: ',data)
                          await asyncio.sleep(1)
            