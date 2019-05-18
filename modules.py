#Errors=
SeverReplyStatus={
    '200':'[+] 200 OK',
    '204':'[+] Sever Returned status 204',
    '302':'[!] Sever Returned status 302 redirect',
    '403':'[-] 403-Forbidden',
    '404':'[-] 404 Not Found',
    '405':'[-] 405 ERROR',
    '408':'[-] Request Time out',
    '500':'[-] Sever ERROR 500',
    '503':'[-] Sever Error 503'

}
from simhash import Simhash
from Dicts import header
import requests
#THIS IS THE FUN to identify the result of replys
def getReplyStatusNumber(replys):
    return replys[11:-2]
#THIS IS THE FUN to ana the res of reply
def GetReplyStatus(ReplyStatusNumber):
    try:
        print(SeverReplyStatus[ReplyStatusNumber]) 
    except:
        print('Unknown error')  

#test=str(requests.get('http://39.106.97.149/151351531.txt'))
#method: GetReplyStatus(getReplyStatusNumber(test))
#THIS IS THE FUN TO CHECK THE URL;

#def precheck(inputs):
"""
def precheck(inputs):
    if inputs[0:5] == "http:":
        if inputs[:-1]!='/':
            return inputs
        else:
            inputs[:-1]=''
            return inputs
    else:
        return "http://"+inputs
"""

#The FUN to identify 404:
def identify404(domain,nowdomain):
    page4041=requests.get(domain+'/dgasgdfsdf.txt',headers=header)
    page4042=requests.get(domain+'/dfag04ggg00dfw32a.xpd',headers=header)
    pagenow=requests.get(nowdomain,headers=header)
    debugcode=[403,405,500,503,302,301]
    if pagenow.status_code == 404:
        return False
    if pagenow.status_code in debugcode:
        print(SeverReplyStatus[str(pagenow.status_code)])
    hash_page4041=Simhash(str(page4041.content))
    hash_page4042=Simhash(str(page4042.content))
    hash_pagenow=Simhash(str(pagenow.content))
    if hash_page4041.distance(hash_page4042) != 0:
        print("[!] Maybe different returns,check yourself: "+nowdomain)
    else:
        if hash_pagenow.distance(hash_page4041) < 3:
            return False
        else:
            return True

"""
test1=requests.get('http://www.baidu.com/dgagasgf.txt')
test2=requests.get('http://www.baidu.com/')
print(test1.content)
a=Simhash(str(test1.content))
b=Simhash(str(test2.content))
print(a.distance(b))
"""
"""
class id_404:
    def __init__(self,domain):
        self._page404=[]
        self._url404=[]
        self._path404=["gawrgfsdfwagrsdfgwwwasdfvv"]
        self._rcode404=[200,302,301]
        for 404path in self._path404:
            for 404path in self._path404:
                if domain[-1]=='/':
                    url=domain+404path
                else:
                    url=domain+'/'+ 404path
                response=requests.get(url)
                if response.status_code in self._rcode404:
                    self.check_next(response.content,url)
    
    def check_next(self, _page404, _url404):
        if _page404 not in self._page404:
            self._page404.append(_page404)
        if _url404 not in self._url404:
            self._url404.append(_url404)
    
    def judegesim(self, page_1,page_2):
        page_1_hash=Simhash(page_1)
        page_2_hash=Simhash(page_2)
        sim=page_1_hash.distance(page_2_hash)
        if sim > 3:
            return True
        else:
            return False
    def is404(self,url):
        if url in self
"""
def SerachURL(URLstr):
    count=len(URLstr)
    fnum=0
    for i in range(count-1,-1,-1):
        if URLstr[i]=='/' and URLstr[i-1]=='/':
            fnum=i+1
            break
        elif not((URLstr[i]>='a' and URLstr[i]<='z') or (URLstr[i]>='A' and URLstr[i]<='Z') or (URLstr[i]>='0' and URLstr[i]<='9') or URLstr[i]=='+' or URLstr[i]=='/' or URLstr[i]=='?' or URLstr[i]=='%' or URLstr[i]=='#' or URLstr[i]=='&' or URLstr[i]=='=' or URLstr[i]=='.'):
            fnum=i+1
            break
    newURLstr=URLstr[fnum:count]
    if newURLstr[count-fnum-1]=='/':
        CorrectURL="http://"+URLstr[fnum:count-1]
    else:
        CorrectURL="http://"+URLstr[fnum:count]
    return CorrectURL
