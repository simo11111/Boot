import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , xKEys , base64 , datetime , re , socket , threading
from protobuf_decoder.protobuf_decoder import Parser
from black9 import *
from black9 import xSendTeamMsg
from black9 import Auth_Chat
from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

def AuTo_ResTartinG():
    time.sleep(6 * 60 * 60)
    print('\n - AuTo ResTartinG The BoT ... ! ')
    p = psutil.Process(os.getpid())
    for handler in p.open_files():
        try:
            os.close(handler.fd)
        except Exception as e:
            print(f" - Error CLose Files : {e}")
    for conn in p.net_connections():
        try:
            if hasattr(conn, 'fd'):
                os.close(conn.fd)
        except Exception as e:
            print(f" - Error CLose Connection : {e}")
    sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))
    python = sys.executable
    os.execl(python, python, *sys.argv)
       
def run_SPamSq_simulation(uid, K, V, repeat=20, delay=0.2):
    print(f"[SIMULATION] SPamSq x{repeat} -> UID={uid}")
    for i in range(repeat):
            try:
            	pkt = SPamSq(uid, K, V)  
            except Exception as e:
            	print(f"[SIMULATION] SPamSq() raised: {e}")
            	return
            	if isinstance(pkt, str):
            	   try:
            	   	pkt_bytes = bytes.fromhex(pkt)
            	   except Exception:
            	   	pkt_bytes = pkt.encode('utf-8')
            	elif isinstance(pkt, (bytes, bytearray)):
            	   		pkt_bytes = bytes(pkt)
            	else:
            		pkt_bytes = str(pkt).encode('utf-8')
            		hex_preview = pkt_bytes.hex()[:300] + ("..." if len(pkt_bytes.hex()) > 300 else "")
            		print(f"[{i+1:02d}/{repeat}] len={len(pkt_bytes)} hex_preview={hex_preview}")
            		time.sleep(delay)
            		print("[SIMULATION] done.")
    
def ResTarT_BoT():
    print('\n - ResTartinG The BoT ... ! ')
    p = psutil.Process(os.getpid())
    open_files = p.open_files()
    connections = p.net_connections()
    for handler in open_files:
        try:
            os.close(handler.fd)
        except Exception:
            pass           
    for conn in connections:
        try:
            conn.close()
        except Exception:
            pass
    sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))
    python = sys.executable
    os.execl(python, python, *sys.argv)

def execute_ghost_command(client, teamcode, client_number, clients_list):
    success = False
    try:
            if hasattr(client, 'CliEnts2') and client.CliEnts2 and hasattr(client, 'key') and client.key and hasattr(client, 'iv') and client.iv:
            	join_packet = JoinTeamCode(teamcode, client.key, client.iv)
            	client.CliEnts2.send(join_packet)
            	start_time = time.time()
            	response_received = False
            	while time.time() - start_time < 8:
            	       try:
            	           if hasattr(client, 'DaTa2') and client.DaTa2 and len(client.DaTa2.hex()) > 30:
            	           	hex_data = client.DaTa2.hex()
            	           	if '0500' in hex_data[0:4]:
            	           	       try:
            	           	           if "08" in hex_data:
            	           	           	decoded_data = DeCode_PackEt(f'08{hex_data.split("08", 1)[1]}')
            	           	           else:
            	           	           	decoded_data = DeCode_PackEt(hex_data[10:])
            	           	           	dT = json.loads(decoded_data)
            	           	           	if "5" in dT and "data" in dT["5"]:
            	           	           		team_data = dT["5"]["data"]
            	           	           		if "31" in team_data and "data" in team_data["31"]:
            	           	           		  sq = team_data["31"]["data"]
            	           	           		  idT = team_data["1"]["data"]
            	           	           		  client.CliEnts2.send(ExitBot('000000', client.key, client.iv))
            	           	           		  time.sleep(0.2)
            	           	           		  ghost_packet = GhostPakcet(idT, name, sq, client.key, client.iv)
            	           	           		  client.CliEnts2.send(ghost_packet)
            	           	           		  success = True
            	           	           		  response_received = True
            	           	           		  break
            	           	       except Exception as decode_error:
            	           	           try:
            	           	               if len(hex_data) > 20:
            	           	               	alternative_data = DeCode_PackEt(hex_data)
            	           	               	if alternative_data:
            	           	               		pass
            	           	               	
            	           	           except:
            	           	           	pass
            	           	           	time.sleep(0.1)
            	       except Exception as loop_error:
            	       	time.sleep(0.1)
            	       	if not response_received:
            	       		try:
            	       			ghost_packet_alt = GhostPakcet(teamcode, name, "1", client.key, client.iv)
            	       			client.CliEnts2.send(ghost_packet_alt)
            	       			time.sleep(0.02)
            	       			success = True
            	       		except Exception as alt_error:
            	       			pass
            	       	else:
            	       		pass
    except Exception as e:
            	pass
            	return success
    
def GeT_Time(timestamp):
    last_login = datetime.fromtimestamp(timestamp)
    now = datetime.now()
    diff = now - last_login   
    d = diff.days
    h , rem = divmod(diff.seconds, 3600)
    m , s = divmod(rem, 60)    
    return d, h, m, s

def Time_En_Ar(t): 
    return ' '.join(t.replace("Day","يوم").replace("Hour","ساعة").replace("Min","دقيقة").replace("Sec","ثانية").split(" - "))
    
Thread(target = AuTo_ResTartinG , daemon = True).start()
            
class FF_CLient():

    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.Get_FiNal_ToKen_0115()     
            
    def Connect_SerVer_OnLine(self , Token , tok , host , port , key , iv , host2 , port2):
            global CliEnts2 , DaTa2 , AutH
            try:
                self.AutH_ToKen_0115 = tok    
                self.CliEnts2 = socket.create_connection((host2 , int(port2)))
                self.CliEnts2.send(bytes.fromhex(self.AutH_ToKen_0115))                  
            except:pass        
            while True:
                try:
                    self.DaTa2 = self.CliEnts2.recv(99999)
                    if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:	         	    	    
                            self.packet = json.loads(DeCode_PackEt(f'08{self.DaTa2.hex().split("08", 1)[1]}'))
                            self.AutH = self.packet['5']['data']['7']['data']
                    
                except:pass    	
                                                            
    def Connect_SerVer(self , Token , tok , host , port , key , iv , host2 , port2):
            global CliEnts       
            self.AutH_ToKen_0115 = tok    
            self.CliEnts = socket.create_connection((host , int(port)))
            self.CliEnts.send(bytes.fromhex(self.AutH_ToKen_0115))  
            self.DaTa = self.CliEnts.recv(1024)          	        
            threading.Thread(target=self.Connect_SerVer_OnLine, args=(Token , tok , host , port , key , iv , host2 , port2)).start()
            self.Exemple = xMsGFixinG('12345678')
            while True:      
                try:
                    self.DaTa = self.CliEnts.recv(1024)   
                    if len(self.DaTa) == 0 or len(self.DaTa2) == 0:	            		
                        try:            		    
                            self.CliEnts.close() ; self.CliEnts2.close() ; self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)                    		                    
                        except:
                            try:
                                self.CliEnts.close() ; self.CliEnts2.close() ; self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                            except:
                                self.CliEnts.close() ; self.CliEnts2.close() ; ResTarT_BoT()	            
                                      
                    if '1200' in self.DaTa.hex()[0:4] and 900 > len(self.DaTa.hex()) > 100:
                        if b"***" in self.DaTa:self.DaTa = self.DaTa.replace(b"***",b"106")         
                        try:
                           self.BesTo_data = json.loads(DeCode_PackEt(self.DaTa.hex()[10:]))	       
                           self.input_msg = 'besto_love' if '8' in self.BesTo_data["5"]["data"] else self.BesTo_data["5"]["data"]["4"]["data"]
                        except: self.input_msg = None	   	 
                        self.DeCode_CliEnt_Uid = self.BesTo_data["5"]["data"]["1"]["data"]
                        self.CliEnt_Uid = EnC_Uid(self.DeCode_CliEnt_Uid , Tp = 'Uid')
                               
                    if 'besto_love' in self.input_msg[:10]:
                        self.CliEnts.send(xSEndMsg(f'''[C][B][00f7f9]━━━━━━━━━━━━
[C][B][FFFFFF]instagram :
[C][B][0012ff]z9o_v
[c][b][0012ff]silver
[C][B][00f7f9]━━━━━━━━━━━━
[C][B][FFFFFF]لعرض الاوامر اكتب
[b][c][{ArA_CoLor()}]/[C][B]help''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.3)
                        self.CliEnts.close() ; self.CliEnts2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	                    	 	 
                                                               
                    if b'/start' in self.DaTa or b'/help' in self.DaTa or 'en' in self.input_msg[:2]:
                        self.result = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        if self.result:
                            self.Status , self.Expire = self.result
                            self.CliEnts.send(xSEndMsg(f'''[b][c][{ArA_CoLor()}]
فتح سكود لصديقك عبر ايدي :
[C][B][ffffff]/[C][B]3/[ id ]
/[C][B]5/[ id ]
/[C][B]6/[ id ][b][c][{ArA_CoLor()}]
تحويل الفريق إلى:
[C][B][ffffff]/[C][B]3  /[C][B]5  /[C][B]6  [b][c][{ArA_CoLor()}]
جلب لاعب إلى الفريق:
[C][B][ffffff]/[C][B]inv [ id ][b][c][{ArA_CoLor()}]
سبام طلبات انضمام:
[C][B][ffffff]/[C][B]x [ id ][b][c][{ArA_CoLor()}]
سبام رومات:
[C][B][ffffff]/[C][B]room [ id ][b][c][{ArA_CoLor()}]
معرفة حالة اللاعب:
[C][B][ffffff]/[C][B]status [ id ][b][c][{ArA_CoLor()}]
معرفة إذا كان اللاعب مبند:
[C][B][ffffff]/[C][B]check [ id ]
[b][c][{ArA_CoLor()}]
سبام طلبات صداقة:
[C][B][ffffff]/[C][B]spam [ id ][b][c][{ArA_CoLor()}]
زيادة عدد زوار الحساب:
[C][B][ffffff]/[C][B]visit  [ id ][b][c][{ArA_CoLor()}]
تزويد 100 لايك للحساب 
[C][B][ffffff]/[C][B]like  [ id ]
''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''[b][c][{ArA_CoLor()}]
مقبرة السكود  :
[C][B][ffffff]/[C][B]code [ Team Code  ]
سبام رسائل في الفريق
[C][B][ffffff]/msg/[team code] رسالة
[b][c][{ArA_CoLor()}]دخول شبح للسكواد
[C][B][ffffff]/cod[team code]
    \n''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)		
                            self.CliEnts.send(xSEndMsg(f'''
    [b][c][FFD700]━━━━━━━━━━━━[ffffff]
    [b][c][{ArA_CoLor()}]id => [ffffff]{xMsGFixinG(self.DeCode_CliEnt_Uid)} 
    [b][c][{ArA_CoLor()}]  Status => [ffffff]{self.Status} 
    [b][c][{ArA_CoLor()}]  Expire In => [ffffff]{self.Expire}
    [b][c][{ArA_CoLor()}]  Version => v1
    [FFD700]━━━━━━━━━━━━[ffffff]\n''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	   	       		
                        elif False == self.result:
                            DeLet_Uid(self.DeCode_CliEnt_Uid , Token)  
                            
                    
                    
                   
                                       
                                       #muteee
                    elif '/mute' in self.input_msg[:6]:
                        self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        target = self.input_msg[6:].strip()
                        if self.ChEck_ReGister and ChEck_Commande(target):
                                try:
                                	self.CliEnts.send(xSEndMsg(f'جاري محاولة ميوت : {xMsGFixinG(target)}', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                	join_pkt = GenJoinSquadsPacket(target, key, iv)
                                	self.CliEnts2.send(join_pkt)
                                	time.sleep(0.4)
                                	
                                	if hasattr(self, 'DaTa2') and '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                	   d = json.loads(DeCode_PackEt(self.DaTa2.hex()[10:]))
                                	   idT = d["5"]["data"]["1"]["data"] if "5" in d and "data" in d["5"] and "1" in d["5"]["data"] else None
                                	   sq = d["5"]["data"]["31"]["data"] if "5" in d and "data" in d["5"] and "31" in d["5"]["data"] else None
                                	   self.CliEnts.send(MuTe(target, key, iv))
                                	   time.sleep(0.05)
                                	   self.CliEnts.send(xSEndMsg(f'تم إرسال طلب الميوت لـ {xMsGFixinG(target)}', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                	else:
                                	   self.CliEnts.send(MuTe(target, key, iv))
                                	   self.CliEnts.send(xSEndMsg('تم إرسال طلب ميوت (بدون تحقق من السكواد).', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                	   time.sleep(0.3)
                                	   self.CliEnts.close(); self.CliEnts2.close()
                                	   self.Connect_SerVer(Token, tok, host, port, key, iv, host2, port2)
                                except Exception as e:
                                	self.CliEnts.send(xSEndMsg(f'خطأ أثناء محاولة الميوت: {e}', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                	time.sleep(0.2)
                                	self.CliEnts.close(); self.CliEnts2.close()
                                	self.Connect_SerVer(Token, tok, host, port, key, iv, host2, port2)
                        else:
                            self.CliEnts.send(xSEndMsg(f'استعمال خاطئ. مثال: /mute {self.Exemple}', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                            
                            
                            
                            
                            
                    
                    elif '/who-is-the-best' in self.input_msg[:2]:
                        self.result = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        if self.result:
                            self.Status , self.Expire = self.result
                            self.CliEnts.send(xSEndMsg(f'''Black
    ''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''
Top''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)		
                            self.CliEnts.send(xSEndMsg(f'''1 in world''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	        
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''Black
    ''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''
Top''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)		
                            self.CliEnts.send(xSEndMsg(f'''1 in world''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	        
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''Black
    ''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''
Top''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)		
                            self.CliEnts.send(xSEndMsg(f'''1 in world''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	        
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''Black
    ''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)
                            self.CliEnts.send(xSEndMsg(f'''
Top''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.3)		
                            self.CliEnts.send(xSEndMsg(f'''1 in world''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	        
                            time.sleep(0.3)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	   	       		
                        elif False == self.result:
                            DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                     
                    elif '/code' in self.input_msg[:5]:
                        self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        self.id , self.nm = (self.input_msg[6:].split(" ", 1) if " " in self.input_msg[6:] else [self.input_msg[6:], "@MIMO TOP"])  
                        self.Zx = ChEck_Commande(self.id)
                       
                        if self.ChEck_ReGister and True == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] JoinInG With Code {self.id}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            self.CliEnts2.send(GenJoinSquadsPacket(self.id, key, iv))
                            time.sleep(0.3)

                            if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                self.dT = json.loads(DeCode_PackEt(self.DaTa2.hex()[10:]))
                                sq = self.dT["5"]["data"]["31"]["data"]
                                idT = self.dT["5"]["data"]["1"]["data"]
                                print(idT)	            	            	            	            	            	            
                                self.CliEnts2.send(ExiT('000000' , key , iv))	            	            
                                self.CliEnts2.send(ghost_pakcet(idT, self.nm , sq , key , iv))  
                                for i in range(200):
                                   self.CliEnts2.send(GenJoinSquadsPacket(self.id, key, iv))
                                   self.CliEnts2.send(ghost_pakcet(idT, self.nm , sq , key , iv))
                                   time.sleep(0.001)
                                   self.CliEnts2.send(ExiT('000000' , key , iv))
                                   self.CliEnts2.send(ghost_pakcet(idT, self.nm , sq , key , iv))

                           

                        elif False == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /cood <code>\n - Ex : /cood 517284\n', 9 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        elif False == self.ChEck_ReGister:
                            DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                    elif '/msg/' in self.input_msg[:5]:
                        self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        self.id , self.nm = (self.input_msg[5:].split(" ", 1) if " " in self.input_msg[5:] else [self.input_msg[5:], ""])
                        self.Zx = ChEck_Commande(self.id)
                        if self.ChEck_ReGister and True == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] Wait for sending message    : {self.id}\n', 9 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            
                            g = GenJoinSquadsPacket(self.id, key, iv)
                            self.CliEnts2.send(g)
                            print(g)
                            time.sleep(0.5)

                            if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                
                                self.dT = json.loads(DeCode_PackEt(self.DaTa2.hex()[10:]))
                                
                                idT = self.dT["5"]["data"]["1"]["data"]
                                sq = self.dT["5"]["data"]["14"]["data"]
                                
                                 
                                self.CliEnts.send(Auth_Chat(idT, sq, key, iv))
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] succesfull snd message : {self.id}\n', 9 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                
                                self.CliEnts.send(xSendTeamMsg(f'\n[b][c][{ArA_CoLor()}] {self.nm}\n',idT , key , iv))
                                self.CliEnts2.send(ExiT('000000' , key , iv))
                                time.sleep(4)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)  
                                
                                
                                            	            	            
                                
                            

                        elif False == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /cood <code>\n - Ex : /cood 517284\n', 9 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        elif False == self.ChEck_ReGister:
                            DeLet_Uid(self.DeCode_CliEnt_Uid , Token)

                    elif '/ban/' in self.input_msg[:5]:
                        self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                        self.id = self.input_msg[5:].split(" ", 1)[0]
                        self.Zx = ChEck_Commande(self.id)
                        if self.ChEck_ReGister and True == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'[b][c][{ArA_CoLor()}]تم تشجيل دخول by silver', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            
                            g = GenJoinSquadsPacket(self.id, key, iv)
                            self.CliEnts2.send(g)
                            print(g)
                            time.sleep(0.5)

                            if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                
                                self.dT = json.loads(DeCode_PackEt(self.DaTa2.hex()[10:]))
                                
                                idT = self.dT["5"]["data"]["1"]["data"]
                                sq = self.dT["5"]["data"]["14"]["data"]
                                
                                 
                                self.CliEnts.send(Auth_Chat(idT, sq, key, iv))
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] BAN msg SS : {self.id}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                for i in range(10):
                                    self.CliEnts.send(xSendTeamMsg(f'[b][c][{ArA_CoLor()}]تم تشجيل دخول by Black',idT , key , iv))
                                    self.CliEnts2.send(ExiT('000000' , key , iv))
                                time.sleep(4)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)  
                                
                                
                                            	            	            
                                
                            

                        elif False == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /cood <code>\n - Ex : /cood 517284\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        elif False == self.ChEck_ReGister:
                            DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                    elif '/like' in self.input_msg[:5]: 	
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)	            		    
                            self.res , self.time = ChEck_Limit(self.DeCode_CliEnt_Uid , 'like')
                            self.id = self.input_msg[6:]
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and self.res and True == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] SendinG LiKes To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))   
                                a1 , a2 , a3 , a4 , a5 = Likes(self.id)   
                                if a3 == a4:
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][ffffff] Please Try Likes After 24H.. !\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    time.sleep(0.3)
                                    self.CliEnts.close() ; self.CliEnts2.close()
                                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)                	
                                else:
                                    self.CliEnts.send(xSEndMsg(f'''[b][c][90EE90]\n [SuccEssFuLLy] - UpGradE LiKes !
        [ffffff]	
          PLayer Name : {a1}
          PLayer Uid : {xMsGFixinG(self.id)}
          PLayer SerVer : {a2}
          LiKes BeFore : {xMsGFixinG(a3)}
          LiKes AFter : {xMsGFixinG(a4)}
          LiKes GiVen : {a5}
          RemaininG : {self.res}
         
           [90EE90]Dev : LWESS_ANTIBAN\n''', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    time.sleep(0.3)
                                    self.CliEnts.close() ; self.CliEnts2.close()
                                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	 
                                      
                            elif False == self.res and True == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][ffffff] U Reched Max Limit To SEnd LiKes\n Try AfTer : {xMsGFixinG(self.time)} !\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))  
                                      
                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /like <id>\n - Ex : /like {self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	      
                                                     
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                                                       
                    elif '/spam' in self.input_msg[:5]: 	
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg[6:]
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and True == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] SendinG Spam To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))   
                                self.Req = Requests_SPam(self.id)	     
                                if True == self.Req:
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][90EE90]SuccEssFuLLy SendinG SPam\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    time.sleep(0.3)
                                    self.CliEnts.close() ; self.CliEnts2.close()
                                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	
                                             
                                elif False == self.Req:
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][FFD700]FaiLEd SendinG SPam\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    self.CliEnts.close() ; self.CliEnts2.close()
                                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                    
                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /spam <id>\n - Ex : /spam {self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                    
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)      
                                                               
                    elif '++' in self.input_msg[:2]:   
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg.replace("++", "", 1).strip()
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and True == self.Zx:			    
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] GeTinG InFo FoR {xMsGFixinG(self.id)}\n' , 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.3)
                                self.CliEnts.send(xSEndMsg(GeT_PLayer_InFo(self.id , Token) , 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                
                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use ++ <id>\n - Ex : ++ {self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                                    
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)          	               	    	
                    elif '/5' in self.input_msg[:2]:    
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            if self.ChEck_ReGister:         	  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] GeneRaTinG 5 In Squid\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(5 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(3)		      
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)	
                                                                    
                    elif '/6' in self.input_msg[:2]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            if self.ChEck_ReGister:         	  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] GeneRaTinG 6 In Squid\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(6 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)

                    elif '/3' in self.input_msg[:2]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            if self.ChEck_ReGister:         	  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] GeneRaTinG 3 In Squid\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(3 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                                    
                    elif '/5/' in self.input_msg[:4]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg[4:]
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and True == self.Zx:         	  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] 5 In Squid To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(5 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.id , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)

                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /c5/<id>\n - Ex : /c5/{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)  
                                                    
                    elif '/6/' in self.input_msg[:4]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg[4:]	    	    
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and True == self.Zx:  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] 6 In Squid To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(6 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.id , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)

                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /c6/<id>\n - Ex : /c6/{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                                
                    elif '/3/' in self.input_msg[:4]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg[4:]	    	    
                            self.Zx = ChEck_Commande(self.id)
                            if self.ChEck_ReGister and True == self.Zx:  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] 3 In Squid To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(3 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.id , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)

                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /c3/<id>\n - Ex : /c3/{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                                
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)
                                                            
                    elif '/inv' in self.input_msg[:5]:
                            self.ChEck_ReGister = ChEck_The_Uid(self.DeCode_CliEnt_Uid)
                            self.id = self.input_msg[5:]
                            self.Zx = ChEck_Commande(self.id)    
                            if self.ChEck_ReGister and True == self.Zx:  
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] GeTinG PLayer {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                self.CliEnts2.send(OpEnSq(key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(cHSq(5 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)			         
                                self.CliEnts2.send(SEnd_InV(1 , self.id , key , iv))
                                time.sleep(0.5)
                                self.CliEnts2.send(SEnd_InV(1 , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(3)
                                self.CliEnts.close() ; self.CliEnts2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2) 

                            elif False == self.Zx:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /inv<id>\n - Ex : /inv{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                                     
                            elif False == self.ChEck_ReGister:
                                DeLet_Uid(self.DeCode_CliEnt_Uid , Token)    		             

                    if '/pp/' in self.input_msg[:4]:
                        self.id = self.input_msg[4:]	 
                        self.Zx = ChEck_Commande(self.id)
                        if True == self.Zx:	            		     
                            for i in range(20):
                                threading.Thread(target=lambda: self.CliEnts2.send(SPamSq(self.id , key , iv))).start()
                            time.sleep(0.1)    			         
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] SuccEss Spam To {xMsGFixinG(self.id)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.1)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	            		      	
                        elif False == self.Zx: 
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /pp/<id>\n - Ex : /pp/{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	
                            time.sleep(0.1)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	            		

                    elif '/room' in self.input_msg[:4]:
                        self.res , self.time = ChEck_Limit(self.DeCode_CliEnt_Uid , 'Spam_Room')
                        self.id , self.nm = (self.input_msg[4:].split(" ", 1) if " " in self.input_msg[4:] else [self.input_msg[4:], "Black"])
                        self.Zx = ChEck_Commande(self.id)	
                        if self.res and True == self.Zx:
                            try:	      		    
                                self.CliEnts2.send(GeT_Status(self.id , key , iv))
                                time.sleep(0.3)
                            except:pass    	            	
                            if '0f00' in self.DaTa2.hex()[:4]:
                                try:	            		
                                    packet = self.DaTa2.hex()[10:]
                                    self.BesTo_data = json.loads(DeCode_PackEt(packet))
                                    self.room_uid = self.BesTo_data['5']['data']['1']['data']['15']['data']
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] SuccEss SpamRoom To {xMsGFixinG(self.room_uid)}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    for i in range(999):
                                        threading.Thread(target=lambda: self.CliEnts2.send(SPam_Room(self.id , self.room_uid , self.nm , key , iv))).start()
                                    time.sleep(0.1)
                                    self.CliEnts.close() ; self.CliEnts2.close()
                                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	    		       
                                except:pass
                                
                        elif False == self.res and True == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][ffffff] U Reched Max Limit To SEnd SPam\n Try AfTer : {xMsGFixinG(self.time)} !\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.1)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                            
                        elif False == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /room<id> <name>\n - Ex : /room{self.Exemple} Black Team\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.1)
                            self.CliEnts.close() ; self.CliEnts2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)	
                    elif '/ou/' in self.input_msg[:4]:
                        self.id_part = self.input_msg[4:]
                        parts = self.id_part.split(" ", 1)
                        self.id = parts[0] 
                        self.ghost_name = parts[1] if len(parts) > 1 else "Blackf-t"
                        self.Zx = ChEck_Commande(self.id)
                        if True == self.Zx:
                            try:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] جاري إرسال طلب انضمام إلى سكواد اللاعب {xMsGFixinG(self.id)}\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                self.CliEnts2.send(SPamSq(self.id, key, iv))
                                time.sleep(2)
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] في انتظار قبول الطلب...\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                self.CliEnts2.send(AccEpT(self.id, self.AutH, key, iv))
                                time.sleep(2)
                                start_time = time.time()
                                while time.time() - start_time < 10:  
                                    if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                        packet = self.DaTa2.hex()[10:]
                                        self.BesTo_data = json.loads(DeCode_PackEt(packet))
                                        self.sq_code = self.BesTo_data["5"]["data"]["31"]["data"]
                                        self.sq_leader = self.BesTo_data["5"]["data"]["1"]["data"]
                                        self.CliEnts2.send(ExiT('000000', key, iv))
                                        time.sleep(1)
                                        self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] جاري إرسال الشبح "{self.ghost_name}" إلى السكواد {xMsGFixinG(self.sq_code)}\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                        self.CliEnts2.send(ghost_pakcet(self.sq_leader, self.ghost_name, self.sq_code, key, iv))
                                        time.sleep(0.01)
                                        self.CliEnts2.send(ExiT('000000', key, iv))
                                        time.sleep(0.01)
                                        self.CliEnts.send(xSEndMsg(f'\n[b][c][90EE90]تم إرسال الشبح "{self.ghost_name}" بنجاح!\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                                        break
                                    time.sleep(0.1)
                                else:
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][FF0000]لم يتم قبول الطلب خلال الوقت المحدد\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))                                
                            except Exception as e:
                                self.CliEnts.send(xSEndMsg(f'\n[b][c][FF0000]حدث خطأ: {str(e)}\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                            time.sleep(0.3)
                            self.CliEnts.close(); self.CliEnts2.close()
                            self.Connect_SerVer(Token, tok, host, port, key, iv, host2, port2)
                            
                        elif False == self.Zx:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - الصيغة الصحيحة: /9t/<آيدي>\n - مثال: /9t/{self.Exemple}\n', 2, self.DeCode_CliEnt_Uid, self.DeCode_CliEnt_Uid, key, iv))
                            time.sleep(0.1)
                            self.CliEnts.close(); self.CliEnts2.close()
                            self.Connect_SerVer(Token, tok, host, port, key, iv, host2, port2)
                    elif '/status' in self.input_msg[:4]:
                        self.id = self.input_msg[4:]
                        self.Zx = ChEck_Commande(self.id)
                        if True == self.Zx:	            		     
                            try:
                                  self.CliEnts2.send(GeT_Status(self.id , key , iv))
                                  time.sleep(0.3)
                            except:pass   
                            if '0f00' in self.DaTa2.hex()[:4]:
                                packet = self.DaTa2.hex()[10:]
                                try:
                                    self.BesTo_data = json.loads(DeCode_PackEt(packet))
                                    self.target_id = self.BesTo_data["5"]["data"]["1"]["data"]["1"]["data"]
                                    self.h = self.BesTo_data["5"]["data"]["1"]["data"]["3"]["data"]
                                except:pass						
                                try:status_data = self.BesTo_data["5"]["data"]["1"]["data"]["3"]["data"]
                                except:pass
                                try:		
                                    if self.h == 1:
                                        try:
                                            self.last = self.BesTo_data["5"]["data"]["1"]["data"]["4"]["data"]	                
                                        except:
                                            self.last = 'No DaTa !'
                                        self.name = GeT_Name(self.target_id , Token)
                                        self.name = str(self.name)
                                        self.CliEnts.send(xSEndMsg(f"[b][c]\n Status InFo Of The PLayer : \n\n[{ArA_CoLor()}]PLayer Uid : {xMsGFixinG(self.target_id)}\nPLayer Status : SoLo\nPLayer s'Name : {self.name}\nLast Login : {xMsGFixinG(datetime.fromtimestamp(self.last).strftime('%I:%M %p %d/%m/%y'))}\n\n[ffffff] Dev : Black\n", 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                        time.sleep(0.3)
                                        self.CliEnts.close() ; self.CliEnts2.close()
                                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)					
                                    elif self.h == 2:
                                        self.leader = xMsGFixinG(self.BesTo_data["5"]["data"]["1"]["data"]["8"]["data"])
                                        self.group_count = self.BesTo_data["5"]["data"]["1"]["data"]["9"]["data"]
                                        self.group_count2 = self.BesTo_data["5"]["data"]["1"]["data"]["10"]["data"]
                                        self.leader_id = self.BesTo_data["5"]["data"]["1"]["data"]["8"]["data"]
                                        self.name = GeT_Name(self.leader_id , Token)
                                        self.name = str(self.name)
                                        self.time = self.BesTo_data["5"]["data"]["1"]["data"]["4"]["data"]
                                        self.CliEnts.send(xSEndMsg(f"[b][c]\n Status InFo Of The PLayer : \n\n[{ArA_CoLor()}]PLayer Uid : {xMsGFixinG(self.target_id)}\nPLayer Status : His In Squid\nSquid s'Leader : {self.leader}\nLeader s'Name : {self.name}\nSquid Count : {self.group_count}/{self.group_count2 + 1}\nLast Login : {xMsGFixinG(datetime.fromtimestamp(self.time).strftime('%I:%M %p %d/%m/%y'))}\n\n[ffffff] Dev : Black\n", 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                        time.sleep(0.3)
                                        self.CliEnts.close() ; self.CliEnts2.close()
                                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                    elif self.h in [3 , 5]:
                                        self.CliEnts.send(xSEndMsg(f"[b][c]\n Status InFo Of The PLayer : \n\nPLayer Uid : {xMsGFixinG(self.target_id)}\nPLayer Status : In Game\nLast Login : {xMsGFixinG(datetime.fromtimestamp(self.time).strftime('%I:%M %p %d/%m/%y'))}\n\n[ffffff]  Dev : blackf-t\n", 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                        time.sleep(0.3)
                                        self.CliEnts.close() ; self.CliEnts2.close()
                                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                    else:
                                        self.CliEnts.send(xSEndMsg(f'\n[b][c][FFD700]FaiLEd GeTinG STaTus InFo\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                        time.sleep(0.3)
                                        self.CliEnts.close() ; self.CliEnts2.close()
                                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                except:pass
                        if False == self.Zx: self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] - PLease Use /status<id>\n - Ex : /status{self.Exemple}\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))	
                                                          
                        
                                                           
                    elif '/ayj' in self.input_msg[:3]:  
                        self.CliEnts.send(xSEndMsg(f'hhhh', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv)) 
                        time.sleep(0.3)   
                        self.CliEnts2.send(SPamSq(self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(1)
                        self.CliEnts2.send(AccEpT(self.DeCode_CliEnt_Uid , self.AutH , key , iv))

                    elif '/psps/' in self.input_msg[:6]:
                        self.id , self.nm = (self.input_msg[6:].split(" ", 1) if " " in self.input_msg[6:] else [self.input_msg[6:], "sponge japoni"])  
                        
                        
                        self.CliEnts.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] Preparing ghost for {xMsGFixinG(self.id)}...\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        
                        
                        self.CliEnts2.send(OpEnSq(key , iv))
                        time.sleep(1)  
                        
                        
                        self.CliEnts2.send(cHSq(5 , self.id , key , iv))
                        time.sleep(1)  
                        
                        
                        start_time = time.time()
                        while time.time() - start_time < 5: 
                            if '0500' in self.DaTa2.hex()[0:4] and len(self.DaTa2.hex()) > 30:
                                self.dT = json.loads(DeCode_PackEt(self.DaTa2.hex()[10:]))
                                if "5" in self.dT and "data" in self.dT["5"] and "31" in self.dT["5"]["data"]:
                                    sq = self.dT["5"]["data"]["31"]["data"]
                                    print(f"Successfully got squad code: {sq}")
                                    
                                    
                                    self.CliEnts2.send(SEnd_InV(1 , self.id , key , iv))
                                    time.sleep(3)
                                    
                                    
                                    self.CliEnts2.send(ExiT('000000' , key , iv))
                                    time.sleep(1)
                                    
                                    
                                    for i in range(10):  
                                        self.CliEnts2.send(ghost_pakcet(self.id , self.nm , sq , key , iv))
                                        time.sleep(0.5)
                                    
                                    self.CliEnts.send(xSEndMsg(f'\n[b][c][90EE90]Ghost sent successfully!\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                    break
                            time.sleep(0.1)
                        else:
                            self.CliEnts.send(xSEndMsg(f'\n[b][c][FF0000]Failed to get squad info!\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        
                        self.CliEnts.close(); self.CliEnts2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)

                    elif '/mit' in self.input_msg[:2]:#1750289322058798839_51s3raxooz
                            for i in range(100): 
                                self.CliEnts2.send(ghost_pakcet(self.DeCode_CliEnt_Uid ,'8679231987', '1750287629500765351_vfhkisb7hv' , key , iv))
                                time.sleep(0.1)     	    
                            self.CliEnts.send(xSEndMsg(f'\n[b][c]DONE  !\n', 2 , self.DeCode_CliEnt_Uid , self.DeCode_CliEnt_Uid , key , iv))           		      	            			      	
                except Exception as e:
                    self.CliEnts.close() ; self.CliEnts2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2)
                                    
    def GeT_Key_Iv(self , serialized_data):
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)
        timestamp , key , iv = my_message.field21 , my_message.field22 , my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp , key , iv    

    def Guest_GeneRaTe(self , uid , password):
        self.url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        self.headers = {"Host": "100067.connect.garena.com","User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)","Content-Type": "application/x-www-form-urlencoded","Accept-Encoding": "gzip, deflate, br","Connection": "close",}
        self.dataa = {"uid": f"{uid}","password": f"{password}","response_type": "token","client_type": "2","client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3","client_id": "100067",}
        try:
            self.response = requests.post(self.url, headers=self.headers, data=self.dataa).json()
            self.Access_ToKen , self.Access_Uid = self.response['access_token'] , self.response['open_id']
            time.sleep(0.2)
            print(' - Starting Black Freind BoT !')
            print(f' - Uid : {uid}\n - Password : {password}')
            print(f' - Access Token : {self.Access_ToKen}\n - Access Id : {self.Access_Uid}')
            return self.ToKen_GeneRaTe(self.Access_ToKen , self.Access_Uid)
        except Exception: ResTarT_BoT()    
                                        
    def GeT_LoGin_PorTs(self , JwT_ToKen , PayLoad):
        self.UrL = 'https://clientbp.ggwhitehawk.com/GetLoginData'
        self.HeadErs = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JwT_ToKen}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB51',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': 'clientbp.ggwhitehawk.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate, br',}       
        try:
                self.Res = requests.post(self.UrL , headers=self.HeadErs , data=PayLoad , verify=False)
                self.BesTo_data = json.loads(DeCode_PackEt(self.Res.content.hex()))  
                address , address2 = self.BesTo_data['32']['data'] , self.BesTo_data['14']['data'] 
                ip , ip2 = address[:len(address) - 6] , address2[:len(address) - 6]
                port , port2 = address[len(address) - 5:] , address2[len(address2) - 5:]             
                return ip , port , ip2 , port2          
        except requests.RequestException as e:
                print(f" - Bad Requests !")
        print(" - Failed To GeT PorTs !")
        return None, None   
        
    def ToKen_GeneRaTe(self , Access_ToKen , Access_Uid):
        self.UrL = "https://loginbp.ggwhitehawk.com/MajorLogin"
        self.HeadErs = {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion': 'OB51',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'Content-Length': '928',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host': 'loginbp.ggwhitehawk.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'}   
        self.dT = bytes.fromhex('1a13323032352d31302d33312030353a31383a3235220966726565206669726528013a07312e3131382e344232416e64726f6964204f532039202f204150492d3238202850492f72656c2e636a772e32303232303531382e313134313333294a0848616e6468656c64520c4d544e2f537061636574656c5a045749464960800a68d00572033234307a2d7838362d3634205353453320535345342e3120535345342e32204156582041565832207c2032343030207c20348001e61e8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e329a012b476f6f676c657c36323566373136662d393161372d343935622d396631362d303866653964336336353333a2010d3137362e32382e3133352e3233aa01026172b201203433303632343537393364653836646134323561353263616164663231656564ba010134c2010848616e6468656c64ca010d4f6e65506c7573204135303130ea014034653739616666653331343134393031353434656161626562633437303537333866653638336139326464346335656533646233333636326232653936363466f00101ca020c4d544e2f537061636574656cd2020457494649ca03203161633462383065636630343738613434323033626638666163363132306635e003b5ee02e803ff8502f003af13f803840780048c95028804b5ee0290048c95029804b5ee02b00404c80401d2043d2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f6c69622f61726de00401ea045f65363261623933353464386662356662303831646233333861636233333439317c2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f626173652e61706bf00406f804018a050233329a050a32303139313139303236a80503b205094f70656e474c455332b805ff01c00504e005c466ea05093372645f7061727479f80583e4068806019006019a060134a2060134b2062211541141595f58011f53594c59584056143a5f535a525c6b5c04096e595c3b000e61')
        current_time = str(datetime.now())[:-7].encode()
        self.dT = self.dT.replace(b'2025-07-30 14:11:20' , current_time)
        self.dT = self.dT.replace(b'4e79affe31414901544eaabebc4705738fe683a92dd4c5ee3db33662b2e9664f' , Access_ToKen.encode())
        self.dT = self.dT.replace(b'4306245793de86da425a52caadf21eed' , Access_Uid.encode())
        self.PaYload = bytes.fromhex(EnC_AEs(self.dT.hex()))  
        self.ResPonse = requests.post(self.UrL, headers = self.HeadErs ,  data = self.PaYload , verify=False)        
        if self.ResPonse.status_code == 200 and len(self.ResPonse.text) > 10:
            self.BesTo_data = json.loads(DeCode_PackEt(self.ResPonse.content.hex()))
            self.JwT_ToKen = self.BesTo_data['8']['data']           
            self.combined_timestamp , self.key , self.iv = self.GeT_Key_Iv(self.ResPonse.content)
            ip , port , ip2 , port2 = self.GeT_LoGin_PorTs(self.JwT_ToKen , self.PaYload)            
            return self.JwT_ToKen , self.key , self.iv, self.combined_timestamp , ip , port , ip2 , port2
        else:
            sys.exit()
      
    def Get_FiNal_ToKen_0115(self):
        token , key , iv , Timestamp , ip , port , ip2 , port2 = self.Guest_GeneRaTe(self.id , self.password)
        self.JwT_ToKen = token        
        try:
            self.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            self.AccounT_Uid = self.AfTer_DeC_JwT.get('account_id')
            self.EncoDed_AccounT = hex(self.AccounT_Uid)[2:]
            self.HeX_VaLue = DecodE_HeX(Timestamp)
            self.TimE_HEx = self.HeX_VaLue
            self.JwT_ToKen_ = token.encode().hex()
            print(f' - ProxCed Uid : {self.AccounT_Uid}')
        except Exception as e:
            print(f" - Error In ToKen : {e}")
            return
        try:
            self.Header = hex(len(EnC_PacKeT(self.JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(self.EncoDed_AccounT)
            self.__ = '00000000'
            if length == 9: self.__ = '0000000'
            elif length == 8: self.__ = '00000000  '
            elif length == 10: self.__ = '000000'
            elif length == 7: self.__ = '000000000'
            else:
                print('Unexpected length encountered')                
            self.Header = f'0115{self.__}{self.EncoDed_AccounT}{self.TimE_HEx}00000{self.Header}'
            self.FiNal_ToKen_0115 = self.Header + EnC_PacKeT(self.JwT_ToKen_ , key , iv)
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")
        self.AutH_ToKen = self.FiNal_ToKen_0115
        self.Connect_SerVer(self.JwT_ToKen , self.AutH_ToKen , ip , port , key , iv , ip2 , port2)        
        return self.AutH_ToKen , key , iv
def StarT_SerVer():

    FF_CLient('4237081864','2A7C44D6B2CC4ED08AC3CD86319E9E006594F86AA2FDCD94D5007A6B65545AEC')
StarT_SerVer() 