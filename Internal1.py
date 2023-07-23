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

reader = SimpleMFRC522()

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

servo.setup()

# Initialize the count variable to track unsuccessful attempts
count = 0

def readKeyPadData(pressedValue):
    global count

    mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)

    try: 
        print(pressedValue)
        if pressedValue == "1234":
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






























# import time
# from mfrc522 import SimpleMFRC522
# import RPi.GPIO as GPIO
# import StepperMotor as door
# import sys
# import asyncio
# import firebase_setup
# import Constants

# import touchSensorIn as lightSensor
# import IRSensor as servoMotorSensor

# reader = SimpleMFRC522()

# collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

# # Initialize the count variable to track unsuccessful attempts
# count = 0

# def readKeyPadData(pressedValue):
#     global count

#     mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)

#     try: 
#         print(pressedValue)
#         if pressedValue == "1234":
#             door.setup()
#             door.loop() 
#             mainDoorValue.update({'mDoorStatus': "opened"})
#             time.sleep(0.1)
#             mainDoorValue.update({'mDoorStatus': "closed"}) 
#             # asyncio.run(readIRData())
#             asyncio.run(readSensors())
            
            
            
#             # asyncio.ensure_future(readSensors())
#             count = 0  # Reset the count when the correct code is entered
#         else:
#             print("Hi, I am in else block")
#             print(count)
#             count += 1
#             if count > 3:
#                 print("Camera activated")
#                 count = 0  # Reset the count after executing the camera print
#     except:
#         GPIO.cleanup()
#         sys.exit()


# async def readSensors():
#     #  # Run both sensor reading functions as separate tasks
#     # sensor_task1 = asyncio.create_task(read_sensor_data())
#     # sensor_task2 = asyncio.create_task(read_IR_Sensor_Data())
    
#     # # Wait for both tasks to complete (which will be never as they run indefinitely)
#     # await asyncio.gather(sensor_task1, sensor_task2)
#     while True:
#             await read_sensor_data()
#             await read_IR_Sensor_Data()  
#             await asyncio.sleep(1) 

# # async def readIRData():
# #     # while True:        
# #             await read_IR_Sensor_Data()           
# #             await asyncio.sleep(1) 
   

# async def read_sensor_data():
#                 # while True:      
#                           data =  lightSensor.touchFunctionality() 
#                           print('Status: ',data)
#                           await asyncio.sleep(1)

# async def  read_IR_Sensor_Data():
#                 # while True: 
#                            servoMotorSensor.setup()          
#                            data = servoMotorSensor.loop()                         
#                            await asyncio.sleep(1)
            
