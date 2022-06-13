import os, winreg

if __name__ == "__main__":
    reghive = winreg.HKEY_CURRENT_USER
    regpath = "Environment"
    targetdir = os.getcwd()

    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, access=winreg.KEY_ALL_ACCESS)

    path = ""
    i = 0
    while True:
        value = winreg.EnumValue(key, i)

        if value[0] == "Path":
            path = value[1]
            break

        i += 1

    new_path = f"{targetdir};{path}"
    print(new_path)

    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
