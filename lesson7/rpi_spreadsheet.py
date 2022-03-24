import json
import sys
import time
import datetime
import gspread
import psutil
import subprocess
from system_info import get_temperature
from oauth2client.service_account import ServiceAccountCredentials
GDOCS_OAUTH_JSON       = 'KEY_FILE_NAME.json'
GDOCS_SPREADSHEET_NAME = 'SPREADSHEET_NAME'
FREQUENCY_SECONDS      = 10
def login_open_sheet(oauth_key_file, spreadsheet):
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, 
                      scopes = ['https://spreadsheets.google.com/feeds',
                                'https://www.googleapis.com/auth/drive'])
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet. Check OAuth credentials, spreadsheet name, and')
        print('make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None

def find_previous_row(worksheet):
  str_list = list(filter(None, worksheet.col_values(1)))
  return len(str_list)

def find_max_rows(worksheet):
  return len(worksheet.get_all_values())

while True:
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
    dat = datetime.datetime.now()
    cpu = psutil.cpu_percent()
    tmp = get_temperature()
    print(dat)
    print('CPU Usage:   {0:0.1f} %'.format(cpu))
    print('Temperature: {0:0.1f} C'.format(tmp))
    try:
        previous_row = find_previous_row(worksheet)
        max_rows = find_max_rows(worksheet)

        if previous_row < max_rows:
            worksheet.update_acell("A{}".format(previous_row), str(dat))
            worksheet.update_acell("B{}".format(previous_row), cpu)
            worksheet.update_acell("C{}".format(previous_row), tmp)
        else:
          worksheet.append_row((str(dat), cpu, tmp))
#        worksheet.append_row((dat, cpu, tmp))
# gspread==0.6.2
# https://github.com/burnash/gspread/issues/511  
    except:
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)
