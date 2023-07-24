import RPi.GPIO as GPIO
import Keypad

ROWS = 4
COLS = 4
keys = ['1', '2', '3', 'A',
        '4', '5', '6', 'B',
        '7', '8', '9', 'C',
        '*', '0', '#', 'D']

rowsPins = [18, 7, 13, 15]
colsPins = [19, 29, 31, 33]

# Global variable to store the pressed keys as a string



def loop():
    global pressed_keys_str 
    pressed_keys_str = ""
    keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
    keypad.setDebounceTime(50)
    while len(pressed_keys_str) < 4:
        key = keypad.getKey()
        if key != keypad.NULL:
            # print("You Pressed Key: %c" % key)
            pressed_keys_str += key
    return pressed_keys_str

pressed_keys_str = loop()



# if __name__ == '__main__':     #Program start from here
#     print ("Program is starting ... ")
#     try:
#         loop()
#     except KeyboardInterrupt:  #When 'Ctrl+C' is pressed, exit the program. 
#         GPIO.cleanup()