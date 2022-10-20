
# POO - Programação Orientada a Objetos

# class = Classe (conjunto de metodos)
# def   = Metodos 

class Pessoa:
    # Metodo construtor. Voce nao chama esse metodo, ele é altomaticamente usado quando voce chama a classe (Pessoa)
    def __init__(self, nome, idade, cpf, rg, pais):
        self.nome  = nome
        self.idade = idade
        self.cpf   = cpf
        self.rg    = rg
        self.pais  = pais

    # Todos os outros metodos abaixo precisam ser chamados
    def Andar(self):
        print(f'O(a) {self.nome} esta andando')

    def Comer(self):
        print(f'O(a) {self.nome} esta comendo')

    def Pagar(self):
        print(f'O(a) {self.nome} esta pagando conta do cpf: {self.cpf} no {self.pais}')

    def Info(self):
        print(f'Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf} \nRG: {self.rg} \nPais: {self.pais}')



# Objeto
pessoa_1 = Pessoa('Lukas', 22, 12345, 54321, 'Brasil')

# Com esse objeto "pessoa_1" você pode usar o metodo e variaveis (iniciadas com "self.") da classe onde esse objeto foi criado
print('Usando os metodos')
pessoa_1.Andar()
pessoa_1.Comer()
pessoa_1.Pagar()
pessoa_1.Info()
print('\nUsando as variaveis')
print(f'Nome: {pessoa_1.nome}')
print(f'Idade: {pessoa_1.idade}')
print(f'CPF: {pessoa_1.cpf}')
print(f'RG: {pessoa_1.rg}')
print(f'Pais: {pessoa_1.pais}')




