# %%
arquivo = open("arquivo.txt", 'a')
arquivo.write("\neita ferro 2")
arquivo.close()

# %%
arquivo = open("arquivo.txt", 'r')
conteudo = arquivo.readlines()
arquivo.close()
print(conteudo)
print(type(conteudo))
# %%
with open("arquivo.txt",'r') as file:
    conteudo = file.read()
print(conteudo)
# %%
