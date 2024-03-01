# %%
dados = {"nome":"paulo",
         "sobrenome":"minor",
         "idade":31,
         "filhos":[{"nome":"Maria", "idade":2}]}
nome = dados["nome"]
print(nome)
print(dados["filhos"][0]["idade"])
# %%

tipo_sorvete = input("tipo sorbet: ")
sabor = input("sabor: ")
cobertura = input("cobertura: ")

valor = 0

sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.5,
    "cestinha": 4.0
}

valor += sorvetes[tipo_sorvete]

coberturas = {
    "caramelo":1.5,
    "morango":1.5,
    "chocolate":1.5
}

valor += coberturas[cobertura]

print("seu sorvete ", tipo_sorvete, " de ", sabor, " e cobertura ", cobertura, " custa: ", valor)

# %%
dados.keys()
dados.values()
dados.items()
# %%
