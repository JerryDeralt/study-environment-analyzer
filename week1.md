# Week 1

## Goals
- Learn DS18B20 protocols
- Read DS18B20

## What I Learned
![wiring according to manufacturer; after testing using voltmeter there's no faults.](<DS18B20 wiring.png>)
- `DQ` = data output. in reality it's just a node that allows the GPIO to measure voltage at that point relative to GND.
- DQ is connected to VCC via a resistor and is wired to GND via a transistor (essentially a switch) that creates open circuit by default. This means DQ's default reading (measured by the GPIO) is 3.3V.
    - the resistor is called a `pull-up` resistor, because it essentially pulls DQ to 3.3V (up).
- DS18B20 is able to turn on the transistor, closing the switch and allowing current flow to cause a voltage drop thanks to the resistor. DQ now reads 0V.
    - DQ is being `pulled-down` because it's being connected to GND.