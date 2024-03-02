# %%
def soma(op,a,b,*args):
    total = 0
    if op == "soma":
        total = a+b
        for i in args:
            total += i
        return total
    elif op == "sub":
        total = a-b
        for i in args:
            total -= i
print(soma("soma", 10, 20,30,40,50))
# %%
dados = ['téo','calvo',31,['tia','joaninha']]
nome, sobrenome, *lixo = dados
print(nome)
print(sobrenome)
print(lixo)
# %%
a = 10
b= 20
print(a,b)

a, b = b, a
print(a,b)

c = a
a = b
b = c
print(a,b)
# %%
