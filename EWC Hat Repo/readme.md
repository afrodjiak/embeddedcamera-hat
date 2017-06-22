## Overview
The wearable embedded camera is a cost efficient way to tell a story with video snippets. The snippets can be captured in one sitting or over the course of several days. The hardware is housed in baseball cap and can be worn on the head fairly comfortably. Wearable embedded camera allows a user to covertly record first person POV with by embedding the system into an accessory. It can be inconvenient or unsafe to record with a device in hand. Covert recording triggers
legal and ethical privacy concerns.

### Design Thinking
This project was created with the following questions in mind:
* What does sousveillance gear look like?
* How could a community organizer visually tell a story of an unjust police encounter?
* How does a first person POV impact a visual story?
* What is the potential for abuse of this tool and what can be done to curtail abuse?

### Hardware
The Raspberry Pi Zero drives this prototype. The Pi NoIR camera board is powered by the Raspberry Pi via camera cable. A PowerBoost 500 is used to power the rechargable lithium ion battery. The battery in turn, powers the Raspberry Pi. The PowerBoost has a standard micro USB to connect to an external power source.

### Known/Potential Issues

1. The code python script does not include code for the slide switch nor the LED light.

### Bill of Materials

* Raspberry Pi Zero
* Raspberry Pi NoIR Camera Board (8 megapixels)
* Raspberry Pi Zero Camera Cable
* Minimum 16gb micro SD card
* PowerBoost 500 Charger
* 500mAH/3.7v Lithium-Ion Polymer Battery
* 6mm Slim Tactile Pushbutton (optional)
* Breadboard-Friendly SPDT Slide Switch
* LED sequin (optional)
* Nylon washer
* Needle and thread (matching the other grommets in your hat)
* Soldering iron and wire

### Hardware Assembly

Creating the Hat Pinhole
1. Using a seam ripper, gently remove about half an inch of the hat’s middle seam. Use a hat with a middle seam like a snapback, five panel or baseball cap. Gently remove about a half inch of the seam to create pinhole for the camera.
2. Center the nylon washer with a finger over the new pinhole.
Sew the washer in place. Sewing this pinhole in place is what allows the hat to remain covert. Secure it with a knot in the thread followed by looping over a couple times and knotting again.

Setting up the PowerBoost
1. There are three legs on the slide switch. Cut off the right or left leg. Do not cut the middle leg.
2. Solder two wires to the remaining two legs.
3. Grab another two wires and solder them to the PowerBoost's EN and GR pins.
4. Now we'll need to connect this to the Raspberry Pi. Take two new wires and solder them to the negative and positive pins on the PowerBoost.
5. Solder the opposite wire ends to the PowerBoost. The positive wire will connect to 5V on Raspberry Pi. The negative wire will pin in to GND on Raspberry Pi. It’s best to solder to the bottom of the board.

OPTIONAL: Wiring the LED and Pushbutton
Pushbutton and LED are optional but could be programmed as a shutdown button and recording indicator, respectively. If you decide to use these parts, you’ll need to add code for it the system to indicate recording or respond to the pushbutton.
1. Solder two wires to the 6mm slim button and two wires to the LED sequin. Reference the GPIO map for connection details.
2. Connect the button and the LED sequin to the Raspberry Pi. Reference the GPIO map for connection details.

Sewing the Camera Module
1. Going back to the hat, align the camera with the pinhole and sew in place.
2. Hold the camera module in place with your fingers and begin sewing through the module’s (yellow) corner circles. The camera module will probably shift a bit as it’s sewn so it’s important to check the pinhole for alignment intermittently.
3. Connect the camera ribbon cable. There is a specific orientation of the cable so be sure it is oriented properly.
4. Connect the other end of the ribbon cable to the Raspberry Pi and secure with kapton tape.

Sewing the Raspberry Pi
1. Sew the Raspberry Pi to the top of the hat. The kapton tape will ensure the ribbon will easily remain seated in place. Be sure the ribbon cable rests comfortably along the top of the hat and isn’t pulling.
2. Tuck all other components into the hat.
3. Sew a lining around half the hat’s diameter. This will protect the hair and head but also make the hardware and SD card easily accessible.

Bringing it all together
1. Plug the lithium ion battery in to the Powerboost.
2. Charge the battery using a standard micro USB and an external power source.
3. With another computer, insert the SD card (with adapter) and install the Raspbian Jessie operating system using Ether.
4. Remove the SD card adapter and insert the SD card into the Raspberry Pi.
4. With an external monitor, wired keyboard, wired mouse and micro USB power cable connect all accessories then access the Raspberry Pi Zero desktop.
5. Open the Python application and copy/type the python code from this repository (mytimelapsehat.py)
6. File --> Run. You should see the code running.
