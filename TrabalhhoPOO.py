##- Criar uma aplicação simulando um sistema de pagamento de uma empresa. Utilize o conceito de "INTERFACE" estudado nas últimas aulas. A ideia é simular o esquema de pagamento dos funcionários,
# onde para cada classe de um tipo de funcionário (por exemplo, gerente, desenvolvedor sênior, estagiário) ele tenha seu próprio cálculo de salário;
##- No final do arquivo principal dar uma breve explicação de como sua aplicação está funcionando;
##- Fiquem à vontade para criar o código em qualquer linguagem de programação orientada a objetos.


class Funcionario:
    
    def __init__ (self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

#Definindo a classe Funcionario com os atributos : nome, funcao e salario

    def salario_definido(self):
        salario = 0
        if self.funcao == "Gerente":
            salario = 10000
        elif self.funcao == "Dev":
            salario = 8000
        elif self.funcao == "Estagiario":
            salario = 2000
        else:
            salario = 0
        self.salario = salario
        return self.salario

#Metodo calcular salario que vai definir o salario de acordo com a funcao do funcionario, ja estando definido o valor de cada funcao

class Gerente(Funcionario):
    
    def __init__(self, nome):
        super().__init__(nome, "Gerente", 0)
        self.salario_definido()

class Dev(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, "Dev", 0)
        self.salario_definido()

class Estagiario(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, "Estagiario", 0)
        self.salario_definido()

#Definidas as classes dos funconarios, herdando da classe Funcionario e chamando o metodo salario_definido no seu metodo construtor

def main():
    funcionarios = [
        Gerente("Neymar"),
        Dev("Messi"),
        Estagiario("Cristiano Ronaldo"),
    ]

    for funcionario in funcionarios:
        print(f"Nome: {funcionario.nome}, Função: {funcionario.funcao}, Salário: R${funcionario.salario:.2f}")
    
if __name__ == "__main__":
    print("Sistema de Pagamento de Funcionários")
    print("====================================")
    print("Funcionários cadastrados:")
    print("------------------------------------")
    main()

# A função main cria uma lista de funcionários com diferentes funções 
#O for chama o a classe funcionario dentro da aba de funcionarios, e printa os detalhes