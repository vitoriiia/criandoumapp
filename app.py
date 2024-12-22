
import os 

print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
       \n""") 

# \n serve para pular linha em python 

print ('1. Cadastrar restaurante')
print ('2. Listar restaurante')
print ('3. Ativar restaurante')
print ('4. Sair \n')

opcao_escolhida = int (input('Escolha uma opção: '))

def finalizar_app():
       os.system('cls') 
       print('Finalizando o app\n')
     





if opcao_escolhida == 1:
       print('Cadastrar restaurante')

elif opcao_escolhida == 2:
       print('Listar restaurantes')

elif opcao_escolhida == 3:
       print('Ativar restaurante')

else:
       finalizar_app()

#  == é usado para definir igual, é usado dois porque é diferente de atribuir