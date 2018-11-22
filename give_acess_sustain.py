"""
Give access to power with RFID card read.
"""
import time
from csv_helper import read_csv
import MFRC522
import RPi.GPIO as GPIO
from rgb_blink import rgb_blink


# DATABASE SETUP
CSV_FILE = 'ms_lockout.csv'
DATA = read_csv(CSV_FILE)
user_ids = [col[0] for col in DATA]
access_col_idx = 3

GPIO.setmode(GPIO.BOARD)

# RELAY SETUP
RELAY_PIN = 16  # GPIO.BOARD setting
GPIO.setup(RELAY_PIN, GPIO.OUT)
relay_modes = [GPIO.HIGH, GPIO.LOW]
relay_now = 0

# LED SETUP
LED_PINS = [11, 13, 15]
for p in LED_PINS:
    GPIO.setup(p, GPIO.OUT)

RFID_READER = MFRC522.MFRC522()
uid = ''
print('Waiting to read card...')
while True:

    (status, TagType) = RFID_READER.MFRC522_Request(RFID_READER.PICC_REQIDL)
    (status, uid) = RFID_READER.MFRC522_Anticoll()

    if status == RFID_READER.MI_OK:
        # Read RFID card
        uid_now = '-'.join([str(i) for i in uid])
        if uid_now == uid:
            continue
        else:
            print('RFID card read: %s' % uid_now)
            uid = uid_now
            try:
                user_index = user_ids.index(uid)
                print('User found: %i' % user_index)

                if DATA[user_index][access_col_idx] == 'yes':
                    print('%s has acess.' % DATA[user_index][1])
                    GPIO.output(RELAY_PIN, relay_modes[relay_now])
                    rgb_blink(LED_PINS, "green", 1)
                    time.sleep(1)
                    if relay_now == 1:
                        relay_now = 0
                    elif relay_now == 0:
                        relay_now = 1
                    else:
                        relay_now = 0
                else:
                    print('%s does not have acess.' % DATA[user_index][1])
                    rgb_blink(LED_PINS, "red", 1)
            except:
                print('User not found!')
                rgb_blink(LED_PINS, "blue", 2)

        print('\nWaiting to read card...')
    else:
        print('No card')
