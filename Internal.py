import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import StepperMotor as door
import sys
import asyncio
import firebase_setup
import Constants

import touchSensorIn as lightSensor
import IRSensor as servoMotorSensor

reader = SimpleMFRC522()

collection = firebase_setup.db.collection(Constants.COLLECTION_NAME)

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
            # asyncio.run(readIRData())
            asyncio.run(readSensors())
            
            
            
            # asyncio.ensure_future(readSensors())
            count = 0  # Reset the count when the correct code is entered
        else:
            print("Hi, I am in else block")
            print(count)
            count += 1
            if count > 3:
                print("Camera activated")
                count = 0  # Reset the count after executing the camera print
    except:
        GPIO.cleanup()
        sys.exit()


async def readSensors():
    #  # Run both sensor reading functions as separate tasks
    # sensor_task1 = asyncio.create_task(read_sensor_data())
    # sensor_task2 = asyncio.create_task(read_IR_Sensor_Data())
    
    # # Wait for both tasks to complete (which will be never as they run indefinitely)
    # await asyncio.gather(sensor_task1, sensor_task2)
    while True:
            await read_sensor_data()
            await read_IR_Sensor_Data()  
            await asyncio.sleep(1) 

# async def readIRData():
#     # while True:        
#             await read_IR_Sensor_Data()           
#             await asyncio.sleep(1) 
   

async def read_sensor_data():
                # while True:      
                          data =  lightSensor.touchFunctionality() 
                          print('Status: ',data)
                          await asyncio.sleep(1)

async def  read_IR_Sensor_Data():
                # while True: 
                           servoMotorSensor.setup()          
                           data = servoMotorSensor.loop()                         
                           await asyncio.sleep(1)
            
















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

# def readKeyPadData(pressedValue):
#         mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)
        
#         try: 
#            print(pressedValue)
#            if pressedValue == "1234":
#                 door.setup()
#                 door.loop() 
#                 mainDoorValue.update({'mDoorStatus':"opened"})
#                 time.sleep(0.1)
#                 mainDoorValue.update({'mDoorStatus':"closed"}) 
#                 asyncio.run(readSensors())
#            else:
#                 print("Hi I am in else block")
#                 print(count)
#                 count = count + 1
#                 if count > 3:
#                         print("camera activated")          
#         except:
#             GPIO.cleanup()
#             sys.exit()


# async def readSensors():

#     while True:
#             await read_sensor_data()  
#             await asyncio.sleep(1) 
#             await read_IR_Sensor_Data() 
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

# async def  read_IR_Sensor_Data():
#                            data = servoMotorSensor.loop()                         
#                            await asyncio.sleep(1)
            