#Função que imprime o menu do banco para os clientes

def menu():
    print('1 - Novo Cliente')
    print('2 - Apaga Cliente')
    print('3 - Débito')
    print('4 - Depósito')
    print('5 - Extrato')
    print('6 - Transferência Entre Contas')
    print("7 - Poupança")
    print('0 - Sair')


#Função que pede um valor referente ao menu para o cliente
def escolha_menu():
    escolhamenu = int(input("Escolha a opção desejada: "))
    return escolhamenu



#Função que armazena dados de novo cliente e os imprime
def novo_cliente():
        # Variavel para abrir o arquivo que irá guardar as informações dos clientes 
        arquivo = open("arquivo.txt", "a")
        nome = input("Digite seu nome: ")
        cpf = int(input("Digite seu CPF: "))
        conta = input("Qual o tipo de conta, comum ou plus: ")
        valor = int(input("Qual valor inicial de sua conta: "))
        senha =int(input("Escolha uma senha: "))
        print(nome)
        print(cpf)
        print(conta)
        print(valor)
        print(senha)
        # Condição que incluí as informações no arquivo
        while nome != "":
            arquivo = open("arquivo.txt", "a")
            arquivo.write("%s %s %s %s %s\n" % (nome, cpf, conta, valor, senha))
            arquivo.close()
            break

#Função para apagar clientes do arquivo
def apaga():
       cpf_apaga = input("Digite seu cpf: ")
       clientes = []
       with open("arquivo.txt", "r+") as f:
           clientes_arquivo = f.readlines()
           for cliente in clientes_arquivo:
               x = cliente.split()
               if x[1] != cpf_apaga:
                   clientes.append(cliente)
                   print("Cliente Apagado!")
       f.close()
       with open("arquivo.txt", "w") as f:
           for c in clientes:
                f.write(c)
       f.close()                   
       



#Função para retirar valores da conta
def debito():
    cpf_debito = int(input("Digite seu cpf: "))
    senha_debito = int(input("Digite sua senha: "))
    valor_debito = int(input("Escolha o valor que deseja debitar: "))
    clientes = []
    with open("arquivo.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf_debito:
                x[3] = int(x[3]) - valor_debito
            cliente = ("%s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4]))    
            clientes.append(cliente)
    with open("arquivo.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close()       
    
    

          

#Função para colocar valores na conta
def deposito():
    cpf_deposito = int(input("Digite seu cpf: "))
    valor_deposito = int(input("Escolha o valor que deseja depositar: "))
    clientes = []
    with open("arquivo.txt", "r+") as f:
        clientes_arquivo = f.readlines()
        for cliente in clientes_arquivo:
            x = cliente.split()
            if int(x[1]) == cpf_deposito:
                x[3] = int(x[3]) + valor_deposito
            cliente = ("%s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4]))    
            clientes.append(cliente)
    with open("arquivo.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close()       

#Função que imprime o extrato do cliente
def extrato():
    cpf_extrato = int(input("Digite seu cpf: "))
    senha_extrato = int(input("Digite sua senha: "))

#Funçao que permite transferir dinheiro entre contas
def transferencia():
    cpf_trans = int(input("Digite seu cpf: "))
    senha_trans = int(input("Digite sua senha: "))
    cpf_destino = int(input("Digite o cpf do destinatário: "))
    valor_trans = int(input("Digite o valor para a transferência: "))
    clientes = []
    with open("arquivo.txt", "r") as f:
        clientes_arquivo = f.readlines()
    for cliente in clientes_arquivo:
        x = cliente.split()
        if int(x[1]) == cpf_trans:
            x[3] = int(x[3]) - valor_trans
            cliente = ("%s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4]))
        clientes.append(cliente)        
        if int(x[1]) == cpf_destino:
            x[3] = int(x[3]) + valor_trans
            cliente = ("%s %s %s %s %s\n" % (x[0], x[1], x[2], x[3], x[4]))    
        clientes.append(cliente)
    with open("arquivo.txt","w") as f:
        for cliente in clientes:
            f.write(cliente)
    f.close()       

#Função para mudar o dinheiro para a poupança
def poupança():
    cpf_pou = int(input("Digite seu cpf: "))
    senha_pou = int(input("Digite sua senha: "))
    valor_pou = int(input("Escolha o valor para transferir a poupança: "))

#Condição que permite as funções rodarem e retorna o menu após uso
while True:
    menu()
    x = escolha_menu()   
    if x == 1:
        novo_cliente()
    elif x == 2:  
        apaga()
    elif x == 3:
        debito()
    elif x == 4:
        deposito()
    elif x == 5:
        extrato()
    elif x == 6:
        transferencia()
    elif x == 7:
        poupança()
    elif x == 0:
        break
    else:
        print("Opção Inválida")        





        
