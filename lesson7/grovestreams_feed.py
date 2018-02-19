# GroveStreams.com Python version 2.7 Feed Example
# Demonstrates uploading two stream feeds within a URL and URL
# encoding

# This example uploads two stream feeds, random temperature and humidity
# samples every 10 seconds.
# A full "how to" guide for this example can be found at:
# https://www.grovestreams.com/developers/getting_started_helloworld_python.html
# It relies and the GroveStreams API which can be found here:
# https://www.grovestreams.com/developers/api.html#1

# License:
# Copyright 2014 GroveStreams LLC.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#GroveStreams Setup:

#* Sign Up for Free User Account - https://www.grovestreams.com
#* Create a GroveStreams organization
#* Enter the GroveStreams org uid under "GroveStreams Settings" below
#*    (Can be retrieved from a GroveStreams organization:
#*     Tools toolbar button - View Organization UID)
#* Enter the GroveStreams api key under "GroveStreams Settings" below
#*    (Can be retrieved from a GroveStreams organization:
#*     click the Api Keys toolbar button,
#*     select your Api Key, and click View Secret Key)

import time
import datetime
import http.client
import random
import urllib.request, urllib.parse, urllib.error


if __name__ == '__main__':

    #GroveStreams Settings
    api_key = "YOUR_SECRET_API_KEY_HERE"    #Change This!!!

    component_id = "sensor1 - hello world"
    base_url = '/api/feed?'

    conn = http.client.HTTPConnection('www.grovestreams.com')

    while True:

        temperature_val = random.randrange(-10, 40)
        humidity_val = random.randrange(0, 100)

        #Upload the feed
        try:
            #Let the GS servers set the sample times. Encode parameters
            url = base_url + urllib.parse.urlencode({'compId' : component_id,
                                                     'temperature' : temperature_val,
                                                     'humidity' : humidity_val})

            #Alternative URL that includes the sample time
            #now = datetime.datetime.now()
            #sample_time = int(time.mktime(now.timetuple())) * 1000
            #url = base_url + urllib.parse.urlencode({'compId' : component_id, 'time' : sample_time, 'temperature' : temperature_val, 'humidity' : humidity_val})

            #Alternative URL that uses the stream order to determine where
            # to insert the samples
            #url = base_url + urllib.parse.urlencode({'compId' : component_id, 'data' : [temperature_val, humidity_val]}, True)

            #The api_key token can be passed as URL parameters or as a cookie.
            # We've chosen to pass it as a cookie to keep the URL length small as
            # some devices have a URL size limit
            headers = {"Connection" : "close", "Content-type": "application/json",
                       "Cookie" : "api_key="+api_key}

            #GS limits feed calls to one per 10 seconds per outward facing router IP address
            #Use the ip_addr and headers assignment below to work around this
            # limit by setting the below to this device's IP address
            #ip_addr = "192.168.1.72"
            #headers = {"Connection" : "close", "Content-type": "application/json", "X-Forwarded-For": ip_addr, "Cookie" : "org="+org+";api_key="+api_key}

            print('Uploading feed to: ' + url)

            conn.request("PUT", url, "", headers)

            #Check for errors
            response = conn.getresponse()
            status = response.status

            if status != 200 and status != 201:
                try:
                    if (response.reason != None):
                        print('HTTP Failure Reason: ' + response.reason + ' body: ' + response.read())
                    else:
                        print('HTTP Failure Body: ' + response.read())
                except Exception:
                    print('HTTP Failure Status: %d' % (status) )

        except Exception as e:
            print('HTTP Failure: ' + str(e))

        finally:
            if conn != None:
                conn.close()

        #Pause for ten seconds
        time.sleep(10)

    # quit
    exit(0)
