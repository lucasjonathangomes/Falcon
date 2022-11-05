
import eel
import support

eel.init('telas')

@eel.expose 
def Retorna_info(qual_info, turma='None', time='None'):
	'''
	qual_info: Qual informação você quer que retorne - turmas; times; alunos \n
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
		
		else:
			info = inicio.Alunos()

		return info 
	except:
		return ['']

eel.start("html/teste.html", port=8000)



