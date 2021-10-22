print("Tuplas não podem ser modificadas apos serem inicializadas...")
a = ("carro", 1, [1, 2, 3, 4])
print(a)
a[2].append(5)
print(a)
# a[1] = 42 TypeError: tuple

print(a.count("carro"))
print(a.index("carro"))
