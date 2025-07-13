class Contato():
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        list
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def email(self):
        return self.__email
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @email.setter
    def email(self, email):
        self.__email = email
    
class Agenda():
    def __init__(self):
        self.__contatos = []
    
    @property
    def contatos(self):
        return self.__contatos
    
    def inserir_contato(self, contato):
        self.__contatos.append(contato)
    
    def remover_contato(self, nome):
        for contato in self.__contatos:
            if contato.nome == nome:
                self.__contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso.")
                return
        print(f"Contato {nome} não encontrado.")
    
    def atualizar_contato(self, nome, novo_nome=None, novo_telefone=None, novo_email=None):
        for contato in self.__contatos:
            if contato.nome == nome:
                if novo_nome:
                    contato.nome = novo_nome
                if novo_telefone:
                    contato.telefone = novo_telefone
                if novo_email:
                    contato.email = novo_email
                print(f"Contato {nome} atualizado com sucesso.")
                return
        print(f"Contato {nome} não encontrado.")
    
    def pesquisar_contato(self, nome):
        for contato in self.__contatos:
            if contato.nome == nome:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}")
                return
        print(f"Contato {nome} não encontrado.")
    
    def listar_contatos(self):
        if not self.__contatos:
            print("Nenhum contato na agenda.")
            return
        for contato in sorted(self.__contatos, key=lambda c: c.nome):
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}")

agenda = Agenda()

contato1 = Contato("Marcos", "1234-5678", "marcos@email.com")
contato2 = Contato("João", "9876-5432", "joao@email.com")
agenda.inserir_contato(contato1)
agenda.inserir_contato(contato2)

print("Lista de Contatos:")
agenda.listar_contatos()

print("\nPesquisa de Contato:")
agenda.pesquisar_contato("João")

print("\nAtualizando Contato:")
agenda.atualizar_contato("João", novo_telefone="1111-2222", novo_email="novojoao@email.com")

print("\nRemovendo Contato:")
agenda.remover_contato("Marcos")

print("\nLista de Contatos Atualizada:")
agenda.listar_contatos()