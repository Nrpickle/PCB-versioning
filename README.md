This github repo parses my internal shorthand for recording issues with my PCBs and generates markdown to make it "pretty". Reference [www.nickmccomb.net/pcb](http://www.nickmccomb.net/pcb) for more documentation on the PCBs themselves. 

 Note that the "fixed" notation used in these messages reffers to something being fixed in the next version, and is moved to that category when the next version is being designed.
# Table of Contents 
* [Ocean Mixing Group](#ocean-mixing-group)
  * [EBox Auxillary](#ebox-auxillary)
    * [Version 1](#57072)
    * [Version 2](#41311)
    * [Version 2.1](#10859)
    * [Version 3](#90439)
  * [Iridium 9603 Breakout](#iridium-9603-breakout)
    * [Version 1](#7492)
  * [Low Voltage Disconnect](#low-voltage-disconnect)
    * [Version 1](#30945)
  * [Power Distribution Board](#power-distribution-board)
    * [Version 1](#86889)
    * [Version 2.1](#70525)
    * [Version 2.2](#62127)
    * [Version 2.3](#48273)
  * [ROSS Comms](#ross-comms)
    * [Version 1](#80809)
    * [Version 1.1](#36259)
  * [Science Serial Adapter](#science-serial-adapter)
    * [Version 1](#90163)
  * [XTend Daughterboard](#xtend-daughterboard)
    * [Version 1](#36089)
    * [Version 2](#16791)
    * [Version 3](#89994)
    * [Version 4](#9734)
* [Personal](#personal)
  * [LATCH](#latch)
    * [Version 1](#7989)

# Ocean Mixing Group
## EBox Auxillary
<a name="57072"></span>
### Version 1

#### Functional 
- Fuse the relays

#### Silkscreen 

#### Documentation 
- Change molex connector pinouts

### Fixed 
- Vin and agnd connected
- Need to add more test points!
- Add hall effect switches (d10 is down and d11 is up)
- D4 needs to be kill and d5 needs to be start (currently they are reversed)
- Change tx/rx directions on the molex serial connector
- Add serial number
- Www.digikey.com/product-detail/en/omron-electronics-inc-emc-div/g5le-1-e-dc5/z2616-nd/1277875
- Www.digikey.com/product-detail/en/cynergy-3/dat70515/725-1029-nd/752001
- Https://www.digikey.com/product-detail/en/alpha-omega-semiconductor-inc/ao3422/785-1015-1-nd/1855957

------------- 
<a name="41311"></span>
### Version 2

#### Functional 
- Fuse the relays?

#### Silkscreen 

#### Documentation 
- Change molex connector pinouts

### Fixed 
- Kill relay pads too small
- Mosfet drain/source backwards
- Reverse the ft2232 tx/rx labels to be more readable

------------- 
<a name="10859"></span>
### Version 2.1

#### Functional 
- Fuse the relays?
- Add llc to the esc pwm output?

#### Silkscreen 

#### Documentation 
- Change molex connector pinouts

### Fixed 

#### Functional 
- Gnd and voltage testpoints
- Reduce size of ft2232 pads
- Add strain gauge sensor

------------- 
<a name="90439"></span>
### Version 3

#### Functional 
- Add llc to the esc pwm output?
- Ensure traces are differentially routed for the usb datalines
- Fix ft2232 functionality
- Add sd card reader

#### Silkscreen 

#### Documentation 
- Change molex connector pinouts

### Fixed 

#### Functional 

------------- 
## Iridium 9603 Breakout
<a name="7492"></span>
### Version 1

#### Functional
- Power on/off should be connected to 5v not 3v3

------------- 
## Low Voltage Disconnect
<a name="30945"></span>
### Version 1

#### Issues
- C4 and c3 should be swapped, .1uf drain cap and 100uf between vin and gnd
- Vin cap's position cap needs to make sense, currently doesn't
- Non-optimal layout for q1
- Check layout for c3, needs to be directional and circular
- Test pads are labeled incorrectly (backwards)

------------- 
## Power Distribution Board
<a name="86889"></span>
### Version 1

#### Silkscreen 

#### Functional 
- Check j15 with external resource
- Add testing input ports
- Add reverse voltage protection?
- Oscillator test point
- Recompute values for voltage detection op amp
- Implement usb hub (296-43109-1-nd)

#### Component selection 
- C8 not on bom
- C9 not on bom
- R11, r12 not on bom
- C13 not on bom

#### Inventory 

#### Documentation 
- Molex connector pinout needs to be fixed on internal documentation (they are currently reversed)

### Fixed 

#### Silkscreen
- Make j27 more clear
- No versioning marks
- C13 label is obscured
- Label aux6 and aux7 servo ports as 5v
- R15 label is obscured
- J20 and c12 labels conflict
- C17 label is obscured
- Receiver is misspelt
- C4 is poorly labeled
- Led orientation dots need to be bigger (pcbway didn't print some of them)
- Red led is oriented opposite of green ones
- Fix oscillator footprint to comply with avr186 (done as much as i'm going to)
- Add ftdi breakout points (compatable with solderable in readers)
- Orientation marks for molex connectors (2 and 3 pin)

#### Functional
- Make large, multimeter gnd test point
- Add dip setting switch
- Remove q1
- Vias touch the crystal's case
- Add fusing for rear aux power (rearbattpower), we blew a fuse
- Relay pinout is incorrect (activate the diode with the uc)
- J27's polarity is reversed
- Add solder to 27 large mounting holes
- U8 pinout too large (about 2x)
- J15's pads were placed on the wrong side of the board (meaning they're reversed)
- Voltage sense system needs to change [need to accurately sense difference between 10 and 13 volts]
- Ftdi missing gnd on pin 7

#### Inventory
- R16 not on bom
- U5 not on bom
- Order more current sensors

------------- 
<a name="70525"></span>
### Version 2.1

#### Silkscreen 

#### Functional 

#### Component selection 

#### Inventory 

#### Documentation 

### Fixed 

#### Silkscreen
- Uusb port label needs to be moved slightly higher [are these even needed?]
- Serial number label
- Label opamp resistors with a dot for ease of soldering

#### Functional
- Route power through larger pads on the rear battery fuse
- Reset pin on ftdi chip should not be tied low
- Ensure usb connector pinout is correct (pdbv2.1 was flipped)
- Switching trace for 20v supply needs to be high power
- Replace separate ftdi chips with double
- Build in protection for the adc so it can't receive 20v (diodes!)
- Add 5v rail to voltage sense opamp
- Add test points for: temperature sensor, single current ic sense line
- Add smoothing capacitor on temperature sensor (<=1uf)
- Add auxiliary connection for raspi 5v/power the raspi using molex connector instead of usb
- Current going from ftdi device to rest of circuit? [this really won't be an issue, though, because the whole system will be on always]
- Add vertical usb connector: reference solidworks model of mounting plate for placement
- Replace 330uf capacitor with through hole.
- The opamp measuring the rear voltage needs a gnd reference to the rear battery
- - need to add a case if the rear battery isn't plugged in (as often happens), this could be a pull down resistor

#### Component selection
- C8 not on bom'
- C9 not on bom
- Replace3 tmp36 with smaller range tmp37 (20mv per deg c compared to 10mv per deg c) [this actually does not require any changes to the circuit]

#### Inventory
- Need more c4's
- Need more c8's (a lot)
- Reminders:
- Unshelve polygons
- 20v switching regulator needs to be grounded, dumbass

------------- 
<a name="62127"></span>
### Version 2.2

#### Silkscreen 

#### Functional 

#### Component selection 

#### Inventory 
- Need more 20v regulators
- Need more 1.07k resistors
- Need more 680 resistors
- Need more 10k resistors
- Need more 220 resistors
- Need more 2.7uf caps
- Need more 10uf caps
- Need more 4.7uf caps
- Need more 3.3uf caps
- Need more current sensors (u2, u3, u4, u9)
- Need more 10v shunts (u14)
- Need more u16

#### Documentation 

### Fixed 

#### Silkscreen
- Labels for xtend tx/rx
- Label for usb hub power supply
- Label for rpi power molex connector

#### Functional
- Remove 2.5v adc reference voltage's dependence from the 5v rail
- Remove adc protection (refactor?)
- Replace u8
- Connect a precision reference voltage (e.g. 10v through a resisitor divider into the adc void sendstringpc(const char stufftosend[]))
- Connect multiple, if possible?
- Make d14 level with the other leds
- Vin of 20v switching regulator needs to be connected

#### Component selection

#### Inventory
- Reminders:

------------- 
<a name="48273"></span>
### Version 2.3

#### Silkscreen 
- Label male and female xt60s to be explicit

#### Functional 
- Add post diode to midpower
- Slightly larger relay holes
- Ftdi usb connector flipped
- Current sense capacitor location

#### Component selection 

#### Inventory 

#### Documentation 

### Fixed 

#### Silkscreen

#### Functional

#### Component selection

#### Inventory

------------- 
## ROSS Comms
<a name="80809"></span>
### Version 1

#### Silk

#### Functional
- Add pull up/down resistor to xbee on/off line so that it only activates when the uc tells it to

### Fixed
- Rgb led needs 3v3 on the anode instead of gnd
- The iridium connector is backwards
- Move r2 silk3
- Add xtal silkscreen
- C1 doesn't have polarity marking
- Move c2 polarity marking
- C12/c17 via hole causes confusion
- Optional: add led output on xbee on/sleep output pin (by default apparently dio9)

------------- 
<a name="36259"></span>
### Version 1.1

#### Silk
- U7 label
- Make explicit c9, c10 orientation

#### Functional
- Add pull up/down resistor to xbee on/off line so that it only activates when the uc tells it to
- C3/c4 gnd traces need to be strengthened

#### Misc
- Make unnecessiarialy 0402 caps larger: c13, c14, c17, c20

### Fixed

------------- 
## Science Serial Adapter
<a name="90163"></span>
### Version 1

#### Silkscreen 

#### Functional 
- Rs232 capability
- Usb connector upside down
- Add "smart" capability?
- Doesn't work

#### Component selection 

#### Inventory 

#### Documentation 

### Fixed 

#### Silkscreen

#### Functional

#### Component selection

#### Inventory
- Reminders:

------------- 
## XTend Daughterboard
<a name="36089"></span>
### Version 1

#### Functional
- If barrel jack holes are not drilled, then v+ does not connect to vin

### Fixed
- Xtend footprint incorrect
- Df13 holes too small (should be .5 mm)
- Led footprint wrong
- If using barebones, increase ground plane clearance, for ease of soldering
- Barebones - barrel jack holes not drilled
- Inductor pads too close together (check that moving apart doesn't expose ground plane to pads, maybe only an outward widening of pads is required) #note, these are actually perfect, they just are meant to reflow. i widened the pads to enable hand-soldering

------------- 
<a name="16791"></span>
### Version 2

#### Potential changes 
- Use right angle header for mcu connection: http://www.digikey.com/product-detail/en/90136-2205/wm8206-nd/415812z

#### Issues 
- U4 (comparitor) completely wrong form factor [n/a]
- Increase size of 5vsw vias [n/a]
- Add clear label to px connector
- Pour ground plane

### Fixed  
- Barrel jack footprint wrong
- Label c1 orientation
- Add orientation lines to c2 and d4
- Change c1 orientation
- Fix current monitor
- Extend gnd plane under
- Change r5 value (rssi resistor) to 60-100 ohms
- Increase size of aux holes, slightly

------------- 
<a name="89994"></span>
### Version 3

#### Silkscreen 

#### Connectors 
- Switch to df13's that can solder to the board (e.g. the ones the pixhawk uses)

#### Functional 

#### Documentation 
- Molex connector pinout needs to be fixed on internal documentation (they are currently reversed)

### Fixed 
- Max voltage input is actually 16v (limited by the barrel jack)
- Dot for u1
- Di pin was not routed to the molex connector
- C1 c2 labels need to rotate -90
- Many "0 width" labels got printed and should be removed (test points, mounting holes)
- Label mcu pin 1

#### # denied #
- Add temperature sensor under the xtend? [no, because there is no uc on the ebox version, and we don't care about the temp of the xtend on the ground station]

------------- 
<a name="9734"></span>
### Version 4

#### Functional 
- Oscillator pads were tented (ordered from df robot)

#### Silkscreen 
- Tx/rx pairs are backwards. this is down to the label on the schemaitc, and therefore is backwards on the board

------------- 
# Personal
## LATCH
<a name="7989"></span>
### Version 1

#### Functional
- Ws2812 footprint totes wrong

------------- 
