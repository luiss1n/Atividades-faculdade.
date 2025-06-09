##- Criar uma aplicação simulando um sistema de pagamento de uma empresa. Utilize o conceito de "INTERFACE" estudado nas últimas aulas. A ideia é simular o esquema de pagamento dos funcionários,
# onde para cada classe de um tipo de funcionário (por exemplo, gerente, desenvolvedor sênior, estagiário) ele tenha seu próprio cálculo de salário;
##- No final do arquivo principal dar uma breve explicação de como sua aplicação está funcionando;
##- Fiquem à vontade para criar o código em qualquer linguagem de programação orientada a objetos.

funcionarios = []

#Aquii eu defini a lista funcionarios que vai armazenar os dados dos funcionarios cadastrados, Defino pro programa ficar em loop, até o usuario sair

while True:
    print("\nBem vindo à folha de pagamento da empresa LSZ")
    print("Você deseja fazer qual opção?")
    print("1 - Cadastrar Funcionário")
    print("2 - Ver Funcionário e Salário")
    print("3 - Receber Salário")
    print("4 - Sair do sistema")

#Printei as opções que o usuário pode escolher

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do funcionário: ")
        funcao = input("Digite a função do funcionário (Gerente, Dev, Estagiário): ")

        if funcao == "Gerente":
            salario = 10000
        elif funcao == "Dev":
            salario = 8000
        elif funcao == "Estagiario":
            salario = 2000
        else:
            salario = 0
            print("Você tá brincando comigo? Salário definido como R$0.")

        funcionarios.append({
            "nome": nome,
            "funcao": funcao,
            "salario": salario,
            "total_recebido": 0
        })

        print(f"Funcionário cadastrado: Nome: {nome}, Função: {funcao}, Salário: R${salario:.2f}")

#A função apppend adiciona um "armazem" com os dados do funcionário na lista funcionarios , qui ele cadastra o funcionário, recebendo o nome e a função, e definindo o salário de acordo com a função que ele escolheu

    elif opcao == 2:
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print("\nFuncionários cadastrados:")
            for f in funcionarios:
                print(f"Nome: {f['nome']}, Função: {f['funcao']}, Salário: R${f['salario']:.2f}, Total Recebido: R${f['total_recebido']:.2f}")

# Aqui ele verifica se há funcionários cadastrados, e se ele existir, printa os dados

    elif opcao == 3:
        nome = input("Digite o nome do funcionário: ")
        encontrado = False
        for f in funcionarios:
            if f["nome"] == nome:
                f["total_recebido"] += f["salario"]
                total_geral = f["salario"] + f["total_recebido"]

                print("\nPagamento realizado com sucesso:")
                print(f"Nome: {f['nome']}")
                print(f"Função: {f['funcao']}")
                print(f"Salário Base: R${f['salario']:.2f}")
                print(f"Total Recebido até agora: R${f['total_recebido']:.2f}")
                print(f"Total Acumulado (Salário Base + Total Recebido): R${total_geral:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Funcionário não encontrado, tente ver a lista e coloque um funcionário que trabalhe aqui.")

#Aqui ele ve se o funcionário existe, e se existir, ele recebe o salario, e adiciona o valor ao seu salario total, e mostra tudo que ele ja recebeu

    elif opcao == 4:
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
#Aqui ele ve se a opção é válida, e se não for, ele pede para o usuário tentar novamente, e se ele sair, quebra o sistema
