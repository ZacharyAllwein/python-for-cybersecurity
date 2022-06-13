import PyInstaller.__main__
import shutil, os

cwd = os.getcwd()
filename = "malicious.py"
exename = "benign.exe"
usbdir = os.path.join(cwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)

PyInstaller.__main__.run(
    [
        "malicious.py",
        "--onefile",
        "--clean",
        "--log-level=ERROR",
        "--name=" + exename,
    ]
)

shutil.move(os.path.join(cwd, "dist", exename), cwd)
shutil.rmtree("dist")
shutil.rmtree("build")
os.remove(exename + ".spec")
