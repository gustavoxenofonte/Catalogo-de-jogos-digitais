class Relatorio:
    """ Representa um relatório que usa as informações da coleção e dos jogos

    Atributos:

        total_horas (float): Total de horas em todas as coleções, ou somentena coleção selecionada
        media_nota_jogos (float): Media de todos os jogos das coleções, ou somente da coleção selecionada
        percentual_status (float): Percentual de conclusão de jogos de todas as coleções, ou somente da coleção selecionada
        top_5_jogados (List[Jogo]): Lista com os 5 jogos mais jogados de todas as coleções, ou somente da coleção selecionada

    """
    def __init__(self, total_horas: float = 0, media_nota_jogos: float = 0, percentual_status: float = 0, top_5_jogados: list = None):
        self.__total_horas = total_horas
        self.__media_nota_jogos = media_nota_jogos
        self.__percentual_status = percentual_status
        self.__top_5_jogados = top_5_jogados

    def __str__(self):
        return f"Total de horas em todas as coleções: {self.__total_horas}, Média da nota em todas as coleções: {self.__media_nota_jogos}\nPercentual de conclusão em todas as coleções: {self.__percentual_status}\nTop 5 mais jogados de todas as coleções: {self.__top_5_jogados}"

    # Fiz somente a base da classe pois ela só funcionará quando se relacionar com outras classes