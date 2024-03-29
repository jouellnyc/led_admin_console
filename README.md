# led_admin_console

**Administrative Console for LEDs - (Stone Age Slack/Skype)**

I had an idea about putting two Rpi Picos together so they could communicate wirelessly with each other without a 3rd party AP - just the 2 picos.

Having used ESP32-S3-Box's before as APs I figure it would be trivial.

Like many on the internet, it did not work [so well](https://forums.raspberrypi.com/viewtopic.php?t=363911).

Instead, I wired up 3 esp32s and used espnow. 

The goal was to have something to:
- Bring to work and have people marvel at
- Show children and watch their faces light up
- Sell to VCs for millions of dollars

The magic being if you hit the red button on ESP1 the red led on ESP32 turns on. Ditto for green and yellow.
Further magic is holding down the button plays the "Darth Vader March" 

If using at work it can be a "poor man's Slack/Skype" - share your status as green, yellow, or red (with or with DVM)...

![Esp32s](/images/PXL_20240126_035208295.jpg)


You are free to modify the code and placement, here's how the pic is setup:

**Connections**

| GPIO Pin | Connection|
| -------- | --------- |
| GPIO 27  | Yellow LED|
| GPIO 14  | Green  LED|
| GPIO 32  | Red n  LED|
| GPIO 18  | Yellow Button |
| GPIO 22  | Green  Button |
| GPIO 15  | Red    Button |
| GPIO  4  | Slider for Red Button (DVM on/off) |

- Standard LEDs - 220-440 Ohms  should be fine for resistors.
- [Premium RGY Buttons](https://www.amazon.com/gp/product/B01E38OS7K)
- Piezo buzzer - anywhere electronics are sold 
- Slide switch is just a simple slide switch, [Premium Slide Switches](https://www.amazon.com/gp/product/B0BCK9JDWY/)

ESP32's tend to vary in terms of their pin placement.

**Install**
- Upload everything except /images to / in Thonny/IDE
- updated peers.py with the mac address of the opposite esp32:
    
  Find it like this: `import mac` from the REPL
- reboot

