class Colecao:
    """ Representa uma coleção do usuário

    Podem existir várias coleções

    Atributos:
        nome_colecao (str): Nome da coleção
        jogos: (list[Jogo]): Lista com todos os jogos da coleção

    """
    def __init__(self, nome_colecao: str, jogos: list):
        self.__nome_colecao = nome_colecao
        self.__jogos = jogos

    def __str__(self):
        return f"Nome da coleção: {self.__nome_colecao}\nJogos:{self.__jogos}"

    def __eq__(self, outra_colecao: object):
        if not isinstance(outra_colecao, Colecao):
            return False

        return (self.__nome_colecao.lower() == outra_colecao.__nome_colecao.lower() and self.__jogos == outra_colecao.__jogos)

    @property
    def nome_colecao(self):
        return self.__nome_colecao

    @nome_colecao.setter
    def nome_colecao(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome_colecao = novo_nome
        else:
            print("Nome inválido")

    @property
    def jogos(self):
        return self.__jogos

    @jogos.setter
    def jogos(self, novos_jogos):
        if isinstance (novos_jogos, list):
            self.__jogos = novos_jogos
        else:
            print("Lista de jogos inválida")