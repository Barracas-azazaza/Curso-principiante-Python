# Elaborado por Camilo Andrés Barragán Gómez
import time #Importar librería time
i=1 #Asignar variable
print("En un momento el sistema dirá a quienes unirá en amor") #Impresión de mensaje
time.sleep(2) #Tiempo de espera
quienes = "ella+yo" #Variable
print(quienes) #Impresión de mensajes
time.sleep(2) #Tiempo de espera
print("Buscando errores") #Impresión de mensaje
time.sleep(2) #Tiempo de espera
while i>0: #Bucle while
    if quienes == quienes: #Condición
        print("Ella no te ama según el error: ",i) #Mensaje incluyendo mostrar el incremento del error
        i+=1 #Aumento de la variable