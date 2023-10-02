#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
subjects = ["matematicas", "fisica", "historia", "quimica"]
print(subjects)
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
for subject in subjects:
    print(f"Yo estudio la materia de {subject}" )

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

subjects = ["Fisica", "Matematicas","Lenguaje", "Quimica"]
scores = []
for subject in subjects:
    score = int(input(f"Que calificacion obtubiste en {subject}:"))
    scores.append(score) #agregar elemento a la fila
for i in range(len(subjects)):
    print(f"En la materia {subjects[i]} has sacado {scores[i]}")


#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
lottery = []
for i in range(7):
    lottery.append(int(input("Ingrese un numero ganador de la loteria:")))
    lottery.sort()
print(f"El numero ganador es: {str(lottery)}")

#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.reverse() #numeros inverso
for number in numbers:
    print(f"Los numeros en orden inverso es {number}")

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
subjects = ["Fisica", "Matematicas","Lenguaje", "Quimica"]
passed = []
for subject in subjects:
    score= int(input(f"Que califaficacion obtuviste en {subject}:"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print(f"Tienes que repetir la materia {str(subjects)}")

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)

#palabra palidroma
word = input("ingrese una palabra: ")
reverse_word = word
word = list(word)
reverse_word= list(reverse_word)
reverse_word.reverse()
if word == reverse_word:
    print("la palabara es palimdromo")
else:
    print("no es palindromo")

#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
prices = [50, 75, 46, 22, 80, 65, 8,]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print(f"el numero menor es {str(min)}")
print(f"el numero menor es {str(max)}")

#tuplas
tupla = (1,2,3,4)
tup = list(tupla)
tup.append(6)
tuple(tup)
print(tup)

#diccionario
dictionary = {"Nombre": "Arianna", "Apellido": "Alvarado", "Edad": 18}
print(dictionary)
for key in dictionary:
    print(key)
for value in dictionary.values():
    print(value)

for key , value in dictionary.items():
    print(key, value)

dictionary.clear()
print(dictionary)
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input("Que fruta desea: ").title()
kg= float(input("Cuantos kilos desea?:"))
if fruit in fruits:
    print(kg, "kilos de", fruit, "valen", fruits[fruit]*kg, "$")
else:
    print("la fruta que desea no se encuenta en stock")

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
course = {"matematicas":6 , "fisica": 7, "quimica": 9}
total_credits = 0
for subject, credits in course.items():
    print(subject, "tiene", credits, "creditos")
    total_credits+=credits
print(f"el total de creditos es: {total_credits}")

#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
information = {}
condiction = True
while condiction:
    key = input("Que informacion desea introducir")
    value = input(key + ":")
    information[key]= value
    print(information)
    condiction = input("Quieres aña dir mas informacion (si/no)") == "si"


#ejercicio
# #solicitar al usuario que ingrese numeros enteros positivos y, por cada uno, imprimir la suma de los digitos que lo componen. la condicion de corte es que se ingrese le numero -1. al finalizar, mostar cuantos de los nuemros ingresados por el usurio fueron pares.
pair_number = 0
total_digit= 0
while True:
    number= int(input("ingrese un nuemro enetro positivo (-1 para finalizar): "))
    if number == -1 :
        break

    if number % 2 == 0:
        pair_number+= 1

    digit_quantity= len(str(number))
    total_digit+=digit_quantity
    print(f"El número {number} tiene {digit_quantity} dígitos.")

print(f"el total de numeros pares es: {pair_number} ")
print(f"el total de digitos: {total_digit} ")

#tupla 2
animals = ("gato", "perro", "chivo", "vaca")
for animal in animals:
    print(animal)

animal = list(animals)
animal.append("cabra")
tuple(animal)
print(animal)

#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# Total	Coste
basket = {}
condiction_1 = True

while condition_1:
    key = input("Que articulo desea introducir: ")
    value = float(input("introduzca el precio del ariculo: " + key + ":"))
    basket[key]= value
    print(basket)
    condition_1 = input("Deseas añadir algo mas (si/no)") == "si"

cost = 0
print("lista de los compra")
for key , value in basket.items():
    print(key, value)
    cost+=value
print(f"el coste total de la compra es: {cost}")

#pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10.
number = int(input("Ingrese un numero por favor: "))
multiplication_table = []
for i in range(1, 11):
    multiplication_table.append(i*number)
print(multiplication_table)

#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
random_numbers = []
while True:
    number= int(input("Ingrese un numero: "))
    if number == 0:
        break
    random_numbers.append(number)
random_numbers.sort()
print(random_numbers)

#lo mismo pero ahira de mayor a menor
random_numbers = []
while True:
    number= int(input("Ingrese un numero: "))
    if number == 0:
        break
    random_numbers.append(number)
random_numbers.reverse()
print(random_numbers)

#Pide una cadena por teclado, mete los caracteres en una lista sin espacios.
chain = input("dame un cadena: ")
print(chain)
chain_1 = []
for i in chain:
    if i != " ":
        chain_1.append(i)
print(chain_1)

#pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres
chain = input("dame un cadena: ")
print(chain)
chain_1 = []
for i in chain:
    if i not in chain_1:
        chain_1.append(i)
print(chain_1)

#Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
tupla_number = (1,2,3,4,5,6,0,6,7,8,9,6)
number = int(input("Dame un numero: "))
counter= 0
for i in tupla_number:
    if i == number:
        counter +=1
print(f"el numero {number} se repite {counter}")

#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.
tupla_number = (10, 15, 20, 40)
min = max = tupla_number[0]
for i in tupla_number:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f"el numero minino es {min}")
print(f"el numero maximo es {max}")

# Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.
information_1 = {}
condition_2 = True
while condition_2:
    name= input("Desea ingresar alguna informacion: ")
    phone = input(name + ":")
    if name not in information_1:
        information_1[name] = phone
        print("agreado")
    else:
        print("esta repetido")

    condition_2 = input("Desea agregar mas informacion (si/no)") == "si"
print(information_1)
