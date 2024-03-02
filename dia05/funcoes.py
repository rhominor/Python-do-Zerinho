# %%
def funcao(x):
    res = x + 10
    return res
print(funcao(10))
# %%
def texto():
    return "texto"
print(texto())
# %%
def soma(a, b):
    return a + b
print(soma(1,2))
# %%
def soma1(a, b=0):
    return a + b
    #primeiro os argumentos obrigatórios e dps os opcionais
print(soma1(10))
# %%
def soma2(a=0, b=0):
    return a + b
print(soma2(10,))
# %%
