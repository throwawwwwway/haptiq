# Update wifishield

## Info

Some wifishields are not updated and they will **not operate properly** with Arduino software.
This document is to provide quick guidance for **OSX plateforms**.

[Source](http://katrinaeg.com/arduino-wifi-firmware-upgrade.html)

## Guidance

- [Install dfu-programmer](http://dfu-programmer.github.io/) OR 

>	brew install dfu-programmer

- Detach the wifishield from the arduino, place the jumper like [this](http://katrinaeg.com/images/arduino/arduino-wifi-jumper.jpg) and connect with USB cable to the computer

- Download latest version of Arduino on github:

>	git clone --depth=1 https://github.com/arduino/Arduino

- Make your current directory at arduino/hardware/arduino/avr/firmwares/wifishield/scripts
*the structure might change, but it should be around hardware and wifishield*

- Execute the script to upgrade

>	sudo sh ./ArduinoWifiShield_upgrade_mac.sh -a Applications/Arduino.app/Contents/Java/ -f shield

- Should get something like this:

>		       Arduino WiFi Shield upgrade
>		=========================================
>		Disclaimer: to access to the USB devices correctly, the dfu-programmer
>		needs to be used as root. Run this script as root.
>
>		****Upgrade WiFi Shield firmware****
>
>		Validating...
>		257254 bytes used (101.30%)
>
>		Done. Remove the J3 jumper and press the RESET button on the shield.
>		Thank you!

- Replace jumper and press the reset button 1-3 seconds, disconnect

- Check if version is >= 1.1.0 with following program:

>		#include <WiFi.h>
>
>		void setup() {
>		  Serial.begin(9600);
>		  Serial.println("the version is: ");
>		  Serial.println(WiFi.firmwareVersion());
>		}
>
>		void loop() {
>		}
