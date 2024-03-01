# %%
numero_sorte = 7

for i in range(3):
    while True:
        try:
            numero = int(input("entre um número entre 1 e 15: "))
            break
        except ValueError:
            print("numero..")

    if numero == numero_sorte:
        print("vc ganho puto")
        break
    elif numero > numero_sorte:
        print("vc erou. tente menor")
    else:
        print("erou. tente mais")
# %%
try:
    numero = int(input("numero: "))
except ValueError as err:
    print("burro. número")
# %%
