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

# Procesamiento de datos 

prodpar = ((8 + 10 + 8) / 3 ) * 0.35
prodlab = ((9 + 8 + 8) / 3 ) * 0.35

na = prodpar + prodlab

pf = 8 - na

nf = (pf * 10) / 3

print("\n Nota final de parcial: {} \n nota final de laboratorio: {}".format(prodpar,prodlab))

print("Deberá obtener una nota en el proyecto final de: ", nf, "para pasar con nota minima de 8")

