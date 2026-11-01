# Catálogo de Jogos Digitais

## Sumário

* [Descrição do Projeto](https://www.google.com/search?q=%23descri%C3%A7%C3%A3o-do-projeto)
* [Objetivo do Projeto](https://www.google.com/search?q=%23objetivo-do-projeto)
* [Funcionalidades](https://www.google.com/search?q=%23funcionalidades)
* [Instalação e execução](https://www.google.com/search?q=%23instala%C3%A7%C3%A3o-e-execu%C3%A7%C3%A3o)
* [Exemplos de uso](https://www.google.com/search?q=%23exemplos-de-uso)
* [Configuração](https://www.google.com/search?q=%23configura%C3%A7%C3%A3o)
* [Persistência dos dados](https://www.google.com/search?q=%23persist%C3%AAncia-dos-dados)
* [Estrutura Planejada de Classes](https://www.google.com/search?q=%23estrutura-planejada-de-classes)
* [UML Textual](https://www.google.com/search?q=%23uml-textual)

## Descrição do Projeto

* Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**
* O sistema consiste no desenvolvimento de um **catálogo pessoal de jogos digitais** que permite ao usuário organizar sua coleção e acompanhar seu progresso em diferentes tipos de jogos

## Objetivo do Projeto

* Aplicar os conceitos de Programação Orientada a Objetos por meio do desenvolvimento de um sistema de gerenciamento de jogos digitais para aprendizado.
* O projeto utiliza conceitos como:
* Classes e objetos
* Encapsulamento
* Herança
* Relacionamento entre classes
* Atributos e métodos
* Persistência simples usando JSON
* Regras de negócio
* Interface CLI

## Funcionalidades

* Cadastro de usuários e de coleções (um usuário pode ter várias)
* Cadastro de jogos de quatro tipos: genérico (jogo), campanha, competitivo e cooperativo
* Controle de status: `Não iniciado` → `Jogando` → `Finalizado`
* Registro de horas jogadas e avaliação (nota de 0 a 10) após finalizar
* Relatório com total de horas, média das notas, percentual de conclusão e top 5 mais jogados
* Aviso de meta anual de jogos finalizados
* Dados salvos em arquivo JSON

## Instalação e execução

### Pré-requisitos

Para executar o sistema, é necessário ter o [`Python 3`](https://www.python.org/downloads/) instalado no computador. O projeto não utiliza bibliotecas externas, sendo desenvolvido apenas com recursos nativos da linguagem Python. Porém, caso deseje rodar os testes, será necessário a biblioteca `pytest`

### 1. Clonar o repositório

Primeiramente, clone o repositório do projeto:

```bash
git clone https://github.com/gustavoxenofonte/Catalogo-de-jogos-digitais.git
```

Em seguida, acesse a pasta do projeto:

```bash
cd Catalogo-de-jogos-digitais
```

### 2. Executar o sistema

Após acessar a pasta do projeto, execute o arquivo principal utilizando o Python:

**Importante:** rode sempre a partir da **raiz do projeto** (a pasta que contém `src/`). Os caminhos do `config.json` e do banco JSON são relativos a ela.

```bash
python src/main.py <comando> [opções]
```

Caso o sistema utilize o comando `python3` no seu ambiente, utilize:

```bash
python3 src/main.py <comando> [opções]
```

Para ver a ajuda geral ou a ajuda de um comando:

```bash
python src/main.py --help
python src/main.py adicionar --help
```

### Comandos disponíveis

| Comando | O que faz | Exemplo de uso |
| --- | --- | --- |
| `criar-usuario` | Cria um usuário | `criar-usuario Gustavo` |
| `criar-colecao` | Cria uma coleção para o usuário | `criar-colecao -u Gustavo Favoritos` |
| `adicionar` | Adiciona um jogo a uma coleção | `adicionar -u Gustavo -c Favoritos -g Aventura -p Switch -a 2017 Zelda` |
| `listar` | Lista os jogos (todas as coleções ou só uma) | `listar -u Gustavo [-c Favoritos]` |
| `iniciar` | Muda o status do jogo para `Jogando` | `iniciar -u Gustavo Zelda` |
| `horas` | Soma horas jogadas ao jogo | `horas -u Gustavo Zelda 2.5` |
| `finalizar` | Marca o jogo como `Finalizado` (nota opcional) | `finalizar -u Gustavo Zelda --nota 9` |
| `avaliar` | Dá ou altera a nota de um jogo já finalizado | `avaliar -u Gustavo Zelda 8.5` |
| `relatorio` | Mostra o relatório geral do usuário | `relatorio -u Gustavo` |

### Opções principais

| Opção | Usada em | Significado |
| --- | --- | --- |
| `-u`, `--usuario` | todos, exceto `criar-usuario` | Nome do usuário (obrigatório) |
| `-c`, `--colecao` | `adicionar`, `listar` | Nome da coleção (obrigatório no `adicionar`) |
| `-g`, `--genero` | `adicionar` | Gênero do jogo (obrigatório) |
| `-p`, `--plataforma` | `adicionar` (obrigatório); `iniciar`, `horas`, `finalizar`, `avaliar` (opcional) | Plataforma do jogo. Nos comandos que só localizam o jogo, serve para desempatar quando o mesmo título existe em mais de uma plataforma |
| `-a`, `--ano` | `adicionar` | Ano de lançamento (obrigatório) |
| `-t`, `--tipo` | `adicionar` | `jogo` (padrão), `campanha`, `competitivo` ou `cooperativo` |
| `--missoes-totais` | `adicionar -t campanha` | Total de missões (padrão: 1) |
| `--jogadores-max` | `adicionar -t cooperativo` | Máximo de jogadores (padrão: 2) |
| `--nota` | `finalizar` | Nota de 0 a 10 dada na hora de finalizar |

Títulos com espaço precisam de aspas: `"God of War"`.

## Exemplos de uso

Aqui está um exemplo de um fluxo completo do programa. Ele demonstra não só os comandos, mas também as saídas reais.

```console
python src/main.py criar-usuario Gustavo
Usuário 'Gustavo' criado.

python src/main.py criar-colecao -u Gustavo Favoritos
Coleção 'Favoritos' criada.

python src/main.py adicionar -u Gustavo -c Favoritos -g Aventura -p Switch -a 2017 Zelda
'Zelda' adicionado a 'Favoritos'.

python src/main.py adicionar -u Gustavo -c Favoritos -g Acao -p PS5 -a 2018 -t campanha --missoes-totais 20 "God of War"
'God of War' adicionado a 'Favoritos'.

python src/main.py adicionar -u Gustavo -c Favoritos -g MOBA -p PC -a 2009 -t competitivo LoL
'LoL' adicionado a 'Favoritos'.

python src/main.py adicionar -u Gustavo -c Favoritos -g Co-op -p PC -a 2020 -t cooperativo --jogadores-max 4 "It Takes Two"
'It Takes Two' adicionado a 'Favoritos'.

python src/main.py iniciar -u Gustavo Zelda
'Zelda' agora está Jogando.

python src/main.py horas -u Gustavo Zelda 2.5
'Zelda': 2.5h jogadas.

python src/main.py finalizar -u Gustavo Zelda --nota 9
'Zelda' finalizado.
AVISO: 1 de 12 jogos finalizados em 2026 (faltam 11).

python src/main.py listar -u Gustavo
== Favoritos ==
- Zelda
Switch
2.5h
Finalizado
- God of War
PS5
0.0h
Não iniciado
- LoL
PC
0.0h
Não iniciado
- It Takes Two
PC
0.0h
Não iniciado

python src/main.py relatorio -u Gustavo
Total de horas: 2.50
Média das notas: 9.00
Percentual de conclusão: 25.00%
Top 5 mais jogados:
Zelda (2.5h)
God of War (0.0h)
LoL (0.0h)
It Takes Two (0.0h)

AVISO: 1 de 12 jogos finalizados em 2026 (faltam 11).
```

### Exemplos de erros

```console
$ python src/main.py adicionar -u Gustavo -c Favoritos -g Aventura -p Switch -a 2017 Zelda
Erro: Zelda já existe na plataforma Switch.

$ python src/main.py avaliar -u Gustavo Zelda 9        # antes de finalizar
Erro: Só é possível avaliar um jogo depois de finalizado.

$ python src/main.py horas -u Gustavo Zelda -- -1
Erro: Para adicionar horas, o valor deve ser maior que 0.

$ python src/main.py iniciar -u Gustavo Hades          # com 3 jogos já em andamento
Erro: Limite de 3 jogos simultâneos atingido (God of War, LoL, Zelda).

$ python src/main.py finalizar -u Gustavo Zelda        # Zelda existe no Switch e no PC
Erro: Zelda existe em mais de uma plataforma

$ python src/main.py iniciar -u Gustavo Zelda -p PC    # desempatando com -p
'Zelda' agora está Jogando.
```

## Configuração

Caso deseje mudar a configuração padrão da meta anual de jogos finalizados e do máximo de jogos jogando simultaneamente. Acesse o arquivo: `src/config/config.json` e troque os valores

```json
{
    "meta_anual_finalizados": 12,
    "max_jogando_simultaneos": 3
}

```

| Chave | Tipo | Descrição |
| --- | --- | --- |
| `meta_anual_finalizados` | inteiro >= 0 ou `null` | Meta de jogos finalizados no ano. Com `null`, o aviso é desativado |
| `max_jogando_simultaneos` | inteiro >= 1 | Limite de jogos com status `Jogando` ao mesmo tempo |

## Persistência dos dados

Os dados ficam em `src/database/arquivos.json`, escritos com `json.dump` e lidos com `json.load`. As coleções ficam **aninhadas dentro do usuário**, e cada jogo guarda o campo `tipo` para saber qual classe recriar ao carregar:

```json
[
    {
        "Usuario": "Gustavo",
        "Colecoes": [
            {
                "Nome_colecao": "Favoritos",
                "Jogos": [
                    {
                        "titulo": "Zelda",
                        "genero": "Aventura",
                        "plataforma": "Switch",
                        "horas_jogadas": 2.5,
                        "status": "Finalizado",
                        "nota": 9.0,
                        "tipo": "Jogo",
                        "data_inicio": "2026-11-01",
                        "data_termino": "2026-11-01",
                        "ano_lancamento": 2017
                    }
                ]
            }
        ]
    }
]

```

O projeto vem com um arquivos.json com um usuário que serve para demonstração

## Estrutura Planejada de Classes

* Observação: a estrutura foi planejada na entrega 1, com o andamento do projeto, atributos e métodos mudaram de nome, ou não foram incluídos e outros não listados foram adicionados
* As classes se encontram na pasta [src/domain](src/domain)

| Classe | Atributos | Métodos |
| --- | --- | --- |
| **Jogo** | titulo, genero, plataforma, horas_jogadas, status, nota, data_inicio, data_fim, ano_lancamento | registrar_progresso(), finalizar_jogo(), reiniciar_jogo(), avaliar() |
| **JogoCampanha** | missoes_totais, missoes_concluidas, percentual_conclusao | atualizar_progresso() |
| **JogoCompetitivo** | partidas_jogadas, vitorias, derrotas, ranking, winrate | registrar_partida(), calcular_winrate() |
| **JogoCooperativo** | jogadores_max, num_sessoes, participantes_freq | registrar_sessao(participantes: list[str]), adicionar_participante(nome:str) |
| **Colecao** | nome_colecao, jogos | adicionar_jogo, remover_jogo(), filtrar_por(), ordenar_por() |
| **Usuario** | nome, colecoes | criar_colecao(), remover_colecao() |
| **Relatorio** | total_horas, media_nota_jogos, percentual_status, top_5_jogados | gerar_relatorio() |

## UML Textual

* Para melhor organização do README, O UML se encontra no arquivo `UML.md`
* [Clique aqui para acessá-lo](UML.md)