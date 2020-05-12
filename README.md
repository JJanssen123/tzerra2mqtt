# tzerra2mqtt
Python script for reading Remeha Tzerra central heating boiler data and send the data as mqtt messages.
 
To use this script you need:
* a RS232 to TCP converter like <a target="_blank" href="https://nl.aliexpress.com/item/32807885568.html">this one</a>
* a ttl to RS232 converter like <a target="_blank" href="https://nl.aliexpress.com/item/4000055222836.html">this one</a>.

Put the ip-address of the RS232 to TCP converter in settings.py.

Connect the PC output of the heater to the ttl to RS232 converter using a RJ10/4P4C connector, for instance a cut in half telephone handset cable. Connect the ttl converter to the RS232 to TCP converter.

![rj10 in PC output]() ![cable to ttl converter]() ![ttl converter to TCP converter]()

You will need the Eclipse Paho MQTT Python client library, use pip for installation: **pip3 install paho-mqtt**

The script returns the current running values of the heater. All values are sent as an mqtt message to your mqtt broker. In settings.py you can set the brokers address, the topic and some other mqtt stuff.

The script is meant to run every minute (or 5) as a cronjob e.g. 

**\* \* \* \* \* /usr/bin/python3 /home/pi/tzerra2mqtt/tzerra2mqtt.py > /home/pi/tzerra2mqtt/cronlog.txt**
