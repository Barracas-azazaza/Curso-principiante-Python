Foods=["manzanas","pan","queso","leche"]
print(Foods[0])
print(Foods[1])
print(Foods[2])
print(Foods[3])
for Food in Foods:
    print(Food)
    if Food=="queso":
        print("Tienes que comprar")
        print(Food)
        break
for number in range(1,10): #Llega un número antes
    print(number)
for letra in "hello":
    print(letra)
count=4
while count<=10:
    print(count)
    count+=1