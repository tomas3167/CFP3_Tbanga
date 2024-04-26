 #Cual seria la logica para evaluar un numero y si es este mayor o igual a 6, mostrar el mensaje "Verde" y sino mostrar el mensaje "Rojo"

 #Variables
 #En python existe la posibilidad de declarar variables vacias, es decir, con valor "None"
# nota = 8
# color = None
# if nota >= 6:
#     print("Verde")
# else:
#     print("Rojo")

 #OPERADOR TERNARIO: Nos permite evaluar una condicion de manera abreviada
# nota = 7
# color = "Verde" if nota >= 6 else "Rojo"
# print(nota, color)

 #Dado un numero entero, imprimir "Es par" si el numero es par, sino "Es impar"
# num = 6
# par_impar = "Es par" if num%2 == 0 else "Impar"
# print(num, par_impar)

 #Dado dos numeros enteros A y B, Imprimir "A es mayor" si A es mayor que B, "B es mayor", si B es mayor que A, si son iguales, mostrar el mensaje "Ambos son iguales"
# A = int(input("Ingrese el primer numero"))
# B = int(input("Ingrese el segundo numero"))
# resultado = "A es mayor" if A > B else ("B es mayor" if B > A else "Ambos son iguales") 
            #### El elif no se puede usar en el operador ternario
# print(resultado)

 #FUNCIONES ANIDADAS: Las funciones pueden ser anidadas, es decit, una funcion puede contener a otra funcion
#EJEMPLO: Operaciones Bancarias: Deposito, Retiro
def operacion():
    def deposito(cantidad, balance):
        return balance + cantidad
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None, "No tiene saldo suficiente para esta operacion"
    print(deposito(100,400))
    print(retiro(800,500))
# operacion()

    #Agregar a la funcion anterior la opcion de especificar el tipo de operacion que se desea realizar, en el caso de no especificar una, tomar el valor deposito como default
def operacion(cantidad, balance, tipo='Deposito'):
    def deposito(cantidad, balance):
        return balance + cantidad
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None, "No tiene saldo suficiente para esta operacion"
        
    if tipo == 'Deposito':
        return deposito(cantidad, balance)
    elif tipo == 'Retiro':
        return retiro(cantidad, balance)

resultado = operacion(100,300,'Retiro')
# print(resultado)

 #Escribir una funcion que reciba 2 numeros y un caracter que indique el tipo de operacion a realizar (+ - * /). La funcion debe devolver el resultado de la operacion aritmetica. Utilizar funciones anidadas para implementar las operaciones. La operacion por default sera suma.

def calculadora(num1, num2, tipo='+'):
    def suma(num1,num2):
        return num1 + num2
    def resta(num1,num2):
        return num1 - num2
    def multiplicacion(num1,num2):
        return num1 * num2
    def division(num1,num2):
        return num1 / num2
    
    if tipo=='+':
        return suma(num1,num2)
    elif tipo=='-':
        return resta(num1,num2)
    elif tipo=='*':
        return multiplicacion(num1,num2)
    elif tipo=='/':
        return division(num1,num2)

resultado = calculadora(20,10,'/')
print(resultado)