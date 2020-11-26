import http.client, urllib.request, urllib.parse, urllib.error
from time import localtime, strftime
import psutil
import time
from pickle import dump as pickle_dump # Pridhvi Myneni
from pickle import load as pickle_load
from os.path import exists as file_exists
from os.path import isfile as is_file
PICKLE_FILE_NAME = "API_KEY.pickle"
API_KEY_INDEX = "API_KEY"
def doit():
	cpu_pc = psutil.cpu_percent()
	mem = psutil.virtual_memory()
	mem_avail_mb = mem.available/(1024*1024)
	params = urllib.parse.urlencode({'field1': cpu_pc, 'field2':
             mem_avail_mb,'key':'YOURKEYHERE'})
	headers = {"Content-type":
               "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print(cpu_pc)
		print(mem_avail_mb)
		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		print(response.status, response.reason)
		data = response.read()
		conn.close()
	except:
		print("connection failed")
#sleep for 60 seconds (api limit of 15 secs)
if __name__ == "__main__":
	if file_exists(PICKLE_FILE_NAME) and is_file(PICKLE_FILE_NAME): # Pridhvi Myneni
		save_file = None
		with open(PICKLE_FILE_NAME, 'rb') as f:
			save_file = pickle_load(f)
		KEY = save_file[API_KEY_INDEX]
	else:
		key = input("An API key savefile was not found. Enter Write API Key >>> ")
		should_save = input("Should we save this key for future use? [y/N] >>> ")
		KEY = key.strip()
		if len(should_save)>0 and should_save.lower().startswith("y"):
			with open(PICKLE_FILE_NAME, 'wb') as f:
				pickle_dump({API_KEY_INDEX: KEY}, f)  
	while True:
		doit()
		time.sleep(60)
