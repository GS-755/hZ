from os import system
from time import sleep
import psutil as ps 

MAX_FREQ = 144
MIN_FREQ = 60

def set_freq(hzValue) -> None:
  system(f"runtime\\qres.exe f={str(hzValue)}")

def main() -> None:
  while(True):
    battery = ps.sensors_battery()
    plugged = battery.power_plugged
    if(plugged == False):
      set_freq(MIN_FREQ)
    set_freq(MAX_FREQ)
    sleep(0.15)




