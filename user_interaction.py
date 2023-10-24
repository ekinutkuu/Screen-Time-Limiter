import datetime
import os
import json



print('''

███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗    ████████╗██╗███╗   ███╗███████╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║    ╚══██╔══╝██║████╗ ████║██╔════╝
███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║       ██║   ██║██╔████╔██║█████╗  
╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║       ██║   ██║██║╚██╔╝██║██╔══╝  
███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║       ██║   ██║██║ ╚═╝ ██║███████╗
╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝\n

\t\t██╗     ██╗███╗   ███╗██╗████████╗███████╗██████╗ 
\t\t██║     ██║████╗ ████║██║╚══██╔══╝██╔════╝██╔══██╗
\t\t██║     ██║██╔████╔██║██║   ██║   █████╗  ██████╔╝
\t\t██║     ██║██║╚██╔╝██║██║   ██║   ██╔══╝  ██╔══██╗
\t\t███████╗██║██║ ╚═╝ ██║██║   ██║   ███████╗██║  ██║
\t\t╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

''')



username = os.getlogin()
currentLocation = str(os.getcwd())
projectFolderPath = f"C:\\Users\\{username}\\Documents\\Screen Time Limiter"
projectFolderPath2 = f"C:\\Users\\{username}\\Documents\\Screen Time Limiter\\pyFiles"
startupLocation = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
configLocation = None
mainLocation = None
if not os.path.exists(projectFolderPath):
    os.mkdir(projectFolderPath)
if not os.path.exists(projectFolderPath2):
    os.mkdir(projectFolderPath2)


with open("config.json","r") as json_file:
    config_data = json.load(json_file)

firstLaunch = config_data.get("firstLaunch")

confirmationLoop = True
if firstLaunch == 1:
    while confirmationLoop == True:
        userConfirmation = input("Do you want to run this project every time at windows starts? | Y/N : ")

        if userConfirmation.lower() == "y" or userConfirmation.lower() == "yes":
            config_data["firstLaunch"] = 0
            config_data["savedToStartup"] = "True"
            with open("config.json","w") as json_file:
                json.dump(config_data, json_file, indent=4)

            os.rename(currentLocation+"\\user_interaction.py", projectFolderPath+"\\user_interaction.py")
            os.rename(currentLocation+"\\ScreenTimeLimiter.bat", startupLocation+"\\ScreenTimeLimiter.bat")
            os.rename(currentLocation+"\\config.json", projectFolderPath+"\\config.json")
            os.rename(currentLocation+"\\main.exe", projectFolderPath+"\\main.exe")
            os.rename(currentLocation+"\\pyFiles\\main.py", projectFolderPath+"\\pyFiles\\main.py")
            os.rename(currentLocation+"\\pyFiles\\main.pyw", projectFolderPath+"\\pyFiles\\main.pyw")
            os.rename(currentLocation+"\\pyFiles\\readme.txt", projectFolderPath+"\\pyFiles\\readme.txt")

            print("\nProject will run every time at windows starts.")
            print("Project files moved to Windows Documents folder!")
            print("Read the github readme file for detailed information! (github.com/ekinutkuu/Screen-Time-Limiter)\n")

            configLocation = projectFolderPath+"\\config.json"
            mainLocation = projectFolderPath+"\\main.exe"
            confirmationLoop = False
        elif userConfirmation.lower() == "n" or userConfirmation.lower() == "no":
            #print("\nYour preferences have been saved!\n")
            print("\n")
            configLocation = currentLocation+"\\config.json"
            mainLocation = currentLocation+"\\main.exe"

            confirmationLoop = False
        else:
            print("Invalid value! Try Again...")
elif firstLaunch == 0:
    configLocation = currentLocation+"\\config.json"
    mainLocation = currentLocation+"\\main.exe"


allowedHourInput = int(input("Allowed Hour: "))
allowedMinuteInput = int(input("Allowed Minute: "))

with open(configLocation, "r") as jsonFile:
    configData = json.load(jsonFile)

configData["allowedHour"] = allowedHourInput
configData["allowedMinute"] = allowedMinuteInput

with open(configLocation, "w") as jsonFile:
    json.dump(configData, jsonFile, indent=4)


currentTime = datetime.datetime.now()

totalMinutes = currentTime.hour * 60 + currentTime.minute
totalMinutes += allowedHourInput * 60 + allowedMinuteInput

endHour = totalMinutes // 60
endMinute = totalMinutes % 60

if endHour >= 24:
    endHour = endHour % 24


print("Start Time:", str(currentTime.hour).zfill(2) + ":" + str(currentTime.minute).zfill(2))
print("End Time:", str(endHour).zfill(2) + ":" + str(endMinute).zfill(2), "\n")
print("Logs related to the screen time limiter will be saved to the Windows Documents folder!")

a = input("Press enter to start...")

os.startfile(mainLocation)
