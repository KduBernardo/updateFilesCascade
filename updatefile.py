import sys


def filestream(filepath):
    item = []
    with open(filepath,'r') as file:
         for line in file:
             item.append(line)
    return item



def go(fsplit,lsplit):
    filebase = sys.argv[1]
    listitem = filestream(filebase)
    filepath = sys.argv[2]
    linesfile = filestream(filepath)
    dicio = {}
    out = ''
    for i in listitem:
        k = i.split(',')[0]
        v = i.split(',')[1]
        dicio[str(k)] = str(v).strip()
    for i in linesfile:
        for k, v in dicio.items():
            i = i.replace(str(k+fsplit), str(v+lsplit))
        out = out+i
    fileout = open(str(filepath+'.new'), 'w')
    fileout.write(out)
    fileout.close()


param1=','
param2=' '
go(param1,param2)


