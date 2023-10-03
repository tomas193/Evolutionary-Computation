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

pesos=[]
valores=[]
knap_full=False
v=0
for i in range(0,objetos):
    pesos.append(random.uniform(1,10))
    valores.append(pesos[i]+5)
    v+=pesos[i]
v=v/2 #capacidad mochila

print("\ncap. mochila: ",v)
print("pesos:")
print(pesos)
print("valores: ")
print(valores)
print("\npoblación original:")
for k in range(0,len(pob)):
    print(pob[k])

def sum(pob,pesos):
    sum=0
    for i in range(0,len(pob)):
        sum+=pesos[i]*pob[i]
    if sum>v:
        knap_full=True
    else:
        knap_full=False
    return(knap_full,sum)

def sacar_objetos(pob):
    i=0
    while True:
        pob[i]=0
        if sum(pob,pesos)[0]==False:
            break
        i+=1
    return(pob)

def insertar_objetos(pob):
    i=0
    while True:
        if i>=len(pob):
            break
        pob[i]=1
        if sum(pob,pesos)[0]==True:
            pob[i]=0
        i+=1
    return(pob)

pesos_cromosomas=[]
def peso_cromosoma(crom):
    temp=0
    for x in range(0,len(crom)):
        temp+=crom[x]*pesos[x]
    pesos_cromosomas.append(temp)

for i in range(0,cromosomas):
    peso_cromosoma(pob[i])
    if sum(pob[i],pesos)[0]==True:
        sacar_objetos(pob[i])
        insertar_objetos(pob[i])
    else:
        insertar_objetos(pob[i])

del pesos
del knap_full
profit=[]

for i in range(0,cromosomas):
    aux=[]
    sum=0
    for k in range(0,objetos):
        sum+=valores[k]*pob[i][k]
    aux.append(sum)
    aux.append(i)
    profit.append(aux)
del valores
print("\npoblación reparada con valores:")
for k in range(0,len(pob)):
    print(pob[k], profit[k][0])

profit.sort()

print("\npoblación reparada con valores ordenados:")
for k in range(0,len(pob)):
    print(pob[profit[k][1]], profit[k][0])

pn=[]
cn=[]
sumpi=[]
sum=0
nkeep=math.ceil(cromosomas*tasa)
for i in range(0,nkeep):
    sum+=(i+1)
    cn.append(profit[i][0]-max(profit)[0])
aux=0
for k in range(1,nkeep+1):
    pn.append((nkeep-k+1)/sum)
    aux+=pn[k-1]
    sumpi.append(aux)
print("\ncostos normalizados: ",cn)
print("probabilidades: ",pn)
print("suma de probabilidades: ",sumpi)

padre=[]
madre=[]
sel=True
print('\nnumero aleatorio','\tsumpi correspondiente')
for i in range(0,nkeep):
    aleatorio=random.random()
    print(aleatorio,end='\t')
    k=0
    while True:
        if aleatorio<sumpi[k]:
            break
        k+=1
    if sel==True:
        padre.append(pob[profit[k][1]])
        sel=False
    else:
        madre.append(pob[profit[k][1]])
        sel=True
    print(sumpi[k])

print('\npadre: ',padre)
print('madre: ',madre)

#Tomas Araujo 2023
