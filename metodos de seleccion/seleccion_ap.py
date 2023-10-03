import random
import math

objetos=int(input("\nobjetos: "))
cromosomas=int(input("poblacion: "))
tasa=float(input("Tasa de seleccion: "))
pob=[]
for i in range(0,cromosomas):
    temp=[]
    for k in range(0,objetos):
        temp.append(random.randint(0,1))
    pob.append(temp)
    print(temp)

nkeep=math.ceil(cromosomas*tasa)
sum=0
pn=[]
sumpi=[]
for i in range(0,nkeep):
    sum+=(i+1)
aux=0
for k in range(1,nkeep+1):
    pn.append((nkeep-k+1)/sum)
    aux+=pn[k-1]
    sumpi.append(aux)

print('\npn:',pn)
print('sumpi:',sumpi)
print('\n')
padre=[]
madre=[]
sel=True
print('numero aleatorio','\tsumpi correspondiente')
for i in range(0,nkeep):
    aleatorio=random.random()
    print(aleatorio,end=' ')
    k=0
    while True:
        if aleatorio<sumpi[k]:
            break
        k+=1
    if sel==True:
        padre.append(pob[k])
        sel=False
    else:
        madre.append(pob[k])
        sel=True
    print(sumpi[k])

print('\npadre: ',padre)
print('madre: ',madre)

#Tomas Araujo 2023
