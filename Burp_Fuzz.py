from modules import Display_Color,PRIMARY_COLOR_DEFINE #COLORS
from modules import main_LOGO,main_LOGO_style_Blue,main_LOGO_style_Green,main_LOGO_style_Red,main_LOGO_style_LightRed
from modules import IDENTIFY_MAIN,ServerReplyStatus
from modules import Standard_URL_Convert,Check_Alive
import os
from urllib.parse import urlparse,parse_qs
import requests
from Dicts import header
import hashlib 
import threading
import time
#Dependence Payload Lib /sql_fuzz.txt,/ssrf_fuzz.txt,/xss_fuzz.txt,/parameter.txt
dictsLib=['/sql_fuzz.txt','/ssrf_fuzz.txt','/xss_fuzz.txt']
#Final Result List
Valid_Result=[]
#Get MD5 Function
def stringtomd5(originstr):
    signaturemd5 = hashlib.md5()
    signaturemd5.update(originstr.encode('utf-8'))
    return signaturemd5.hexdigest()
#Called in Thread
def Get_FuzzTest(url,dictPath):
    defaultpath=os.path.dirname(__file__)
    path=defaultpath+dictPath
    try:
        payload_dicts=open(path,'r',errors='ignore')
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Lake dicts named"+dictPath))
        return 
    payloads=[]
    for line in payload_dicts:
        line=payload_dicts.readline()
        payloads.append(line[:-1])
    parameter=parse_qs(urlparse(url).query)
    scheme=urlparse(url).scheme
    URL=scheme+'://'+urlparse(url).netloc
    test_response=requests.get(url=url,headers=header)
    el=['4','5']
    #Judge whether the URL is valid
    if(str(test_response.status_code)[0] in el):
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Url Unreachable"))
        return
    #Get MD5 from the usual page MD5
    Orign=stringtomd5(test_response.text)
    for key in parameter:
        for payload in payloads:
            parameter[key]=payload
            Test_result=requests.get(url=URL,headers=header,params=parameter)
            #Judge whether present payload is valid
            if(stringtomd5(Test_result.text)!=Orign):
                print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,ServerReplyStatus[str(Test_result.status_code)]+"--->"+key+"="+payload))
                Valid_Result.append(key+"="+payload)
            else:
                print(ServerReplyStatus[str(Test_result.status_code)]+"--->"+key+"="+payload)
    #Read Parameter dicts
    try:
        parameter_dicts=open(defaultpath+'/parameter_fuzz.txt','r',errors='ignore')
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Lake dicts named"+dictPath))
        return 
    param=[]
    for line in parameter_dicts:
        line=parameter_dicts.readline()
        param.append(line[:-1])
    for param_payload in param:
        for payload in payloads:
            parameter[param_payload]=payload
            Test_result=requests.get(url=URL,headers=header,params=parameter)
            if(stringtomd5(Test_result.text)!=Orign):
                print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,ServerReplyStatus[str(Test_result.status_code)]+"--->"+key+"="+payload))
                Valid_Result.append(key+"="+payload)
            else:
                print(ServerReplyStatus[str(Test_result.status_code)]+"--->"+key+"="+payload)
        del parameter[param_payload]

#Define Thread    
class RunThread(threading.Thread):
    def __init__(self,url,Dict_path):
        threading.Thread.__init__(self)
        self.Url=url
        self.path=Dict_path
    def run(self):
        Get_FuzzTest(self.Url,self.path)




#Start Function Here! Fuzz all API
def Run_Fuzz_now(url):
    #SQL Fuzz Thread
    sql_thread=RunThread(url,dictsLib[0])
    sql_thread.start()
    #Xss Fuzz Thread
    Xss_thread=RunThread(url,dictsLib[1])
    Xss_thread.start()
    #ssrf Fuzz Thread
    ssrf_thread=RunThread(url,dictsLib[2])
    ssrf_thread.start()
    while(1):
        time.sleep(1)
        #check whether threads Completed operation
        if(ssrf_thread.is_alive() and Xss_thread.is_alive() and sql_thread.is_alive()):
            continue
        else:
            print("Valid Payload:")
            for i in Valid_Result:
                print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,i))
        

def Burp_Fuzz():
    main_LOGO_style_Green()
    print("\nFUZZ target:")
    url_raw=input()
    url_in=Standard_URL_Convert(url_raw)
    Check_Alive(url_in)
    Run_Fuzz_now(url_in)
    
#Example Here

#Run_Fuzz_now("http://39.106.97.149/?a=1&b=2")
