from simhash import Simhash
from Dicts import header
import requests
from colorama import Fore, Back, Style, init  # THE COLORAMA USED FOR DISPLAY COLORED NOTES

init(autoreset=True)  # -- AUTO RESET THE COLOR OF OUTPUTS --#

# -- =======================RAW DATA AERA=================================== --#
# --* Below are some raw data for extended modules to call with *--#
# -- $ServerReplyStatus is used for external function to call with in order to display the error reply of the Server --#
SeverReplyStatus = {
    '200': '[+] 200 OK',
    '204': '[+] Sever Returned status 204',
    '302': '[!] Sever Returned status 302 redirect',
    '403': '[-] 403-Forbidden',
    '404': '[-] 404 Not Found',
    '405': '[-] 405 ERROR',
    '408': '[-] Request Time out',
    '500': '[-] Sever ERROR 500',
    '503': '[-] Sever Error 503'

}
LOGO = {
    1: r'    ____      _           ____                        ',
    2: r'   / __ \\   (_)  ____   ( __ )   __  __   _____   ____',
    3: r'  / / / /  / /  / ___/  / __  |  / / / /  / ___/  / __ \\',
    4: r' / /_/ /  / /  / /     / /_/ /  / /_/ /  / /     / /_/ /',
    5: r'/_____/  /_/  /_/      \____/   \__,_/  /_/     / .___/ ',
    6: r'                                               /_/      '
}

# -- =======================RAW DATA AERA=================================== --#
'''---------------------------RAW DATA AERA ENDS RIGHT HERE-----------------'''

'''#-- =====================================================================================FUNCTION AERA============================================================= --#'''

"""==================--WRITTEN BY LapterGrsd--====================-"""


# ------------------COLOR_PRIMARY_DEFINE----------------------------------#
# -- THE FUNCTION TO CHANGE THE OUTPUT COLOR --#
# -- USAGE: print (Display_Color.LOGO(PRIMARY_COLOR_DEFINE,"stes")) --#
class Display_Color(object):
    def WRONG(self, s):
        return Fore.RED + s + Fore.RESET

    def SUCCESS(self, s):
        return Fore.GREEN + s + Fore.RESET

    def WARNING(self, s):
        return Fore.YELLOW + s + Fore.RESET

    def LOGO(self, s):  # -- COLOR
        return Fore.MAGENTA + s + Fore.RESET
PRIMARY_COLOR_DEFINE = Display_Color()  # -- THE CLASS FOR COLORED OUT PUTS --#


# ---------------------main_LOGO-----------------------------------------#
# -- FUNCTION TO DISPLAY LOGO --#
def main_LOGO():
    for i in range(1, 7):
        print(Display_Color.LOGO(PRIMARY_COLOR_DEFINE, LOGO[i]))

main_LOGO()


# --------------------get_Reply_StatusNumber-------------------------------#
# -- Function to get a returned status code and convert it to str --#
# -- ! NOTICE: FUNCTION OUT OF STYLE, MAY CAUSE ERRORS ! --#
def get_Reply_StatusNumber(replys):
    return replys[11:-2]


# -----------------------Display_Reply_Status-------------------------------#
# -- Function to Display the Returned Results --#
# -- Function takes two param,P1 as the ERROR list dict,P2 as the Reply_status of the server. --#
def Display_Reply_Status(ERROR_LIST, ReplyStatusNumber):
    try:
        print(ERROR_LIST[ReplyStatusNumber])
    except:  # -- The Function needed to be rewrite, in order to deal the unknown error as more s possible --#
        print('Unknown error')


# --------------------------identify_404------------------------------------#
# -- Main Function to identify 404 and wrong replys with status 200 --#
# -- domain uses as url trying to judge whether it existed or not, nowdomain display the error msg --#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def identify_404(domain, nowdomain):
    try:
      page4041 = requests.get(domain + '/dgasgdfsdf.txt', headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except requests.exceptions.ChunkedEncodingError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "There is something wrong! \n ChunkedEncodingError!\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    try:
      page4042 = requests.get(domain + '/dfag04ggg00dfw32a.xpd', headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    try:
      pagenow = requests.get(nowdomain, headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    debugcode = [403, 405, 500, 503, 302, 301]
    if pagenow.status_code == 404:
        return False
    if pagenow.status_code in debugcode:
        print(SeverReplyStatus[str(pagenow.status_code)])
    try:
        hash_page4041 = Simhash(str(page4041.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    try:
        hash_page4042 = Simhash(str(page4042.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    try:
        hash_pagenow = Simhash(str(pagenow.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    if hash_page4041.distance(hash_page4042) != 0:  # Check whether 404 has different echos
        print("[!] Maybe different returns,check yourself: " + nowdomain)
    else:
        if hash_pagenow.distance(hash_page4041) < 3:
            return False
        else:
            return True


"""-----------------LAPTER GRSD!S AEERA ENDS RIGHT HERE------------------"""

'''#-=============================--- WRITTEN BY NOTHING_H -==================================-#'''


# -- main Function to convert url to standard url --#
# -- FUNCTION receive one str param,returns a standard url like "http://example.com/admin" --#
def Standard_URL_Convert(URLstr):
    count = len(URLstr)
    fnum = 0
    for i in range(count - 1, -1, -1):
        if URLstr[i] == '/' and URLstr[i - 1] == '/':
            fnum = i + 1
            break
        elif not ((URLstr[i] >= 'a' and URLstr[i] <= 'z') or (URLstr[i] >= 'A' and URLstr[i] <= 'Z') or (
                URLstr[i] >= '0' and URLstr[i] <= '9') or URLstr[i] == '+' or URLstr[i] == '/' or URLstr[i] == '?' or
                  URLstr[i] == '%' or URLstr[i] == '#' or URLstr[i] == '&' or URLstr[i] == '=' or URLstr[i] == '.'):
            fnum = i + 1
            break
    newURLstr = URLstr[fnum:count]
    if newURLstr[count - fnum - 1] == '/':
        CorrectURL = "http://" + URLstr[fnum:count - 1]
    else:
        CorrectURL = "http://" + URLstr[fnum:count]
    return CorrectURL


# -------------------------------Standard_URL_Convert-------------------------#
'''#-=-----------------=Nothing_H !S AREA ENDS RIGHT HERE===--------------------------------==-#'''

'''#-- =============================================================== FUNCTION AERA END RIGHT HERE ============================================================= --#'''

# -- BELOW ARE FUNCTIONS UNUSED --#
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
