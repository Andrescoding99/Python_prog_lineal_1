# Operaciones matematicas: Suma, resta, multiplicación y división
# Un solo print e interpolado

print("Calculo de operaciones matemáticas")

# Definicion de variables 

a = 0
b = 0

#Captura de datos

a = float(input("Ingresa el valor del primer número: "))
b = float(input("Ingresa el valor del segundo número: "))

#Procesamiento de datos

suma = (a + b)
resta = (a - b)
multiplicacion = ( a * b)
division = ( a / b)

#Muestra

print("\n El resultado de las 4 operaciones de los dos valores es: \n suma: {} \n resta: {} \n multiplicación: {} \n división: {}".format(suma,resta,multiplicacion,division))
