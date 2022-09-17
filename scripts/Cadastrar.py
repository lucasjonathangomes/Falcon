
from support import *


class Cadastrar:
    def __init__(self, jan):
        self.jan = jan
        self.path = Caminho_ate_Falcon()+"//fotos//"

        self.jan.geometry("1440x1024+350+20")
        self.jan.iconbitmap(default=self.path+"telaCadastro.png")
        self.jan.resizable(width=FALSE, height=FALSE)

        self.Criar_Label()

    def Criar_Label(self):
        self.img_fundo = Retorna_imagem('telaCadastro.png')
        self.img_botao = Retorna_imagem("botao.png")
        
        self.label_fundo = Label(self.jan, image=self.img_fundo)
        self.label_fundo.pack()

        self.listaCargo = ["Admin", "Aluno PO", "Líder do Grupo/Instrutor", "Fake Client", "Líder Tecnico", "Aluno"]

        self.ComboBox_cargo = ttk.Combobox(values=self.listaCargo)
        self.ComboBox_cargo.place(width=500, height=60, x=323, y=320)

        self.entryNome = Entry(self.jan, bd=2, font=("Arial", 20), justify=LEFT)
        self.entryNome.place(width=500, height=60, x=323, y=447)

        self.entryEmail = Entry(self.jan, bd=2, font=("Arial", 20), justify=LEFT)
        self.entryEmail.place(width=500, height=60, x=323, y=547)

        self.entrySenha = Entry(self.jan, show="*", bd=2, font=("Arial", 20), justify=LEFT)
        self.entrySenha.place(width=500, height=60, x=323, y=647)

        self.botaoCadastro = Button(self.jan, bd=0, image=self.img_botao, command=self.Salvar_user)
        # self.botaoCadastro.place(width=279, height=69, x=550, y=805)
        self.botaoCadastro.place(width=279, height=69, x=800, y=505)

        self.lista_itens = [self.label_fundo, self.ComboBox_cargo, self.entryNome, self.entryEmail, self.entrySenha, self.botaoCadastro]

    def Salvar_user (self):
        self.cargo = self.ComboBox_cargo.get()
        self.nome = self.entryNome.get().strip()
        self.email = self.entryEmail.get().strip()
        self.senha = self.entrySenha.get()

        self.users = Ler_JSON('users.json')

        info_user_valido = self.Validar_info()

        if info_user_valido:
            self.users[self.user_name] = {   
                                            "nome": self.nome,
                                            "cargo": self.cargo,
                                            "email": self.email,
                                            "acesso": 'Aluno',
                                            "senha": self.senha
                                        }
            
            Salvar_JSON('users.json', self.users)
            Destruir_itens(self.lista_itens)
    
    def Validar_info(self):
        status = False 
        user = self.email.split('@')[0].lower()

        # Verificar Cargo 
        if self.cargo.strip() == '' or self.cargo.strip() not in self.listaCargo:
            self.Error('Cargo', 'O cargo não existe e/ou não foi selecionando')
        # Verificar Nome
        elif self.nome.strip() == '':
            self.Error('None', 'O nome é obrigatório')
        
        # Verificar Email
        elif '@' not in self.email:
            self.Error('Email invalido', 'O Email está no formato errado. \nExemplo: exemplo@gmail.com')

        # Verificar User
        elif user in self.users:
            self.Error('Nome do Email ja cadastrado', f'O nome "{user}" ja esta cadastrado, se esqueceu a senha aperte em "esqueci a senha" na hora de fazer o login. \nOBS: A extenção do email não diferencia o nome de usuario.')

        # Verificar Senha
        elif len(self.senha) < 5:
            self.Error('Senha', 'A senha deve ter no minimo 5 digitos')
   
        # Passou em todos os anteriores
        else:
            self.user_name = user
            status = True 
        
        return status 

    def Error(self, titulo, msg):
        messagebox.showerror(titulo, msg)
        

# jan = Tk()
# Cadastrar(jan)
# jan.mainloop()

