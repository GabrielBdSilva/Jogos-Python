import random
def jogar():
    print("*********************************")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) fácil (2) médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite o seu numero entre 1 e 100: ")
        chute = int(chute) #sem essa linha diria que errou pq o valor do chute seria uma string!
        print("Voce digitou", chute)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue #sai de todo o bloco q ta identado no if e pula tudo e repete o laço

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos")
            break #para a execução e já sai do laço
        else:
            if(maior):
                print("Você errou! o seu chute foi maior do que o número secreto")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. você fez {}".format(numero_secreto,pontos))
            elif(menor):
                print("Você errou! o seu chute foi Menor do que o número secreto")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. você fez{}".format(numero_secreto,pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1
    print("Fim do jogo")

if(__name__)=="__main__":#variavel name possui o valor main, quando é executado o arquivo direto
    jogar() #quando ta assim ele não executa a função quando é importada

