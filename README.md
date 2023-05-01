# Welcome to SharkCam!

This library is intended to be used with a SharkNinja vacuum robot, and relies on the robot's autonomous navigation capabilities to run appropriately. Currently, the application can successfully start the robot, stop the robot, and take pictures at designated intervals. After they are captured, the pictures are stored in a cloud database and can be viewed from within the app. Users can choose to turn the "auto capture" feature on or off, and customize the delay between photo captures. 

## Quickstart
This guide assumes that you have all necessary prerequisites installed, and all necessary hardware. For a detailed installation guide, check the [README_SOFTWARE](/README_SOFTWARE.md) and [README_HARDWARE](/README_HARDWARE.md).

To start the Pi server:
Power on the Pi by single pressing the power button on the battery hat
Connect Raspberry Pi to the same network as the mobile application and Expo server
Navigate to the piServer folder
Run the command “node app.js”

To start the mobile application:
* Connect mobile device and device acting as the Expo server to the same network
* Open the Expo Go application on your mobile device
* From a terminal, navigate to the photo-app folder
* Run the command `npx expo start`
* Once connected to the server, run the application from Expo Go on your mobile device

After starting the Pi server and the mobile application, you should be able to capture photos and control the robot. Congrats!

## Gotchas and Things to Look Out For

This application was developed as a proof of concept for SharkNinja, and is not intended for widespread release. As such, it has a few quirks.

Given that we did not have access to the SharkNinja codebase, we took some liberties with hard coded variables and developed our application to have minimal setup from the terminal. Why? SharkNinja already has prompts to determine a user’s IP address, protocols for communication between a phone and the robot, etc. in their SharkClean app. If adopted, our mobile application would be merged with theirs, eliminating the need for user setup from the server side. As such, some of our code is hardware and/or network specific. 

Within the photo-app/App.js code is a variable called WS_URL. This is the web socket URL that corresponds to the server running on the Raspberry Pi. In order for communication to take place between the Pi and mobile app, WS_URL must be set to the IP address of the Pi. This address includes the port through which the Pi server is sending packets. 
The format of the address is as follows:
`ws://<pi_ip_address:port>`

Likewise, the port specified in `server.listen()` of piServer/app.js should be the same as that specified in the photo-app/App.js code.

Additionally, within the piServer/piCommunication.py file, the robot_ip variable must be set to the robot’s ip address.

One other “gotcha” of the app comes from the way in which photos are automatically captured. In order to have a process that runs consistently, an interval is called on the photo capture screen. Intervals, unlike other functions called, persist after the user navigates away from the screen. To prevent throwing an error, the interval must be killed once a new screen is accessed by the user. We solved this problem by saving the interval ID in cache, and having code to kill intervals on every screen. 

Finally, there’s the matter of calling threaded Python scripts from a Javascript application. Because the robot’s control library is written in Python, the application needs to be able to contact the Pi server and run appropriate scripts from the Pi. This problem was solved by spawning Python scripts on the Pi based on messages received from the mobile app. Sometimes the threaded scripts can act erratically. While we have not found a specific reason for this- the scripts acted as expected when not spawned from Javascript code- it’s worth noting that the current version of the software is stable. 

## Full System Block Diagram
![System Block Diagram (Pi version) v2-Full System drawio (6)](https://user-images.githubusercontent.com/34608438/235390114-d2704a3f-cf7b-40f4-b8b4-14cf80f19cf9.png)

