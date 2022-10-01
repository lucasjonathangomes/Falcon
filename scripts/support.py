
import os
import json
from tkinter import *
from re import findall
from tkinter import ttk
# import awesometkinter as atk
from tkinter import messagebox
from random import randrange, choice

class Declarar_user: 
    def __init__(self, user):
        json_info = Ler_JSON('users.json')
        user_info = json_info[user] 
        self.user = user
        self.email = user_info['email']
        self.cargo = user_info['cargo']
        self.acesso = user_info['acesso'] 

def Retorna_imagem(nome):
    '''Retorna a imagem da pasta "fotos"'''
    path = Caminho_ate_Falcon()
    return PhotoImage(file=f'{path}\\fotos\\{nome}')

def Destruir_itens(lista:list):
    '''
    Para destruir (apagar) itens. Recebe uma lista como parametro. \n
    Exemplo de itens: Botões, Label, Entry, ...\n 
    '''
    for item in lista:
        try:
            item.destroy()

        except:
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

def Criar_Perguntas(frame:Frame, perguntas:list, entry_width:int|None=None, values:list|None=None, answer_style:str='entry', cor_fund:str|None=None, cor_letr:str|None=None, font:tuple|None=None):
    '''
    Cria as perguntas da lista "perguntas". \n
    As perguntas são criadas como Label, mas as resposta podem ser criadas como Entry ou Combobox, 
    você escolhe no parametro "style_answer" (entry, combobox). \n
    Retorna duas listas com os elementos das perguntas e respostas, respectivamente, que foram criados.
    '''
    answer_style = answer_style.lower().strip()
    lista_perguntas = []
    lista_perguntas = []

    for pergunta in perguntas:
        p = Label(frame, text=pergunta, font=font)
        p.pack()

        if answer_style == 'entry':
            r = Entry(frame, font=font, width=entry_width) 
        elif answer_style == 'combobox':
            r = ttk.Combobox(frame, values=values, font=font)
        else:
            raise 'Valor invalido para o parametro answer_style. Valores esperado: (entry, combobox)'
        r.pack()
        # Label(frame).pack()
    
    return lista_perguntas, lista_perguntas

