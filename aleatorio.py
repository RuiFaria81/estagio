import random

print (random.randint(0, 5))

print(random.random() * 100)

print(random.choice( ['laranja', 'branco', 'azul']))

Lista = [2, 109, False, 10, "André", 482, "Música"]
print(random.choice(Lista))

print(random.randrange(0, 30 ,5))

from random import shuffle
aleatorio = [[i] for i in range(2, 0)]
print(shuffle(aleatorio))