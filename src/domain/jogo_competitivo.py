from .jogo import Jogo
from datetime import date
from typing import Optional

tipo = "Competitivo"

class JogoCompetitivo(Jogo):
    """ Representa um jogo competitivo

    Herda de Jogo

    Atributos:
        partidas_jogadas (int): Total de partidas jogadas
        vitorias (int): Total de vitórias
        derrotas (int): Total de derrotas
        ranking (int): Classificação do usuário em relação a outros jogadores
        winrate (float): Taxa de vitória (vitorias / partidas_jogadas)
    """
    def __init__(self, titulo: str, genero: str, plataforma: str, ano_lancamento: int, horas_jogadas: float = 0, status: str = "Não iniciado", nota: Optional[float] = None, data_inicio: Optional[date] = None, data_termino: Optional[date] = None, partidas_jogadas: int = 0, vitorias: int = 0, derrotas: int = 0, ranking: int = None):
        super().__init__(titulo, genero, plataforma, ano_lancamento, horas_jogadas, status, nota, data_inicio, data_termino)
        self.__partidas_jogadas = partidas_jogadas
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__ranking = ranking
        if self.__partidas_jogadas != 0:
            self.__winrate = self.__vitorias / self.__partidas_jogadas * 100
        else:
            self.__winrate = 0

    def __str__(self):
        info_jogo = super().__str__()
        if self.__ranking == None:
            ranking_str = "Sem rank"
        else:
            ranking_str = self.__ranking

        info_competitivo = f"\nTotal de partidas: {self.__partidas_jogadas}, Vitórias: {self.__vitorias}, Derrotas: {self.__derrotas}\nRanking: {ranking_str}, Taxa de vitória (winrate): {self.__winrate:.2f}%"

        return info_jogo + info_competitivo

    def __repr__(self):
        info_jogo = super().__repr__()
        info_competitivo = f"\nTotal de partidas: {self.__partidas_jogadas}, Vitórias: {self.__vitorias}, Derrotas: {self.__derrotas}\nRanking: {self.__ranking}, Taxa de vitória (winrate): {self.__winrate:.2f}%"
        
        return info_jogo + info_competitivo

    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas

    @partidas_jogadas.setter
    def partidas_jogadas(self, novas_partidas_jogadas):
        if isinstance(novas_partidas_jogadas, int) and novas_partidas_jogadas >= 0:
            self.__partidas_jogadas = novas_partidas_jogadas
            
        elif isinstance(novas_partidas_jogadas, str) and novas_partidas_jogadas.isdigit() and int(novas_partidas_jogadas) >= 0:
            self.__partidas_jogadas = int(novas_partidas_jogadas)
            
        else:
            print("Tipo inserido de novas partidas jogadas é inválido")  

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, novas_vitorias):
        if isinstance(novas_vitorias, int) and novas_vitorias >= 0:
            self.__vitorias = novas_vitorias
            
        elif isinstance(novas_vitorias, str) and novas_vitorias.isdigit() and int(novas_vitorias) >= 0:
            self.__vitorias = int(novas_vitorias)
            
        else:
            print("Tipo inserido de vitórias é inválido")

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, novas_derrotas):
        if isinstance(novas_derrotas, int) and novas_derrotas >= 0:
            self.__derrotas = int(novas_derrotas)

        elif isinstance(novas_derrotas, str) and novas_derrotas.isdigit() and int(novas_derrotas) >= 0:
            self.__derrotas = int(novas_derrotas)

        else:
            print("Tipo inserido de derrotas é inválido")

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, novo_ranking):
        if isinstance(novo_ranking, int) and novo_ranking >= 0:
            self.__ranking = int(novo_ranking)

        elif isinstance(novo_ranking, str) and novo_ranking.isdigit() and int(novo_ranking) >= 0:
            self.__ranking = int(novo_ranking)

        else:
            print("Tipo inserido de ranking é inválido")