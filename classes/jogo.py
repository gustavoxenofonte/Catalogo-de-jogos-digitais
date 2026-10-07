from datetime import date
from typing import Optional

class Jogo:
    """ Representa a classe base para gerenciamento de jogos na coleção.
    
    As classes JogoCampanha, JogoCompetitivo e JogoCooperativo herdam de Jogo

    Atributos:
        titulo (str): Título do Jogo (Ex: Super Mario, Dark Souls)
        genero (str): Genero do Jogo (Ex: Plataforma, Souls Like)
        plataforma (str): Plataforma onde está jogando (Ex: Playstation, Xbox, PC)
        horas_jogadas (float): Número de horas jogadas até o momento
        status (str): Não iniciado, jogando, finalizado
        nota (float): Nota de 0 a 10
        data_inicio (date): Data em que o usuário começou o jogo
        data_termino (date): Data em que o usuário terminou o jogo
        ano_lancamento (date): Ano de lançamento oficial do jogo
    
    """
    def __init__(self, titulo: str, genero: str, plataforma: str, ano_lancamento: int, horas_jogadas: float = 0, status: str = "Não iniciado", nota: Optional[float] = None, data_inicio: Optional[date] = None, data_termino: Optional[date] = None):
        self.__titulo = titulo
        self.__genero = genero
        self.__plataforma = plataforma 
        self.__horas_jogadas = horas_jogadas
        self.__status = status
        self.__nota = nota
        if data_inicio != None:
            self.__data_inicio = data_inicio
        else:
            self.__data_inicio = date.today()
        self.__data_termino = data_termino # Como quando o usuário adicionar o jogo, a princípio, ele ainda não vai tê-lo zerado, não faz sentido exigir uma data de término do jogo
        self.__ano_lancamento = ano_lancamento

    def __str__(self):
        if self.__nota == None:
            nota_str = "Sem nota"
        else:
            nota_str = self.__nota
        
        if self.__data_termino == None:
            data_termino_str = "Jogo ainda não finalizado"
        else:
            data_termino_str = self.__data_termino

        return f"Título: {self.__titulo}, Genero: {self.__genero}, Plataforma: {self.__plataforma}\nHoras jogadas: {self.__horas_jogadas}, Status: {self.__status}, Nota: {nota_str}\nData de Início: {self.__data_inicio}, Data de Término: {data_termino_str}, Ano de lançamento: {self.__ano_lancamento}"

    def __repr__(self):
        return f"Título: {self.__titulo}, Genero: {self.__genero}, Plataforma: {self.__plataforma}\nHoras jogadas: {self.__horas_jogadas}, Status: {self.__status}, Nota: {self.__nota}\nData de Início: {self.__data_inicio}, Data de Término: {self.__data_termino}, Ano de lançamento: {self.__ano_lancamento}"

    def __eq__(self, outro: object):
        if not isinstance(outro, Jogo):
            return False

        return (self.__titulo.lower() == outro.__titulo.lower() and self.__plataforma.lower() == outro.__plataforma.lower())

    # Compara horas_jogadas
    def __lt__(self, outro):
        if not isinstance(outro, Jogo):
            return NotImplemented
        return self.__horas_jogadas < outro.__horas_jogadas

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo:str):
        if isinstance(novo_titulo, str):
            self.__titulo = novo_titulo
        else:
            print("Titulo inválido")

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, novo_genero:str):
        if isinstance(novo_genero, str):
            self.__genero = novo_genero
        else:
            print("Genero inválido")

    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self, nova_plataforma:str):
        if isinstance(nova_plataforma, str):
            self.__plataforma = nova_plataforma
        else:
            print("Plataforma inválida")

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, valor: float):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__horas_jogadas = float(valor)
        else:
            print("Horas jogadas devem ser maiores ou iguais a 0")

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova_nota):
        if isinstance(nova_nota, (int, float)) and nova_nota >= 0:
            self.__nota = float(nova_nota)
        elif isinstance(nova_nota, str) and nova_nota.isdigit() and float(nova_nota) >= 0:
            self.__nota = float(nova_nota)
        else:
            print("Nota inválida")

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, nova_data_inicio):
        if isinstance(nova_data_inicio, date):
            self.__data_inicio = nova_data_inicio
        else:
            print("Data inválida")

    @property
    def data_termino(self):
        return self.__data_termino

    @data_termino.setter
    def data_termino(self, nova_data_termino):
        if isinstance(nova_data_termino, date):
            self.__data_termino = nova_data_termino
        else:
            print("Data inválida")

    def adiciona_horas(self, valor:float):
            if isinstance(valor, (int, float)) and valor > 0:
                self.__horas_jogadas += valor
            else:
                print("Para adicionar horas, o valor deve ser maior que 0")
    
    def remove_horas(self, valor:float):
        if isinstance(valor, (int, float)) and valor > 0:
            if self.__horas_jogadas - valor >= 0:
                self.__horas_jogadas -= valor
            else:
                print("Não é possível remover essa quantidade de horas")
        else:
            print("Para remover horas, o valor precisa ser maior que 0")

    def finalizar_jogo(self, data_final: Optional[date] = None, nota: Optional[float] = None):
        if data_final == None:
            self.__data_termino = date.today()
            validacao_data = True

        else:
            if isinstance(data_final, date):
                self.__data_termino = data_final
                validacao_data = True
            else:
                print("Data inválida")
                validacao_data = False

        validacao_nota = True
        
        if nota != None:
            if isinstance(nota, (float, int)) and nota >= 0:
                self.__nota = float(nota)
                validacao_nota = True
            elif isinstance(nota, str) and nota.isdigit() and nota >= 0:
                self.__nota = float(nota)
                validacao_nota = True
            else:
                print("Nota inválida")
                validacao_nota = False

        if validacao_data and validacao_nota:
            self.__status = "Finalizado"
        else:
            print("O jogo não foi finalizado")

class JogoCampanha:
    """ Representa um jogo modo campanha (ou modo história)

    Herda de Jogo

    Atributos:
        missoes_totais (int): Total de missões que o jogo possui
        missoes_concluidas (int): Total de missões que o usuário concluiu
        percentual_conclusao (float): Percentual com base no total de missões e no número de missões concluidas (missoes_concluidas / missoes_totais)

    """
    def __init__(self, missoes_totais: int, missoes_concluidas: int = 0):
        self.__missoes_totais = missoes_totais
        self.__missoes_concluidas = missoes_concluidas
        if missoes_totais != 0:
            self.__percentual_conclusao = missoes_concluidas / missoes_totais * 100
        else:
            self.__percentual_conclusao = None 

    def __str__(self):
        return f"Missões Totais: {self.__missoes_totais}, Missões Concluidas: {self.__missoes_concluidas}, Percentual de Conclusão: {self.__percentual_conclusao:.2f}%"

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

class JogoCompetitivo:
    """ Representa um jogo competitivo

    Herda de Jogo

    Atributos:
        partidas_jogadas (int): Total de partidas jogadas
        vitorias (int): Total de vitórias
        derrotas (int): Total de derrotas
        ranking (int): Classificação do usuário em relação a outros jogadores
        winrate (float): Taxa de vitória (vitorias / partidas_jogadas)
    """
    def __init__(self, partidas_jogadas: int = 0, vitorias: int = 0, derrotas: int = 0, ranking: int = None):
        self.__partidas_jogadas = partidas_jogadas
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__ranking = ranking
        if self.__partidas_jogadas != 0:
            self.__winrate = self.__vitorias / self.__partidas_jogadas * 100
        else:
            self.__winrate = 0

    def __str__(self):
        if self.__ranking == None:
            ranking_str = "Sem rank"
        else:
            ranking_str = self.__ranking

        return f"Total de partidas: {self.__partidas_jogadas}, Vitórias: {self.__vitorias}, Derrotas: {self.__derrotas}\nRanking: {ranking_str}, Taxa de vitória (winrate): {self.__winrate}%"


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

class JogoCooperativo:
    """ Representa um jogo cooperativo

    Herda de Jogo

    Atributos:
        jogadores_max (int): Número de jogadores máximos de um jogo cooperativo
        num_sessoes (int): Número de sessões/partidas jogadas até o momento
        participantes_freq (List[str]): Lista de jogadores frequentes

    """
    def __init__(self, jogadores_max: int, num_sessoes: int = 0, participantes_freq: list[str] = None):
            self.__jogadores_max = jogadores_max
            self.__num_sessoes = num_sessoes
            self.__participantes_freq = participantes_freq
    
    def __str__(self):
        if self.__participantes_freq == None:
            participantes_str = "Sem participantes frequentes"
        else:
            participantes_str = self.__participantes_freq

        return f"Máximo de jogadores: {self.__jogadores_max}, Número de sessões: {self.__num_sessoes}\nParticipantes Frequentes: {participantes_str}"

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
