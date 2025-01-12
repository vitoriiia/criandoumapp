
import os 


restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa(): 

       print ("""
       ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
       ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
       ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
       ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
       ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
       ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
              \n""") 

# \n serve para pular linha em python 

def exibir_opcoes():

       print ('1. Cadastrar restaurante')
       print ('2. Listar restaurante')
       print ('3. Ativar restaurante')
       print ('4. Sair \n')

def finalizar_app():
       os.system('cls') 
       print('Finalizando o app\n')


def opcao_invalida():
    print('Opção Inválida!\n')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input ('Digite uma tecla para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes\n') 

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('Digite uma tecla para voltar ao menu principal')
    main()
     
def escolher_opcoes():

       try:
              opcao_escolhida = int(input('Escolha uma opção: '))

              if opcao_escolhida == 1:
                     cadastrar_novo_restaurante()


              elif opcao_escolhida == 2:
                     listar_restaurantes()

              elif opcao_escolhida == 3:
                     print('Ativar restaurante')

              elif opcao_escolhida == 4:
                     finalizar_app()

              else:
                     opcao_invalida()  
       except:
              opcao_invalida()


#  == é usado para definir igual, é usado dois porque é diferente de atribuir

def main():
       os.system('cls') # usado para limpar os dados
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcoes()



if __name__=='__main__':
       main()
