import os
header={"headers":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
          (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
#print(os.path.dirname(__file__))
def AddDictsPrimary():
    defaultpath=os.path.dirname(__file__)
    path=input("Please input the path of your dicts:")
    #IF THE PATH UNSET USE THE DEFALUT PATH
    if path=='':
        print("Prepare to use the default dicts in E:/python/PYVSC/4/dicts.txt")
        path=defaultpath+r"\dicts.txt"
    dictsread=open(path,'r')
    DICTSOUTPUT=list()
    OUTRANGE=list()
    for line in open(path):
        line=dictsread.readline()
        DICTSOUTPUT.append(line)
    for single in DICTSOUTPUT:
        OUTRANGE.append(single[0:-1])
    return OUTRANGE
