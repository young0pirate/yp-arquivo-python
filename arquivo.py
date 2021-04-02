arq = open("fa.txt","a")
arqb = open("fa.txt","r")
print("1 - Escrever\n2 - Abrir:\n")
es = int(input("O que quer fazer?\nAbrir ou escrever:\n>>>>> "))
print("===================")

if es == 1:
    nome = input('Digite seu nome: ')
    idade = int(input('Sua idade: '))
    arq.write("\nSeu nome é: "+nome)
    arq.write("\nSua idade é: {}".format(idade))
arq.close()
if es == 2:
    print("Os seus dados:\n",arqb.read())
    arqb.close()