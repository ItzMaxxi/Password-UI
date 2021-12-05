import time
import os
import sys


# Creator: ItzMaxxi // Senha é um teste!

senha = "1234" # ALTERE A SENHA!!!! (Não obrigatório mas recomendado)
usuario = "ItzMaxxi", "Admin" #Adiciona um, não vai mudar nada, só para lembrar

def menu(): # Menu onde pergunta o usúario
	os.system('cls')
	os.system(f'title Password UI')
	print("Hello World! Escreva o usúario")
	inputt = input('Usuário: ')
	if inputt == 'ItzMaxxi' or inputt == 'Admin':
		senha_locker()
	else:
		print('Try again! Please wait 5 seconds')
		time.sleep(5)
		menu()

def senha_locker(): # Menu 2 que pergunta a senha para redirecionar
	os.system('cls')
	print("Hello World! Por favor, digite a senha!")
	inputtt = input('Senha: ')
	if inputtt == '1234':
		admin_commands()
	else:
		print('Try again! Please wait 5 seconds')
		time.sleep(5)
		senha_locker()

def admin_commands(): # Menu de admin (pode ser acessado quando a senha e o usúario forem corretos; Bruteforce pode funcionar, mas vai demorar.)
	os.system('cls')
	print('''
Comandos:

(1) - Visualizar a senha


		''')
	inputtt4 = input('Senha: ')
	if inputtt4 == '1':
		print("A senha é 1234")
		time.sleep(2)
		admin_commands()
	else:
		print("Tente novamente mais tarde! ErRoR!")
		time.sleep(2)
		admin_commands()

menu()