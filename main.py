import winreg
from winreg import QueryValueEx
import subprocess
import winshell
from pathlib import Path
import time
import os
import pywinauto
from pywinauto import Application
import win32gui
import win32con
import win32com.client
from math import floor

os.system("mode con cols=50")
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def state(num):
    if num == "1":
        return f"Not Rendering"
    else:
        return f"Rendering"

desktop = Path(winshell.desktop())
flag_started = False
flag_stopped = False
# program = r'C:\Windows\System32\schtasks.exe'
# arguments = (f'/run /tn "MinerStart"')
count = 0
os.startfile(fr"C:\rndr-master\start.bat")
print("RNDR Started")
time.sleep(120)

while True:

    if __name__ == "__main__":
        results = []
        top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "error" in i[1].lower():
            print("Memory fail RNDR")
            win32gui.ShowWindow(i[0], 5)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('enter')
            win32gui.SetForegroundWindow(i[0])

            win32gui.PostMessage(i[0], win32con.WM_CLOSE, 0, 0)
            time.sleep(0.5)
            break

    root = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    policy_key = winreg.OpenKeyEx(root, r"SOFTWARE\OTOY")
    print(policy_key)
    value_key = QueryValueEx(policy_key, "RNDR_IDLE")
    if value_key[0] == "1":
        if not flag_started:
            if count != 0:
                time.sleep(120)
                if value_key[0] == "1":
            # subprocess.call([program, arguments])
                    os.startfile(fr"{desktop}\PhoenixMiner_4.0b_Windows\PhoenixMiner.exe")
            # subprocess.call([fr"{desktop}\PhoenixMiner_4.0b_Windows\PM.bat"])
                else:
                    continue
            else:
                os.startfile(fr"{desktop}\PhoenixMiner_4.0b_Windows\PhoenixMiner.exe")
            flag_started = True
            flag_stopped = False
    elif value_key[0] == "0":
        if not flag_stopped:
            if __name__ == "__main__":
                results = []
                top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if "phoenixminer" in i[1].lower():
                    print(i)
                    win32gui.ShowWindow(i[0], 5)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(i[0])

                    win32gui.PostMessage(i[0], win32con.WM_CLOSE, 0, 0)
                    time.sleep(0.5)
                    break

            flag_stopped = True
            flag_started = False
    winreg.CloseKey(policy_key)
    print(f"State of Render Node: {state(value_key[0])}")
    print(f"Current run in secs: {floor(time.perf_counter())}")
    time.sleep(10)
    count += 1