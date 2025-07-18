import random
# Precisa ter dois espaços em branco entre os import.
# É o inicio da função, fora os comentários.
# As linhas do código podem ter apenas 79 caracteres.


def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_aleatorio = random.randint(1, 100)
    max_tentativas = 10
    
    
    print("Bem-vindo ao Jogo de Adivinhação")
    print("Tente adivinhar o número entre 1 e 100.")
    
    for tentativa in range(max_tentativas):
        palpite = int(input("Digite sua tentativa: "))
        
        if palpite < numero_aleatorio:
            print("Muito baixo, tente um número maior.")
        elif palpite > numero_aleatorio:
            print("Muito alto, tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em "f"{tentativa + 1} tentativas!")
            return
        
    print(f"Suas {max_tentativas} tentativas acabaram.")
    f" O numero correto era {numero_aleatorio}."
    
    
if __name__ == "__main__":
    jogo_adivinhacao()
