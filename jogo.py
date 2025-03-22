import random

class JogoAdivinhacao():
    def __init__(self):
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0
    
    @property
    def numero_secreto(self):
        return self.__numero_secreto
    
    @property
    def tentativas(self):
        return self.__tentativas
    
    def fazer_tentativa(self, tentativa) -> str:
        self.__tentativas += 1
        if tentativa < self.__numero_secreto:
            return "O número secreto é maior."
        elif tentativa > self.__numero_secreto:
            return "O número secreto é menor."
        else:
            return f"Parabéns! Você acertou o número em {self.__tentativas} tentativas!"
    
    def reiniciar_jogo(self):
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0

# Exemplo de uso do JogoAdivinhacao

if __name__ == "__main__":
    jogo = JogoAdivinhacao()
    acertou = False

    while not acertou:
        tentativa = int(input("Digite um número entre 1 e 100: "))
        resultado = jogo.fazer_tentativa(tentativa)
        print(resultado)
        if tentativa == jogo.numero_secreto:
            acertou = True