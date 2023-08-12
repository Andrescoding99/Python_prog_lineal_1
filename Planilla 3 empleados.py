# Calculo de planilla
# Mostrar: Nombre, cargo, salario bruto, descuento total, salario neto.

print("Calculo de planillas de tres empleados")

#Definición de variables y constantes

salB1 = 0 #salB es Salario Bruto
desT1 = 0 #dest es Descuento total
salN1 = 0 #salN es Salario Neto

salB2 = 0 #salB es Salario Bruto
desT2 = 0 #dest es Descuento total
salN2 = 0 #salN es Salario Neto

salB3 = 0 #salB es Salario Bruto
desT3 = 0 #dest es Descuento total
salN3 = 0 #salN es Salario Neto

ISSS = 0.03
AFP = 0.0725
RENTA = 0.10 # El 10% se mantiene dentro de un rango $472.01 - $895.24

# Captura de datos

nombre1 = input("\nIngresa el nombre del primer empleado: ")
cargo1 = input("Ingresa el cargo del primer empleado: ")
salB1 = float(input("Ingresa el salario bruto del primer empleado: "))

nombre2 = input("\nIngresa el nombre del segundo empleado: ")
cargo2 = input("Ingresa el cargo del segundo empleado: ")
salB2 = float(input("Ingresa el salario bruto del segundo empleado: "))

nombre3 = input("\nIngresa el nombre del tercer empleado: ")
cargo3 = input("Ingresa el cargo del tercer empleado: ")
salB3 = float(input("Ingresa el salario bruto del tercer empleado: "))

# Procesamiento de datos

desT1 = (salB1*0.03) + (salB1*0.0725) + (salB1*0.10) 
salN1 = salB1 - desT1

desT2 = (salB2*0.03) + (salB2*0.0725) + (salB2*0.10) 
salN2 = salB2 - desT2

desT3 = (salB3*0.03) + (salB3*0.0725) + (salB3*0.10) 
salN3 = salB3 - desT3

#Muestra

print ("\nPrimer empleado, \n nombre: {} \n cargo: {} \n salario bruto: {} \n descuento total {} \n salario neto {}".format(nombre1, cargo1, salB1, desT1, salN1) )
print ("Segundo empleado, \n nombre: {} \n cargo: {} \n salario bruto: {} \n descuento total {} \n salario neto {}".format(nombre2, cargo2, salB2, desT2, salN2) )
print ("Tercer empleado, \n nombre: {} \n cargo: {} \n salario bruto: {} \n descuento total {} \n salario neto {}".format(nombre3, cargo3, salB3, desT3, salN3) )
