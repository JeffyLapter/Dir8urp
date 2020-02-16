from modules import PRIMARY_COLOR_DEFINE,Display_Color
import os
HELP_DOUCUMENT="""
    --THIS IS A PRIMARY HELP DOC OF THE TOOLS--
    type "DB" to use the Directory Burp module,
    type "FUZZ" to use the FUZZ Burp module,
    type "HELP" to show this Document
    type CTRL+Z to get back to the primary Selector to start your use

"""
def READ_HELP_DOUCUMENTS():
    #print("#  ---  Dir8urp Help Doucumention v0.1 alpha  ---  #\n"+Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,HELP_DOUCUMENT))
    print("#  ---  Dir8urp Help Doucumention v0.1 alpha  ---  #\n"+Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,HELP_DOUCUMENT))
    try:
        input()
    except EOFError:
        pass