from pathlib import Path
from domain import Jogo, JogoCampanha, JogoCooperativo, JogoCompetitivo
import json

class CadastroJson:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.caminho = Path("src") / "database" / nome_arquivo
        self.caminho.parent.mkdir(parents=True, exist_ok=True)

    def carregar(self):
        with self.caminho.open("r", encoding="utf-8") as arquivo:
           dados = json.load(arquivo)

        return [Jogo.from_dict(item) for item in dados]

    def salvar(self, lista_jogos):
        dados = [item.to_dict() for item in lista_jogos]

        with self.caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)