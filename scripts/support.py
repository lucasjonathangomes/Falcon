
import os
import json
import hashlib
from re import findall

class DeclararUser: 
    def __init__(self, user):
        '''
        Esse metodo vai salvar o user em uma instancia para que posa ser usado depois as infomações do usuário 
        '''

        json_info = Arquivos().Ler_JSON('users.json')
        user_info = json_info[user]
        self.user_info = {
                            'User': user,
                            'Nome': user_info['Nome'], 
                            'Email': user_info['Email'],
                            'Cargo': user_info['Cargo']
                        }

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

        if oq_cadastrar == 'aluno':
            self.json_user = Arquivos().Ler_JSON('users.json')
            return self.__Cadastrar_aluno()

        else:
            self.json_turmas = Arquivos().Ler_JSON('turmas.json')
            
            if oq_cadastrar == 'turma':
                return self.__Cadastrar_turma() 

            elif oq_cadastrar == 'time':
                return self.__Cadastrar_time() 
                
            elif oq_cadastrar == 'sprint':
                return self.__Cadastrar_sprint() 

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

    def __Cadastrar_aluno(self):
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

        def Validar_senha(senha):
            '''Vai verificar se está de acordo com o esperado - quantidade de digitos; letras; numeros; caracteres especiais'''
            todos_regex = ['[a-z]', '[A-Z]', '[!|@$|%|&|*|(|)]', '[1-9]']

            for regex in todos_regex:
                if len(findall(regex, senha)) == 0 or len(senha) < 8:
                    msg = 'A senha tem que ter no minimo 8 digitos, letras minúscula e maiúscula, '\
                        'numeros, e um dos caracteres especiais a seguir: !, @,#, $, %, &, *, (, )'
                    return [False, msg]

            return [True]

        def Salvar_aluno_no_time(turma, time, cargo, nome):
            turmas = Arquivos().Ler_JSON('turmas.json')

            if cargo == 'Desenvolvedor':
                # Se for desenvolvedor apenas adicionamos o nome do aluno na lista
                turmas[turma][time][cargo].append(nome)
            
            else:
                if turmas[turma][time][cargo] != '':
                    # Se o cargo escolhido para esse aluno já estiver ocupado, então vamos retornar False 
                    # e o nome do aluno que está no cargo escolhido
                    return [False, turmas[turma][time][cargo]]
                
                else:
                    # Se não tiver ocupado então salvamos o aluno nesse cargo
                    turmas[turma][time][cargo] = nome
            
            # Adicionamos esse aluno na lista de alunos
            turmas[turma][time]['Alunos'].append(nome)
            Arquivos().Salvar_JSON('turmas.json', turmas)

            return [True]

        # Padronizar as informações 
        turma = self.info['Turma'].strip()
        time  = self.info['Time'].strip()
        nome  = self.info['Nome'].strip().title()
        email = self.info['Email'].strip()
        senha = self.info['Senha']
        cargo = self.info['Cargo']

        ## Fazer todas as validações ##

        # Turma 
        if turma == '':
            return [False, 'Seleciona uma turma para esse aluno']
        
        # Time
        if time == '':
            return [False, 'Seleciona um time para esse aluno'] 

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

        ## Fim das validações ## 

        senha = hashlib.md5(bytes(senha, encoding="utf-8")).hexdigest()
        user = email.split('@')[0].strip()

        if user in self.json_user:
            user = Criar_nome_user(user)
        
        deixar_sequencial = {
                'Nome' : nome,
                'Email': email,
                'Turma': turma,
                'Time' : time,
                'Cargo': cargo,
                'Senha': senha 
        }

        self.json_user[user] = deixar_sequencial 

        usuario_salvo_no_time = Salvar_aluno_no_time(turma, time, cargo, nome)
        if not usuario_salvo_no_time[0]:
                return [False, f'O cargo "{cargo}" já esta preenchido pelo aluno "{usuario_salvo_no_time[1]}" para essa turma e time escolhido']

        Arquivos().Salvar_JSON('users.json', self.json_user)

        return [True, f'Aluno salvo com sucesso! Nome de usuario é: {user}']

    def __Cadastrar_sprint(self):
        pass
       
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

        if qual_info in ['turmas', 'times', 'alunos']:
            self.arquivo = Arquivos().Ler_JSON('turmas.json')
        else:
            self.arquivo = Arquivos().Ler_JSON('users.json') 

    def Turmas(self):
        return list(self.arquivo) 

    def Times(self):
        return list(self.arquivo[self.turma])

    def Alunos(self):
        return self.arquivo[self.turma][self.time]['Alunos']
    
    def User(self):
        return user_info.user_info 

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
        self.user = user.lower()
        self.nome = Arquivos().Ler_JSON('users.json')[user]['Nome']

        self.info = self.__Pegar_historico()

        return self.__Deixar_em_html()

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



        html = f'<h2> Avaliador: {self.nome} </h2> \n'

        for id in self.info: 
            # Vai percorrer todos os alunos que o usuario avaliou
            # então a variavel "id" vai ser o nome do aluno que foi avaliado
            html += f'<h3> Avaliado: {id} </h3> \n'

            for id_avaliacao in self.info[id]:
                info_avaliacao = self.info[id][id_avaliacao]
                
                for info in info_avaliacao:
                    pixels = Definir_pixel_div(info)
                    html += '<div class="info-left-and-right"> \n'
                    html += f'<div class="info-left"> <p class="info" id="info-{pixels}px"> {info}: </p> </div> \n'
                    html += f'<div class="info-left"> <p class="info" id="info-{pixels}px"> {info_avaliacao[info]} </p> </div> \n'
                    html += '</div>'
        
        return html




def Login(user, senha):
    todos_users = Arquivos().Ler_JSON('users.json')
    user = user.strip()

    if user in todos_users:
        senha = hashlib.md5(bytes(senha, encoding="utf-8")).hexdigest()
        if senha == todos_users[user]['Senha']:
            # Salvando algumas informações do aluno para usar depois como o cargo e nome
            global user_info
            user_info = DeclararUser(user)
            return True 
    
    return False 

def Caminho_ate_Falcon():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Falcon', os.path.dirname(__file__))[0]


# print(Historico().Retorna_historico('lu'))
