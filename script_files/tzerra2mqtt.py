#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3 as published by
#    the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details. <http://www.gnu.org/licenses/>.
#
#    Written in 2012 by Jorg Janssen <http://www.zonnigdruten.nl/>

import socket
import paho.mqtt.publish as publish
import json
from rc_comm import *
from settings import *

params_used = dict({'Status': 0,
    'Substatus': 0,    
    'ModulaireWarmtevraag': 0,    
    'AUWarmtevraag': 0,
    'WWWarmtevraag': 0,        
    'CVSetpoint': 0,        
    'WWSetpoint': 0,
    'InternSetpoint': 0,
    'RegelTemp': 0,    
    'AanvoerTemp': 0,
    'RetourTemp': 0,        
    'AutomaatTemp': 0,            
    'GewenstVermogen': 0,                
    'BeschikbaarVermogen': 0,
    'GeleverdVermogen': 0,
    'Gasklep': 0,
    'Ontsteking': 0,
    'Ionisatie': 0,
    'Ionisatiestroom': 0,
    'Pomp': 0,    
    'PompPercentage': 0,
    'Driewegklep': 0,
    'Tapdebiet': 0,            
    'VentilatorToeren': 0,            
    'WWComfort': 0})

# BEGIN PROGRAM ----------------------------------------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
s.settimeout(1)

try:
    s.connect((TCP_IP, TCP_PORT)) # connect to tcp-converter
except:
    Debug("Unable to connect to tcp converter -  " + str(sys.exc_info()[0]), 1)
    # quit
else:
    # "flush":print
    while (1):
        try:
            chunk = s.recv(1) # block untill timeout
        except:
            break
    # send the  command
    rq = Request()
    rq.send(s)
    response = Read(s)

    if response:
        for Key,Value in params_used.items():
            params_used[Key] = response.values[Key]
        
        # mqtt publish    
        mqttstring = json.dumps(params_used) 
        try:
            publish.single(topic=mqtt_topic, payload=mqttstring, hostname=mqtt_broker, auth={'username':mqtt_username,'password':mqtt_password}, retain=True)
        except:
            Debug('mqtt publish failed', 1)
    s.close()
    
# END PROGRAM ---------------------------------------------