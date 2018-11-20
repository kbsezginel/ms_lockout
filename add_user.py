"""
Add new user to csv file.
"""
import datetime
from csv_helper import read_headers, append_csv


CSV_FILE = 'ms_lockout.csv'

# Read RFID card
rfid = '111-22-33-44'
print('RFID card read: %s' % rfid)

# Ask for user info and update CSV file
headers = read_headers(CSV_FILE)[1:-1]
row = [rfid]
for h in headers:
    value = input('Please enter %s: ' % h)
    row.append(value)

now = datetime.datetime.now()
row.append(now.strftime('%b-%d-%Y'))
append_csv(CSV_FILE, row)
