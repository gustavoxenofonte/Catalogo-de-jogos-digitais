#  Catálogo de jogos digitais

## Descrição do projeto

- Projeto desenvolvido para a disciplina de Programação Orientada a Objetos (POO)

- O sistema consiste no desenvolvimento de um catálogo pessoal de jogos digitais que permite:
    - Cadastro de jogos
    - Registro de progresso de jogatina
    - Organização por plataforma ou gênero
    - Geração de relatórios de desempenho e tempo jogado

## Objetivo do projeto

- Aplicar conceitos de POO para aprendizado

## Estrutura planejada de classes

| Classe | Atributos | Métodos |
|:-------| :----------:| :--------: |
| Jogo | titulo, genero, plataforma, horas_jogadas, status, nota, data_inicio, data_fim, ano_lancamento | registrar_progresso(), finalizar_jogo(), reiniciar_jogo(), avaliar() |
| JogoCampanha | missoes_totais, missoes_concluidas, percentual_conclusao | atualizar_progresso() |
| JogoCompetitivo |  partidas_jogadas, vitorias, derrotas, ranking, winrate | registrar_partida(), calcular_winrate() |
| JogoCooperativo | jogadores_max, num_sessoes, participantes_freq | atualizar_info() |
| Colecao | nome_colecao, jogos | adicionar_jogo, remover_jogo(), filtrar_por(), ordenar_por() |
| Usuario | nome, colecoes | criar_colecao, remover_colecao |
| Relatorio | total_horas, media_nota_jogos, percentual_status, top_5_jogados | gerar_relatorio()|

## UML Textual

- Para melhor organização do README, O UML se encontra no arquivo `UML.md`
    - [Clique aqui para acessá-lo](UML.md)