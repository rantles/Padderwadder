import board
import busio
import displayio
import adafruit_imageload
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Module
from kmk.modules.direct_pins import DirectPins
from kmk.modules.holdtap import HoldTap

# OLED setup
displayio.release_displays()
i2c = busio.I2C(board.D5, board.D4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(
display_bus,
width=128,
height=32,
)

def load_picture(filename):
bitmap, palette = adafruit_imageload.load(
filename,
bitmap=displayio.Bitmap,
palette=displayio.Palette,
)
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
return group

# load both pictures once when the macropad starts
pictures = [
load_picture("/image1.bmp"),
load_picture("/image2.bmp"),
]
display.root_group = pictures[0]

class PictureSwitcher(Module):
def __init__(self):
self.picture_number = 0

def process_key(self, keyboard, key, is_pressed, int_coord):
# swap picture only on the press not when the key is released
if is_pressed:
self.picture_number = 1 - self.picture_number
display.root_group = pictures[self.picture_number]
return key

# keymap
keyboard = KMKKeyboard()
holdtap = HoldTap()
keyboard.modules.append(holdtap)
keyboard.modules.append(
DirectPins(pins=(board.D10, board.D9, board.D8))
)
keyboard.modules.append(PictureSwitcher())

keyboard.keymap = [
[KC.Z,KC.HT(KC.SPC, KC.F2), KC.C]
]

if __name__ == "__main__":
keyboard.go()