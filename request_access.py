"""
Request access to power with RFID card read.
"""
import requests
import time
import MFRC522
import RPi.GPIO as GPIO
from rgb_blink import rgb_blink


SERVER_IP = '192.168.0.108:5000'
POST_ADDRESS = 'http://%s/post' % SERVER_IP
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
print('Waiting to read card...')
while True:

    (status, TagType) = RFID_READER.MFRC522_Request(RFID_READER.PICC_REQIDL)
    (status, uid) = RFID_READER.MFRC522_Anticoll()

    if status == RFID_READER.MI_OK:
        # Read RFID card
        uid = '-'.join([str(i) for i in uid])
        print('RFID card read: %s' % uid)
        data = {'device': 'drill', 'uid': uid}
        try:
            req = requests.post(POST_ADDRESS, data=data)
            if req.text == 'yes':
                print('%s has acess.' % uid)
                GPIO.output(RELAY_PIN, relay_modes[relay_now])
                rgb_blink(LED_PINS, "green", 1)
                time.sleep(1)
                if relay_now == 1:
                    relay_now = 0
                elif relay_now == 0:
                    relay_now = 1
                else:
                    relay_now = 0
            elif req.text == 'no':
                print('%s does not have acess.' % uid)
                rgb_blink(LED_PINS, "red", 1)
            elif req.text == 'not-found':
                print('%s not in database.' % uid)
                rgb_blink(LED_PINS, "blue", 2)
        except Exception as e:
            print('Cannot make request!\n%s' % e)
            rgb_blink(LED_PINS, "purple", 3)

        print('\nWaiting to read card...')
