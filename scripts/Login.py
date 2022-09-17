
# from Avaliacao_FK import *
from Avaliacao import * 
from Cadastrar import * 
from support import *


class Login:
    def __init__(self, jan):
        self.jan = jan
        self.jan.geometry("1440x1024+350+20")
        self.jan.resizable(width=FALSE, height=FALSE)

        self.login_name = Label(self.jan, text='Login', fg='red', font=('Arial', 100))
        self.login_name.place(x=500, y=300)

        self.user = Label(self.jan, text='Usuario', font=('Arial', 20), fg='blue')
        self.user.place(x=500, y=500)

        self.user_entry = Entry(self.jan, width=25)
        self.user_entry.place(x=610, y=515)

        self.pasw = Label(self.jan, text='Senha', font=('Arial', 20), fg='blue')
        self.pasw.place(x=500, y=600)

        self.pasw_entry = Entry(self.jan, width=25, show='*')
        self.pasw_entry.place(x=610, y=615)

        self.login_button = Button(self.jan, text='Login', font=('Arial', 10), fg='blue', 
                                    command=lambda:self.Sing_in(self.user_entry.get(), self.pasw_entry.get()))
        self.login_button.place(x=820, y=580)

        self.register_button = Button(self.jan, text='Registrar-se', font=('Arial', 10), fg='blue', command=lambda:self.Sing_up())
        self.register_button.place(x=820, y=610)

        self.lista_itens = [self.user, self.user_entry, self.pasw,self.pasw_entry, self.login_button, self.register_button, self.login_name]

    def Sing_in(self, user, psw):
        users = Ler_JSON('users.json')

        if user in users:
            passw = users[user]['senha']
            if passw == psw:
                Destruir_itens(self.lista_itens)
                # user_info = Declarar_user(user)
                # AvaliacaoFK(self.jan, user_info)
                Avaliar(self.jan)
            
            else:
                self.Mensagem_erro()
        
        else:
            self.Mensagem_erro()

    def Sing_up(self):
        Cadastrar(self.jan) 

    def Mensagem_erro(self):
        messagebox.showerror(title='ERROR', message='Algo deu errado, verifique seu usuario e/ou sua senha')




# jan = Tk()

# Login(jan)

# jan.mainloop()

