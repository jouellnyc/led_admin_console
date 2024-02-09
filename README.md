# led_admin_console
Administrative Console for LEDs - (Stone Age Slack/Skype)

I had an idea about putting two Rpi Picos together so they could communicate wirelessly with each other without a 3rd party AP - just the 2 picos.

Having used ESP32-S3-Box's before as APs I figure it would be trivial.

Like many on the internet, it did not work [so well](https://forums.raspberrypi.com/viewtopic.php?t=363911)

Instead, I wired up 3 esp32s and used espnow. 

The goal was to have something to:
- Bring to work and have people marvel at
- Show children and watch their faces light up

The magic being if you hit the red button on ESP1 the red led on ESP32 turns on. Ditto for green and yellow.
Further magic is holding down the button plays the "Darth Vader March" 

If using at work it can be a "poor man's Slack/Skype" - share your status as green, yellow, or red (with or with DVM)...


 



