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
#    Written in 2015 by Jorg Janssen <http://www.zonnigdruten.nl/>

#                                         0        2        4        6        8        10       12       14       16       18       20        22        24       26    27       29   30   31   32   33   34       36   37   38   39   40   41   42   43   44       46   47   48   49   50   51       53       55   56       58        60  61   62   63   64
# norm:     02  01  FE | 06  48  02  01 | B6  0D | B6  0D | 80  F3 | 00  80 | 00  80 | 00  80 | D8  0E | D0  07 | 74  0E | 70  17 | D0  07 |  00  00 |  00  00 |  00 | 74  0E | 00 | 14 | 00 | 64 | 00 | 00  00 | 03 | C2 | 03 | 05 | 08 | FF | FF | 00 | 00  00 | 00 | FF | FF | 00 | C0 | B6  0D | 00  00 | 00 | 00  80 | 45  03 | FF | FF | 00 | 00 | FB  E1  03 
#                      |                |   3510 |   3510 |        |        |        |        |  3800  |  2000  | 3700   | 6000   |  2000  |       0 |       0 |   0 | 3700   |  0 | 20 |  0 |100 |  0 |        |0011|                                                                    | 3510   |        |    |        |        |
#                                       | aanv.t |  ret.t | ww-in t| buitent|boilert |        |autm t  |ruimte t|cv setp | ww setp|ruimtset|volstrset| volstr  |I.str| Int.sp |Bvrm|Pomp|    |Gwvr|Glvr|                             Stat|Vrgr|Blok|Subs|Fanspeed|                        |Regeltmp|Tapdbiet|    |ZboilTmp| HMI    |CVHM|WWHM|Smod|R232|

import datetime
from settings import *

class Response:
    """General class for storing any response"""
    def __init__(self, bytes):
        self.bytes = bytes[7:]
        self.values = {}
        self.getValues()

    def getValues(self):
        #int.from_bytes(self.bytes[0:2],  byteorder='little', signed = False)
        self.values['AanvoerTemp'] = int.from_bytes(self.bytes[0:2],  byteorder='little', signed = False) #/100.00
        self.values['RetourTemp'] = int.from_bytes(self.bytes[2:4],  byteorder='little', signed = False) #/100.00
        self.values['AutomaatTemp'] = int.from_bytes(self.bytes[12:14],  byteorder='little', signed = False) #/100.00
        self.values['RuimteTemp'] = int.from_bytes(self.bytes[14:16],  byteorder='little', signed = False) #/100.00
        self.values['CVSetpoint'] = int.from_bytes(self.bytes[16:18],  byteorder='little', signed = False) #/100.00
        self.values['WWSetpoint'] = int.from_bytes(self.bytes[18:20],  byteorder='little', signed = False) #/100.00
        self.values['RuimteSetpoint'] = int.from_bytes(self.bytes[20:22],  byteorder='little', signed = False) #/100.00
        self.values['Ionisatiestroom'] = int.from_bytes(self.bytes[26:27],  byteorder='little', signed = True)            
        self.values['InternSetpoint'] = int.from_bytes(self.bytes[27:29],  byteorder='little', signed = False) #/100.00
        self.values['PompPercentage'] = int.from_bytes(self.bytes[30:31],  byteorder='little', signed = True)
        self.values['BeschikbaarVermogen'] = int.from_bytes(self.bytes[29:30],  byteorder='little', signed = True)
        self.values['GewenstVermogen'] = int.from_bytes(self.bytes[32:33],  byteorder='little', signed = True)    
        self.values['GeleverdVermogen'] = int.from_bytes(self.bytes[33:34],  byteorder='little', signed = True)
        self.values['ModulaireRegelaar'] = format(self.bytes[36],'08b')[7]
        self.values['ModulaireWarmtevraag'] = format(self.bytes[36],'08b')[6]        
        self.values['AUWarmtevraag'] = format(self.bytes[36],'08b')[5]
        #self.values['Vorstbeveiliging'] = format(self.bytes[36],'08b')[4]
        self.values['WWComfort'] = format(self.bytes[36],'08b')[3] # inverse van WWEco
        #self.values['WWBlokkering'] = format(self.bytes[36],'08b')[2]        
        #self.values['Anti Legionella'] = format(self.bytes[36],'08b')[1]
        self.values['WWWarmtevraag'] = format(self.bytes[36],'08b')[0]        
        #self.values['BlokkerendeIngang'] = format(self.bytes[37],'08b')[7]
        #self.values['VrijegaveIngang'] = format(self.bytes[37],'08b')[6]        
        self.values['Ionisatie'] = format(self.bytes[37],'08b')[5]
        #self.values['Tapschakelaar'] = format(self.bytes[37],'08b')[4]
        #self.values['Min. gasdruk'] = format(self.bytes[37],'08b')[2]        
        #self.values['CVVrijgave'] = format(self.bytes[37],'08b')[1]
        #self.values['WWvrijgave'] = format(self.bytes[37],'08b')[0]    
        self.values['Gasklep'] = abs(int(format(self.bytes[38],'08b')[7])-1) # 1 = dicht, 0 = open 
        self.values['Ontsteking'] = format(self.bytes[38],'08b')[5]
        self.values['Driewegklep'] = format(self.bytes[38],'08b')[4]
        #self.values['ExterneDriewegklep'] = format(self.bytes[38],'08b')[3] 
        #self.values['ExterneGasklep'] = format(self.bytes[38],'08b')[1]
        self.values['Pomp'] = format(self.bytes[39],'08b')[7] #aan/uit
        #self.values['Boilerpomp'] = format(self.bytes[39],'08b')[6]        
        #self.values['Externe CV pomp'] = format(self.bytes[39],'08b')[5]
        #self.values['Statusmelding'] = format(self.bytes[39],'08b')[3] 
        self.values['OTSmartPower'] = format(self.bytes[39],'08b')[0]    
        self.values['Status'] = int.from_bytes(self.bytes[40:41],  byteorder='little', signed = True)    
        self.values['Substatus'] = int.from_bytes(self.bytes[43:44],  byteorder='little', signed = True)    
        self.values['Vergrendeling'] = int.from_bytes(self.bytes[41:42],  byteorder='little', signed = True) #failure code        
        self.values['Blokkering'] = int.from_bytes(self.bytes[42:43],  byteorder='little', signed = True) # error code
        self.values['VentilatorToeren'] = int.from_bytes(self.bytes[24:26],  byteorder='little', signed = False)
        #self.values['SUstatus'] = int.from_bytes(self.bytes[46:47],  byteorder='little', signed = True)
        #self.values['SUvergrendeling'] = int.from_bytes(self.bytes[47:48],  byteorder='little', signed = True)
        #self.values['SUblokkering'] = int.from_bytes(self.bytes[48:49],  byteorder='little', signed = True)            
        #self.values['Waterdruk'] = int.from_bytes(self.bytes[49:50],  byteorder='little', signed = True) # commented in remehadoc    
        self.values['RegelTemp'] = int.from_bytes(self.bytes[51:53],  byteorder='little', signed = False) #/100.00
        self.values['Tapdebiet'] = int.from_bytes(self.bytes[53:55],  byteorder='little', signed = False) #/100.00
        #self.values['ZonneboilerTemp'] = int.from_bytes(self.bytes[56:58],  byteorder='little', signed = False) #/100.00
        #self.values['HMIactief'] = int.from_bytes(self.bytes[58:60],  byteorder='little', signed = False)            
            
class Request:
    """Class for building requests"""
    def __init__(self):
        self._request = bytearray(b'\x02\xfe\x01\x05\x08\x02\x01\x69\xab\x03')
    def send(self, socket):
        socket.sendall(self._request)

def Read(socket):
    """Call this after sending a request. It will return an array of response objects, if any."""        
    bytes = bytearray()
    while (1): # recv
        try:
            chunk = socket.recv(1) # block untill timeout
            bytes.extend(chunk)
        except:
            break
    if (len(bytes) == 0): # No response
        Debug("No response")
    elif (len(bytes) < 67):
        Debug("Incomplete response")
    else:  
        rs = Response(bytes)
        return rs    

def Debug(mess, level):
    if(level <= debug_level):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        print (now + ": " + mess + "\r\n")
