class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def farol(self):
        print(f"O {self.marca} {self.modelo} está com o farol aceso: farol alto.")

# Criando um objeto da classe Carro
meu_carro = Carro("Uno", "com escada", 2022)

# Chamando o método farol
meu_carro.farol()