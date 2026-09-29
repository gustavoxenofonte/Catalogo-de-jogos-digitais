# UML Textual

## Diagrama Visual
```mermaid
classDiagram
    class Jogo {
        -titulo: str
        -genero: str
        -plataforma: str
        -horas_jogadas: float
        -status: str
        -nota: float
        -data_inicio: date
        -data_termino: date
        -ano_lancamento: int
        +registrar_progresso(horas: float)
        +finalizar_jogo()
        +reiniciar_jogo()
        +avaliar(nota: float)
    }

    class JogoCampanha {
        -missoes_totais: int
        -missoes_concluidas: int
        -percentual_conclusao: float
        +atualizar_progresso(missoes: int)
    }

    class JogoCompetitivo {
        -partidas_jogadas: int
        -vitorias: int
        -derrotas: int
        -ranking: int
        -winrate: float
        +registrar_partida()
        +calcular_winrate()
    }

    class JogoCooperativo {
        -jogadores_max: int
        -num_sessoes: int
        -participantes_freq: List[str]
        +registrar_sessao(participantes: List[str])
        +adicionar_participante(nome: str)
    }

    class Colecao {
        -nome_colecao: str
        -jogos: List[Jogo]
        +adicionar_jogo(jogo: Jogo)
        +remover_jogo(jogo: Jogo)
        +filtrar_por()
        +ordenar_por(criterio: str)
    }

    class Usuario {
        -nome: str
        -colecoes: Dict[str, Colecao]
        +criar_colecao(nome: str)
        +remover_colecao(nome: str)
    }

    class Relatorio {
        -total_horas: float
        -media_nota_jogos: float
        -percentual_status: float
        -top_5_jogados: List[Jogo]
        +gerar_relatorio()
    }

    Jogo <|-- JogoCampanha
    Jogo <|-- JogoCompetitivo
    Jogo <|-- JogoCooperativo
    Usuario "1" *-- "*" Colecao
    Colecao "1" o-- "*" Jogo
    Relatorio ..> Jogo
```
## Classe: `Jogo` (Classe Base)

### Atributos

* `- titulo: str`
* `- genero: str`
* `- plataforma: str`
* `- horas_jogadas: float`
* `- status: str`
* `- nota: float`
* `- data_inicio: date`
* `- data_termino: date`
* `- ano_lancamento: int`

### Métodos

* `+ registrar_progresso(horas: float)`
* `+ finalizar_jogo()`
* `+ reiniciar_jogo()`
* `+ avaliar(nota: float)`

---

## Classe: `JogoCampanha` (herda de `Jogo`)

### Atributos

* `- missoes_totais: int`
* `- missoes_concluidas: int`
* `- percentual_conclusao: float`

### Métodos

* `+ atualizar_progresso(missoes: int)`

---

## Classe: `JogoCompetitivo` (herda de `Jogo`)

### Atributos

* `- partidas_jogadas: int`
* `- vitorias: int`
* `- derrotas: int`
* `- ranking: int`
* `- winrate: float`

### Métodos

* `+ registrar_partida()`
* `+ calcular_winrate()`

---

## Classe: `JogoCooperativo` (herda de `Jogo`)

### Atributos

* `- jogadores_max: int`
* `- num_sessoes: int`
* `- participantes_freq: List[str]`

### Métodos

* `+ registrar_sessao(participantes: List[str])`
* `+ adicionar_participante(nome: str)`

---

## Classe: `Colecao`

### Atributos

* `- nome_colecao: str`
* `- jogos: List[Jogo]`

### Métodos

* `+ adicionar_jogo(jogo: Jogo)`
* `+ remover_jogo(jogo: Jogo)`
* `+ filtrar_por()`
* `+ ordenar_por(criterio: str)`

---

## Classe: `Usuario`

### Atributos

* `- nome: str`
* `- colecoes: Dict[str, Colecao]`

### Métodos

* `+ criar_colecao(nome: str)`
* `+ remover_colecao(nome: str)`

---

## Classe: `Relatorio`

### Atributos

* `- total_horas: float`
* `- media_nota_jogos: float`
* `- percentual_status: float`
* `- top_5_jogados: list[Jogo]`

### Métodos

* `+ gerar_relatorio()`
