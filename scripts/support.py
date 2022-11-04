
import os
import json
import hashlib
from re import findall

class DeclararUser: 
    def __init__(self, user):
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
        Recebe dois parametros. \n
        oq_cadastrar: O que quer cadastrar - turma; time; sprint; aluno \n
        info: Todas as informações necessarias para cadastrar o que você escolheu (tem que ser em dicionario) \n
        Retorna: Uma lista. \n
        1° item: True ou False (se conseguiu ou não cadastrar) \n
        2° item: Uma mensagem, se não conseguiu cadastrar essa mensagem fala o porque \n
        Exemplo: [True, "Aluno salvo com sucesso!"] \n
        Exemplo: [False, "Ja existe esse time na turma Falcon"]
        '''
        self.info = info

        if oq_cadastrar == 'aluno':
            self.json_user = Arquivos().Ler_JSON('users.json')
            return self.Cadastrar_aluno()

        else:
            self.json_turmas = Arquivos().Ler_JSON('turmas.json')
            
            if oq_cadastrar == 'turma':
                return self.Cadastrar_turma() 

            elif oq_cadastrar == 'time':
                return self.Cadastrar_time() 
                
            elif oq_cadastrar == 'sprint':
                return self.Cadastrar_sprint() 

    def Cadastrar_turma(self):
        turma_nome = self.info['Turma'].strip()
        if turma_nome in self.json_turmas:
            return [False, f'Turma "{turma_nome}" já existe']
        
        else:
            self.json_turmas[turma_nome] = {}

            Arquivos().Salvar_JSON('turmas.json', self.json_turmas)
            return [True, f'Turma "{turma_nome}" salvo com sucesso!']

    def Cadastrar_time(self):
        turma = self.info['Turma'].strip()
        time = self.info['Time'].strip()

        if time.lower() in [nome.lower() for nome in self.json_turmas[turma]]:
            # Ja existe o nome do time escolhido no banco de dados
            return [False, f'O time "{time}" já existe na turma {turma}. Escolha outro nome para o time ou use o time que já existe']

        else:
            self.json_turmas[turma][time] = {}
            Arquivos().Salvar_JSON('turmas.json', self.json_turmas)
            return [True, f'Time "{time}" salvo com sucesso na turma {turma}']

    def Cadastrar_aluno(self):
        def Criar_nome_user(user):
            cont = 1
            while True:
                novo_user = user + str(cont)
                if not novo_user in self.json_user:
                    return novo_user

        def Validar_senha(senha):
            todos_regex = ['[a-z]', '[A-Z]', '[!|@|#|$|%|&|*|(|)]', '[1-9]']

            for regex in todos_regex:
                if len(findall(regex, senha)) == 0 or len(senha) < 8:
                    msg = 'A senha tem que ter no minimo 8 digitos, letras minúscula e maiúscula, '\
                        'numeros, e um dos caracteres especiais a seguir: !, @,#, $, %, &, *, (, )'
                    return [False, msg]

            return [True]

        # Padronizar as informações 
        nome  = self.info['Nome'].strp().title()
        email = self.info['Email'].strp()
        senha = self.info['Senha']

        # Fazer todas as validações 
        # Turma 
        if self.info['Turma'].strp() == '':
            return [False, 'Seleciona uma turma para esse aluno']
        
        # Time
        if self.info['Time'].strp() == '':
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

        senha = hashlib.md5(bytes(senha, encoding="utf-8")).hexdigest()
        user = email.split('@')[0].strip()

        if user in self.json_user:
            user = Criar_nome_user(user)
        
        self.info['Senha'] = senha 
        self.json_user[user] = self.info 

        Arquivos().Salvar_JSON('users.json', self.json_user)

        return [True, f'Aluno salvo com sucesso! Nome de usuario é: {user}']
   
    def Cadastrar_sprint(self):
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
        self.turma = turma.strip()
        self.time = time.strip()

        if qual_info in ['turmas', 'times']:
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

def Login(user, senha):
    todos_users = Arquivos().Ler_JSON('users.json')
    user = user.strip()

    if user in todos_users:
        senha = hashlib.md5(bytes(senha, encoding="utf-8")).hexdigest()
        if senha == todos_users[user]['Senha']:
            global user_info
            user_info = DeclararUser(user)
            return True 
    
    return False 

def Caminho_ate_Falcon():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Falcon', os.path.dirname(__file__))[0]

