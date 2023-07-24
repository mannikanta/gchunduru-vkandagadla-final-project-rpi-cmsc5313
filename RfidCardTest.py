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

def loop():
        try:
                global count
                mainDoorValue = collection.document(Constants.DOCUMENT_MAIN_DOOR)
                id, text = reader.read()
                print('Id: ',id)
                print('text: ',text)
                if id == 114018660653 or id == 222867724730:
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
 
