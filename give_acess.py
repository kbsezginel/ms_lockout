"""
Give access to power with RFID card read.
"""
import time
from csv_helper import read_csv
import MFRC522
import RPi.GPIO as GPIO


CSV_FILE = 'ms_lockout.csv'
DATA = read_csv(CSV_FILE)
print(DATA)
user_ids = [col[0] for col in DATA]
print(user_ids)
access_col_idx = 3

RELAY_PIN = 11  # GPIO.BOARD setting
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)
relay_modes = [GPIO.HIGH, GPIO.LOW]
relay_now = 0

RFID_READER = MFRC522.MFRC522()
print('Waiting to read card...')
while True:

    (status, TagType) = RFID_READER.MFRC522_Request(RFID_READER.PICC_REQIDL)
    (status, uid) = RFID_READER.MFRC522_Anticoll()

    if status == RFID_READER.MI_OK:
        # Read RFID card
        uid = '-'.join([str(i) for i in uid])
        print('RFID card read: %s' % uid)

        try:
            user_index = user_ids.index(uid)
            print('User found: %i' % user_index)

            if DATA[user_index][access_col_idx] == 'yes':
                print('%s has acess.' % DATA[user_index][1])
                GPIO.output(RELAY_PIN, relay_modes[relay_now])
                time.sleep(1)
                if relay_now == 1:
                    relay_now = 0
                elif relay_now == 0:
                    relay_now = 1
                else:
                    relay_now = 0
            else:
                print('%s does not have acess.' % DATA[user_index][1])
        except:
            print('User not found!')

        print('\nWaiting to read card...')
