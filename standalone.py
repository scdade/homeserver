class luxtronic(object):

        def __init__(self):#,pItem,localvars):
            try:
                import random
            except ImportError:
                import whrandom as random
            try:
                from hashlib import md5 as _md5
            except ImportError:
                import md5 as oldmd5
                _md5 = lambda x='',oldmd5=oldmd5: oldmd5.md5(x)
            self.md5 = _md5
            self.lastStatus=[];
            self.id = "LUXTRONIC"
            self.connect_status = ""
            self.last_raw_message = "noch keine Meldungen"
            self.is_running = True
            self.callinfo  = {}
                  #Errorcodes
            self.E_LT_OK            = 0       #All is fine
            self.E_LT_NETWORKERROR  = -2000   #error while connecting to server or server not found
            self.E_LT_INVALIDANSWER = -2001   #different response/answer was expcted for request

            self.LUXTRONIC2_IP='192.168.178.23'
            #LUXTRONIC2_IP='127.0.0.1'

            #Datadescription from java_daten.php; source: https://www.symcon.de/forum/threads/24003-Alpha-Innotec-W%C3%A4rmepumpe-%C3%BCber-Lan-anbinden
            self.LUXTRONIC2_STATUSFIELD=[
            "1","2","Temperatur WW","4","5","6","7","8","9","10",
            "Temperatur_TVL_Vorlauf",       #index 10
            "Temperatur_TRL_Ruecklauf",     #11
            "Sollwert_TRL_HZ_Ruecklauf_Soll",   #12
            "Temperatur_TRL_ext_Ruecklauf_Extern",#13
            "Temperatur_THG_Heissgas",#14
            "Temperatur_TA_Aussenfuehler",#15
            "Mitteltemperatur",#16
            "Temperatur_TBW",#17
            "Einst_BWS_akt",#18
            "Temperatur_TWE_Waermequelle_Ein",#19
            "Temperatur_TWA_Waermequelle_Aus",#20
            "Temperatur_TFB1",#21
            "Sollwert_TVL_MK",#22
            "Temperatur_RFV",#23
            "Temperatur_TFB2",#24
            "Sollwert_TVL_MK2",#25
            "Temperatur_TSK",#26
            "Temperatur_TSS",#27
            "Temperatur_TEE",#28
            "ASDin",
            "BWTin",
            "EVUin",
            "HDin",
            "MOTin",
            "NDin",
            "PEXin",
            "SWTin",
            "AVout",
            "BUPout",
            "HUPout",
            "MA1out",
            "MZ1out",
            "VENout",
            "VBOout",
            "VD1out",
            "VD2out",
            "ZIPout",
            "ZUPout",
            "ZW1out",
            "ZW2SSTout",
            "ZW3SSTout",
            "FP2out",
            "SLPout",
            "SUPout",
            "MZ2out",
            "MA2out",
            "Zaehler_BetrZeitVD1",
            "Zaehler_BetrZeitImpVD1_Impulse_Verdichter",
            "Zaehler_BetrZeitVD2",
            "Zaehler_BetrZeitImpVD2",
            "Zaehler_BetrZeitZWE1",
            "Zaehler_BetrZeitZWE2",
            "Zaehler_BetrZeitZWE3",
            "Zaehler_BetrZeitWP",
            "Zaehler_BetrZeitHz",
            "Zaehler_BetrZeitBW",
            "Zaehler_BetrZeitKue",
            "Time_WPein_akt",
            "Time_ZWE1_akt",
            "Time_ZWE2_akt",
            "Timer_EinschVerz",
            "Time_SSPAUS_akt",
            "Time_SSPEIN_akt",
            "Time_VDStd_akt",
            "Time_HRM_akt",
            "Time_HRW_akt",
            "Time_LGS_akt",
            "Time_SBW_akt",
            "Code_WP_akt",
            "BIV_Stufe_akt",
            "WP_BZ_akt",
            "SoftStand1",
            "SoftStand2",
            "SoftStand3",
            "SoftStand4",
            "SoftStand5",
            "SoftStand6",
            "SoftStand7",
            "SoftStand8",
            "SoftStand9",
            "SoftStand10",
            "AdresseIP_akt",
            "SubNetMask_akt",
            "Add_Broadcast",
            "Add_StdGateway",
            "ERROR_Time0",
            "ERROR_Time1",
            "ERROR_Time2",
            "ERROR_Time3",
            "ERROR_Time4",
            "ERROR_Nr0",
            "ERROR_Nr1",
            "ERROR_Nr2",
            "ERROR_Nr3",
            "ERROR_Nr4",
            "AnzahlFehlerInSpeicher",
            "Switchoff_file_Nr0",
            "Switchoff_file_Nr1",
            "Switchoff_file_Nr2",
            "Switchoff_file_Nr3",
            "Switchoff_file_Nr4",
            "Switchoff_file_Time0",
            "Switchoff_file_Time1",
            "Switchoff_file_Time2",
            "Switchoff_file_Time3",
            "Switchoff_file_Time4",
            "Comfort_exists",
            "HauptMenuStatus_Zeile1",
            "HauptMenuStatus_Zeile2",
            "HauptMenuStatus_Zeile3",
            "HauptMenuStatus_Zeit",
            "HauptMenuAHP_Stufe",
            "HauptMenuAHP_Temp",
            "HauptMenuAHP_Zeit",
            "SH_BWW",
            "SH_HZ",
            "SH_MK1",
            "SH_MK2",
            "Einst_Kurzrpgramm",
            "StatusSlave_1",
            "StatusSlave_2",
            "StatusSlave_3",
            "StatusSlave_4",
            "StatusSlave_5",
            "AktuelleTimeStamp",
            "SH_MK3",
            "Sollwert_TVL_MK3",
            "Temperatur_TFB3",
            "MZ3out",
            "MA3out",
            "FP3out",
            "Time_AbtIn",
            "Temperatur_RFV2",
            "Temperatur_RFV3",
            "SH_SW",
            "Zaehler_BetrZeitSW",
            "FreigabKuehl",
            "AnalogIn",
            "SonderZeichen",
            "SH_ZIP",
            "WebsrvProgrammWerteBeobarten",
            "WMZ_Heizung",
            "WMZ_Brauchwasser",
            "WMZ_Schwimmbad",
            "WMZ_Seit",
            "WMZ_Durchfluss",
            "AnalogOut1",
            "AnalogOut2",
            "Time_Heissgas"];

            #import threading
            #self._thread = threading.Thread(target=self._connect,name="thread_LUX_UPDATE")
            #self._thread.setDaemon(True)
            #self._thread.is_running=True;
            #self._thread.start()
            #self.updateInterval = 60;
            #self.setWWTemp=(False,0);
            
        def setUpdateInterval(self,timeout):
            self.updateInterval = timeout;
            
        def _connect(self):
            import time;
            self.timeoutcounter=0;
            
            print("Thread is started");
            while self.is_running:
                try:
                    if self.timeoutcounter<=0:
                        print("updating status now");
                        self._updateStatus();
                        self.timeoutcounter=self.updateInterval;
                    else:
                        print(" delay -1");
                        self.timeoutcounter=self.timeoutcounter-1;
                except:
                    print("updateStatus error");

                if( self.setWWTemp[0] ):
                    try:
                        print("set new WW-Temp "+str(self.setWWTemp[1]))
                        self.LuxtronicSetValue(2,self.setWWTemp[1]);
                        print("done Setting new WW Temp")
                        self.setWWTemp=(False,0)
                        
                    except (KeyError,ValueError):
                        print("error bei set WW Temp")
                time.sleep(1);
            
            print("Thread is closed");
                    
        def LuxtronicExecReadCmd(self, cmdId ):
            return self.LuxtronicTransmit( cmdId,0,bytearray());    

        def LuxtronicTransmit( self,cmdId,paramterId,senddata ):
            import socket
            import struct
            answer=bytearray()
            print(senddata);
            outData = struct.pack('!i', cmdId);
            outData = outData+struct.pack('!i', paramterId);
            if(len(senddata)):
                outData = outData+senddata;#hier fehlt was,wenn mehr als 1 32bit wert gesendet wird...nicht allgemeingenug
            print(outData);

            #Create TCP/IP socket
            try:
                import sys
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("Connecting to:"+ self.LUXTRONIC2_IP);
                s.connect((self.LUXTRONIC2_IP, 8888))
                #send request and data
                print(outData);
                s.send(outData)
                #read header
                answerCmd   = struct.unpack( '!i', s.recv(4))[0];
                stat        = struct.unpack( '!i', s.recv(4))[0];
                datalength  = struct.unpack( '!i', s.recv(4))[0];

                if answerCmd == cmdId:
                    answer = s.recv(datalength*4);
                    print(answer)
                    errorcode = self.E_LT_OK;
                else:
                    errorcode = self.E_LT_INVALIDANSWER;
                #s.shutdown(SHUT_RDWR);
                s.close()
            except:
                errorcode = self.E_LT_NETWORKERROR;

            return(errorcode,answer)


        def LuxtronicDecodeStatus(self, rawStatus ):
            import struct;
            result=[];
            print(len(rawStatus))
            rawValues=struct.unpack("!183i",rawStatus);
            for i in range(159):
                try:
                    if(i==2 or (i>=10 and i<=28)):
                       value = (float(rawValues[i])*0.1);
                    else:
                       value = rawValues[i];
                except:
                    value=-99999
                #hier ggf. mal noch die betriebsstundenzaehler wandeln
                result.append( [i,self.LUXTRONIC2_STATUSFIELD[i],value] );

            return result;

        def LuxtronicReadStatus(self):
            (errorcode,rawstatus)=self.LuxtronicExecReadCmd( 3004 )

            if(errorcode==self.E_LT_OK):
               print(rawstatus)
               result=self.LuxtronicDecodeStatus(rawstatus)
            else:
               result=[];
               print("Reading Status Error = "+str(errorcode));
            return result;

        def LuxtronicSetValue(self, paramter,value ):
            import struct;
            print("Setting ",paramter," to value: ",value);
            if(paramter==2 or (paramter>=10 and paramter<=28)):
               rawValue = (value*10);
            elif(paramter<=34):
               rawValue=value;
            elif(paramter<=35):#Analog-Output
               rawValue=value;
            elif(paramter<=55):#Digial-Out
               rawValue=(value!=0);
            else:
               rawValue=value;

            result=self.LuxtronicTransmit( 3002,paramter,struct.pack("!i",int(rawValue))) ;
            
            return result;


        def log(self,msg,severity='info'):
            import time
            _msg_uid = self.md5( "%s%s" % ( self.id, time.time() ) ).hexdigest()
            _msg = '<log><id>%s</id><facility>LUXTRONIC</facility><severity>%s</severity><message>%s</message></log>' % (_msg_uid,severity,msg)
            self.send_to_hs_out(2,_msg)
        def getValue(self,index):
                return self.lastStatus[index][2];
            
        def updateStatus(self,ip):#update erfolgt im hintergrund thread, also nur die IP umsetzen
                self.LUXTRONIC2_IP=ip;
                return 0;
            
        def _updateStatus(self):
                result=-1;
                try:
                    print("Reading Temperature started")
                    status=self.LuxtronicReadStatus()
                    print(status);
                    print("Reading Temperature finished")
                    self.lastStatus=status;
                except (KeyError,ValueError):
                    print("error bei readtemp")
                return result;
        def setTemp(self,temp):
                self.setWWTemp=(True,temp)
            
        

print "stand-alone-dump"
lux = luxtronic()
lux._updateStatus()
