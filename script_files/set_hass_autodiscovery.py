import paho.mqtt.publish as publish
import json
from settings import *

for entity in mqtt_autodiscovery_config:
    type = mqtt_autodiscovery_config[entity]["type"]    
    topic = (mqtt_hass_topic + '/' + type + '/' + device["model"] + '_' + device["name"] + '/' + entity + '/config').lower()
    
    message = mqtt_autodiscovery_config[entity]["config"]    
    message["name"] = entity
    message["unique_id"] = device["model"] + "_" + device["name"] + "_" + entity
    message["state_topic"] = (mqtt_base_topic + "/" + device["model"] + "/" + device["name"]).lower()
    message["device"] = device
    print(topic)
    publish.single(topic=topic, payload=json.dumps(message), hostname=mqtt_broker, auth={'username':mqtt_username,'password':mqtt_password}, retain=True) 
   

