# Calculo de planilla
# Mostrar: Nombre, cargo, salario bruto, descuento total, salario neto.

print("Caculo de planillas de tres empleados")

#Definición de variables y constantes

salB = 0 #salB es Salario Bruto
desT = 0 #dest es Descuento total
salN = 0 #salN es Salario Neto

ISSS = 0.03
AFP = 0.0725
RENTA = 0.10

# Captura de datos

nombre1 = input("Ingresa el nombre del primer empleado: ")
cargo1 = input("Ingresa el cargo del primer empleado: ")
salB = float(input("Ingresa el salario bruto del primer empleado: "))

nombre2 = input("\nIngresa el nombre del segundo empleado: ")
cargo2 = input("Ingresa el cargo del segundo empleado: ")
salB = float(input("Ingresa el salario bruto del segundo empleado: "))

nombre3 = input("\nIngresa el nombre del tercer empleado: ")
cargo3 = input("Ingresa el cargo del tercer empleado: ")
salB = float(input("Ingresa el salario bruto del tercer empleado: "))

# Procesamiento de datos

desT = (salB*0.03) + (salB*0.0725) + (salB*0.10) 
salN = salB - desT

#Muestra

print ("\nPrimer empleado, nombre: {} cargo: {} salario bruto: {} descuento total {} salario neto {}".format(nombre1, cargo1, salB, desT, salN) )
print ("Segundo empleado, nombre: {} cargo: {} salario bruto: {} descuento total {} salario neto {}".format(nombre2, cargo2, salB, desT, salN) )
print ("Tercer empleado, nombre: {} cargo: {} salario bruto: {} descuento total {} salario neto {}".format(nombre3, cargo3, salB, desT, salN) )
