import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import StepperMotor as door
import sys
import threading
import firebase_setup
import Constants
 
import touchSensorIn as lightSensor
import IRSensor as servoMotorSensor
import ServoMotor as servo
import Temperature as tempAndHumdity
import camera_handler as camera


reader = SimpleMFRC522()

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

count  = 0;

def readCard():
        global count
        mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)
        try: 
           print("hey Im in MFRC522")
           id, text = reader.read()
           count = 0
           print('ID:', id)
           if id == 114018660653 or id == 222867724730 or id == "None":
                  door.setup()
                  door.loop() 
                  mainDoorValue.update({'mDoorStatus': "opened"})
                  time.sleep(0.1)
                  mainDoorValue.update({'mDoorStatus': "closed"}) 
                  sensor_thread = threading.Thread(target=readSensors)
                  sensor_thread.start()

                  ir_thread = threading.Thread(target=readIRData)
                  ir_thread.start()

                  hygroThermoGraph_Thread  = threading.Thread(target=readTemparatureData())
                  hygroThermoGraph_Thread.start()

                  count = 0  # Reset the count when the correct code is entered
           else:
                   print(count)
                   count += 1
                   if count > 3:
                      camera.capture()
                      print("Camera activated")
                      count = 0  # Reset the count after executing the camera print
        except:
                GPIO.cleanup()
                sys.exit()

def readSensors():
    while True:
        read_sensor_data()  
        time.sleep(1)

def readIRData():
    while True:        
        read_IR_Sensor_Data()           
        time.sleep(1) 

def readTemparatureData():
    while True:
        read_temp_data()
        time.sleep(1)        

def read_sensor_data():
    # while True:      
    data = lightSensor.touchFunctionality() 
    print('Status: ', data)
    time.sleep(1)

def read_IR_Sensor_Data():
    # while True: 
    servoMotorSensor.setup()          
    data = servoMotorSensor.loop()                         
    time.sleep(1)

def read_temp_data():
    tempAndHumdity.loop()
    time.sleep()
 
#                 count = 0
#                 door.setup()
#                 door.loop() 
#                 mainDoorValue.update({'mDoorStatus':"opened"})
#                 time.sleep(0.1)
#                 mainDoorValue.update({'mDoorStatus':"closed"}) 
#                 asyncio.run(readSensors())
#            else:
#                 count = count + 1
#                 if count == 3:
#                         print("camera activated")        

#         except:
#             GPIO.cleanup()
#             sys.exit()


# async def readSensors():

#     while True:
#             await read_sensor_data()  
#             await asyncio.sleep(1)  
#     # # Create tasks for each sensor
#     # print("Hi execution is in Read_sensor")
#     # tasks = [
#     #     read_sensor_data(), 
#     # ]
#     # await asyncio.gather(*tasks)

# async def read_sensor_data():
                    
#                           data =  lightSensor.touchFunctionality() 
#                           print('Status: ',data)
#                           await asyncio.sleep(1)
            