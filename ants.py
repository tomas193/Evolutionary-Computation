import random

weights=[70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
profits=[135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]

c=750 #knapsack capacity
tasa_ev=0.5
hormigas=10
profit_backpack=0

def mu(profit,weight):
    u=profit/(weight**2)
    return u

objetos=len(weights)

def select_objects():
    #selecciona 3 objetos aleatorios y escoje 1 dependiendo de su probabilidad
    objetos=[]
    mus=[]
    probas=[]
    suma=0

    for i in range(0,3): #se insertan 3 objetos
        objeto=[]
        num=random.randint(0,14) #seleccionar objeto aleatorio
        objeto.append(weights[num])
        objeto.append(profits[num])
        u=mu(profits[num],weights[num]) #calcular atractividad
        mus.append(u)
        suma+=u
        objetos.append(objeto) #insertar objeto con peso y profit a una lista temporal
    del objeto
    del num

    for i in mus: #calcular probabilidad de cada objeto
        probas.append(i/suma)

    lim1=probas[0]
    lim2=lim1+probas[1]
    num=(random.uniform(0,1))
    #print(num)

    if num<lim1:
        return(objetos[0])
    elif lim1<=num<lim2:
        return(objetos[1])
    else:
        return(objetos[2])

def partial_sol():
    vc=c
    pp=0
    profit=0
    parcial=[]
    datos=[] #[peso total, profit total]
    while vc>0:
        objeto=select_objects()
        parcial.append(objeto)
        vc-=objeto[0]
        pp+=objeto[0]
        profit+=objeto[1]
    
    datos.append(pp)
    datos.append(profit) 
    parcial.sort()
    return(parcial,datos)

def reparacion():
    #se sacan objetos para nivelar el peso
    reparar=partial_sol()
    parcial=reparar[0]
    datos=reparar[1]

    for i in parcial:
        if i[0]>=datos[0]-c:
            datos[1]-=i[1]
            datos[0]-=i[0]
            parcial.pop(parcial.index(i))
            break
    sol=[]
    sol.append(parcial)
    sol.append(datos)
    return(sol)

def soluciones():
    sol=[]
    datos=[]
    for i in range(0,hormigas):
        rep=reparacion()
        sol.append(rep[0])
        datos.append(rep[1])

    for i in datos:
        i[0],i[1]=i[1],i[0]

    solucion=[]
    idx=datos.index(max(datos))
    solucion.append(sol[idx])
    solucion.append(datos[idx])
    return(solucion)

def solucion_final():
    sol=[]
    datos=[]
    solucion=[]

    for i in range(0,1000):
        temp=soluciones()
        sol.append(temp[0])
        datos.append(temp[1])

    idx=datos.index(max(datos))
    solucion.append(sol[idx])
    solucion.append(datos[idx])
    print('profit: ',solucion[1][0], 'peso: ',solucion[1][1],'\t',solucion[0])

solucion_final()

#Jorge Tomás Araujo González 2023
