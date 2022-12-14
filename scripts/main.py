
import eel
import support

eel.init('telas')

@eel.expose
def Fazer_login(user, pasw):
	login_correto = support.Login(user, pasw)
	if login_correto:
		return True
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
	qual_info: Qual informação você quer que retorne - turmas; times; alunos, user \n
	turma: Para retornar todos os times precisa escolher uma turma \n
	time: Para retornar todos os alunos precisa escolher uma turma e um time \n
	Exemplo 1: Retorna_info('turmas') \n
	Exemplo 2: Retorna_info('times', 'Banco de Dados') \n
	Exemplo 3: Retorna_info('alunos', turma='Banco de Dados', time='Falcon')
	'''
	try:
		qual_info = qual_info.strip().lower()
		inicio = support.RetornaInfo(qual_info, turma=turma, time=time)
		if qual_info == 'turmas':
			info = inicio.Turmas()

		elif qual_info == 'times':
			info = inicio.Times()
		
		elif qual_info == 'user':
			info = inicio.User()

		elif qual_info == 'alunos historico':
			info = inicio.Alunos_historico()

		elif qual_info == 'alunos grafico':
			return inicio.Alunos_graficos()
		
		elif qual_info == 'times grafico':
			return inicio.Times_grafico()
		
		else: # Alunos
			info = inicio.Alunos()

		return info 

	except:
		return []

@eel.expose 
def Avaliacao(info:dict):
	'''
	info: Todas as informações para salvar a avaliação. As informações são: turma, time, avaliado, pergunta 1, resposta 1,...
	retorna: True ou False
	'''
	return support.Avaliar().Salvar_avaiacao(info) 

@eel.expose 
def Historico(user):
	return support.Historico().Retorna_historico(user) 

@eel.expose
def RetornaInfoAcesso(qual_info, turma=''):
	return support.RetornaInfoAcesso().Inicio(qual_info, turma)

@eel.expose
def Grafico_info(qual_grafico, filtro=''):
	return support.GraficoInfo().Retorna_info_pro_grafico(qual_grafico, filtro=filtro)

eel.start("html/login.html", port=8000)

