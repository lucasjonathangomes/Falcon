
import os
import json
from tkinter import *
from re import findall
import awesometkinter as atk
from tkinter import messagebox
from random import randrange, choice

class Declarar_user: 
    def __init__(self, user, email:str|None=None, cargo:str|None=None, acesso:str|None=None):
        self.user = user 
        self.email = email
        self.cargo = cargo
        self.acesso = acesso 

def Retorna_imagem(nome):
    '''Retorna a imagem da pasta "fotos"'''
    path = Caminho_ate_Scripts()
    print(path)
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
    with open(Caminho_ate_Scripts()+'\\json\\'+nome, encoding="utf-8") as a:
        arquivo = json.load(a) 
    return arquivo 

def Ler_Excel():
    pass 

def Salvar_JSON(nome:str, novo_json:dict):
    with open(Caminho_ate_Scripts()+'\\json\\'+nome, 'w') as a:
        json.dump(novo_json, a)

def Caminho_ate_Scripts():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Scripts', os.path.dirname(__file__))[0]

def Criar_Perguntas(frame:Frame, perguntas:list, cor_fund:str|None=None, cor_letr:str|None=None, font:tuple|None=None):
    '''
    Cria perguntas da lista "perguntas". \n
    Retorna a lista com os elementos (Label) que foram criados.
    '''
    list_label_perguntas = []
    list_entry_perguntas = []

    for pergunta in perguntas:
        p = Label(frame, text=pergunta, font=font)
        p.pack()
        r = Entry(frame, width=5)
        r.pack()
        list_label_perguntas.append(p)
        list_entry_perguntas.append(r)
    
    return list_label_perguntas, list_entry_perguntas



