msg = "Prueba con Strings en Python"

print ("La variable msg dice:",msg)
print("La variable msg, en la posicion [0] tiene una:", msg[0])
print("La variable msg, desde posicion [0] a la [10] tiene el siguiente string:", msg[0:10])
print("La variable msg, desde posicion [0] hasta el final tiene el siguiente string:", msg[11:])
print ("Python" in msg[0:7])
print ("Python" in msg[7:])

edad = 40
nombre = 'Gerardo'

nombreyedad = "Hola {1}. Tenes {0} años.".format(edad, nombre)
print (nombreyedad)