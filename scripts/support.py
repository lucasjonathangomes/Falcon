
import os
import json
import hashlib
from re import findall
from random import randrange, choice

class Cadastrar:
    def Iniciar_cadastro(self, oq_cadastrar:str, info:dict):
        self.info = info 

        if oq_cadastrar == 'usuario':
            self.json_user = Ler_JSON('users.json')
            return self.Cadastrar_usuario()

        else:
            self.json_turmas = Ler_JSON('turmas.json')
            
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
            Salvar_JSON('turmas.json', self.json_turmas)
            return [True, f'Turma "{turma_nome}" salvo com sucesso!']

    def Cadastrar_time(self):
        pass 

    def Cadastrar_usuario(self):
        pasw = self.info['Senha']
        senha = hashlib.md5(bytes(pasw, encoding="utf-8")).hexdigest()
        

    def Cadastrar_sprint(self):
        pass 

def Ler_JSON(nome):
    with open(Caminho_ate_Falcon()+'\\json\\'+nome, encoding="utf-8") as a:
        arquivo = json.load(a) 
    return arquivo 

def Ler_Excel():
    pass 

def Salvar_JSON(nome:str, novo_json:dict):
    with open(Caminho_ate_Falcon()+'\\json\\'+nome, 'w') as a:
        json.dump(novo_json, a, indent=4)

def Caminho_ate_Falcon():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Falcon', os.path.dirname(__file__))[0]
