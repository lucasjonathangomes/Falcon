
import eel
import support

eel.init('telas')

@eel.expose
def Fazer_login(user, pasw):
	print(user)
	print(pasw)
	eel.go_to('menu.html')

@eel.expose
def Testar_os_botoes():
	print('Botão Valido!')

@eel.expose
def Atualizar_pagina(nome_pagina):
		eel.go_to(nome_pagina)

@eel.expose
def Cadastrar(oq_cadastrar:str, info:dict):
	oq_cadastrar = oq_cadastrar.strip().lower()
	
	resultado = support.Cadastrar().Iniciar_cadastro(oq_cadastrar, info)
	print(resultado)


eel.start("html/login.html", port=8000)
