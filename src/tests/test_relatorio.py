from domain import Usuario, Colecao, Jogo, gera_relatorio


def test_relatorio_total_de_horas_e_percentual():
    usuario = Usuario("Gustavo")
    usuario.colecoes["Favoritos"] = Colecao("Favoritos", [])
    usuario.adicionar_jogo("Favoritos", Jogo("Hades", "Roguelike", "PC", 2020, horas_jogadas=10))
    usuario.adicionar_jogo("Favoritos", Jogo("Celeste", "Plataforma", "PC", 2018, horas_jogadas=5))
    usuario.buscar_jogo("Hades").finalizar_jogo()

    texto = str(gera_relatorio(usuario))

    assert "Total de horas: 15.00" in texto
    assert "Percentual de conclusão: 50.00%" in texto