import os, random
from datetime import datetime, timedelta

# check if customtask is already running and deltes it
if os.system("schtasks /query /tn CustomTask") == 0:
    os.system("schtasks /delete /f /tn CustomTask")

# what this task does
print("Hi I am a custom task")

# current path
filedir = os.path.join(os.getcwd(), "sched.py")

# repetition
interval = 1
dt = datetime.now() + timedelta(minutes=interval)

# formatting date and time for schtasks
t = f"{str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}"
d = f"{dt.month}/{str(dt.day).zfill(2)}/{dt.year}"

# print(f"schtasks /create /tn CustomTask /tr \"{filedir}\" /sc once /st {t} /sd 0{d}")

# scheduling the task
os.system(f'schtasks /create /tn CustomTask /tr "{filedir}" /sc once /st {t} /sd 0{d}')

input()
