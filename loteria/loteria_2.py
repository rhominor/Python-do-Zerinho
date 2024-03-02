# %%

import random

def valida_entrada():
    while True:
        try:
            numero = int(input("numero entre 1 e 15: "))
            return numero
        except ValueError:
            print("numero..")

numero_sorte = random.randint(1,15)

for i in range(3):
    numero = valida_entrada()

    if numero == numero_sorte:
        print("vc ganho puto")
        break
    elif numero > numero_sorte:
        print("vc erou. tente menor")
    else:
        print("erou. tente mais")

# %%
