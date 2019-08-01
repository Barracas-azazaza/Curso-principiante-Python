print("ingrese el numero de datos a guardar")
veces=float(input())
datos=[]
n=0
acumulador=0
acumulador2=0
promedio=acumulador/veces
while n<veces:
    print("Ingrese numero")
    numero=float(input())
    info={
        "digito":numero
    }
    datos.append(info)
    acumulador=numero+acumulador
    n=n+1
promedio=float(acumulador/veces)
print(promedio)
for r in datos:
    acumulador2=float(r["digito"]-promedio)**2+acumulador2

varianza=float(acumulador2/veces)
print(varianza) 