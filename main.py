from gpiozero import MCP3008
from gpiozero import LED
from gpiozero.pins.lgpio import LGPIOFactory
import gpiozero.pins.lgpio
import lgpio
from time import sleep
from gpiozero import PWMLED
from gpiozero import Button

def __patched_init(self, chip=None):
    gpiozero.pins.lgpio.LGPIOFactory.__bases__[0].__init__(self)
    chip = 0
    self._handle = lgpio.gpiochip_open(chip)
    self._chip = chip
    self.pin_class = gpiozero.pins.lgpio.LGPIOPin

gpiozero.pins.lgpio.LGPIOFactory.__init__ = __patched_init
factory = LGPIOFactory()

# led = PWMLED(21, pin_factory=factory)
LO_plus = Button(16, pin_factory=factory)
LO_minuls = Button(20, pin_factory=factory)
output = MCP3008(0, pin_factory=factory)

while True:
    rate = -1 if LO_minuls.is_pressed else 1
    value = output.value * rate
    print(value)
    # led.blink(on_time=value, off_time=1 - value, n=1, background=False)
