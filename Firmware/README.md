# padderwadder

A macropad featuring an OLED and Rotary Encoder

* Keyboard Maintainer: [Allyssa Kho](https://github.com/rantles)
* Hardware Supported: Padderwadder PCB, XIAO RP2040
* Hardware Availability: [Hardware](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html)

Make example for this keyboard (after setting up your build environment):

    make padwad:default

Flashing example for this keyboard:

    make padwad:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions]

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
