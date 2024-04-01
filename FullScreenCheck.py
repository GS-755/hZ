import ctypes

def is_fullscreen() -> bool:
  try: 
    return ctypes.windll.user32.IsFullScreen(0) == 1
  except: 
    return False;
