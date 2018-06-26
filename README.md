This github repo parses my internal shorthand for recording issues with my PCBs and generates markdown to make it "pretty". Reference [www.nickmccomb.net/pcb](http://www.nickmccomb.net/pcb) for more documentation on the PCBs themselves. 

 Note that the "fixed" notation used in these messages refers to something being fixed in the next version, and is moved to that category when the next version is being designed.
# Table of Contents 
* [OSU Robotics Club](#osu-robotics-club)
  * [Drawer Sensing PCB](#drawer-sensing-pcb)
    * [Version 1](#69055)
  * [Iris](#iris)
    * [Version 1](#64999)
    * [Version 2](#13473)
  * [Motor Node](#motor-node)
    * [Version 1](#57148)
  * [Part Sensing PCB](#part-sensing-pcb)
    * [Version 1](#34491)
* [Ocean Mixing Group](#ocean-mixing-group)
  * [EBox Auxillary](#ebox-auxillary)
    * [Version 1](#25056)
    * [Version 2](#97517)
    * [Version 2.1](#68202)
    * [Version 3](#62434)
  * [Iridium 9603 Breakout](#iridium-9603-breakout)
    * [Version 1](#56109)
  * [Low Voltage Disconnect](#low-voltage-disconnect)
    * [Version 1](#87710)
  * [Power Distribution Board](#power-distribution-board)
    * [Version 1](#33173)
    * [Version 2.1](#65967)
    * [Version 2.2](#65157)
    * [Version 2.3](#64498)
  * [ROSS Comms](#ross-comms)
    * [Version 1](#16206)
    * [Version 1.1](#37841)
  * [Science Serial Adapter](#science-serial-adapter)
    * [Version 1](#27036)
  * [XTend Daughterboard](#xtend-daughterboard)
    * [Version 1](#36916)
    * [Version 2](#97692)
    * [Version 3](#76090)
    * [Version 4](#6946)
* [Personal](#personal)
  * [LATCH](#latch)
    * [Version 1](#26829)

# OSU Robotics Club
## Drawer Sensing PCB
<a name="69055"></span>
### Version 1

#### Functional
- J2 pinout incorrect (needs to be swizzled)

------------- 
## Iris
<a name="64999"></span>
### Version 1

#### Silkscreen 
- No serial number spot on silkscreen
- No modbus id number spot on silkscreen

#### Functional 
- Used can tx/rx instead of hardware uart
- Connections from ftdi to rs485 transceiver wrong, need to short de / re pins together, then this connection goes to ftdi enable. pwren for the rs485 converted is wrong naming and doesn’t reflect its purpose. no connection to pwren on 4232 needed...
- Likely that this should use a high-speed usb hub instead of the current full-speed implementation. it is easy, without deliberate planning, to hit the bottleneck of the usb hub.
- No invert needed for s.bus connection (bridge pins)
- Missing 3v3 rail connection to vbat pin on teensy. will program without it, but will not boot without it.
- Remove gnd connection for rs485 going out of the board (to ensure reverse protection downstream)

#### Component selection 
- For r46 vs r47 selection, only r47 is needed.

#### Inventory 

#### Documentation 

------------- 
<a name="13473"></span>
### Version 2

#### Silkscreen 
- U87 pin 1 silkscreen dot not visible
- R1 silkscreen not visible

#### Functional 

#### Component selection 

#### Inventory 

#### Documentation 

------------- 
## Motor Node
<a name="57148"></span>
### Version 1

#### Silkscreen 

#### Functional 
- Missing 3v3 rail connection to vbat on teensy. will program without it, but will not boot without it. connect vbat (pin 21) to the 3v3 side of c12 (closest to the xtal)
- Mcu mistakenly connected to the 5vsys, needs to be connected to the 3v3 net (as there is no 5v net on this board)
- Rgb led missing 3v3 anode connection. currently connected to non-present 5vsys net.

#### Component selection 
- Switching regulator that was purchased is not compatible with the design. a pin-compatible new one was specc'd and ordered, it is included in the bom as "alternative" parts. only u1, l1, c2, and r1 are changed. an 1n4148 diode also needs to be added per lt1933's datasheet. see schematic: https://raw.githubusercontent.com/osuroboticsclub/rover20172018/master/electrical/documents/nodes/files/motorv1bodge1.jpg

#### Inventory 

#### Documentation 

------------- 
## Part Sensing PCB
<a name="34491"></span>
### Version 1

#### Functional
- Needs to change to actual multiplexing ic
- Need to add the same connectors as the drawer sensing pcb

------------- 
# Ocean Mixing Group
## EBox Auxillary
<a name="25056"></span>
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
<a name="97517"></span>
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
<a name="68202"></span>
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
<a name="62434"></span>
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
<a name="56109"></span>
### Version 1

#### Functional
- Power on/off should be connected to 5v not 3v3

------------- 
## Low Voltage Disconnect
<a name="87710"></span>
### Version 1

#### Issues
- C4 and c3 should be swapped, .1uf drain cap and 100uf between vin and gnd
- Vin cap's position cap needs to make sense, currently doesn't
- Non-optimal layout for q1
- Check layout for c3, needs to be directional and circular
- Test pads are labeled incorrectly (backwards)

------------- 
## Power Distribution Board
<a name="33173"></span>
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
<a name="65967"></span>
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
<a name="65157"></span>
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
<a name="64498"></span>
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
<a name="16206"></span>
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
<a name="37841"></span>
### Version 1.1

#### Silk
- U7 label missing
- Make explicit c9, c10 orientation

#### Functional
- Add pull up/down resistor to xbee on/off line so that it only activates when the uc tells it to
- C3/c4 gnd traces need to be strengthened
- Add more reliable power connector

#### Misc
- Make unnecessiarialy 0402 caps larger: c13, c14, c17, c20

### Fixed

------------- 
## Science Serial Adapter
<a name="27036"></span>
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
<a name="36916"></span>
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
<a name="97692"></span>
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
<a name="76090"></span>
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
<a name="6946"></span>
### Version 4

#### Functional 
- Oscillator pads were tented (ordered from df robot)

#### Silkscreen 
- Tx/rx pairs are backwards. this is down to the label on the schemaitc, and therefore is backwards on the board

------------- 
# Personal
## LATCH
<a name="26829"></span>
### Version 1

#### Functional
- Ws2812 footprint totes wrong

------------- 
