[ROSE][#ROSE]
# ROSE
## EBox Auxillary
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
## Power Distribution Board
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
