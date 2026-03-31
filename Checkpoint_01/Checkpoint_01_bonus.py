
from random import randint

secreto = randint(1, 100)
tentativas = 0
print("Tente adivinhar o número de 1 a 100")
while True:

    if tentativas >= 7:
        print("GAME OVER!!!")
        print(f"Número secreto era {secreto}")
        break
    else:
        userNUmber = int(input("Qual seu palpite? "))
        if userNUmber == secreto:
            print(f"Você acertou em {tentativas} tentativas!!!")
            break
        elif userNUmber > secreto:
            print("Vish o número é um pouco maior...")
            tentativas += 1
            print(f"Tentativas {tentativas}")
        elif userNUmber < secreto:
            print("Vish o número é um pouco maior...")
            tentativas += 1
            print(f"Tentativas {tentativas}")