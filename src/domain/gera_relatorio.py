from .relatorio import Relatorio
from repositories.cadastroJson import CadastroJson

""" Representa um relatório que usa as informações da coleção e dos jogos

    Atributos:

        total_horas (float): Total de horas em todas as coleções, ou somentena coleção selecionada
        media_nota_jogos (float): Media de todos os jogos das coleções, ou somente da coleção selecionada
        percentual_status (float): Percentual de conclusão de jogos de todas as coleções, ou somente da coleção selecionada
        top_5_jogados (List[Jogo]): Lista com os 5 jogos mais jogados de todas as coleções, ou somente da coleção selecionada
"""

def gera_relatorio(usuario):
    cadastro = CadastroJson("arquivos.json")
    dados = cadastro.carregar()
    usuario_encontrado = cadastro.procurar_nome(usuario)

    if usuario_encontrado:
        total_horas = 0

        for i in dados:
            total_horas += i.nome.colecoes.horas_jogadas

        print(f"Total de jogos: {len(usuario.jogos)}\n Total de horas: {total_horas}")
        return usuario_encontrado
    else:
        print("Usuario não encontrado")
        return None
