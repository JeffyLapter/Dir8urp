from os import system
from modules import LOGO
from modules import main_LOGO
from modules import PRIMARY_COLOR_DEFINE
from modules import AVAILABLE_USER_SELECT
from rely import READ_HELP_DOUCUMENTS
USER_SELECTION='UNDEFINED'
while USER_SELECTION not in AVAILABLE_USER_SELECT:
    system('cls')
    main_LOGO()
    print("#-- Dir8urp is an Penetration testing tool, Which uses for WEB Penetration test --#")
    print("#-- THIS TOOL IS DEVELOPED BY JeffyLapter, alazymechnaic, HC1024 , NothingH")
    print("#-- Any unauthorized attack is "+PRIMARY_COLOR_DEFINE.WRONG("ILLEGAL")+", and the developer of the program is not liable for any legal disputes arising therefrom. --#")
    print('#-- TYPE "HELP" TO CHECK OUT HOW TO USE THIS TOOL --#')
    USER_SELECTION=input()#USER`S SELECTION
if AVAILABLE_USER_SELECT[USER_SELECTION] == 1:
    READ_HELP_DOUCUMENTS()
elif AVAILABLE_USER_SELECT[USER_SELECTION] == 2:
    print("burp begin")
