from modules import Display_Color,PRIMARY_COLOR_DEFINE #COLORS
from modules import main_LOGO,main_LOGO_style_Blue,main_LOGO_style_Green,main_LOGO_style_Red,main_LOGO_style_LightRed
from modules import IDENTIFY_MAIN
from os import system
from modules import Standard_URL_Convert
from Dicts import AddDictsPrimary
def BDirectory():
    system('cls')
    main_LOGO_style_Blue()
    TEST=IDENTIFY_MAIN()
    URL=''
    try:
        URL= input("Please input your url:"+" "*5+ "eg:http://example.com/\n")
        while URL == '':
            URL=input(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"CAN`T BE EMPTY URL,TRY AGAIN:\n"))
        URL= Standard_URL_Convert(URL)
    except EOFError:
        exit(0)
    #URL CONVERTED TO A STANDARD ONE http://admin.com
    print(Display_Color.WARNING(PRIMARY_COLOR_DEFINE,"Assuming to Build A Hash Library of the Target Site:"+URL))
    LIST=IDENTIFY_MAIN.Add_Hash_Library(TEST,URL)
    print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,"Hash Library Created Successfully, Preparing to Burp"))
    burppath=AddDictsPrimary()
    #print(burppath)
    print("Result Given Below:\n")
    for path in burppath:
        NOWURL=URL+'/'+path
        IDENTIFY_MAIN.DISPLAY_MAIN(TEST,NOWURL,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,NOWURL))
    input(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,"TYPE ANY THING TO GET BACK TO THE PRIMARY MENU:"))
#BDirectory()







"""URL="http://jggz.jinan.cn/col/col1863/index.hom"
LIST=IDENTIFY_MAIN.Add_Hash_Library(TEST,URL)
#print(IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL))
IDENTIFY_MAIN.DISPLAY_MAIN(TEST,URL,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL))
URL1="http://jggz.jinan.cn/col/col1863/index.html"
IDENTIFY_MAIN.DISPLAY_MAIN(TEST,URL1,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL1))
URL2="http://jggz.jinan.cn/col/col1863/admin.log"
IDENTIFY_MAIN.DISPLAY_MAIN(TEST,URL2,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL2))
URL3='http://jggz.jinan.cn/art/'
IDENTIFY_MAIN.DISPLAY_MAIN(TEST,URL3,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,URL3))
"""
#IDENTIFY_MAIN.DISPLAY_MAIN(TEST,$URL2,IDENTIFY_MAIN.IDENTIFY_FUNCTION(TEST,LIST,$URL2))

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


    



