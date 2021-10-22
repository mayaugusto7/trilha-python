diasDaSemana = {
    1: "domingo",
    2: "segunda",
    3: "terça",
    4: "quarta",
    5: "quinta",
    6: "sexta"
}

print("Dicionario dias da semana...")
print(diasDaSemana)
print("Adicionando item...")
diasDaSemana[7] = "sabado"
print(diasDaSemana)
print(diasDaSemana[3])

print("Listando keys e values")
print("keys: ", list(diasDaSemana.keys()))
print("values: ", list(diasDaSemana.values()))
print("items: ", list(diasDaSemana.items()))

print("For in keys ->")
for key in diasDaSemana.keys():
    print(key)
