
# Screen Time Limiter

The main purpose of this project is limit the screen time.

**You can run this project with :**
```
$ python user_interaction.py
```
Note that cmd/terminal must be run as **administrator** mode when typing the command.

When you run this file, it will ask you the following question: do you want to run this project every time at windows starts? You can adjust this as you wish. Remember that, If you do not answer "yes/y" to the question, this question will be asked again in every run. Once other various information about limiting the screen is entered, an invisible exe file **(main.exe)** will run in the background. It will adjust the screen's time based on the data you provided and shut down the computer at the specified time. Information regarding the screen time spent will be saved in the windows documents folder.

# Warnings !

 - If you want to run this project, you should **run cmd as administrator!**

 - If you answer "yes/y" to the windows startup option, **the location of "ScreenTimeLimiter.bat" will be changed to:**
	```
	C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
	```
	This .bat file will run user_interaction.py every time at windows starts. This will make the project run every time at windows starts.
	
	You can disable this feature by removing this file from here.
 
 - If you answer "yes/y" to the windows startup option, project files will be moved to Windows Document Folder. Please do not move the project files from here, for the project to work properly. 

	If you answer "no/n" to the question, there will be no problem to move the project folder anywhere.

# Notes

 - In the future, I will add a feature which we can automatically remove the windows startup feature.
 
 - I am aware that there are some design flaws in the project. I will try to find a better way in the future. Stay tuned!

