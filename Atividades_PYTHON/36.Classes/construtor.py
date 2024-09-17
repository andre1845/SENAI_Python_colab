
class Pessoa:
   # Metodo CONSTRUTOR 
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        
    def cumprimentar(self, nome):
        print (f'Ola {nome}, tudo bem?')
    
    def responder(self, nome1):
        print (f'Estou bem, {nome1}. e vc?')
    

        
        
if __name__ == '__main__':
    
    #nome = input('Informe o nome do usuário: ')
    #idade = int(input('Informe a idade do usuário: '))
    #cpf = input('Informe o cpf do usuário: ')
    #email = input('Informe o email do usuário: ')
    
    ## usuario = Pessoa(nome, idade, cpf, email)
    
    # print(f'Nome: {usuario.nome}')
    # print(f'cpf: {usuario.cpf}')
    # print(f'Idade: {usuario.idade}')
    # print(f'email: {usuario.email}')
    
    p1 = Pessoa('Mario', 34, '222333444', 'as@sa.com')
    p2 = Pessoa('Juia', 29, '222111333','qw@sa')
    
    p1.cumprimentar(p2.nome)
    p2.responder(p1.nome)
    
    
    