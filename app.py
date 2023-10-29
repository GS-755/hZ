from os import system
from time import sleep
import psutil as ps 

MAX_FREQ = 144
MIN_FREQ = 60

def set_freq(hzValue) -> None:
  system(f"runtime\\QRes.exe f={str(hzValue)}")

def main() -> None:
  while(True):
    battery = ps.sensors_battery()
    plugged = battery.power_plugged
    if(plugged):
      set_freq(MAX_FREQ)
    else:
      set_freq(MIN_FREQ)
    sleep(0.1)

try:
  main()
except Exception:
  main()




