class Aluno():
    def __init__(self, nome, matricula, notas):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = notas
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def notas(self):
        return self.__notas
    
    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    def calcular_media(self):
        return sum(self.__notas) / len(self.__notas)
    
    def aprovado(self, media_minima):
        return self.calcular_media() >= media_minima

class Curso():
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def alunos(self):
        return self.__alunos
    
    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)
    
    def calcular_media_geral(self):
        total_notas = 0
        total_alunos = len(self.__alunos)
        for aluno in self.__alunos:
            total_notas += aluno.calcular_media()
        return total_notas / total_alunos if total_alunos > 0 else 0
    
    def listar_aprovados(self, media_minima):
        aprovados = []
        for aluno in self.__alunos:
            if aluno.aprovado(media_minima):
                aprovados.append(aluno)
        return aprovados

aluno1 = Aluno("Marcos", 12345, [7, 8, 9])
aluno2 = Aluno("João", 67890, [5, 6, 7])
aluno3 = Aluno("Ana", 11223, [9, 10, 8])

curso = Curso("Matemática")

curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)
curso.adicionar_aluno(aluno3)

print(f"Média Geral do Curso: {curso.calcular_media_geral()}")

aprovados = curso.listar_aprovados(7)
print("\nAlunos Aprovados:")
for aluno in aprovados:
    print(f"{aluno.nome} - Matrícula: {aluno.matricula}")