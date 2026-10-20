from .jogo import Jogo
from datetime import date
from typing import Optional

class JogoCooperativo(Jogo):
    """ Representa um jogo cooperativo

    Herda de Jogo

    Atributos:
        jogadores_max (int): Número de jogadores máximos de um jogo cooperativo
        num_sessoes (int): Número de sessões/partidas jogadas até o momento
        participantes_freq (List[str]): Lista de jogadores frequentes

    """

    tipo = "Cooperativo"

    def __init__(self, titulo: str, genero: str, plataforma: str, ano_lancamento: int, jogadores_max: int, horas_jogadas: float = 0, status: str = "Não iniciado", nota: Optional[float] = None, data_inicio: Optional[date] = None, data_termino: Optional[date] = None, num_sessoes: int = 0, participantes_freq: list[str] = None):
            super().__init__(titulo, genero, plataforma, ano_lancamento, horas_jogadas, status, nota, data_inicio, data_termino)
            self.__jogadores_max = jogadores_max
            self.__num_sessoes = num_sessoes
            self.__participantes_freq = participantes_freq
    
    def __str__(self):
        info_jogo = super().__str__()

        if self.__participantes_freq == None:
            participantes_str = "Sem participantes frequentes"
        else:
            participantes_str = self.__participantes_freq

        info_cooperativo = f"\nMáximo de jogadores: {self.__jogadores_max}, Número de sessões: {self.__num_sessoes}\nParticipantes Frequentes: {participantes_str}"

        return info_jogo + info_cooperativo

    def __repr__(self):
        info_jogo = super().__repr__()
        info_cooperativo = f"\nMáximo de jogadores: {self.__jogadores_max}, Número de sessões: {self.__num_sessoes}\nParticipantes Frequentes: {self.__participantes_freq}"
        
        return info_jogo + info_cooperativo

    @property
    def jogadores_max(self):
        return self.__jogadores_max

    @jogadores_max.setter
    def jogadores_max(self, novo_jogadores_max):
        if isinstance(novo_jogadores_max, int) and novo_jogadores_max > 0:
            self.__jogadores_max = novo_jogadores_max
            
        elif isinstance(novo_jogadores_max, str) and novo_jogadores_max.isdigit() and int(novo_jogadores_max) > 0:
            self.__jogadores_max = int(novo_jogadores_max)
            
        else:
            print("Número máximo de jogadores inválido")  

    @property
    def num_sessoes(self):
        return self.__num_sessoes

    @num_sessoes.setter
    def num_sessoes(self, novo_num_sessoes):
        if isinstance(novo_num_sessoes, int) and int(novo_num_sessoes) >= 0:
            self.__num_sessoes = novo_num_sessoes
            
        elif isinstance(novo_num_sessoes, str) and novo_num_sessoes.isdigit() and int(novo_num_sessoes) >= 0:
            self.__num_sessoes = int(novo_num_sessoes)
            
        else:
            print("Número de sessões inválido")  

    @property
    def participantes_freq(self):
        return self.__participantes_freq

    @participantes_freq.setter
    def participantes_freq(self, nova_lista: list[str]):
        if isinstance(nova_lista, list):
            self.__participantes_freq = nova_lista
        else:
            print("A lista fornecida é inválida")

    def to_dict(self):
        dados = super().to_dict()
        dados["jogadores_max"] = self.__jogadores_max
        dados["num_sessoes"] = self.__num_sessoes
        dados["participantes_freq"] = self.__participantes_freq

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
            jogadores_max=dados["jogadores_max"],
            num_sessoes=dados["num_sessoes"],
            participantes_freq=dados["participantes_freq"]
        )