import random

x = 0
x = x + random.randint(1 , 5)
x = x + random.randint(1 , 5)
x = x + random.randint(1 , 5)
x = x + random.randint(1 , 5)
x = x + random.randint(1 , 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
print(x)

#Otra forma de hacerlo es
x = 0
for i in range(10):
    print(x)
    x += random.randint(1,5)
    print(x)

#While se utiliza cuando no se sabe cuantas veces se debe repetir algo
x = 0
while x != 5:
    x = random.randint(1,100)
    continue
    break
print(x)
