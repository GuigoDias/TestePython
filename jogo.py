import random;

print("*********************************");
print("Bem vindo ao teste de adivinhação");
print("*********************************");

numeroSecreto = random.randrange(1,101);
totalDeTentativas = 0;
pontos = 1000;

print(3//2);
print("(1) Fácil (2) Médio (3) Difícil");
nivel = int(input("Defina o nível: "));
if (nivel == 1):
    totalDeTentativas = 20;
elif (nivel == 2):
    totalDeTentativas = 10;
else:
    totalDeTentativas = 5;

for tentativaAtual in range(1 , totalDeTentativas + 1):
    print("Tentativa {} de {}".format(str(tentativaAtual), str(totalDeTentativas)))
    chute = input("Digite um número entre 1 a 100:\n");
    print("Você chutou: " + chute);
    numeroChute = int(chute);

    if(numeroChute < 1 or numeroChute > 100):
        print("Número inválido, por favor informe um número entre 1 a 100\n");
        continue;

    acertou = numeroSecreto == numeroChute;
    maior = numeroChute > numeroSecreto;
    menor = numeroChute < numeroSecreto;

    if(acertou):
        print("Você Acertou e fez {} pontos!".format(pontos));
        break;
    else:
        if(maior):
            print("VOCÊ ERROU! seu número é maior que o que o número secreto!");
        elif(menor):
            print("VOCÊ ERROU! seu número é menor que o que o número secreto!");
        pontosPerdidos = abs(numeroSecreto - numeroChute);
        pontos = abs(pontos - pontosPerdidos);
        if(tentativaAtual == totalDeTentativas):
            print("O número secreto era {} e você fez {} pontos.".format(numeroSecreto,pontos));

print("FIM DE JOGO!");