from domain import Jogo, JogoCampanha, JogoCompetitivo


def test_campanha_e_um_jogo():
    jogo = JogoCampanha("God of War", "Ação", "PS5", 2018, missoes_totais=10)
    assert isinstance(jogo, Jogo)


def test_percentual_da_campanha():
    jogo = JogoCampanha("God of War", "Ação", "PS5", 2018, missoes_totais=10, missoes_concluidas=5)
    assert jogo.percentual_conclusao == 50


def test_winrate_do_competitivo():
    jogo = JogoCompetitivo("LoL", "MOBA", "PC", 2009, partidas_jogadas=10, vitorias=7, derrotas=3)
    assert jogo.winrate == 70


def test_to_dict_e_from_dict():
    jogo = JogoCampanha("God of War", "Ação", "PS5", 2018, missoes_totais=10)
    dados = jogo.to_dict()
    copia = JogoCampanha.from_dict(dados)
    assert copia.to_dict() == dados
