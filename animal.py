from random import *
# o progra continua em excecução enquanto a variável for verdadeira 'True'

executa = True
adjetivos = [ "maravilhoso", "acima da média"," excelente"]
hobbies = [ "andar de bicicleta", "programar", "fazer chá"]

print("Serviço de escolha de nome para animais de estimação")
print("-----------------------")
cont = 0
femea = []
quantidade = []
macho = []

sexo = input('''Qual sexo do seu animalzinho?
Digite femea ou macho:''').upper()
n = int(input("Quantos animais você tem?:"))
for c in range(1, n +1):
    femea = []
    quantidade = []
    macho = []
  

if sexo == 'FEMEA':
    for i in range(n):
        femea.append(input("Digite  nome de seu animalzinho: "))
        cont+=1
    print(cont)
    print(femea)

if sexo == 'MACHO':
    for i in range(n):
        macho.append(input("digite o nome do seu animalzinho: "))
        cont+=1
    print(cont)
    print(macho)

    
    
