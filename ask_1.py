import random
from random import randrange
import numpy as np
import math

def cross_count(plithos_tetradwn): #orizontio metrima
    metr_tetr = 0
    for i in range(n):
        metr_tetr = 0
        for j in range(n):
            if p[i][j] == 1:
                metr_tetr += 1
            else:
                metr_tetr = 0
            if metr_tetr == 4:
                plithos_tetradwn += 1
                metr_tetr -= 1 
    return plithos_tetradwn

def down_count(plithos_tetradwn): #katheto metrima
    metr_tetr = 0
    for j in range(n):
            metr_tetr = 0
            for i in range(n):
                if p[i][j] == 1:
                    metr_tetr += 1
                else:
                    metr_tetr = 0
                if metr_tetr == 4:
                    plithos_tetradwn += 1
                    metr_tetr -= 1 
    return plithos_tetradwn

def left_diagonal_count(plithos_tetradwn): #panw aristera pros katw deksia
    for i in range(n-3):
        metr_tetr = 0 
        for j in range(n-3):
            k1 = i
            k2 = j
            while k1 <= i+3 and k2 <= j+3 :
                if p[k1][k2] == 1 :
                    metr_tetr += 1
                    if metr_tetr == 4 :
                        plithos_tetradwn += 1
                        metr_tetr = 0
                    k1 += 1
                    k2 += 1
                else:
                    metr_tetr = 0
                    break
                
    return plithos_tetradwn

def right_diagonal_count(plithos_tetradwn): #katw aristera pros panw deksia
    for i in range(n-1,2,-1):
        metr_tetr = 0 
        for j in range(n-3):
            k1 = i
            k2 = j
            while k1 >= i-3 and k2 <= j+3 :
                if p[k1][k2] == 1 :
                    metr_tetr += 1
                    if metr_tetr == 4 :
                        plithos_tetradwn += 1
                        metr_tetr = 0
                    k1 -= 1
                    k2 += 1
                else:
                    metr_tetr = 0
                    break
                
    return plithos_tetradwn

n = 8 #diastash
plithos_thesewn = n**2
plithos_monadwn = math.ceil(plithos_thesewn/2)

sum = 0 #sunolo tetradwn
for k in range(100):
    p = []
    for i in range(plithos_thesewn):
        p.append(0)


    metritis = 1
    while metritis <= plithos_monadwn :
        i = randrange(plithos_thesewn)
        if p[i] == 0 :
            p[i] = 1 
            metritis += 1
        else:
            continue

    p = np.reshape(p,(n,n))
    print(p)
    plithos_tetradwn = 0
    plithos_tetradwn = cross_count(plithos_tetradwn)
    plithos_tetradwn = down_count(plithos_tetradwn)
    plithos_tetradwn = left_diagonal_count(plithos_tetradwn)
    plithos_tetradwn = right_diagonal_count(plithos_tetradwn)
    print(plithos_tetradwn)
    sum += plithos_tetradwn

avg = sum/100 #mesos oros tetradwn
print(avg)
