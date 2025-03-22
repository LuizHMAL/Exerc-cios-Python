class Jogador:
    def __init__(self, nome, gols=0):
        self.__nome = nome
        self.__gols = gols

    @property
    def nome(self):
        return self.nome
    
    @property
    def gols(self):
        return self.gols
    
    @nome.setter
    def nome(self, nome):
        self.__nome  = nome 

    @gols.setter
    def gols(self, gols):
        self.__gols = gols

    def exibir_ficha(self):
        if self.__nome  == '':
            self.__nome = "<desconhecido>"
            
        print (f"O jogador {self.__nome} fez {self.__gols} gols no campeonato.")


nome = str(input("Nome do jogador: "))
gols = (input("Número de gols: "))
print (gols.isnumeric())
while gols.isnumeric() ==  False:
    gols = (input("Número inválido, digite novamente o número de gols: "))

jogador = Jogador(nome, gols)

jogador.exibir_ficha()


# if gols.isnumeric():
#     gols = int(gols)

# else:
#     g = 0

# if nome.strip() == "":
#     ficha(gol = gols)
# else: ficha(nome, gols)