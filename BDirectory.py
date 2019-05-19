from modules import Display_Color,PRIMARY_COLOR_DEFINE #COLORS
from modules import main_LOGO,main_LOGO_style_Blue,main_LOGO_style_Green,main_LOGO_style_Red,main_LOGO_style_LightRed
from modules import IDENTIFY_MAIN
from os import system

system('cls')
main_LOGO_style_LightRed()
TEST=IDENTIFY_MAIN()
URL="http://jggz.jinan.cn"
LIST=IDENTIFY_MAIN.Add_Hash_Library(TEST,URL)
print(IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL))


#PPP1=requests.get(URL)
#PPP2=str(PPP1.content)
#ppp3=Simhash(PPP2)
#print(ppp3.value)
#print(LIST)
#class BD_MAIN_IDENTIFY_EXISTING(object):
'''main_LOGO()
main_LOGO_style_Blue()
main_LOGO_style_Green()
main_LOGO_style_Red()'''


    



