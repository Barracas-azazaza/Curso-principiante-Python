demo=[1,"hello",1.34,True,[1,2,3]]
colors=["red","green","blue"]
print(type(colors))
print(dir(colors))
print(len(colors))
print(dir(demo))
print(len(demo))
numbers_list=list((1,2,3,4))
print(type(numbers_list))
r=list(range(1,11))
print(r)
print(colors[1])
print(colors[-1])
print("green" in colors)
print(colors)
colors[1]="Yellow"
print(colors)
colors.extend(["violet","rojo"]) #agrego nuevo elemento
print(colors)
colors.insert(5, "amarisho")
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors.index("blue"))
print(colors.count("red"))
print(colors)
colors.pop()
print(colors)
colors.pop()
print(colors)
colors.pop(1)
print(colors)
colors.clear()
print(colors)
colors.index