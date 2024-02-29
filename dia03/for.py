# %%
for s in "String!":
    print(s)
# %%
seq = range(0,10)
for i in seq:
    print(i)
# %%
for i in range(10):
    print(i)
# %%
for i in range(1,16):
    if i % 2 == 0: print(i)
# %%
# 4
nome = input("nome? ")
if "calvo" in nome.lower():
    print("s")
else:
    print("n")
# %%
# 5
nome = input("nome? ")
if "calvo" in nome or "silva" in nome:
    print("s")
else:
    print("N")
# %%
# 6
item = input("q tu comprÔ? ")
if item in ["laranja", "jujuba", "túlio"]:
    print("ok")
else:
    print("ñ")
# %%
# 7
palavra = input("diz algo aí: ")
qtd = 0
for s in palavra:
    if s == "a":
        qtd +=1
print("tem ",qtd, " As na tu palavra")
# %%
palavra = input("diz algo aí: ").lower()
print("tem ", palavra.count("a"), " a's na tua palavra")
# %%
# 9
total = 0
while True:
    entrada = input("digita aí saldo")
    if entrada == "":
        break
    total += float(entrada)
print(total)
# %%
