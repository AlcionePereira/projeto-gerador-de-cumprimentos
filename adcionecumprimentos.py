from random import *

print("Gerador de cumprimentos")
print("-----"*5)

adjetivos = [" maravilhoso", "acima da média", "excelentes"]
hobbies = ["andar de bicieta", "programar", "fazer chá"]
favorita = ["é show!!!", " é linda!", " marcou a minha vida."]

nome = input("Qual é seu nome?: ")
musicafavorita = input("Qual sua música favórita?:")

# obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, "Você é", choice(adjetivos), "em", choice(hobbies),"sua música ", musicafavorita, choice(favorita))
print("De nada!")
  
