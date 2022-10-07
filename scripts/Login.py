
from support import *
from Avaliacao import *

class Login:
    def __init__(self, jan):
        self.jan = jan

        self.frame_login = Frame(self.jan, width=500, height=800)
        self.frame_login.pack(side='right')

        self.frame_logo = Frame(self.jan, width=500, height=800)
        self.frame_logo.pack(side='left')

        self.font_label = ('Arial', 20)
        self.font_entry = ('Arial', 15)

        self.Criar_elementos()
    
    def Criar_elementos(self):
        self.img_confirmar = Retorna_imagem('bt_confirmar.png')
        self.img_logo = Retorna_imagem('logo_falcon.png')

        self.label_logo = Label(self.frame_logo, image=self.img_logo)#, relief='groove')
        self.label_logo.pack(side='left')

        self.user = Label(self.frame_login, text='Usuario', font=self.font_label)
        self.user.place(x=10, y=250)

        self.user_entry = Entry(self.frame_login, width=25, font=self.font_entry)
        self.user_entry.place(x=10, y=300)

        self.pasw = Label(self.frame_login, text='Senha', font=self.font_label)
        self.pasw.place(x=10, y=400)

        self.pasw_entry = Entry(self.frame_login, width=25, show='*', font=self.font_entry)
        self.pasw_entry.place(x=10, y=450)

        self.login_button = Button(self.frame_login, image=self.img_confirmar, command=lambda:self.Sing_in())
        self.login_button.place(x=100, y=550)

    def Sing_in(self):
        user = self.user_entry.get().strip()
        psw  = self.pasw_entry.get()

        todos_usuario = Ler_JSON('users.json')

        if user in todos_usuario:
            usuario = todos_usuario[user]
            passw = usuario['senha']
            if passw == psw:
                self.frame_logo.destroy()
                self.frame_login.destroy()

                user_info = {'User': user, 'Perfil': usuario['perfil']}
                
            
            else:
                self.Mensagem_erro()
        
        else:
            self.Mensagem_erro()


    def Mensagem_erro(self):
        messagebox.showerror(title='ERROR', message='Algo deu errado, verifique seu usuario e/ou sua senha')



# jan = Tk()
# Login(jan)
# jan.mainloop()

