import mysql.connector
from mysql.connector import Error
import os  
import getpass 
import psutil


conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='@Pedrinho1')

if conexao.is_connected():
        hcs = conexao.get_server_info()
        print("conectado ao servidor MySQL")

def menu():
 menu()
 os.system('cls')
print('''
/***
 *     __    __       ___      .______       _______  ____    __    ____      ___      .______       _______ 
 *    |  |  |  |     /   \     |   _  \     |       \ \   \  /  \  /   /     /   \     |   _  \     |   ____|
 *    |  |__|  |    /  ^  \    |  |_)  |    |  .--.  | \   \/    \/   /     /  ^  \    |  |_)  |    |  |__   
 *    |   __   |   /  /_\  \   |      /     |  |  |  |  \            /     /  /_\  \   |      /     |   __|  
 *    |  |  |  |  /  _____  \  |  |\  \----.|  '--'  |   \    /\    /     /  _____  \  |  |\  \----.|  |____ 
 *    |__|  |__| /__/     \__\ | _| `._____||_______/     \__/  \__/     /__/     \__\ | _| `._____||_______|
 *                                                                                                           
 *      ______   ______   .__   __. .___________..______        ______    __       __                        
 *     /      | /  __  \  |  \ |  | |           ||   _  \      /  __  \  |  |     |  |                       
 *    |  ,----'|  |  |  | |   \|  | `---|  |----`|  |_)  |    |  |  |  | |  |     |  |                       
 *    |  |     |  |  |  | |  . `  |     |  |     |      /     |  |  |  | |  |     |  |                       
 *    |  `----.|  `--'  | |  |\   |     |  |     |  |\  \----.|  `--'  | |  `----.|  `----.                  
 *     \______| \______/  |__| \__|     |__|     | _| `._____| \______/  |_______||_______|                  
 *                                                                                                           
 *         _______.____    ____      _______..___________. _______ .___  ___.                                
 *        /       |\   \  /   /     /       ||           ||   ____||   \/   |                                
 *       |   (----` \   \/   /     |   (----``---|  |----`|  |__   |  \  /  |                                
 *        \   \      \_    _/       \   \        |  |     |   __|  |  |\/|  |                                
 *    .----)   |       |  |     .----)   |       |  |     |  |____ |  |  |  |                                
 *    |_______/        |__|     |_______/        |__|     |_______||__|  |__|                                
 *                                                                                                           
 */
''')

nome = input('Para iniciar por favor insira seu nome:')

while (nome == ''): 
     print('Insira um nome v??lido.')
     break   



else:
    os.system('cls')

    while True:
        print('Ol??! ', nome,'. Seja bem vindo ao nosso sistema de controle de hardware.')
        print('''
                    
                    
                            [CE] -  Cadastrar Empresa
                            [CM] -  Cadastrar Carro
                            [CC]  - Cadastrar Cliente
                            [LE] - Login Empresa
                            [LC]  - Login Cliente
                            [CD] - Consultar dados 
                            [S]  -  Sair
        ''')
                
        opcao = input('Escolha uma op????o:')

        if(opcao == 'CE' or opcao == 'ce'):
                
                    # conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='sptech')
                
                    cursor = conexao.cursor()
                    
                    nomeEmpresa = input('Qual o nome da empresa?')
                    cnpj = input('Qual o CNPJ?')
                    nomeRepresentante = input('Qual o do representante?')
                    senha = getpass.getpass(prompt='Escolha uma senha:', stream=None);

                    cursor.execute("INSERT INTO Empresa (nomeEmpresa, cnpj, nomeRepresentante, senha) VALUES('{}','{}','{}','{}');".format(nomeEmpresa,cnpj,nomeRepresentante,senha))
                
                    conexao.commit()
                    print('Empresa cadastrada com sucesso!')

        if(opcao == 'CM' or opcao == 'cm'):

                    # conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='sptech')

                    cursor = conexao.cursor()

                    placa = input('Qual a placa?')
                    dataFabricacao = input('Qual a data de fabrica????o?')
                    placaMae = input('Qual o modelo da placa m??e?')
                    placaVideo = input('Qual o modelo da placa de video?')
                    processador = input('Qual o modelo do processador?')
                    voltagem = input('Qual a voltagem do carregador?')
                    fkCliente = input('Qual o c??digo do propriet??rio?')
                    fkEmpresa = input('Qual o c??digo da marca?')

                    cursor.execute("INSERT INTO Carro (placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa) VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa))
                    print('Carro cadastrado com sucesso!')
        if(opcao == 'CC' or opcao == 'cc'):

                    cursor = conexao.cursor()

                    nome = input('Insira o nome do cliente:')
                    senha = getpass.getpass(prompt='Escolha uma senha para o cliente:', stream=None)

                    cursor.execute("INSERT INTO Cliente (nome, senha) VALUES('{}','{}')".format(nome, senha))
                    print('Cliente cadastrada com sucesso!')
        if (opcao == 'LE' or opcao == 'le'):

            cnpj = input('Informe o c??digo de sua empresa:')
            senha = input('Informe sua senha:')
            query = ("SELECT * FROM Empresa")
            cursor = conexao.cursor()
            cursor.execute(query)
            dados = cursor.fetchall()
            
            
            for dado in dados:
                        if(cnpj != dado[2] or senha !=dado[4]):
                            print('C??digo incorreto')
                        else:
                            query2 = ("SELECT modelo, placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa FROM Carro;")
                            cursor = conexao.cursor()
                            cursor.execute(query2)
                            dadosC = cursor.fetchall()

                            print('Ol?? ', dado[1], '!')
                            print('Listando dados de todos os autom??veis dispon??veis:')
                            
                        for dadosCarro in dadosC:
                            print('|Modelo: ',dadosCarro[1])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa:',dadosCarro[2])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Data de fabrica????o:',dadosCarro[3])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa M??e:',dadosCarro[4])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa de V??deo:',dadosCarro[5])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Processador/CPU: ',dadosCarro[6], end="")
                            print(psutil.cpu_percent(interval=None))
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print ('|Carga m??dia dos processos sendo executados: ', end="")
                            print(psutil.getloadavg())
                            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
                            print('|Uso da mem??ria do sistema:', end="")
                            print(psutil.virtual_memory())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Voltagem:', dadosCarro[7])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
                            print('|Id do propriet??rio:', dadosCarro[8])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Carga restante da bateria:', end="")
                            print(psutil.sensors_battery())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')




        if (opcao == 'LC' or opcao == 'lc'):

            login = input('Informe o seu c??digo:')
            senha = getpass.getpass(prompt='Insira sua senha:', stream=None)
            query = ("SELECT * FROM Cliente;")
            cursor = conexao.cursor()
            cursor.execute(query)
            dados = cursor.fetchall()

            for dado in dados:
                    if(login != dado[0] or senha != dado[2]):
                        print('C??digo/senha incorreto!')
            else:
                        os.system('cls')
                        print('Ol?? ', dado[1], '!')
                        print('Listando dados de todos os autom??veis dispon??veis:')
                        query2 = ("SELECT * FROM Carro join Cliente where Carro.fkCliente = Cliente.idCliente;")
                        cursor = conexao.cursor()
                        cursor.execute(query2)
                        dadosC = cursor.fetchall()

                       
                        
                        for dadosCarro in dadosC:
                            print('|Modelo: ',dadosCarro[1])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa:',dadosCarro[2])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Data de fabrica????o:',dadosCarro[3])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa M??e:',dadosCarro[4])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa de V??deo:',dadosCarro[5])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Processador/CPU: ',dadosCarro[6], end="")
                            print(psutil.cpu_percent(interval=None))
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print ('|Carga m??dia dos processos sendo executados: ', end="")
                            print(psutil.getloadavg())
                            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
                            print('|Uso da mem??ria do sistema:', end="")
                            print(psutil.virtual_memory())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Voltagem:', dadosCarro[7])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
                            print('|Id do propriet??rio:', dadosCarro[8])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Carga restante da bateria:', end="")
                            print(psutil.sensors_battery())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')


        if(opcao == 'CD' or opcao == 'cd'):
            os.system('cls')

            print('''   
                     ___??????????????????????_____
                    |????????????????____????????????????|
                    |????????????????????????????????????????|
                    ??(@)(@)??????????????(@)(@)??
            ''')
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print('|Listando dados de seu autom??vel Tesla Model X:')
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print('|Processador/CPU: ', end="")
            print(psutil.cpu_percent(interval=None))
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print ('|Carga m??dia dos processos sendo executados: ', end="")
            print(psutil.getloadavg())
            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
            print('|Uso da mem??ria do sistema:', end="")
            print(psutil.virtual_memory())
            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
            print('|Carga restante da bateria:', end="")
            print(psutil.sensors_battery())
            print ('|------------------------------------------------------------------------------------------------------------------------------------')


        if(opcao == 's' or opcao == 'S'):
            os.system('cls')               
            conexao.close()
            print('Obrigada por utilizar nosso programa!')
        break

