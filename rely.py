
from simhash import Simhash
import requests
from Dicts import header
from modules import SeverReplyStatus
"""
test1=requests.get('https://blog.csdn.net/csdnnews/article/details/dddssc.kl',headers=header)
test2=requests.get('https://blog.csdn.net/csdnnews/article/dddddddddddddcx.vdd',headers=header)
a=Simhash(str(test1.content))
b=Simhash(str(test2.content))
print(a.distance(b))
"""


def identify404(domain,nowdomain):
    page4041=requests.get(domain+'/dgasgdfsdf.txt',headers=header)
    page4042=requests.get(domain+'/dfag04ggg00dfw32a.xpd',headers=header)
    pagenow=requests.get(nowdomain,headers=header)
    debugcode=[403,405,500,503,302,301]
    if pagenow.status_code in debugcode:
        print(SeverReplyStatus[str(pagenow.status_code)])
    hash_page4041=Simhash(str(page4041.content))
    hash_page4042=Simhash(str(page4042.content))
    hash_pagenow=Simhash(str(pagenow.content))
    if hash_page4041.distance(hash_page4042) != 0:
        print("Maybe different returns,check yourself: "+nowdomain)
    else:
        if hash_pagenow.distance(hash_page4041) < 3:
            return False
        else:
            return True

if identify404(r"https://www.inspc.org.cn",r"https://www.inspc.org.cn"):
    print("true")
else:
    print("sss")
