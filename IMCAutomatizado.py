# Desenvolvido por Maria Eduarda Neves 
# Desenvolvido por Ricardo Teixeira

import os, math
import mysql.connector 

con = mysql.connector.connect(host='localhost', database='db_imc', user='aluno', password='sptech')

if con.is_connected():
        db_imc = con.get_server_info()
        print("conectado ao servidor MySQL")

def menu():
 menu()

os.system('cls')
print('''
  ____                         _           _       
 |  _ \                       (_)         | |      
 | |_) | ___ _ __ ___   __   ___ _ __   __| | ___  
 |  _ < / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \ 
 | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) |
 |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/
   _____      _            _           _                  
  / ____|    | |          | |         | |                 
 | |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _  
 | |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | 
 | |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | 
  \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_| 
  _____ ______  _____
 |_   _|  \/  |/ ____|                                   
   | | | \  / | |                                         
   | | | |\/| | |                                         
  _| |_| |  | | |____                                     
 |_____|_|  |_|\_____|                                    
                                                          
                            
 ''')

nome = input('Para iniciar por favor insira seu nome:')

os.system('cls')

while True:

        print ('Bem Vindo a Calculadora', nome)

        print('''
                        MENU:

                        [C] - Calcular IMC
                        [H] - Ver Historico
                        [S] - Sair
        ''')

                        
                        
        opcao = input('Escolha uma opção para utilizar:')

        imc = 0
        peso = 0
        altura = 0


        if(opcao == 'c' or opcao == 'C'):

                cursor = con.cursor()
                os.system('cls')
                peso = float(input('Quanto você pesa em kg?(kg)'))
                altura = float(input('Quanto você mede em altura?(m)'))



                if(peso == 0 or altura == 0):
                        print('Insira um valor válido')

                else:

                        os.system('cls')
                        imc = peso/(altura**2)
                        print('|------------------------------------| \n ')
                        print(' Com o peso de {:.2f}               '.format(peso))
                        print(' E altura de {:.2f}\n                '.format(altura))
                        print(' O seu IMC é: {:.2f}\n              '.format(imc))
                        

                        if imc < 18.5:

                                print(' Diagnóstico: Abaixo do peso normal')


                        elif 18.5 <= imc <25:
                                
                                print(' Diagnóstico: Peso normal')

                        elif 25 <= imc <30:

                                print(' Diagnóstico: Sobrepeso')

                        elif 30 <= imc <40:

                                print(' Diagnóstico: Obeso')

                        elif imc >=40:

                                print(' Diagnóstico: Obesidade Mórbida')

                        print(' Dados registrados com sucesso.')
                        print('|------------------------------------|')

                       # arquivo = open("historico.txt", "a")

                        # historico = [nome,"\n", str(peso),"\n",str(altura),"\n", str(round(imc,2)),"\n","\n","\n"]

                        # arquivo.writelines(historico)

                        cursor.execute("INSERT INTO usuario (nomeUsuario, alturaUsuario, pesoUsuario, imcUsuario) VALUES ('{}','{}','{:.2f}', '{:.2f}');".format(nome,peso,altura,imc))
                        con.commit()
                        con.close()
                        print('''
                        Digite "Sim" para voltar para o menu:

                        ''')

                        opcao = input('Continuar para menu:')
                        os.system('cls')

                       
                

        if(opcao == 'h' or opcao =='H'):
                cursor = con.cursor()
                os.system('cls')

                
                cursor.execute("SELECT * FROM usuario")
                

                resultado = cursor.fetchall()

                # Mostra o resultado:
                print('Usuários cadastrados:')

                for linha in resultado :
                        print(linha, "\n")

                print('''
                        Digite "Sim" para continuar para o menu:

                        ''')

                opcao = input('Continuar para Menu:')
                os.system('cls')

        
        elif(opcao == 's' or opcao == 'S'):
                os.system('cls')
                
                # Finaliza a conexão
                con.close()
                print('Obrigada por utilizar nosso programa!')
                break


                