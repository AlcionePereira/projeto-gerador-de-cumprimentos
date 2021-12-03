from random import *
# o progra continua em excecução enquanto a variável for verdadeira 'True'

executa = True
adjetivos = [ "maravilhoso", "acima da média"," excelente"]
hobbies = [ "andar de bicicleta", "programar", "fazer chá"]

print("Gerador de cumprimentos")
print("-----------------------")

nome = input('Qual é o eu nome?: ')

print('''
Menu
c = obter cumprimento
a = adicionar hobby
d = remover hobby
p = imprimir hobbies
q = sair
''')


while executa == True:
    menuChoice = input("\n>_").lower()

    #'C' para um cumprimento
    if menuChoice == 'c':

        print("Aqui está o seu cumprimento", nome , ":")
        # obtem um item aleatório de ambas as listas e adiciona-os ao cumprimento
        print(nome, "você é" , choice(adjetivos), "em" , choice(hobbies))
        print("De nada!")

     #'a' para addiconar hobby
    elif menuChoice == 'a':

        itemToAdd = input("Adicione o hobby: ")
        if itemToAdd not in hobbies:
            hobbies.append(itemToAdd)
        elif itemToAdd in hobbies:
            print("Esse item já tem na lista.")
    

        #'d' para remover um hobby
    elif menuChoice == 'd':

        itemToDelete = input("Insira o hobby a ser removido: ")
        #só remove um itme se ele estiver na lita
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
            print("Item removido!")
        else:
            print("O item não está na lista.")

    
        #'p' para imprimir a lista de hobbies
    elif menuChoice == 'p':
        print(hobbies)

    #'q' para sair
    elif menuChoice == 'q':
        executa = False
    else:
        print("Insira uma opção válida!")


