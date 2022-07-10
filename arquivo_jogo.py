import random

print('*************************')
print('jogo do número da sorte!')
print('*************************')
numero_chute = random.randrange(1, 101)
tentativas_números = 0
pontos = 1000
print('escolha o nível do jogo!')
print('(1)fácil (2)médio (3)difícil')
nnivel_digitado = int(input('Digite o nível do jodo:'))
if nnivel_digitado == 1:
    tentativas_números = 20
elif nnivel_digitado == 2:
    tentativas_números = 10
else:
    tentativas_números = 5
for rodada in range(1, tentativas_números + 1):
    print(f'tentativa {rodada} de {tentativas_números}')
    digita_chute = int(input('digite o número da sorte:'))
    if digita_chute < 1 or digita_chute > 100:
        print('O número digitado tem de está entre 1 e 100!')
        continue
    acertou = digita_chute == tentativas_números
    menor = tentativas_números < digita_chute
    maior = tentativas_números > digita_chute
    if acertou:
        print(f'você acertou o número, e sua quantidade de pontos é {pontos}')
        break
    else:
        pontos_perdidos = abs(numero_chute - digita_chute)
        pontos = pontos - pontos_perdidos
        if menor:
            print('Você errou, o número digitado é menor!')
            if rodada == tentativas_números:
                print(
                    f'O número secreto era {numero_chute} você fez {pontos} pontos'
                )
        elif maior:
            print('Você errou, o número digitado é maior!')
            if rodada == tentativas_números:
                print(
                    f'O numero secreto é {numero_chute} você fez {pontos} pontos'
                )
print('fim do jogo!')
