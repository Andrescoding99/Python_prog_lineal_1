# Calculo de nota final de estudiante
# Parciales (8,10,8) equivaldrian a 35%
# Laboratorios (9,8,8) equivaldrian a 35%

print("Calculo de nota final para pasar con 8")

# Definir las variables

prodpar = 0 # prodpar significa promedio de parcial
prodlab = 0 # prodlab significa promedio de laboratorio
na = 0 # na es nota actual
nf = 0  # nt es nota final
pf = 0 # pf es proyecto final

par1 = 0 # par significa nota de parcial
par2 = 0
par3 = 0
lab1 = 0 # lab significa nota de laboratorio
lab2 = 0
lab3 = 0

# Captura de datos

par1 = float(input("\n Ingrese su nota del primer parcial: "))
par2 = float(input("Ingrese su nota del segundo parcial: "))
par3 = float(input("Ingrese su nota del tercer parcial: "))

lab1 = float(input("\n Ingrese su nota del primer laboratorio: "))
lab2 = float(input("Ingrese su nota del segundo laboratorio: "))
lab3 = float(input("Ingrese su nota del tercer laboratorio: "))

# Procesamiento de datos 

prodpar = ((par1 + par2 + par3) / 3 ) * 0.35
prodlab = ((lab1 + lab2 + lab3) / 3 ) * 0.35

na = prodpar + prodlab

pf = 8 - na

nf = (pf * 10) / 3

print("\n Nota final de parcial: {} \n nota final de laboratorio: {}".format(prodpar,prodlab))

print("Deberá obtener una nota en el proyecto final de: ", nf, "para pasar con nota minima de 8")

