myStr="Hello World car"
print(dir(myStr))
print(myStr.replace("hello","bye")) #No funciona
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.count("o"))
print(myStr.startswith("hello"))
print(myStr.endswith("world"))
print(myStr.split())
print(myStr.split("o"))
print(myStr.find("o"))
print(len(myStr))
print(myStr.index("e"))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[4])
print(myStr[-1])
print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))