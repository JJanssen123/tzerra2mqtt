import paho.mqtt.publish as publish

from settings import *

for entity in mqtt_autodiscovery_config:
        type = mqtt_autodiscovery_config[entity]["type"]  
        t = (mqtt_hass_topic + '/' + type + '/' + device["name"] + '_' + device["model"] + '/' + entity + '/config').lower()
        m = ""

        print(t, m)
        publish.single(topic=t, payload=m, hostname=mqtt_broker, auth={'username':mqtt_username,'password':mqtt_password}, retain=False)   