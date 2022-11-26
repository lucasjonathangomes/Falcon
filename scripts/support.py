
import os
import json
import hashlib
from re import findall
from random import choices
from datetime import datetime

class DeclararUser: 
    def __init__(self, user):
        '''
        Esse metodo vai salvar o user em uma instancia para que posa ser usado depois as infomações do usuário 
        '''

        json_info = Arquivos().Ler_JSON('users.json')
        user_info = json_info[user]
        # self.user_info = {
        #                     'User': user,
        #                     'Nome': user_info['Nome'], 
        #                     'Email': user_info['Email'],
        #                     'Cargo': user_info['Cargo']
        #                 }
        self.user_info = user_info
        self.user_info['User'] = user

class Cadastrar:
    def Iniciar_cadastro(self, oq_cadastrar:str, info:dict):
        '''
        input:
                oq_cadastrar: O que quer cadastrar - turma; time; sprint; aluno 
                info: Todas as informações necessarias para cadastrar o que você escolheu (tem que ser em dicionario)
        
        return:
                Uma lista, onde:
                1° item: True ou False (se conseguiu ou não cadastrar) \n
                2° item: Uma mensagem, se não conseguiu cadastrar essa mensagem fala o porque \n

        exemplos:
                Exemplo: [True, "Aluno salvo com sucesso!"] 
                Exemplo: [False, "Ja existe esse time na turma Falcon"]
        '''
        self.info = info
        oq_cadastrar = oq_cadastrar.lower()

        if oq_cadastrar in ['turma', ' time']:
            self.json_turmas = Arquivos().Ler_JSON('turmas.json')
            
            if oq_cadastrar == 'turma':
                return self.__Cadastrar_turma() 

            elif oq_cadastrar == 'time':
                return self.__Cadastrar_time() 

        elif oq_cadastrar == 'sprint':
            self.json_sprints = Arquivos().Ler_JSON('sprints.json')
            return self.__Cadastrar_sprint()

        else:
            '''
            Aqui vai cadastrar:

            Fake Client
            Instrutor
            Product Owner
            Scrum Master
            Desenvolvedor'''
            
            self.json_user = Arquivos().Ler_JSON('users.json')
            return self.__Cadastrar_usuario()


    def __Cadastrar_turma(self):
        turma_nome = self.info['Turma'].strip().title()
        if turma_nome in self.json_turmas:
            return [False, f'Turma "{turma_nome}" já existe']
        
        else:
            self.json_turmas[turma_nome] = {}

            Arquivos().Salvar_JSON('turmas.json', self.json_turmas)
            return [True, f'Turma "{turma_nome}" salvo com sucesso!']

    def __Cadastrar_time(self): 
        turma = self.info['Turma'].strip().title()
        time = self.info['Time'].strip().title()

        if time.lower() in [nome.lower() for nome in self.json_turmas[turma]]:
            # Ja existe o nome do time escolhido no banco de dados
            return [False, f'O time "{time}" já existe na turma "{turma}". Escolha outro nome para o time ou use o time que já existe']

        else:
            # No time vai ter as seguintes informações
            self.json_turmas[turma][time] = {
                    'PO': '',
                    'Scrum Master': '',
                    'Desenvolvedor': [],
                    'Alunos': []
            }
            Arquivos().Salvar_JSON('turmas.json', self.json_turmas)
            return [True, f'Time "{time}" salvo com sucesso na turma "{turma}"']

    def __Cadastrar_usuario(self):
        def Criar_nome_user(user):
            '''
            Se tiver mais de um user com o mesmo nome então vai ser adicionado uma contagem no fim do nome
            
            exemplo:
                        user1 
            '''
            cont = 1
            while True:
                novo_user = user + str(cont)
                if not novo_user in self.json_user:
                    return novo_user
                
                cont += 1 

        def Salvar_aluno(turma, time, cargo):
            turmas = Arquivos().Ler_JSON('turmas.json')
            
            if cargo == 'Desenvolvedor':
                # Se for desenvolvedor apenas adicionamos o nome do aluno na lista
                turmas[turma][time][cargo].append(nome)
        
            else:
                if turmas[turma][time][cargo] != '':
                    # Se o cargo escolhido para esse aluno já estiver ocupado, então vamos retornar False 
                    # e o nome do aluno que está no cargo escolhido
                    return [False, f'O cargo "{cargo}" já esta preenchido pelo aluno "{turmas[turma][time][cargo]}" para essa turma e time escolhido']
                
                else:
                    # Se não tiver ocupado então salvamos o aluno nesse cargo
                    turmas[turma][time][cargo] = nome
                        # Adicionamos esse aluno na lista de alunos

            turmas[turma][time]['Alunos'].append(nome)
            Arquivos().Salvar_JSON('turmas.json', turmas)

            return [True, f'Aluno salvo com sucesso! Nome de usuario é: {user}']
        
        def Salvar_instrutor_e_fk(turma, cargo, user_name):
            for user in self.json_user:
                aluno = self.json_user[user]
                if aluno['Cargo'] == 'Instrutor' and aluno['Turma'] == turma or aluno['Cargo'] == 'Fake Client':
                    fim_msg = ''
                    if aluno['Cargo'] == 'Instrutor':
                        fim_msg = f' para a turma "{turma}"'
                    return [False, f'Já existe {cargo}{fim_msg}']

            return [True, f'{cargo} salvo com sucesso! Nome de usuario é: {user_name}'] 

        turma = ''
        time = ''
        nome  = self.info['Nome'].strip().title()
        email = self.info['Email'].strip()
        senha = self.info['Senha']
        cargo = self.info['Cargo']

        resultado = self.__Validar_info_padrao(nome, email, senha)

        if not resultado[0]:
            return resultado
        
        senha = Criptografar(senha)
        user = email.split('@')[0].strip()

        if user in self.json_user:
            user = Criar_nome_user(user)

        if cargo == 'Fake Client':
            usuario_salvo = Salvar_instrutor_e_fk('', cargo, user) 

        elif cargo == 'Instrutor':
            turma = self.info['Turma'].strip()
            validado = self.__Validar_turma_e_time(turma, time, validar_time=False)

            if validado[0]:
                usuario_salvo = Salvar_instrutor_e_fk(turma, cargo, user) 

            else:
                return validado

        else:
            turma = self.info['Turma'].strip()
            time = self.info['Time'].strip()
            validado = self.__Validar_turma_e_time(turma, time)

            if validado[0]:
                usuario_salvo = Salvar_aluno(turma, time, cargo)

            else:
                return validado



        deixar_info_sequencial = {
                'Nome' : nome,
                'Email': email,
                'Turma': turma,
                'Time' : time,
                'Cargo': cargo,
                'Senha': senha 
        }

        if usuario_salvo[0]:
            self.json_user[user] = deixar_info_sequencial
            Arquivos().Salvar_JSON('users.json', self.json_user)

        return usuario_salvo

    def __Validar_turma_e_time(self, turma, time, validar_turma=True, validar_time=True):
        if turma == '' and validar_turma:
            return [False, 'Seleciona uma turma para esse usuario']

        if time == '' and validar_time:
            return [False, 'Seleciona um time para esse usuario']

        return [True] 
        

    def __Validar_info_padrao(self, nome, email, senha):
        def Validar_senha(senha):
            '''Vai verificar se está de acordo com o esperado - quantidade de digitos; letras; numeros; caracteres especiais'''
            todos_regex = ['[a-z]', '[A-Z]', '[!|@|#|$|%|&|*|(|)]', '[1-9]']

            for regex in todos_regex:
                if len(findall(regex, senha)) == 0 or len(senha) < 8:
                    msg = 'A senha tem que ter no minimo 8 digitos, letras minúscula e maiúscula, '\
                        'numeros, e um dos caracteres especiais a seguir: !, @,#, $, %, &, *, (, )'
                    return [False, msg]
            
            return [True]

        # Nome
        if nome == '' or len(nome.split()) < 2:                
            return [False, 'Digite o nome e o sobrenome do aluno']

        # Email 
        if email == '' or not '@gmail.com' in email:
            return [False, 'Email inválido. Apenas @gmail.com é aceito']

        # Senha 
        validar_senha = Validar_senha(senha)
        if not validar_senha[0]:
            return [False, validar_senha[1]]
        
        return [True]

    def __Cadastrar_sprint(self):
        def Validar_data(sprts_ini, sprts_fim): 
            formato = '%d/%m/%Y'
            todas_sprints = {}

            # Essa variavel esta aqui para não dar erro no "for"
            ultima_sprint = datetime.now()

            # Validar o inicio da primeira sprint
            if str(datetime.strptime(sprts_ini[0], formato))[:10] < str(datetime.now())[:10]:
                return [False, 'A primeira sprint deve, no minimo, começar hoje.']

            for cont in range(len(sprts_ini)):
                try:
                    data_inicio = datetime.strptime(sprts_ini[cont], formato)
                    data_fim    = datetime.strptime(sprts_fim[cont], formato)
                    # Esta validando as seguintes regras:
                    # 1 - Se a data de inicio é maior que a data de fim
                    # 2 - Se a data de inicio é igual a data de fim
                    # 3 - Se a data de inicio é menor que a ultima data de fim 
                    if data_inicio > data_fim or data_inicio == data_fim or data_inicio < ultima_sprint:
                        return [False, 'A data de inicio não pode ser maior/mesma que a do fim. Verifique as datas.']

                    # if data_inicio > data_fim:
                    #     return [False, 'primeiro']

                    # elif data_inicio == data_fim:
                    #     return [False, 'segundo']
                    
                    # elif data_inicio < ultima_sprint:
                    #     return [False, 'terceiro']


                    ultima_sprint = data_fim

                    todas_sprints[f'Sprint {cont+1}'] = {'Inicio': sprts_ini[cont], 'Fim': sprts_fim[cont]}

                except:
                    return [False, 'Algo deu errado!! Verifique se esqueceu de colocar alguma data e/ou se as datas estão corretas']

            return [True, todas_sprints]

        turma = self.info['Turma']
        sprints_inicio = self.info['Sprint Inicio']  # Vem em formato de lista
        sprints_fim = self.info['Sprint Fim']        # Vem em formato de lista

        if turma == '':
            return [False, 'Escolha uma turma.']

        if turma in list(self.json_sprints):
            return [False, f'Já tem sprints cadastrada na turma {turma}']
        
        validar_datas = Validar_data(sprints_inicio, sprints_fim)

        if not validar_datas[0]:
            return [False, validar_datas[1]]
        
        self.json_sprints[turma] = validar_datas[1]
        Arquivos().Salvar_JSON('sprints.json', self.json_sprints)

        return [True, f'Sprints salva com sucesso para a turma {turma}']

class Arquivos:
    def Ler_JSON(self, nome):
        with open(Caminho_ate_Falcon()+'\\json\\'+nome, encoding="utf-8") as a:
            arquivo = json.load(a) 
        return arquivo 

    def Salvar_JSON(self, nome:str, novo_json:dict):
        with open(Caminho_ate_Falcon()+'\\json\\'+nome, 'w') as a:
            json.dump(novo_json, a, indent=4)

    def Ler_Excel(self):
        pass 

class RetornaInfo:
    def __init__(self, qual_info, turma='None', time='None'):
        qual_info = qual_info.lower().strip()
        self.turma = turma.strip().title()
        self.time = time.strip().title()
        
        if qual_info in ['turmas', 'times', 'alunos', 'alunos grafico', 'times grafico']:
            self.arquivo = Arquivos().Ler_JSON('turmas.json')
        
        else: # user; alunos historico
            self.arquivo = Arquivos().Ler_JSON('users.json') 

    def Turmas(self):
        return list(self.arquivo) 

    def Times(self):
        return list(self.arquivo[self.turma])

    def Alunos(self):
        return self.arquivo[self.turma][self.time]['Alunos']
    
    def Alunos_historico(self):
        alunos = {}

        for user in self.arquivo:
            alunos[user] = self.arquivo[user]['Nome']

        return alunos

    def Alunos_graficos(self):
        alunos = []
        for turmas in self.arquivo:
            for times in self.arquivo[turmas]:
                alunos += self.arquivo[turmas][times]['Alunos']
        return alunos 

    def Alunos_graficos_antigo(self):
        lista_de_alunos = []

        for turmas in self.arquivo:
            for times in self.arquivo[turmas]:
                for alunos in self.arquivo[turmas][times]['Alunos']:
                    lista_de_alunos.append(f'{turmas} / {times} / {alunos}')
        
        return lista_de_alunos

    def Times_grafico(self):
        todos_times = []
        for turma in self.arquivo:
            todos_times += list(self.arquivo[turma])
        
        return todos_times 

    def Times_graficos_antigo(self):
        lista_de_times = []
        for turmas in self.arquivo:
            for times in self.arquivo[turmas]:
                lista_de_times.append(f'{turmas} / {times}')
        
        return lista_de_times

    def User(self):
        return user_info.user_info 

class RetornaInfoAcesso:
    def Inicio(self, qual_info, turma=''):
        qual_info = qual_info.lower()
        self.turma = turma.title()

        # Informações do usuario
        self.user_turma = user_info.user_info['Turma']
        self.user_time  = user_info.user_info['Time']
        self.user_cargo = user_info.user_info['Cargo']

        self.arquivo = Arquivos().Ler_JSON('turmas.json')
        
        if qual_info == 'turma':
            return self.Retorna_turma()

        elif qual_info == 'time':
            return self.Retorna_time()

        else: # alunos
            return self.Retorna_alunos()
            
    def Retorna_turma(self):
        if self.user_cargo == 'Fake Client':
            return list(self.arquivo)
        
        return [self.user_turma]

    def Retorna_time(self):
        if self.user_cargo == 'Fake Client':
            return list(self.arquivo[self.turma])

        return [self.user_time]

    def Retorna_alunos(self):        
        if self.user_cargo == 'Instrutor' or self.user_cargo == 'Fake Client':
            if self.user_cargo == 'Instrutor':
                id = 'Scrum Master'
            else:
                id = 'PO'
            
            alunos = []
            for turmas in self.arquivo:
                for times in self.arquivo[turmas]:
                    aluno = self.arquivo[turmas][times][id].strip()
                    if not aluno == '':
                        alunos.append(aluno)

            return alunos
        
        else:
            return self.arquivo[self.user_turma][self.user_time]['Alunos']

class Avaliar:
    def Salvar_avaiacao(self, info:dict):
        self.info = info
        tudo_respondido = self.__Conferir_info()

        if tudo_respondido:
            self.__Salvar()
            return True  
        
        else:
            return False 

    def __Conferir_info(self):
        for info_respondido in self.info.values():
            if info_respondido.strip() == '':
                return False

        return True

    def __Salvar(self):
        def get_key():
            '''Para salvar mais de uma avaliação do mesmo aluno'''
            try:
                key = int(max(list(historico_do_user))) + 1
            except:
                key = 1
            
            return str(key) 

        historico = Arquivos().Ler_JSON('histrc.json')
        
        nome_usuario = user_info.user_info['User']
        avaliado = self.info['Avaliado']

        if not nome_usuario in historico:
            historico[nome_usuario] = {}

        if not avaliado in historico[nome_usuario]:
            historico[nome_usuario][avaliado] = {}

        historico_do_user = historico[nome_usuario][avaliado]
        key = get_key()
        self.info['Sprint'] = 'Sprint 1'
        historico_do_user[key] = self.info
        Arquivos().Salvar_JSON('histrc.json', historico)

class Historico:
    def Retorna_historico(self, user):
        try:
            self.user = user.lower()
            self.nome = Arquivos().Ler_JSON('users.json')[user]['Nome']

            self.info = self.__Pegar_historico()

            return self.__Deixar_em_html()
        except:
            return ['<h1 class="sem-avaliacao"> Não tem nenhuma avaliação desse usuario </h1>']

    def __Pegar_historico(self):
        histrc = Arquivos().Ler_JSON('histrc.json')
        return histrc[self.user]
    
    def __Deixar_em_html(self):
        def Definir_pixel_div(item):
            lista_20px = [
                            'Turma',
                            'Time',
                            'Avaliado',
                            'Sprint'
                        ]
            px = 70
            if item in lista_20px:
                px = 20 
            
            return px

        '''
        

        
            <div class="info-left">
                <p class="info">Trabalho em equipe, cooperação e descentralização de conhecimento:</p>
            </div>
            <div class="info-right">
                <p class="info">Muito Bom</p>
            </div>
        </div>
        '''

        html = f'<div class="sprints"> <div class="info-sprint"> <p class="info"> Sprint 1 </p> </div> </div> \n'

        for id in self.info: 
            # Vai percorrer todos os alunos que o usuario avaliou
            # então a variavel "id" vai ser o nome do aluno que foi avaliado
            for id_avaliacao in self.info[id]:
                info_avaliacao = self.info[id][id_avaliacao]
                
                for info in info_avaliacao:
                    pixels = Definir_pixel_div(info)
                    html += '<div class="info-left-and-right"> \n'
                    html += f'<div class="info-left"> <p class="info"> {info}: </p> </div> \n'
                    html += f'<div class="info-right"> <p class="info"> {info_avaliacao[info]} </p> </div> \n'
                    html += '</div>'
        
        return html

class GraficoInfo:
    def Retorna_info_pro_grafico(self, qual_filtro, filtro=''):
        '''
        qual_filtro: Turma; Time; Avaliado
        filtro: Nome da Turma, Time ou Avaliado
        '''
        self.filtro = filtro.title().strip()
        self.historico   = Arquivos().Ler_JSON('histrc.json')
        
        if qual_filtro.lower() in ['turmas', 'times']:
            self.qual_filtro = qual_filtro.capitalize().strip('s')
        
        else:
            self.qual_filtro = 'Avaliado'
            
        self.perguntas = [
            'Trabalho em equipe, cooperação e descentralização de conhecimento',
            'Iniciativa e proatividade',
            'Autodidaxia e agregação de conhecimento ao grupo',
            'Entrega de resultados e participação efetiva no projeto',
            'Competência Técnica'
        ]

        soma_e_quantidade = self.__Pegar_info()
        self.medias = self.__Calcular_media(soma_e_quantidade)
        self.medias_filtrado =  self.__Achar_id()

        if self.medias_filtrado[0]:
            novo_dict = self.__Muduar_id(self.medias_filtrado[1])
            config = self.__Padronizar(novo_dict)
            return [True, config]
        
        # Se não entrou no if então não achou o aluno, 
        # então iremos retornar uma mensgem que foi escrita no metodo __Achar_id()
        return self.medias_filtrado

    def __Padronizar(self, informacoes:dict):
        def Cores_aleatoria(qntd):
            lista_de_cores = [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(151, 187, 205, 0.2)'
            ]
            cores  = choices(lista_de_cores, k=qntd)
            borda = [cor[:-6]+')' for cor in cores]

            return cores, borda

        # informacoes  = self.medias_filtrado
        label        = f'Gráfico filtrado por {self.qual_filtro}'
        labels       = list(informacoes)
        data         = [round(valor, 1) for valor in list(informacoes.values())]
        cores, borda = Cores_aleatoria(len(labels))
        background   = cores
        border       = borda

        data = {
            'labels': labels,
            'datasets': [{
                'label': label,
                'data': data,
                'backgroundColor': background,
                'borderColor': border,
                'borderWidth': 1
            }]
        }
        options = {
            'scales': {
                'y': {
                    'beginAtZero': True,
                    'min': 0,
                    'max': 5,
                    'ticks': {
                        'stepSize': 0.5
                    }
                }
            }
        }

        config = {
            'type': 'bar',
            'data': data,
            'options': options
        }

        return config 

    def __Muduar_id(self, dict:dict):
        skills = ['Skill 1', 'Skill 2', 'Skill 3', 'Skill 4', 'Skill 5']
        valores = list(dict.values())
        novo_dict = {}
        for cont in range(5):
            novo_dict[skills[cont]] = valores[cont]
        
        return novo_dict

    def __Achar_id(self):
        try:
            return [True, self.medias[self.filtro]]
        except:
            return [False, f'Não foi encontrado nenhuma avaliação para esse(a) {self.qual_filtro}']
        
    def __Pegar_info(self):
        info_avaliacao_dict = {}
        for user_avaliador in self.historico:
            info_avaliador = self.historico[user_avaliador]
            for avaliado in info_avaliador:
                info_avaliado = info_avaliador[avaliado]
                for id in info_avaliado:
                    id_info_avaliado = info_avaliado[id]
                    # Se for time então vai pegar o time, se for turma então vai pegar a turma
                    filtro = id_info_avaliado[self.qual_filtro]

                    # if self.qual_filtro == 'Time':
                    #     filtro = id_info_avaliado['Turma'] + ' / ' + filtro
                    
                    # elif self.qual_filtro == 'Avaliado':
                    #     filtro = id_info_avaliado['Turma'] + ' / ' + id_info_avaliado['Time'] + ' / ' + filtro

                    if not filtro in info_avaliacao_dict:
                        info_avaliacao_dict[filtro] = {
                            self.perguntas[0]: {'Soma': 0, 'Quantidade': 0},
                            self.perguntas[1]: {'Soma': 0, 'Quantidade': 0},
                            self.perguntas[2]: {'Soma': 0, 'Quantidade': 0},
                            self.perguntas[3]: {'Soma': 0, 'Quantidade': 0},
                            self.perguntas[4]: {'Soma': 0, 'Quantidade': 0}
                        }

                    for cont in range(5):
                        info_avaliacao_dict[filtro][self.perguntas[cont]]['Soma'] += self.__Transformar_valores(id_info_avaliado[self.perguntas[cont]])
                        info_avaliacao_dict[filtro][self.perguntas[cont]]['Quantidade'] += 1
                    
        return info_avaliacao_dict

    def __Transformar_valores(self, valor):
        if valor == 'Excelente':
            novo_valor = 5

        elif valor == 'Muito Bom':
            novo_valor = 4

        elif valor == 'Bom':
            novo_valor = 3

        elif valor == 'Regular':
            novo_valor = 2

        else: # Ruim
            novo_valor = 1

        return novo_valor

    def __Calcular_media(self, informacoes):
        for id in informacoes:
            for pergunta in informacoes[id]:
                informacoes[id][pergunta] = informacoes[id][pergunta]['Soma'] / informacoes[id][pergunta]['Quantidade']
        
        return informacoes



def Criptografar(senha):
    return hashlib.md5(bytes(senha, encoding="utf-8")).hexdigest()

def Login(user, senha):
    todos_users = Arquivos().Ler_JSON('users.json')
    user = user.strip()

    if user in todos_users:
        senha = Criptografar(senha)
        if senha == todos_users[user]['Senha']:
            # Salvando algumas informações do aluno para usar depois como o cargo e nome
            global user_info
            user_info = DeclararUser(user)
            return True 
    
    return False 

def Caminho_ate_Falcon():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Falcon', os.path.dirname(__file__))[0]




# print(GraficoInfo().Retorna_info_pro_grafico('turmas', 'Banco De Dados - 2º Sem 2022'))
