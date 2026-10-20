from .relatorio import Relatorio

""" Representa um relatório que usa as informações da coleção e dos jogos

    Atributos:

        total_horas (float): Total de horas em todas as coleções, ou somentena coleção selecionada
        media_nota_jogos (float): Media de todos os jogos das coleções, ou somente da coleção selecionada
        percentual_status (float): Percentual de conclusão de jogos de todas as coleções, ou somente da coleção selecionada
        top_5_jogados (List[Jogo]): Lista com os 5 jogos mais jogados de todas as coleções, ou somente da coleção selecionada
"""

def gera_relatorio(usuario):
    jogos = []
    for colecao in usuario.colecoes.values():
        for jogo in colecao.jogos:
            jogos.append(jogo)

    horas_totais = 0
    soma_notas = 0
    total_notas = 0

    for jogo in jogos:
        horas_totais += jogo.horas_jogadas
        if jogo.nota is not None:
            soma_notas += jogo.nota
            total_notas +=1

    media_notas = 0

    if total_notas > 0:
        media_notas = soma_notas / total_notas

    qtd_finalizados = 0
    
    for jogo in jogos:
        if jogo.status == "Finalizado":
            qtd_finalizados += 1

    percentual_finalizados = qtd_finalizados / len(jogos) * 100

    jogos_ordenados = sorted(jogos, reverse=True) [:5]

    return Relatorio(total_horas= horas_totais, media_nota_jogos=media_notas, percentual_status=percentual_finalizados, top_5_jogados= jogos_ordenados)
