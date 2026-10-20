from .jogo import Jogo
from datetime import date
from typing import Optional

class JogoCampanha(Jogo):
    """ Representa um jogo modo campanha (ou modo história)

    Herda de Jogo

    Atributos:
        missoes_totais (int): Total de missões que o jogo possui
        missoes_concluidas (int): Total de missões que o usuário concluiu
        percentual_conclusao (float): Percentual com base no total de missões e no número de missões concluidas (missoes_concluidas / missoes_totais)

    """

    tipo = "Campanha"

    def __init__(self, titulo: str, genero: str, plataforma: str, ano_lancamento: int, missoes_totais: int, missoes_concluidas: int = 0, horas_jogadas: float = 0, status: str = "Não iniciado", nota: Optional[float] = None, data_inicio: Optional[date] = None, data_termino: Optional[date] = None):
        super().__init__(titulo, genero, plataforma, ano_lancamento, horas_jogadas, status, nota, data_inicio, data_termino)
        self.__missoes_totais = missoes_totais
        self.__missoes_concluidas = missoes_concluidas
        if missoes_totais != 0:
            self.__percentual_conclusao = missoes_concluidas / missoes_totais * 100
        else:
            self.__percentual_conclusao = None 

    def __str__(self):
        info_jogo = super().__str__()

        info_conclusao = f"\nMissões Totais: {self.__missoes_totais}, Missões Concluidas: {self.__missoes_concluidas}, Percentual de Conclusão: {self.__percentual_conclusao:.2f}%" 

        return info_jogo + info_conclusao

    def __repr__(self):
        info_jogo = super().__repr__()
        info_campanha = f"\nMissões Totais: {self.__missoes_totais}, Missões Concluidas: {self.__missoes_concluidas}, Percentual de Conclusão: {self.__percentual_conclusao:.2f}%"

        return info_jogo + info_campanha

    @property
    def missoes_totais(self):
        return self.__missoes_totais

    @missoes_totais.setter
    def missoes_totais(self, novas_missoes_totais):
            self.__missoes_totais = novas_missoes_totais

    @property
    def missoes_concluidas(self):
        return self.__missoes_concluidas

    @missoes_concluidas.setter
    def missoes_concluidas(self, novas_missoes_concluidas):
        self.__missoes_concluidas = novas_missoes_concluidas

    def to_dict(self):
        dados = super().to_dict()
        dados["missoes_totais"] = self.__missoes_totais
        dados["missoes_concluidas"] = self.__missoes_concluidas
        return dados
    
    @classmethod
    def from_dict(cls, dados):
        data_inicio = date.fromisoformat(dados["data_inicio"])
        if dados["data_termino"] == None:
            data_termino = dados["data_termino"]
        else:
            data_termino = date.fromisoformat(dados["data_termino"])
        return cls(
            titulo=dados["titulo"],
            genero=dados["genero"],
            plataforma=dados["plataforma"],
            status=dados["status"],
            nota=dados["nota"],
            horas_jogadas=dados["horas_jogadas"],
            data_inicio=data_inicio,
            data_termino=data_termino,
            ano_lancamento=dados["ano_lancamento"],
            missoes_totais=dados["missoes_totais"],
            missoes_concluidas=dados["missoes_concluidas"]
        )
