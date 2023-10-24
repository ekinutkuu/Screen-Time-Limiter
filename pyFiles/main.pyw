import os
import sys
import datetime
import time
import json


currentLocation = os.path.dirname(sys.executable)

with open(currentLocation+"\\config.json","r") as json_file:
    config_data = json.load(json_file)

allowedHour = config_data.get("allowedHour")
allowedMinute = config_data.get("allowedMinute")

totalMinutes = allowedHour * 60 + allowedMinute
startTime = datetime.datetime.now()
endTime = startTime + datetime.timedelta(minutes=totalMinutes)

while datetime.datetime.now() < endTime:
    remainingTime = endTime - datetime.datetime.now()
    print(f"Remaining Time: {remainingTime}")
    time.sleep(10)

username = os.getlogin()
filePath = f"C:\\Users\\{username}\\Documents\\Screen Time Limiter\\log.txt"
text = (
"The computer was successfully shut down at the specified time! \n" 
+ "Screen Time: " + str(allowedHour) + " hour " + str(allowedMinute) + " minute \n" 
+ "Date and Time: "+str(datetime.datetime.now())+"\n\n"
)
file = open(filePath, "a")
file.write(text)
file.close()
os.system("shutdown /s /t 1")
