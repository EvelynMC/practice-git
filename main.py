# Variables
## Las variables asumen el tipo de dato una vez que se les asigna un valor.

boolean = True # True or False
integer = 10
cadenita = "Esta es una cadenita"
flotant = 10.5

print(cadenita + " - " + str(integer)) # str para castear de integer a string
print(integer + flotant)
print(integer * flotant)
print (len(cadenita), cadenita[10: 15])

# Condicionantes
if (boolean == True):
  print("Es verdadero")
elif (boolean == False):
  print("Es mas falso que mi abuela")
# else ....

# Para las condicionantes podemos usar == >= <= != ...
if (integer >= 10 and integer <= 30):
  print("El integer esta entre 10 y 30")
elif (integer > 30 and integer <= 50):
  print("El integer esta entre 31 y 50")
else:
  print("Cualquier otra mierda")

## Switch-case no existe en Py, la forma de emularlo es crear una funcion que retorne el valor de acuerdo lo necesitado.
def switch (argument):
  switcher = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo"
  }

  return switcher.get(argument)

print(switch(3))

# Ciclos
print("=========================")
print("Forcito")
for n in range(0, 5):
  print(n)

print("=========================")
print("Whilesito")
counter = 0
while counter <= 10:
  print(counter)
  counter = counter + 1

## Estructura de datos
print("=========================")
print("Estructuras")
### Array o Lista (Mutable)
arr = [0,1,2,3,4,5,"aca", False]
print(arr[1])
arr.append(7) #agrega un elemento al array
del arr[1] #elimina un elemento del array
print(arr)

### Diccionario (Mutable)
switcher = {
  1: "Enero",
  2: "Febrero",
  3: "Marzo"
}

print(switcher.get(1), switcher[1])
switcher[3] = "Abril"
print(switcher.get(3), switcher[3])
del switcher[2]
print(switcher)

### Tuplas (Inmutable)
tuplita = (1, "asi nomas", True)
print(tuplita)
## Cast to list
lista = list(tuplita)
print(lista)
lista.append(10)
print(lista)

# Funciones
def suma (num1, num2):
  return num1 + num2

def calculator (num1, num2, operator):
  if(operator == "+"):
    print(num1 + num2)
  if(operator == "-"):
    print(num1 - num2)

def myFnc (myArg, *argv):
  print(myArg, argv)

print(suma(10, 15))
calculator(10, 5, '-')

myFnc('hola', 'mundo', 'como', 'estan')
