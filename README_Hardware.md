# Setup
These are setup steps that a user would complete to set up the SharkCam.
## Installing semi-permanent base
* Remove covering from one side of 3M VHB adhesive pad
* Place onto Shark vacuum robot’s LIDAR dome and press firmly for ~30s
* Remove covering from other side of adhesive and press semi-permanent base onto adhesive
This base can remain on the robot at all times, but due can be removed if desired thanks to the adhesive connection.
## Installing from storage configuration
* Connect electronics bay to semi-permanent base with four hex screws and allen key
* Screw column assembly into the threads in the top of electronics bay
* Extend each column section one at a time
* Turn collar counterclockwise to loosen section
* Adjust height and turn collar clockwise to lock in the height
* Plug coiled motor cable into receptacle at top 
## Starting and charging Raspberry Pi
* To start Pi use cutout in side of electronics bay to press battery hat’s power button
* Double press to put into standby mode (hat will also enter standby automatically if Pi shuts down)
* Battery can be charged with Micro USB or quick-charged with USB-C 
   * Note: power is briefly interrupted when charger is connected


# Bill of Materials
| **Description**             | **Part #**   | **Vendor**   | **Quantity** |
|-----------------------------|--------------|--------------|--------------|
| Telescoping Rod             | TBASB1       | Testrite     | 1            |
| Electronics Bay             | WA-37F*16    | Polycase     | 1            |
| Ball Bearing                | 60355K504    | McMasterCarr | 1            |
| Threaded Rod                | N/A          | N/A          | 1            |
| Top Plate                   | 1221T75      | McMasterCarr | 1            |
| Electronics bay cover plate | 8702K94      | McMasterCarr | 1            |
| Motor assy base             | N/A          | N/A          | 1            |
| Semi-permanent base         |lo 85705K19     | McMasterCarr | 1            |
| Aluminum Bearing Support    | N/A          | N/A          | 1            |
| 3D Printed Bearing Holder   | N/A          | N/A          | 1            |
| Stepper motor/driver        | 105990072    | Seeed Studio | 1            |
| Phone Clamp                 | BGMCLAMP     | Adorama      | 1            |
| ToF Sensor                  | 5396         | Adafruit     | 1            |
| Raspberry Pi 3A+            | 1690-1028-ND | DigiKey      | 1            |
| RJ12 6p6c Cable Adapter     | B0859YJ6H4   | Amazon       | 1            |
| 6P6C-UP Wire                | B098TPD49Q   | Amazon       | 1            |




## Mechanical
![image](https://user-images.githubusercontent.com/34608438/235392819-4982bd35-0207-4108-9f9b-d25952738635.png)
  
[Onshape with full CAD assembly](https://cad.onshape.com/documents/72bd84211218be25cda16cd9/w/d1a0387baf2ac60499442a3a/e/67e9507cb4eb0b0e9976e29f)


### Semi-permanent base
* Acrylic plate attached to top of Shark robot’s LIDAR dome with 3M VHB tape 
![_DSC5762](https://user-images.githubusercontent.com/34608438/235392935-653eede9-f1bd-415d-aca1-50a364974345.jpg)


### Electronics bay
Polycase ABS Enclosure
[Product page](https://www.polycase.com/wa-37f)
* Attaches to semi-permanent base with four hex screws
* Acrylic plate attached to box lid with 3M VHB adhesive
   * Four clearance holes with Phillips screws to secure lid of box
   * 3D printed mount for ToF sensor
   * Threaded hole in center for column attachment
   * Receptacle for coiled motor cable plug


### Telescoping column
Testrite 55” Aluminum telescopic tube assembly
[Product page](https://www.testritealuminum.com/products/tbasb1)
* Custom machined threaded (1-12 threads) collar is press-fit onto base of column allowing it to thread into the top of the electronics bay


### Motor assembly
This assembly contains the housing for the stepper motor that rotates the phone mount        
#### Base
* Custom machined aluminum base, tapped to thread into existing 1/8" pipe thread at top section of column
* Four threaded holes (two at a time used) to secure motor housing
#### Housing
3D printed housing 
#### Bearing + bearing support
* McMasterCarr bearing secured with 3D printed top mount and aluminum bottom support
* [Bearing product page](https://www.mcmaster.com/60355K504/)
![_DSC5710](https://user-images.githubusercontent.com/34608438/235392978-8b8ca10b-7249-4532-b5af-fc5cc9e8bc2c.jpg)


#### Shaft
* Custom machined aluminum shaft with flat side
* Clearance hole on flat for connection to phone clamp
* Tapped at top for connection to top plate
* Secured to motor shaft with set screw


## Phone mount
Manfrotto Universal Smartphone Clamp with ¼ thread connections
[Product page](https://www.adorama.com/bgmclamp.html)
* Attached to shaft with knurled screw threaded into female threads of clamp
![_DSC5718](https://user-images.githubusercontent.com/34608438/235393028-cade18b5-961a-40b0-9bd5-e87d459c68cf.jpg)


## Top plate
* [Product page](https://www.mcmaster.com/1221T75/)
* 11.75 diameter acrylic plate
* Used as target for distance sensor, forming light curtain between sensor and plate for obstacle detection
* White paper attached to bottom to improve sensor performance
* Attached to top of shaft with knurled screw


## Electrical


### ToF sensor
Adafruit VL53L4CD Time of Flight Distance Sensor
[Product page](https://www.adafruit.com/product/5396)
[Wiki](https://learn.adafruit.com/adafruit-vl53l4cd-time-of-flight-distance-sensor)
* Range: 1-1300mm
* Accepts 3-5V
* Draws around 20mA
Chosen for affordability, narrow cone of detection, large range, and Python library

![_DSC5717](https://user-images.githubusercontent.com/34608438/235393038-9e8dcbb9-4d65-4740-8dc7-2c7db4b29fe3.jpg)



### Battery Hat
Waveshare Li-polymer Battery HAT
[Product page](https://www.waveshare.com/li-polymer-battery-hat.htm)
[Wiki](https://www.waveshare.com/wiki/Li-polymer_Battery_HAT)
* Output voltage: 5V
* Capacity 3000mA at 3.7V
* Battery life under zero load: 5 hours
* Battery life under our design (expected): 2.0 hours 
* Powers Pi over GPIO
* Powers motor using USB A power rail
Chosen for user friendliness and multiple input/output power ports

![_DSC5777](https://user-images.githubusercontent.com/34608438/235393048-40681a74-618d-4512-9e30-df1fd62a8ce0.jpg)



### Raspberry Pi 3 Model A+
[Vendor page](https://www.digikey.com/en/products/detail/raspberry-pi/RASPBERRY-PI-3-A/9760878)
* RAM: 512 MB
* Input power: 5V
* Consume around 2W
Chosen due to availability, fast processor, and built-in Wifi


### Stepper motor and driver
[Product page](https://www.seeedstudio.com/Gear-Stepper-Motor-Driver-Pack-p-3200.html)
[Wiki](https://wiki.seeedstudio.com/Gear_Stepper_Motor_Driver_Pack/)
Seed Studio Gear Stepper Motor Driver Pack
* 1/64 gear ratio
* 5V input
* Draws 120mA at max operation


### 6P6C coiled telephone cable
* Coiled length: 1.3 feet (40 cm)
* Uncoiled length: 10 feet (300 cm)
* 6 input/output pins


## Power requirements 
### Battery hat power calculation 
Given battery capacity of 3000mA at 3.7V
Energy = 3Ah * 3.7V = 11.1Wh




### Power consumption of the circuit
| Component      | Voltage (V) | Current (mA) | Power(W) |
|----------------|-------------|--------------|----------|
| Stepper motor  | 5           | 120          | 0.6      |
| Tof sensor     | 3.3         | 20           | 0.066    |
| Pi 3 A+ w/wifi | n/a         | n/a          | 1.7      |
Power consumption is 0.6 + 0.066 + 1.7 = 2.366W


### Operating time of the design
Estimated Theoretical Operating time = 11.1Wh / 2.666W = 4.7 hours


## Wiring
Add the hat on top of the raspberry pi, connect the motor driver to the physical pins 18, 27, 22, 23 of the pi and connect the stepper motor to the driver using the 6P6C coiled telephone cable. This cable goes along the telescoping pole . For the time of flight sensor, wire the Vin, gnd, scl and sda pins to their pi equivalent.


## Electrical components Set Up
![image](https://user-images.githubusercontent.com/34608438/235393074-b72ec778-2081-460a-b0fa-b153cd228e0e.png)
  



### Pin used on the Pi
| Board Pin numbers | Usage             |
|-------------------|-------------------|
| SDA               | Tof i2c           |
| SCL               | Tof i2c           |
| GPIO 12           | Motor driver pin1 |
| GPIO 13           | Motor driver pin2 |
| GPIO 15           | Motor driver pin3 |
| GPIO 16           | Motor driver pin4 |


# Circuit Schematic
![image](https://user-images.githubusercontent.com/34608438/235393114-e1e31277-5c50-41d7-9e5f-9835601d015e.png)
