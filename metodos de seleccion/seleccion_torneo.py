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
print("pesos objetos:")
print(pesos)
print("valores objetos: ")
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
del pesos_cromosomas
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
nkeep=math.ceil(cromosomas*tasa)
piscina=[]
print("\n\tpoblación reparada\tFitness de cromosomas:")
for k in range(0,len(pob)):
    if k<nkeep:
        piscina.append(pob[k])
    print(k,'\t',pob[k],'\t',profit[k][0])

print('piscina apareamiento: ')
print(piscina)

flag=True
padre=[]
madre=[]
for k in range(0,len(piscina)):
    aux=[]
    for i in range(0,3):
        aux.append(profit[random.randint(0,len(piscina)-1)])
    print('\nseleccionados aleatoriamente: \n',aux)
    print('fitness mas alto: ',max(aux)[0])
    print('indice del cromosoma ganador:',max(aux)[1])

    if flag==True:
        padre.append(piscina[max(aux)[1]])
        flag=False
    else:
        madre.append(piscina[max(aux)[1]])
        flag=True

print('\npadres: \n',padre)
print('madres: \n',madre)

#Tomas Araujo 2023