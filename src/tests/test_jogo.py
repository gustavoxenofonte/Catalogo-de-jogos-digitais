import pytest
from domain import Jogo, RegraDeNegocioError


def test_jogo_novo_comeca_zerado():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    assert jogo.horas_jogadas == 0
    assert jogo.status == "Não iniciado"
    assert jogo.nota is None


def test_adiciona_horas():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    jogo.adiciona_horas(2)
    jogo.adiciona_horas(1.5)
    assert jogo.horas_jogadas == 3.5


def test_horas_negativas_dao_erro():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    with pytest.raises(RegraDeNegocioError):
        jogo.adiciona_horas(-1)


def test_nao_pode_dar_nota_antes_de_finalizar():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    with pytest.raises(RegraDeNegocioError):
        jogo.nota = 8


def test_pode_dar_nota_depois_de_finalizar():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    jogo.finalizar_jogo()
    jogo.nota = 8
    assert jogo.nota == 8


def test_finalizar_muda_status():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    jogo.finalizar_jogo()
    assert jogo.status == "Finalizado"


def test_iniciar_muda_status():
    jogo = Jogo("Zelda", "Aventura", "Switch", 2017)
    jogo.iniciar_jogo()
    assert jogo.status == "Jogando"


def test_mesmo_titulo_e_plataforma_sao_iguais():
    a = Jogo("Zelda", "Aventura", "Switch", 2017)
    b = Jogo("zelda", "Outro", "switch", 2020)
    assert a == b
