'''
import subprocess

subprocess.call(["taskkill","/F","/IM","msedge.exe"])
'''

import psutil
import subprocess

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

if is_process_running('msedge.exe'):
    subprocess.call(["taskkill", "/F", "/IM", "msedge.exe"])
    print("msedge.exe killed successfully.")
else:
    print("msedge.exe is not running.")

