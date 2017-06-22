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
2. Identify camera pinhole in middle box. Place gift set under the tree with a good view and near an outlet.
3. Plug in the gift set, monitor and accessories.

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

1. We’ll start with the hat. Using a seam ripper, gently remove about half an inch of the hat’s middle seam. Use a hat with a middle seam like a snapback, five panel or baseball cap. Gently remove about a half inch of the seam to create pinhole for the camera.
2. Center the nylon washer with a finger over the new pinhole.
Sew the washer in place. Sewing this pinhole in place is what allows the hat to remain covert. Secure it with a knot in the thread followed by looping over a couple times and knotting again.
3. Solder two wires to the slide switch. It’s time to solder! Be sure to check the GPIO map (below) for particulars on where to connect components and wires. Then solder two wires to the Slide switch.
4. Solder the other end of the wires to the PowerBoost. Connect the opposite ends of the same wires to the PowerBoost. Again refer to the GPIO map and be super careful to get the positive and negative connectors right.
5. Now, solder those wires to the Raspberry Pi. It makes sense that these two systems would need to interface with one another since the PowerBoost is what powers the raspberry Pi. It’s best to solder to the bottom of the board. See the GPIO map.
6. Plug the Lithium Ion battery into the PowerBoost.

Pushbutton and LED are optional but could be programmed as a shutdown button and recording indicator, respectively. If you decide to use these parts, you’ll need to add code for it the system to indicate recording or respond to the pushbutton.

7. OPTIONAL: Solder two wires to the 6mm slim button and two wires to the LED sequin. Reference the GPIO map for connection details.
8. OPTIONAL: Connect the button and the LED sequin to the Raspberry Pi. Reference the GPIO map for connection details.

9. Going back to the hat, align the camera with the pinhole and sew in place. Hold the camera module in place with your fingers and begin sewing through the module’s (yellow) corner circles. The camera module will probably shift a bit as it’s sewn so it’s important to check the pinhole intermittently.
10. Connect the camera ribbon cable. There is a specific up and down with the camera cable so be sure it is oriented properly. See image above.
11. Connect the other end of the ribbon cable to the Raspberry Pi and secure with kapton tape.
12. Sew the Raspberry Pi in place. This time instead of using the pinhole as a guide the camera module will be the guide. The kapton tape will ensure the ribbon will easily remain seated in place. Be sure to ribbon cable sits comfortable and isn’t pulling.
13. Tuck all other components into the hat.
14. Sew a lining around half the hat’s diameter. This will protect the hair and head but also make the hardware and SD card easily accessible.
15. Set up the SD card & insert it into the Raspberry Pi. Installation instructions can be found in the Open Lab Github Repository as well as best practices and troubleshooting steps. The instructional in Github runs through installation process for Raspbian as well as writing and running the python script.
16. Have fun! Go tell meaningful stories.
