# import RPi.GPIO as GPIO
# import asyncio
# import RFIDReader
# import KeypadIn as keyIn 
# import Internal

# class MainController:
#     def __init__(self):
#         self.rfid_reader = RFIDReader.SimpleMFRC522()
    
#     def run_main_loop(self):
#         while True:
#             pressed_value = keyIn.loop()
#             self.handle_keypad_data(pressed_value)

#     def handle_keypad_data(self, pressed_value):
#         bool_val = Internal.readKeyPadData(pressed_value)

# if __name__ == "__main__":
#     main_controller = MainController()
#     try:
#         loop = asyncio.get_event_loop()
#         loop.create_task(main_controller.run_main_loop())
#         loop.run_forever()
#     except KeyboardInterrupt:
#         print("Program terminated by user.")
#         GPIO.cleanup()






import RfidCardTest
import KeypadIn as keyIn 
import Internal1
import firebase_setup
import Constants as constants

collection = firebase_setup.db.collection(constants.COLLECTION_NAME)
valueEmbed = collection.document(constants.DOCUMENT_EMBEDDED)
while True:
     #    document_emb = valueEmbed.get().to_dict()
     #    ein = document_emb.get('embedded')
     #    if ein == True:
        #      RfidCardTest.loop()
     #    else:     
              pressedValue =  keyIn.loop()
              boolVal = Internal1.readKeyPadData(pressedValue)
    #  RFIDReader.readCard() 
#    pressedValue =  keyIn.loop()
#    boolVal = Internal1.readKeyPadData(pressedValue)
   
   
#     touchButton.touchFunctionality()


# import threading
# import RFIDReader
# import touchSensorIn as touchButton

# def read_card_thread():
#     while True:
#         RFIDReader.readCard()

# def touch_functionality_thread():
#     while True:
#         touchButton.touchFunctionality()

# # Create and start the threads
# read_card_thread = threading.Thread(target=read_card_thread)
# # touch_functionality_thread = threading.Thread(target=touch_functionality_thread)

# read_card_thread.start()
# # touch_functionality_thread.start()
