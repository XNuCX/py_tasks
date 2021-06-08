import winreg
from winreg import QueryValueEx
import subprocess
import winshell
from pathlib import Path
import time
desktop = Path(winshell.desktop())
flag_started = False
flag_stopped = False
while True:
    root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    policy_key = winreg.OpenKeyEx(root, r"SOFTWARE\OTOY")
    print(policy_key)
    value_key = QueryValueEx(policy_key, "RNDR_IDLE")
    if value_key[0] == "1":
        if not flag_started:
            subprocess.call([fr"{desktop}\Tasks\start_miner.bat"])
            flag_started = True
            flag_stopped = False
    elif value_key[0] == "0":
        if not flag_stopped:
            subprocess.call([fr"{desktop}\Tasks\KILL Miner.bat"])
            flag_stopped = True
            flag_started = False
    winreg.CloseKey(policy_key)
    print(value_key)
    time.sleep(10)
