class Jogo:
    """ Representa a classe base para gerenciamento de jogos na coleção.
    
    As classes JogoCampanha, JogoCompetitivo e JogoCooperativo herdam de Jogo

    Atributos:
        titulo (str): Título do Jogo (Ex: Super Mario, Dark Souls)
        genero (str): Genero do Jogo (Ex: Plataforma, Souls Like)
        plataforma (str): Plataforma onde está jogando (Ex: Playstation, Xbox, PC)
        horas_jogadas (float): Número de horas jogadas até o momento
        status (str): Não iniciado, jogando, finalizado
        nota (float): Nota de 0 a 5 estrelas
        data_inicio (date): Data em que o usuário começou o jogo
        data_termino (date): Data em que o usuário terminou o jogo
        ano_lancamento (date): Ano de lançamento oficial do jogo
    
    """
    pass

class JogoCampanha:
    """ Representa um jogo modo campanha (ou modo história)

    Herda de Jogo

    Atributos:
        missoes_totais (int): Total de missões que o jogo possui
        missoes_concluidas (int): Total de missões que o usuário concluiu
        percentual_conclusao (float): Percentual com base no total de missões e no número de missões concluidas (missoes_concluidas / missoes_totais)

    """
    pass

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
    pass

class JogoCooperativo:
    """ Representa um jogo cooperativo

    Herda de Jogo

    Atributos:
        jogadores_max (int): Número de jogadores máximos de um jogo cooperativo
        num_sessoes (int): Número de sessões/partidas jogadas até o momento
        participantes_freq (List[str]): Lista de jogadores frequentes

    """
    pass