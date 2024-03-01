# %%
minha_lista = []
print(minha_lista)

minha_lista = ["p", "minor", 31, 1.69]
print(minha_lista)

# %%
print(minha_lista[-2:])
# %%
nova_lista = minha_lista[:]
print(nova_lista)
# %%
nova_lista2 = minha_lista
print(nova_lista2)
# %%
notas = []
nota = 7.5
notas.append(nota)
print(notas)
# %%
notas.extend([2.1,10])
print(notas)
# %%
notas = notas + [8, 8.2]
print(notas)
# %%
nomes = ['teo','maria','nah']
for i in nomes:
    print(i.title())

# %%
nomes.remove(nomes[-1])
print(nomes)
# %%
dados = ['rho','minor',31,['ana','bia','cat']]
print(dados[3][-1])
# %%
dados.append(['maria'])
print(dados)
# %%
print(dados[-1][0][0])
# %%

n1 = int(input("nota 1: "))
n2 = int(input("nota 2: "))
n3 = int(input("nota 3: "))
n4 = int(input("nota 4: "))

notas = [n1,n2,n3,n4]
soma = sum(notas)
print(soma)
# %%
alturas = []
for i in range(4):
    a = int(input(f"entre altura {i+1}: "))
    alturas.append(a)
soma = sum(alturas)
print(soma)
# %%
