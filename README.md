# daynight
Dynamically-updating day/night cycle LED driver for the RaspberryPi using the [Sunset-Sunrise API](http://sunrise-sunset.org/api)

## Overview
daynight runs as a daemon thread on a Raspberry Pi and periodically updates local times for sunset, sunrise, and nautical twilight using the Sunset-Sunrise API.
During nautical twilight (after sunset until before dawn), attached LEDs will be driven dark blue at a variable brightness.
During day time, the LEDs are set to light blue.
As twilight ends, LEDs will transition from twilight dark blue through a sunrise color pallete through sunrise until they arrive at their day time light blue.
When sunset begins, they are driven from day time blue through a sunset pallete to night time dark blue as twilight begins.

## Status
Currently working on the daemon fundamentals.

Todo:
- Test time updates
- Implement easy file-based configuration
- Implement LED driver
- Define sunrise and sunset color palletes
- Implement sunrise and sunset sequences
- Browser front-end???
