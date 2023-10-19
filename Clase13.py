
# tupla = (5,12,7,37,8,86,19,7,-783,87,188,7,9,12,7,3982)
# print(tupla[-1])
# print (len(tupla))
# print (tupla.index(87))
# print (tupla[13:])
# print (tupla[8])
# print (tupla.count(7))

# AND Si ambas afirmaciones son verdaderas entonces el final es verdadero (true)
  # print (18 > 5 and 5 == 2)
# OR Si una de las afirmaciones es verdadera entonces el final es verdadero
  # print (5 == 2 or 2 < 1)
# NOT (!=) significa distinto
  # print ( 10 != 10)

# Ejercicio
# Dadas 2 variables, EDAD y NOMBRE hacer:
 # NOMBRE sea diferente de cuatro asteriscos "****"
 # EDAD sea mayor que 10 y a su vez menor que 18
 # Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
 # EDAD multiplicada por 4 sea mayor que 40

nombre = input("Ingrese su nombre")
edad = int(input("Ingrese su edad"))

condicion = [nombre != "****", edad > 10 and edad < 18, len(nombre) >= 3 and len(nombre) < 10, edad*4 > 40] #Esto es una lista por eso va en corchetes

print(condicion)