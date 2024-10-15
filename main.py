import sys
import struct
import numpy as np
from threading import Timer
from gpiozero import MCP3008
from gpiozero import LED
from gpiozero.pins.lgpio import LGPIOFactory
import gpiozero.pins.lgpio
import lgpio
from gpiozero import Button


def __patched_init(self, chip=None):
    gpiozero.pins.lgpio.LGPIOFactory.__bases__[0].__init__(self)
    chip = 0
    self._handle = lgpio.gpiochip_open(chip)
    self._chip = chip
    self.pin_class = gpiozero.pins.lgpio.LGPIOPin

gpiozero.pins.lgpio.LGPIOFactory.__init__ = __patched_init
factory = LGPIOFactory()

LO_plus = Button(16, pin_factory=factory)
LO_minuls = Button(20, pin_factory=factory)
output = MCP3008(0, pin_factory=factory)

fl = 4
chunk_len = 1024

def main ():
  chunks = np.zeros(chunk_len)
  counts = 0
  r = Timer(0.1, lambda x: print('----->', counts), '1')
  r.start()  
  while True:
      rate = -1 if LO_minuls.is_pressed else 1
      value = output.value * rate
      chunks = np.append(chunks[1:len(chunks)], value)
      counts = counts + 1

      sys.stdout.buffer.flush()
      for v in chunks:
        sys.stdout.buffer.write(struct.pack("f", v))
    
main()
