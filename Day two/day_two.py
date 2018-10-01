print(2+2)

"La suma de 1 + 2 es {0}".format(1+2) #format es la mejor de manera para imprir variables
"texto {0}, {1}, {2}".format([],[],[])#segun como la referencies, apareceran en el mensaje.

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...' #esta tambien es una forma de imprimir variables
print(s)

s = 123
print(s)


tax = 12.5 / 100
price = 100.50
print(price * tax)

a = "2"
b = "2"
c = a+b
print(c)#saldra 22

a = 7
print (type(a))#muestra el tipo de dato

aT = True
print ("El valor es Verdadero:", aT, ", el cual es de tipo", type(aT), "\n")

aAnd = True and False
print ("SI es Verdadero Y Falso, entonces es:", aAnd, ", el cual es de tipo", type(aAnd), "\n")

aOr = True or False
print ("SI es Verdadero O Falso, entonces es:", aOr, ", el cual es de tipo", type(aOr), "\n")

aNot = not True
print ("Si NO es Verdadero, entonces es:", aNot, ", el cual es de tipo", type(aNot), "\n")


persona = input('Escribe un numero: ')
personas=int(persona)+2
print('si le sumamos 2 es {0}'.format(personas))
