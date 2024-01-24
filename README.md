# GTA-S4DS-KnowCode-24
Team : GTA , Project : HealthyBand  - S4DS-KnowCode Hackathon : kjsieit College


# Idea is Product name : HealthyBand

its wearable, light weight and less costly... 

which has sensors like:
- Heart Pulse Sensor
- Pulse Oximeter Heart Rate sensor
- MPU6050 : Gyro Scopic Sensor : for body movement , sleep mode detection, etc

extra hardware:
- ESP32 : IoT Board
- Battery Li-ion 3.7V, 2500 mH
- 3 push to ON buttons
- Oled : 1.3 Inch , 128x64 Size

for this prototype product we will cover our product for good product interface  

its actions:
- measure the sensor data then upload on Django Server 
    (in encrypted form)
- also does edge computing
- display the sensor readings on Oled
- if any health parameter is above threshold level (means in alert range)
    then make a alert notifiaction to the docter appointed (if that doctor is busy then next doctor which has less schedules and the nearest
- it gives notification for mediaction which medicine with QTY and time
- tracking daily activity : (suggest some use of this feature)
- sleep tracking and sleep time notification
- remote patient monitoring
- every data will be stored on server in encrypted form and can be visiable on iteractive dashboard for real time insights 
- make some prediction on the data collected and giving recommendation on it or any prediction on it.
-This information can be made avaliable to doctors and medical institutes if the user consensts for diagnosis and or research purposes




# Task Distribution:



### Shaun Part: (rank this tasks according to revelence)
- find best and low compute(moderate) encrypt algo for hardware(ESP32)
- ML Model for health alert detection in advance
- alert threshold level for every sensative parameter
- track daily activity and suggest healthy schedule 
- sleep tracking and healthy sleep timing notification

- try to add more revelent ml algo on collected data from the patient for hackathon

NOTE : for every ml model create a folder in repo under ml section

and for every ml model save the model and the feature name 
also save the inference code for the same saved model (Load, test, predict)



### Sahil Part:
- circuit connection (main Task)
- research on current technology for our project
- compare the branded band and our HealthyBand with 20 points (create a compare table)
- create a Privacy Policy for EHR
- project bullet points ruled paper for Judges(info, description, etc)


### Atharva Part:
- Django Server:(deploy it on Replit Server) (responsive Web-App - [Desktop + Mobile : View])
	- unique-api-token
	- device-token
	- sensor api
	- save the data in encryped form (only for sensative data)
	- view with (public / login cred)
	- access control to the data : doctor, patient, nurse, etc
	- (single Page) : 
		- insights of the patient 
		- sleep track graph
		- medication input form : medicine , qty, description, time, dates/week/month
		- heart rate per day

	- fault tolerance : ... need to decide (Main Role : how reliable our system is ?)

	- notification page : medicine, checkup remainder, etc

	- consensts : for sharing the information with ORG,etc


	- EHR Data Exchange Wall: (make UI similar to Kaggle)
		- rules : encryption, add redenduncy, add noise, etc
		- file format
		- file description:size, no. columns, no. rows, datatype of the columns, 
			and some EDA on it in advance
		- Privacy Policy : how to use it and where to use it, etc
		- for this prototype NO Pay-Wall

- Product Designing:
	- build a proto-type case for the HealthyBand



# Need to Carry Things:

### General Things:
- Toothbrush, toothpaste, and any other personal hygiene items
- water bottle
- some food (snacks)
- cloths : jacket, etc
- 1 book , 1 pen, 1 pencil
- College Id, Addhar Card
- Personal Medications...
- Project Branding Materials: If applicable, bring logos, banners, or any other materials that represent your project.


### Tech Things:
- Laptop + Charger
- headphone / headset
- mobile charger, extention board, Mic


### Project Items:
- ESP32
- Oled
- Heart Rate Sensor
- Li-ion Battery + Charger Chip
- lipo battery
- 3 Push to ON button
- 3 leds : red, green, blue
- MPU6050
- CardBoard, Super Glue, cotton, 
- Dotted PCB, Rainbow wires, soldering Machine, melting wire, tool kit
- band structur of cloth etc
- slide switch ON/OFF