#es1

import random 
x= random.randint(0,50)
y= random.randint (0,50)
z= random.randint (0,50)
if x<y and x<z:
    print (x)
    if y<z:
        print (y)
        print (z)
    else:
        print (z)
        print (y)
elif y<z:
    print (y)
    if x<z:
        print (x)
        print (z)
    else:
        print (z)
        print(x)
else:
    print (z)
    if x<y:
        print (x)
        print (y)
    else:
        print (y)
        print(x)


#es 2 

auto=['auto','bauto','cauto','dauto','euto']
moto=['gatto','hatto','ratto','patto']
listone=auto + moto
listone.sort ()
print (listone)

#es 3

lista=[]
for i in range (50):
    lista.append (random.randint (0,1000))
listadispari =[]
for x in lista :
    if x%2==1:
        listadispari.append(x)
lista=listadispari
print (lista)


#es4
lista=[]
valore=0
for i in range (50):
    lista.append(random.randint(1,100))
for x in lista:
    if x>50 or x<10:
        print(x)
valore= valore+1
print (valore)
