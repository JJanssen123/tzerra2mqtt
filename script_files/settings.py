
# YOUR SETTINGS HERE -----------------------------------------

TCP_IP = '192.168.1.5'  # ip address of rs232-to-tcp converter
TCP_PORT = 23           # tcp port of this converter

mqtt_broker = "localhost"
mqtt_username = "xxx"
mqtt_password = "xxx"
mqtt_base_topic = "domotica"

device = {"model": "CV", "name": "Tzerra", "manufacturer": "Remeha", "sw_version": "1.0", "identifiers": ["tzerra2mqtt"] }

debug_level = 1

# END OF SETTINGS --------------------------------------------

# Home Assistant entities configuration:
mqtt_hass_topic = "homeassistant"
mqtt_autodiscovery_config = {
    "AanvoerTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.AanvoerTemp/100 }}"}},
    "Anti Legionella": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "AutomaatTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.AutomaatTemp/100 }}"}},
    "AUWarmtevraag": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "BeschikbaarVermogen": {"type": "sensor", "config": {"device_class":"power_factor", "unit_of_measurement": "%"}},
    "BlokkerendeIngang": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Blokkering": {"type": "sensor", "config": {}},
    "Boilerpomp": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "CVSetpoint": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.CVSetpoint/100 }}"}},
    "CVVrijgave": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Driewegklep": {"type": "sensor", "config": {"value_template": "{% if value_json.Driewegklep == '1' %}WW{% else %}CV{% endif %}"}},
    "Externe CV pomp": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "ExterneDriewegklep": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "ExterneGasklep": {"type": "binary_sensor", "config": {"device_class": "opening", "payload_off": "0", "payload_on": "1"}},
    "Gasklep": {"type": "binary_sensor", "config": {"device_class": "opening", "payload_off": 0, "payload_on": 1}},
    "GeleverdVermogen": {"type": "sensor", "config": {"device_class":"power_factor", "unit_of_measurement": "%"}},
    "GewenstVermogen": {"type": "sensor", "config": {"device_class":"power_factor", "unit_of_measurement": "%"}},
    "HMIactief": {"type": "sensor", "config": {}},
    "InternSetpoint": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.InternSetpoint/100 }}"}},
    "Ionisatie": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Ionisatiestroom": {"type": "sensor", "config": { "unit_of_measurement": "µA", "icon": "mdi:fire"}},
    "Min. gasdruk": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "ModulaireRegelaar": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "ModulaireWarmtevraag": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Ontsteking": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "OTSmartPower": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Pomp": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "PompPercentage": {"type": "sensor", "config": {"device_class":"power_factor", "unit_of_measurement": "%"}},
    "RegelTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.RegelTemp/100 }}"}},
    "RetourTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.RetourTemp/100 }}"}},
    "RuimteSetpoint": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.RuimteSetpoint/100 }}"}},
    "RuimteTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.RuimteTemp/100 }}"}},
    "Status": {"type": "sensor", "config": {}},
    "Statusmelding": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Statusomschrijving": {"type": "sensor", "config": {}},    
    "SUblokkering": {"type": "sensor", "config": {}},
    "Substatus": {"type": "sensor", "config": {}},
    "Substatusomschrijving": {"type": "sensor", "config": {}},    
    "SUstatus": {"type": "sensor", "config": {}},
    "SUvergrendeling": {"type": "sensor", "config": {}},
    "Tapdebiet": {"type": "sensor", "config": {"value_template": "{{ value_json.Tapdebiet/100 }}", "unit_of_measurement": "l/m", "icon": "mdi:water-pump"}},
    "Tapschakelaar": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "VentilatorToeren": {"type": "sensor", "config": {"unit_of_measurement": "rpm", "icon": "mdi:fan"}},
    "Vergrendeling": {"type": "sensor", "config": {}},
    "Vorstbeveiliging": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "VrijegaveIngang": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "Waterdruk": {"type": "sensor", "config": {}},
    "WWBlokkering": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "WWComfort": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "WWSetpoint": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.WWSetpoint/100 }}"}},
    "WWvrijgave": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "WWWarmtevraag": {"type": "binary_sensor", "config": {"payload_off": "0", "payload_on": "1"}},
    "ZonneboilerTemp": {"type": "sensor", "config": {"device_class": "temperature", "unit_of_measurement": "°C", "value_template": "{{ value_json.ZonneboilerTemp/100 }}"}}
}
