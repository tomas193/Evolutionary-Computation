import random
import math

objetos=int(input("\nobjetos: "))
cromosomas=int(input("poblacion: "))
tasa=float(input("Tasa de seleccion: "))
print("Poblacion: ")
pob=[]
for i in range(0,cromosomas):
    temp=[]
    for k in range(0,objetos):
        temp.append(random.randint(0,1))
    pob.append(temp)
    print(temp)

seleccion=math.ceil(cromosomas*tasa)

print("\nmadres:")
for i in range(0,math.floor(seleccion/2)):
    print(pob[i*2],end=', ')

print('\npadres:')
for i in range(0,math.ceil(seleccion/2)):
    print(pob[(i*2)+1],end=', ')
print("\n")

#Tomas Araujo 2023