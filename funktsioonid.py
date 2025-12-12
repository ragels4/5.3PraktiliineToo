from random import *

#добавил a, b в скобки
def vahetus(a, b):
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n,loend,a,b):
    #добавил букву n в скобки и добавил один tab после 11 строчки и правильно написал loend.append
    for i in range(n):
        loend.append(randint(a,b))
    
def jagamine(loend: list, p: list, n: list, nol: list):
    for el in loend:
        if el>0:
            p.append(el)  # исправил правильно append
        elif el<0:        #убрал лишнее двоеточие
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    #правильно поставил табы
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    #правильно написал функцию
    loend.append(el)
    loend.sort()
