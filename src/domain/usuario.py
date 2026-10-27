from datetime import date
from .colecao import Colecao
from .jogo import Jogo
from .excecoes import RegraDeNegocioError

class Usuario:
    """ Representa o usuário do sistema

    O usuário pode criar diversas coleções, adicionar jogos, fazer relatórios
    
    Atributos:
        nome (str): Nome de usuário
        colecoes (Dict[str, Colecao]): Dicionário com as coleções que o usuário criou. Ele pode criar várias coleções, da maneira que preferir.

    """
    def __init__(self, nome:str, colecoes:dict = None):
        self.__nome = nome
        if colecoes is not None:
            self.__colecoes = colecoes
        else:
            self.__colecoes = {}

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
        return self.__colecoes

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
            colecoes= colecoes
        )

    @property
    def jogos(self):
        #Todos os jogos de todas as coleções.
        todos = []
        for colecao in self.__colecoes.values():
            for jogo in colecao.jogos:
                todos.append(jogo)
        return todos

    def buscar_jogo(self, titulo, plataforma=None):
        achados = []
        for jogo in self.jogos:
            if jogo.titulo.lower() == titulo.lower():
                if plataforma == None or jogo.plataforma.lower() == plataforma.lower():
                    achados.append(jogo)

        if len(achados) == 0:
            raise RegraDeNegocioError(f"Jogo '{titulo}' não encontrado.")
        if len(achados) > 1:
            raise RegraDeNegocioError(f"{titulo} existe em mais de uma plataforma")
        return achados[0]

    def adicionar_jogo(self, nome_colecao, jogo):
        if nome_colecao not in self.__colecoes:
            raise RegraDeNegocioError(f"Coleção '{nome_colecao}' não existe.")
        if jogo in self.jogos:   # usa Jogo.__eq__ 
            raise RegraDeNegocioError(f"{jogo.titulo} já existe na plataforma {jogo.plataforma}.")
        self.__colecoes[nome_colecao].jogos.append(jogo)

    def iniciar_jogo(self, titulo, plataforma=None, limite=3):
        jogo = self.buscar_jogo(titulo, plataforma)
        if jogo.status == Jogo.jogando:
            raise RegraDeNegocioError(f"{jogo.titulo} já está com status Jogando.")

        jogando_agora = []
        for j in self.jogos:
            if j.status == Jogo.jogando:
                jogando_agora.append(j)

        if len(jogando_agora) >= limite:
            nomes = ""
            for j in jogando_agora:
                if nomes != "":
                    nomes += ", "
                nomes += j.titulo
            raise RegraDeNegocioError(f"Limite de {limite} jogos simultâneos atingido ({nomes}).")

        jogo.iniciar_jogo()
        return jogo

    def jogos_finalizados_no_ano(self, ano=None):
        if ano == None:
            ano = date.today().year

        finalizados = []
        for jogo in self.jogos:
            if jogo.status == Jogo.finalizado and jogo.data_termino != None:
                if jogo.data_termino.year == ano:
                    finalizados.append(jogo)
        return finalizados

    def aviso_meta_anual(self, meta):
        if meta == None:
            return None
        feitos = len(self.jogos_finalizados_no_ano())
        if feitos < meta:
            return f"AVISO: {feitos} de {meta} jogos finalizados em {date.today().year} (faltam {meta - feitos})."
        return None