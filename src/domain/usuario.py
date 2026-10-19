from .colecao import Colecao

class Usuario:
    """ Representa o usuário do sistema

    O usuário pode criar diversas coleções, adicionar jogos, fazer relatórios
    
    Atributos:
        nome (str): Nome de usuário
        colecoes (Dict[str, Colecao]): Dicionário com as coleções que o usuário criou. Ele pode criar várias coleções, da maneira que preferir.

    """
    def __init__(self, nome:str, colecoes:dict = None):
        self.__nome = nome
        self.__colecoes = colecoes

    def __eq__(self, outro_usuario):
        if not isinstance (outro_usuario, Usuario):
            return False

        return (self.__nome.lower() == outro_usuario.__nome.lower())

    def __str__(self):
        if self.__colecoes == None:
            colecoes_str = "Nenhuma coleção criada"
        else:
            colecoes_str = str(self.__colecoes)

        return f"Nome do usuário: {self.__nome}\nColeções: {colecoes_str}"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, outro_nome):
        if isinstance(outro_nome, str):
            self.__nome = outro_nome
        else:
            print("Nome inválido")

    @property
    def colecoes(self):
        return f"Coleções: {self.__colecoes}"

    @colecoes.setter
    def colecoes(self, outra_colecao: dict[str]): # Fiz somente a base do setter pois pra ele funcionar precisa se relacionar com outras classes
        self.__colecoes = outra_colecao

    def to_dict(self):
        return {
            "Usuario": self.__nome,
            "Colecoes": [c.to_dict() for c in self.__colecoes.values()],
        }

    @classmethod
    def from_dict(cls, dados):
        colecoes = {}
        for i in dados["Colecoes"]:
            colecao = Colecao.from_dict(i)
            colecoes[colecao.nome_colecao] = colecao
        return cls(
            nome=dados["Usuario"],
            colecoes= colecao
        )