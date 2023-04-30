# Software Overview
This is intended to serve as an intensive guide to installing, configuring, and using our application development environment. Here you will find information on the application’s moving parts, as well as dependencies and installation environments. This application was intended to be a proof of concept- not a widespread release- for the existing SharkClean mobile app.

## Dev Information and Necessary Prerequisite Installations
For the machine designated as the mobile application server:
* npm version: 9.6.2
* body-parser version: 1.19.2
* common version: 0.2.5
* create-react-native-app version: 3.8.0
* expo-cli version: 6.3.2
* express version: 4.17.3
* fd version: 0.0.3
* firebase-tools version: 11.16.1
* fs version: 0.0.1-security
* http-server version: 14.1.0
* http version: 0.0.1-security
* path version: 0.12.7
* react-native-cli version: 2.0.1
* @babel/core version: 7.21.3
* @google-cloud/storage version: 6.9.4
* @react-native-async-storage/async-storage version: 1.17.11
* @react-native-firebase/app version: 17.4.1
* @react-native-firebase/storage version: 17.4.1
* @react-navigation/native-stack version: 6.9.12
* @react-navigation/native version: 6.1.6
* expo-camera version: 13.2.1
* expo-status-bar version: 1.4.4
* expo version: 48.0.7
* firebase version: 9.18.0
* react-native-dropdown-select-list version: 2.0.4
* react-native-safe-area-context version: 4.5.0
* react-native-screens version: 3.20.0
* react-native-tcp-socket version: 6.0.6
* react-native version: 0.71.6
* react-use-websocket version: 4.3.1
* react version: 18.2.0

For the Raspberry Pi Server:
* express version: 4.18.2
* react-native-tcp-socket version: 6.0.6
* ws version: 8.13.0
* Raspberry Pi OS (32 bit)

For the mobile device running the application:
* Expo Go version: 2.28.9

SharkNinja MQTT Client:
This library was created by SharkNinja for the sole use of Boston University Senior Design Team 28
This library cannot be published or redistributed
For source code, contact Team 28 or [Guy DiPietro](mailto:GDiPietro@sharkninja.com) at SharkNinja

## Software Module Overview
### photo-app/App.js
This module is the mobile application itself. It is comprised of a few different sections:
* Styling
* Home Screen
* Settings Screen
* Photo Capture Screen
* Photo Viewing Screen
* Main
#### Styling
Basic styling for buttons, containers, and screens. Matches the SharkNinja color scheme found on their official website.
#### Home Screen
Routes to the photo capture, settings, and photo viewer screens. Kills interval processes initialized on the photo capture screen.
#### Settings Screen
Enables the user to configure delay between photo captures, toggle the auto-capture feature, start and stop the robot, and see the status of the connection between the application and the Pi server. 
#### Camera Screen
Enables the user to switch between phone cameras, take photos, and navigate to the settings page. Kills previously running intervals before starting a new one. Captures settings using asynchronous storage (cache.) Uploads images to Firebase using image URI.
#### Photo View Screen
Pulls images from cloud storage, displays them.
#### Main
Establishes server connection, listens for messages from Pi. Initializes previously mentioned screens. Websocket URL is configured in this code. 
### photo-app/firebase_setup.js
Initializes Firebase configuration. Modification enables photos to be stored in different users’ cloud databases. 
### piServer/app.js
Establishes connection with mobile application using websockets. User specifies communication port in this code. Spawns and stops Python processes to be run on Pi. Spawns appropriate process based on message received from mobile application. 
### piServer/piCommunication.py
Sets `robot_ip` variable used to communicate with the robot. Starts photo capture routine and collision detection routine. 
### piServer/piCommunication.py
Sets `robot_ip` variable used to communicate with the robot. Docks robot using SharkNinja proprietary Python library.

## Dependency Flowchart
![image](https://user-images.githubusercontent.com/61120367/235377449-da75ec70-d3bd-4683-91ff-51496a81650d.png)

## Completing a Clean Installation
Installation for the SharkCam is straightforward, but has a few moving parts. 
### Installation for Machine Acting as Expo Server
1) If necessary, install npm, Expo CLI, and git
2) Clone the SharkCam_SeniorDesign repository
3) Navigate to the photo-app folder
4) Run `npm install` to install dependencies
5) Change the photo-app/App.js `WS_URL` variable to the IP address of your Pi and the port on which your Pi server is listening for packets.
    * *The format should look something like this:* `ws://<pi_ip_address:port>`
    * *The default port is 8080* 
7) Run `npx expo start` to launch the mobile application server- this allows the app to be run on a mobile device
### Installation on the Raspberry Pi Server
1) If necessary, install npm, Node, and git
2) Clone the SharkCam_SeniorDesign repository
3) Navigate to the piServer folder
4) Run `npm install` to install dependencies
5) Change the piServer/piCommunication.py `robot_ip` variable to that of your vacuum robot
6) Change the piServer/stopCommand.py `robot_ip` variable to that of your vacuum robot
7) (Optional) To change the port on which the Pi server is listening, modify the port specified in `server.listen()`
    * *The default port is 8080, and must match the port specified in photo-app/App.js*
8) Run `node app.js` to start the server
### Installation on Mobile Device
1) From the app store, install the Expo Go application
2) Follow application prompts
### Recommended start sequence
1) Pi server
2) Expo server
3) Expo Go

#### Note: All devices must be on the same network for expected application behavior

