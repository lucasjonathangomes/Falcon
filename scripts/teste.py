from support import *

a=Ler_JSON("turma.json")

print("json\n",a)
print("todas as turmas\n",list(a))
print("acessando a turma falcon\n",a["Banco de Dados 1"]["FALCON"])