import json

with open('file_name_here') as f: 
    mydict = f.read() 

mydict = json.loads(mydict)

def dict_count(leksiko,vathos,max):
    length = len(leksiko)
    k = 0
    for i in leksiko.values():
        k += 1
        if k > 1 :
            vathos -= 1
        if type(i) == dict :
            vathos += 1
            if vathos > max :
                max = vathos
            vathos, max = dict_count(i,vathos,max)
        elif type(i) == list :
            vathos += 1
            if vathos > max :
                max = vathos
            vathos, max = list_count(i,vathos,max)
    
    return vathos, max;

def list_count(lista,vathos,max):
    length = len(lista)
    k = 0 
    for j in lista:
        k += 1
        if type(j) == dict :
            vathos += 1
            if vathos > max :
                max = vathos
            vathos, max = dict_count(j,vathos,max)
        elif type(j) == list :
            vathos += 1
            if vathos > max :
                max = vathos
            vathos, max = list_count(j,vathos,max)
        if k == length :
            vathos -=1
    
    return vathos, max;

print(mydict)
vathos = 2
max = -1 

if len(mydict) > 0 :
    vathos, max = dict_count(mydict,vathos,max)
    if max == -1 :
        vathos = 1
        print("Μέγιστο Βάθος :", vathos)
    else : 
        print("Μέγιστο βάθος: ", max)
else :
    vathos = 0
    print("Βάθος :", vathos)
