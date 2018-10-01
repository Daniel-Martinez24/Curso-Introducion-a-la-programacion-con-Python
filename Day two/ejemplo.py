#asi se declara una funcion con "def", seguido del nombre de la funcion
#y entre comillas, los paramentros.
def multiplica(a,b):
	a = a * b
	return a

def div(a,b):
	a = a / b
	return a


quequieres = input()
a = int(input())
b = int(input())

#un if es una condicional, es decir, codigo que se ejecutara si se cumple una condicion
if(quequieres == "multiplica"):
	print("la multiplicación es: {0}".format(multiplica(a,b)))
else: #Else es codigo que se ejecuta, si no se cumple dicha condicion.
	print(div(a,b))



