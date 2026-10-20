from pathlib import Path
from domain import Jogo, JogoCampanha, JogoCooperativo, JogoCompetitivo, Usuario
import json

class CadastroJson:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.caminho = Path("src") / "database" / nome_arquivo
        self.caminho.parent.mkdir(parents=True, exist_ok=True)

    def carregar(self):
        if self.caminho.exists():
            with self.caminho.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return [Usuario.from_dict(item) for item in dados]
        else:
            return []

    def salvar(self, usuarios):
        dados = [item.to_dict() for item in usuarios]

        with self.caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def procurar_nome(self, usuario):
        dados = self.carregar()
    
        nome_encontrado = None
    
        for nome in dados:
            if nome.nome == usuario:
                nome_encontrado = usuario
                return nome_encontrado
        
        return None
    