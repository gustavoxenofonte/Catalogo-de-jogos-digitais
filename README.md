#  Catálogo de jogos digitais

## Descrição do projeto

- Projeto da disciplina de Programação Orientada a Objetos

- Consiste no desenvolvimento de um catálogo pessoal de jogos digitais que permite:
    - Cadastro de jogos
    - Registro de progresso de jogatina
    - Organização por plataforma ou gênero
    - Geração de relatórios de desempenho e tempo jogado.

## Objetivo do projeto

- Aplicar conceitos da disciplina de Programação Orientada a Objetos para aprendizado

## Estrutura planejada de classes

| Classe | Atributos | Métodos |
|:-------| :----------:| :--------: |
| Coleção | jogos | criar_colecao(), visualizar_colecao(), atualizar_colecao() |
| Jogo | titulo, genero, plataforma, horas jogadas, status, nota | cadastrar_jogo(), atualizar_info(), avaliar() |
| JogoCampanha | progresso_historia, missoes_concluidas, percentual_conclusao | atualizar_progresso() |
| JogoCompetitivo |  partidas_jogadas, vitorias, derrotas, ranking, winrate | atualizar() |
| JogoCooperativo | jogadores_max, num_sessoes, participantes_freq | atualizar() |
| Relatório | desempenho, tempo jogado | gerar_relatorio(), filtrar_por() |