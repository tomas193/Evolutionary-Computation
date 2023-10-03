import random
import math

objetos=int(input("\nLongitud de cromosoma: "))
cromosomas=int(input("Tamano de poblacion: "))
tasa=float(input("Tasa de seleccion: "))
print("Poblacion Inicial: ")
pob=[]
for i in range(0,cromosomas):
    temp=[]
    for k in range(0,objetos):
        temp.append(random.randint(0,1))
    pob.append(temp)
    print(temp)

seleccion=math.ceil(cromosomas*tasa)

def madre():
    m_ar=[]
    print("\nmadres:")
    for i in range(0,math.floor(seleccion/2)):
        m_ar.append(pob[random.randint(0,seleccion-1)])
    return(m_ar)

def padre():
    p_ar=[]
    print('\npadres:')
    for i in range(0,math.ceil(seleccion/2)):
        p_ar.append(pob[random.randint(0,seleccion-1)])
    return(p_ar)

print(madre())
print(padre())

#Tomas Araujo 2023
