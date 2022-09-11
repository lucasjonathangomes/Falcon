
import os
import json
from tkinter import *
from re import findall
import awesometkinter as atk
from random import randrange, choice
from tkinter import filedialog, messagebox, ttk


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

def Caminho_ate_Scripts():
    '''Retorna o caminho completo até a pasta Scripts'''
    return findall(r'.*Scripts', os.path.dirname(__file__))[0]


