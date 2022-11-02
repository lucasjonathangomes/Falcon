
import eel
import support

eel.init('telas')

@eel.expose
def Fazer_login(user, pasw):
	login_correto = support.Login(user, pasw)
	if login_correto:
		eel.go_to('menu.html')
	else:
		return False

@eel.expose
def Cadastrar(oq_cadastrar:str, info:dict):
	'''
	oq_cadastrar: O que você desja cadastrar \n
	info: dicionario das informações. Obs - As chaves tem que ter a primeira letra maiuscula
	'''
	oq_cadastrar = oq_cadastrar.strip().lower()
	return support.Cadastrar().Iniciar_cadastro(oq_cadastrar, info)

@eel.expose 
def Retorna_info(qual_info, turma='None', time='None'):
	'''
	qual_info: Qual informação você quer que retorne - turma; time; aluno \n
	turma: Para retornar todos os times precisa escolher uma turma \n
	time: Para retornar todos os alunos precisa escolher uma turma e um time \n
	Exemplo 1: Retorna_info('turmas') \n
	Exemplo 2: Retorna_info('times', 'Banco de Dados') \n
	Exemplo 3: Retorna_info('alunos', turma='Banco de Dados', time='Falcon')
	'''

	qual_info = qual_info.strip().lower()
	inicio = support.RetornaInfo(qual_info, turma=turma, time=time)
	
	if qual_info == 'turmas':
		info = inicio.Turmas()

	elif qual_info == 'times':
		info = inicio.Times()
	
	else:
		info = inicio.Alunos()

	return info 

eel.start("html/login.html", port=8000)


