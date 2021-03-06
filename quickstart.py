# from __future__ import print_function
# from googleapiclient.discovery import build
# from httplib2 import Http
# from oauth2client import file, client, tools

# # If modifying these scopes, delete the file token.json.
# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1wd-SJIKFnhZ15XAFvIoh5tVSlYQGeoRpTpTQQKLoiGQ'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# def main():
#     """Shows basic usage of the Sheets API.
#     Prints values from a sample spreadsheet.
#     """
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     store = file.Storage('token.json')
#     creds = store.get()
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = build('sheets', 'v4', http=creds.authorize(Http()))

#     values = [
#         [
#             Sheet1!A1 #         ]
#     ]
#     body = {
#         'values': values
#     }
#     result = service.spreadsheets().values().update(
#         spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_name,
#         valueInputOption=value_input_option, body=body).execute()
#     print('{0} cells updated.'.format(result.get('updatedCells')))

from __future__ import print_function
import sqlite3
import time
import sys

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('/home/pi/RaspiHeadless/storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('/home/pi/RaspiHeadless/credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

# data = {'properties': {'title': 'RaspiLogTest [%s]' % time.ctime()}}
# res = SHEETS.spreadsheets().create(body=data).execute()
# SHEET_ID = res['spreadsheetId']
# print('Created "%s"' % res['properties']['title'])
SHEET_ID = '14NHYlZAGWZctGriND8Vprd1tjnE-PhfpWpFtHQgjero'

ip = (str(sys.argv[1]))
values = [
        ["Hostname", "IP Adress", "Last Update"],
        [],
        [],
        ["Raspi3's IP:", ip, time.ctime()]
    ]
body = {'values': values }

SHEETS.spreadsheets().values().update(spreadsheetId=SHEET_ID,
    range='A1', body=body, valueInputOption='RAW').execute()
print('Wrote data to Sheet:')
rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
    range='Sheet1').execute().get('values', [])
for row in rows:
    print(row)





