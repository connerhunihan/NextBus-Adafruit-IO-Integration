# NextBus API Integration with AdafruitIO Dashboard
This program sends data from the NextBus API (https://gist.github.com/grantland/7cf4097dd9cdf0dfed14) into an Adafruit IO dashboard, which can then be used by an Arduino setup (https://github.com/connerhunihan/NextBus-AdafruitIO-Arduino-Integration) to create a light display that countdowns the minutes until your next bus arrives. 

## Prerequisites
Adafruit_IO==1.1.0
https://github.com/adafruit/io-client-python

## Deployment
Deployed at https://arcane-temple-62084.herokuapp.com/

## Acknowledgments
Thank you to 5un, dylan-fox, redspruce, and anupandey (https://github.com/5un, https://github.com/dylan-fox, https://github.com/redspruce, https://github.com/anupandey) for your work creating an easy-to-use Python NextBusAPI.

Also, a special thanks to the group that put together the Python client for use with io.adafruit.com
https://github.com/adafruit/io-client-python
