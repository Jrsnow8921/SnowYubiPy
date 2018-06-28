import sys
import time
import signal
import usb.core
from SnowCmd import *

class SnowYubi:

  def __init__(self, dv='Yubikey'):
    self.dv = dv

  def findYubi(self):
    try:
      dev = usb.core.find(find_all=True)
      x = True if any(self.dv in s for s in [self.dv for cfg in dev if self.dv in usb.util.get_string(cfg, cfg.iProduct)]) else False
    except:
      raise
    return x

  def plugin(self):
    while True:
      if self.findYubi() == True:
        SnowCmd().cmdOn()
        time.sleep(2)
        break

  def unplug(self):
    while True:
      if self.findYubi() == False:
        SnowCmd().cmdOff()
        time.sleep(2)
        break

  def run(self):
    try:
      while True:
        self.plugin()
        self.unplug()
    except KeyboardInterrupt:
      sys.exit(0)

SnowYubi().run()
