"""
Add new user to csv file.
"""
import datetime
from csv_helper import read_headers, append_csv
import MFRC522


CSV_FILE = 'ms_lockout.csv'

RFID_READER = MFRC522.MFRC522()
print('Waiting to read card...')
while True:

    # Scan for cards
    (status, TagType) = RFID_READER.MFRC522_Request(RFID_READER.PICC_REQIDL)

    # Get the UID of the card
    (status, uid) = RFID_READER.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == RFID_READER.MI_OK:
        # Read RFID card
        uid = '-'.join([str(i) for i in uid])
        print('RFID card read: %s' % uid)

        # Ask for user info and update CSV file
        headers = read_headers(CSV_FILE)[1:-1]
        row = [uid]
        for h in headers:
            value = input('Please enter %s: ' % h)
            row.append(value)

        now = datetime.datetime.now()
        row.append(now.strftime('%b-%d-%Y'))
        append_csv(CSV_FILE, row)
        print('User added', row)
        break
