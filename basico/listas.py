a = [1, 2, 3, 4]
print(a[0])

print(a[-1])

print(a[1:3])

a[0] = 42
print(a)

# operacoes lista
print("Operacoes Lista append, insert, len e slice a[2:4]")
a = [1, 2, 3, 4, 5]

# adiciona no fim da lista
a.append(6)

# adicionando 0.0 na posicao 0
a.insert(0, 0.0)
print(a)

# len tamanho da lista
print(len(a))

# Modificar trecho da lista
a[2:4] = [5.0, 5.0]
print(a)

# nao cria um novo objeto
a = [1, 2, 3]
b = a

b[0] = 42
print(a)

print("Para copiar uma lista usamos a[:]")
c = a[:]
print(c)
c[0] = 0
print(c)

