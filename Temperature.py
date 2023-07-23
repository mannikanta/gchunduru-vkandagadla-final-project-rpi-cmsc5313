import RPi.GPIO as GPIO
import Adafruit_DHT
from rpi_lcd import LCD
import time
import Constants as constants
import firebase_setup

collection = firebase_setup.db.collection(constants.COLLECTION_NAME)
# 
lcd = LCD()
sensor = Adafruit_DHT.DHT11
pin = 23 
def loop():
    hygrothermo_ref = collection.document(constants.DOCUMENT_TEMP)
    # counts = 0 
    while True:
        # counts += 1
        for i in range(0, 15):
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            if humidity is not None and temperature is not None:
                break
            time.sleep(0.1)
        # print("Humidity: %.2f, \tTemperature: %.2f \n" % (humidity, temperature))
        # lcd.text("Humidity"+" "+str(humidity), 1)
        lcd.text("Temperature"+" "+str(temperature), 2)
        # hygrothermo_ref.update({'':humidity})
        hygrothermo_ref.update({'temp':temperature})
        time.sleep(2)

# if __name__ == '__main__':
#     print('Program is starting...')
#     try:
#         loop()
#     except KeyboardInterrupt:
#         # lcd.clear()
#         GPIO.cleanup()
#     exit()