amigos = ["Tiago", "André", "Maria", "Ana"]
numeros = [1, 2, 3, 6, 8, 41, 32]

outro=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

amigos[2] = "Mário"
print(amigos)

amigos.extend(numeros)
print(amigos)

amigos.append("José")
print(amigos)

amigos.insert(1, "Alice")
print(amigos)

amigos.remove("José")
print(amigos)

amigos.pop()
print(amigos)

print(amigos.index("Alice"))

print(amigos.count("Tiago"))

amigos2 = amigos.copy()
print(amigos2)

amigos.clear()
print(amigos)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

print("\n\n")
print(outro[2][0])
print("\n")
for row in outro:
    print(row)

print("\n")
for row in outro:
    for col in row:
        print(col)

