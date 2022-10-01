
import win32com.client as win32

import smtplib 
def Enviar_email(user_adm_info:dict, user_info:dict):
    outlook = win32.Dispatch('outlook.application')

    email = outlook.CreateItem(0)
    
    email.To = user_adm_info['Email']
    email.Subject = 'Pedido de Acesso'
    email.HTMLBody = f'''
    <p> {user_adm_info['Nome']}, um novo pedido de acesso foi requisitdo!</p> 
    <p> O Usuario {user_info['User']} pediu acesso para ser um aluno lider </p> 
    <p> O Usuario {user_info['User']} pediu acesso para ser um aluno lider </p> 
    '''
    email.Send()

# Enviar_email({'Nome': 'Lukas', 'Email': 'lkfernando12345@gmail.com'}, {'User':'lkfernando'})
