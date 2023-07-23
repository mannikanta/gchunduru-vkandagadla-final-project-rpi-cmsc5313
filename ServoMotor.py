import RPi.GPIO as GPIO
import time

# Additional Feature Code
OFFSE_DUTY = 0.5 #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY 
servoPin = 35


GPIO.setmode(GPIO.BOARD) 
GPIO.setup(servoPin, GPIO.OUT)
GPIO.output(servoPin, GPIO.LOW) 

def setup():
      global p
      p = GPIO.PWM(servoPin, 50) # set Frequece to 50Hz
      p.start(0) # Set initial Duty Cycle to 0  

# additional feature code
def servoWrite(angle): # make the servo rotate to specific angle, 0-180 
    # if(angle<0):
    #     angle = 0
    # elif(angle > 180):
    #     angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY)) # map the angle to duty cycle and output it

def map( value, fromLow, fromHigh, toLow, toHigh): # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def loop(angle):
           try:
              servoWrite(angle)
           except Exception as e:
                 print(e) 