import pytest
from domain import Usuario, Colecao, Jogo, RegraDeNegocioError


def criar_usuario():
    usuario = Usuario("Gustavo")
    usuario.colecoes["Favoritos"] = Colecao("Favoritos", [])
    return usuario


def test_adicionar_jogo():
    usuario = criar_usuario()
    usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "Switch", 2017))
    assert len(usuario.jogos) == 1


def test_nao_pode_duplicar_jogo():
    usuario = criar_usuario()
    usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "Switch", 2017))
    with pytest.raises(RegraDeNegocioError):
        usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "Switch", 2017))


def test_mesmo_titulo_em_outra_plataforma_pode():
    usuario = criar_usuario()
    usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "Switch", 2017))
    usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "PC", 2017))
    assert len(usuario.jogos) == 2


def test_limite_de_3_jogos_jogando():
    usuario = criar_usuario()
    usuario.adicionar_jogo("Favoritos", Jogo("Zelda", "Aventura", "Switch", 2017))
    usuario.adicionar_jogo("Favoritos", Jogo("Hollow Knight", "Metroidvania", "PC", 2017))
    usuario.adicionar_jogo("Favoritos", Jogo("Celeste", "Plataforma", "PC", 2018))
    usuario.adicionar_jogo("Favoritos", Jogo("Hades", "Roguelike", "PC", 2020))
    usuario.iniciar_jogo("Zelda")
    usuario.iniciar_jogo("Hollow Knight")
    usuario.iniciar_jogo("Celeste")
    with pytest.raises(RegraDeNegocioError):
        usuario.iniciar_jogo("Hades")


def test_aviso_quando_nao_bateu_a_meta():
    usuario = criar_usuario()
    aviso = usuario.aviso_meta_anual(2)
    assert aviso is not None


def test_sem_aviso_quando_bateu_a_meta():
    usuario = criar_usuario()
    usuario.adicionar_jogo("Favoritos", Jogo("Celeste", "Plataforma", "PC", 2018))
    usuario.buscar_jogo("Celeste").finalizar_jogo()
    assert usuario.aviso_meta_anual(1) is None
