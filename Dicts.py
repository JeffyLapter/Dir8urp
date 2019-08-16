import os
header={"headers":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
          (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
Dicts_of_404_Pages_Path=['/22243dddddsafatxt','/22222fsadffg22html','/23555ffgd2affDD4html','/sdasgrr3eeasdfsvvcatxt','/24gej040re2nasdf244.orm','/../ggeerv4513ddav.php','/../../4gej040re2nasdf244.orm','/../../../4gej040re2nasdf244.orm','/../../../../4gej040re2nasdf244.orm','/../../../../../4gej040re2nasdf244.orm','/../../../../../../4gej040re2nasdf244orm','/../../../../../../../../4gej040re2nasdf244orm']


#print(os.path.dirname(__file__))
def AddDictsPrimary():
    defaultpath=os.path.dirname(__file__)
    path=input("Please input the path of your dicts:")
    #IF THE PATH UNSET USE THE DEFALUT PATH
    if path=='':
        path=defaultpath+r"\dicts.txt"
        print("Prepare to use the default dicts in "+path+'\n')
    dictsread=open(path,'r',errors='ignore')
    DICTSOUTPUT=list()
    OUTRANGE=list()
    for line in open(path,errors='ignore'):
        line=dictsread.readline()
        DICTSOUTPUT.append(line[1:])
    for single in DICTSOUTPUT:
        OUTRANGE.append(single[0:-1])
    return OUTRANGE
