# Catálogo de Jogos Digitais

## Sumário

- [Descrição do Projeto](#descrição-do-projeto)
- [Objetivo do Projeto](#objetivo-do-projeto)
- [Estrutura Planejada de Classes](#estrutura-planejada-de-classes)
- [UML Textual](#uml-textual)


## Descrição do Projeto

- Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**
- O sistema consiste no desenvolvimento de um **catálogo pessoal de jogos digitais** que permite ao usuário organizar sua coleção e acompanhar seu progresso em diferentes tipos de jogos:
  - Cadastro de jogos
  - Registro de progresso de jogatina
  - Organização dos jogos por plataforma ou gênero
  - Geração de relatórios de desempenho e tempo jogado
  - Acompanhamento de diferentes tipos de jogos
    - Jogos Campanha
    - Jogos Competitivos
    - Jogos Cooperativos
  - Geração de relatórios sobre a coleção e tempo jogado

---

## Objetivo do Projeto

- Aplicar os conceitos de Programação Orientada a Objetos por meio do desenvolvimento de um sistema de gerenciamento de jogos digitais para aprendizado.

- O projeto utiliza conceitos como:

    - Classes e objetos
    - Encapsulamento
    - Herança
    - Relacionamento entre classes
    - Atributos e métodos

---

## Estrutura Planejada de Classes

- As classes se encontram na pasta [classes](classes)

---

| Classe | Atributos | Métodos |
| :--- | :--- | :--- |
| **Jogo** | titulo, genero, plataforma, horas_jogadas, status, nota, data_inicio, data_fim, ano_lancamento | registrar_progresso(), finalizar_jogo(), reiniciar_jogo(), avaliar() |
| **JogoCampanha** | missoes_totais, missoes_concluidas, percentual_conclusao | atualizar_progresso() |
| **JogoCompetitivo** | partidas_jogadas, vitorias, derrotas, ranking, winrate | registrar_partida(), calcular_winrate() |
| **JogoCooperativo** | jogadores_max, num_sessoes, participantes_freq | registrar_sessao(participantes: list[str]), adicionar_participantes(nome:str) |
| **Colecao** | nome_colecao, jogos | adicionar_jogo, remover_jogo(), filtrar_por(), ordenar_por() |
| **Usuario** | nome, colecoes | criar_colecao(), remover_colecao() |
| **Relatorio** | total_horas, media_nota_jogos, percentual_status, top_5_jogados | gerar_relatorio() |

---

## UML Textual

- Para melhor organização do README, O UML se encontra no arquivo `UML.md`
  - [Clique aqui para acessá-lo](UML.md)
