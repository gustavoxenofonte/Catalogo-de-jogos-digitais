from datetime import date
from typing import Optional
from .excecoes import RegraDeNegocioError

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

    tipo = "Jogo"
    nao_iniciado = "Não iniciado"
    jogando = "Jogando"
    finalizado = "Finalizado"

    def __init__(self, titulo: str, genero: str, plataforma: str, ano_lancamento: int, horas_jogadas: float = 0, status: str = "Não iniciado", nota: Optional[float] = None, data_inicio: Optional[date] = None, data_termino: Optional[date] = None):
        self.__titulo = titulo
        self.__genero = genero
        self.__plataforma = plataforma 
        self.__horas_jogadas = 0
        self.horas_jogadas = horas_jogadas
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

    # Compara título
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
    def status(self):
        return self.__status

    @status.setter
    def status(self, outro_status):
        self.__status = outro_status

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise RegraDeNegocioError("Horas jogadas devem ser maiores ou iguais a 0.")
        if valor < self.__horas_jogadas:
            raise RegraDeNegocioError("As horas só podem aumentar (use adiciona_horas).")
        self.__horas_jogadas = float(valor)


    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova_nota):
        if self.__status != Jogo.finalizado:
            raise RegraDeNegocioError("Só é possível avaliar um jogo depois de finalizado.")
        
        if isinstance(nova_nota, (int, float)) and float(nova_nota) >= 0 and float(nova_nota) <= 10:
            self.__nota = float(nova_nota)
        elif isinstance(nova_nota, str) and nova_nota.isdigit() and float(nova_nota) >= 0 and float(nova_nota) <= 10:
            self.__nota = float(nova_nota)
        else:
            raise RegraDeNegocioError("Nota inválida")

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

    def to_dict(self):
        data_inicio_str = self.__data_inicio.strftime("%Y-%m-%d")
        if self.__data_termino is not None:
            data_termino_str = self.__data_termino.strftime("%Y-%m-%d")
        else:
            data_termino_str = self.__data_termino

        return {
            "titulo": self.__titulo,
            "genero": self.__genero,
            "plataforma": self.__plataforma,
            "horas_jogadas": self.__horas_jogadas,
            "status": self.__status,
            "nota": self.__nota,
            "tipo": self.tipo,
            "data_inicio": data_inicio_str,
            "data_termino": data_termino_str,
            "ano_lancamento": self.__ano_lancamento
        }

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
            ano_lancamento=dados["ano_lancamento"]
        )

    def adiciona_horas(self, valor:float):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise RegraDeNegocioError("Para adicionar horas, o valor deve ser maior que 0.")
        self.__horas_jogadas += valor

    def finalizar_jogo(self, data_final: Optional[date] = None, nota: Optional[float] = None):
        # A função só é chamada quando finaliza um jogo, antes disso não é possível atribuir nota ao jogo
        if self.__status == Jogo.finalizado:
            raise RegraDeNegocioError("Jogo já foi finalizado")
        
        if data_final == None:
            self.__data_termino = date.today()
            validacao_data = True

        else:
            if isinstance(data_final, date):
                self.__data_termino = data_final
                validacao_data = True
            else:
                raise RegraDeNegocioError("Data inválida")
                validacao_data = False

        validacao_nota = True
        
        if nota != None:
            if isinstance(nota, (float, int)) and float(nota) >= 0 and float(nota) <= 10:
                self.__nota = float(nota)
                validacao_nota = True
            elif isinstance(nota, str) and nota.isdigit() and float(nota) >= 0 and float(nota) <= 10:
                self.__nota = float(nota)
                validacao_nota = True
            else:
                print("Nota inválida")
                validacao_nota = False

        if validacao_data and validacao_nota:
            self.__status = Jogo.finalizado
        else:
            raise RegraDeNegocioError("Jogo não foi finalizado.")

    def iniciar_jogo(self):
        if self.__status == Jogo.finalizado:
            raise RegraDeNegocioError("Esse jogo já foi finalizado.")
        self.__status = Jogo.jogando
