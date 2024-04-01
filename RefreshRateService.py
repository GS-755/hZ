import subprocess
import configparser
from os import system
from time import sleep
import psutil as ps 
import sys
from FullScreenCheck import is_fullscreen

sys.setrecursionlimit(1500) 
RUNTIME_PATH = 'runtime\\QRes.exe'
APP_NAME = 'RefreshRateService.exe'
CONFIG_PATH = 'config.ini'
VERSION = '1.5.2'

def set_freq(hzValue) -> None:
  system(f"{RUNTIME_PATH} f={str(hzValue)}")

def hide_gui() -> None: 
  subprocess.Popen(APP_NAME, shell=True, stdin=None, stdout=None, stderr=None)

def listen() -> None: 
  while True: 
    battery = ps.sensors_battery()
    plugged = battery.power_plugged
    if not is_fullscreen():
      if(plugged):
        set_freq(int(config['MonitorSpecs']['MAX_FREQ']))
      else:
        set_freq(int(config['MonitorSpecs']['MIN_FREQ']))
      sleep(0.2)

if(__name__ == '__main__'): 
  config = configparser.ConfigParser()
  config.read(CONFIG_PATH)
  listen()
