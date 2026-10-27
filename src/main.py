import argparse
from repositories.cadastroJson import CadastroJson
from config.config import carregar_settings
from domain import Usuario, Colecao, Jogo, JogoCampanha, JogoCompetitivo, JogoCooperativo, gera_relatorio, RegraDeNegocioError

cadastro = CadastroJson("arquivos.json")

def achar_usuario(usuarios, nome):
    for u in usuarios:
        if u == Usuario(nome):
            return u
    raise SystemExit(f"Usuário '{nome}' não existe.")

def avisar_meta(usuario):
    aviso = usuario.aviso_meta_anual(carregar_settings()["meta_anual_finalizados"])
    if aviso:
        print(aviso)

# Comandos

def criar_usuario(args):
    usuarios = cadastro.carregar()
    if Usuario(args.nome) in usuarios:
        raise SystemExit("Esse usuário já existe.")
    usuarios.append(Usuario(args.nome))
    cadastro.salvar(usuarios)
    print(f"Usuário '{args.nome}' criado.")

def criar_colecao(args):
    usuarios = cadastro.carregar()
    usuario = achar_usuario(usuarios, args.usuario)
    usuario.colecoes[args.nome] = Colecao(args.nome, [])  # coleção nova, sem jogos
    cadastro.salvar(usuarios)
    print(f"Coleção '{args.nome}' criada.")

def adicionar(args):
    usuarios = cadastro.carregar()
    usuario = achar_usuario(usuarios, args.usuario)
    # Dados comuns a todo tipo de jogo
    dados = dict(titulo=args.titulo, genero=args.genero, plataforma=args.plataforma, ano_lancamento=args.ano)

    # Cada tipo usa a sua classe
    if args.tipo == "campanha":
        jogo = JogoCampanha(missoes_totais=args.missoes_totais, **dados)
    elif args.tipo == "competitivo":
        jogo = JogoCompetitivo(**dados)
    elif args.tipo == "cooperativo":
        jogo = JogoCooperativo(jogadores_max=args.jogadores_max, **dados)
    else:
        jogo = Jogo(**dados)

    usuario.adicionar_jogo(args.colecao, jogo)
    cadastro.salvar(usuarios)
    print(f"'{args.titulo}' adicionado a '{args.colecao}'.")

def listar(args):
    usuario = achar_usuario(cadastro.carregar(), args.usuario)
    for colecao in usuario.colecoes.values():
        if args.colecao and colecao.nome_colecao != args.colecao:
            continue
        print(f"== {colecao.nome_colecao} ==")
        for jogo in colecao.jogos:
            print(f"- {jogo.titulo}\n{jogo.plataforma}\n{jogo.horas_jogadas}h\n{jogo.status}")

def horas(args):
    usuarios = cadastro.carregar()
    jogo = achar_usuario(usuarios, args.usuario).buscar_jogo(args.titulo, args.plataforma)
    jogo.adiciona_horas(args.horas)
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}': {jogo.horas_jogadas}h jogadas.")

def iniciar(args):
    usuarios = cadastro.carregar()
    usuario = achar_usuario(usuarios, args.usuario)
    limite = carregar_settings()["max_jogando_simultaneos"]
    jogo = usuario.iniciar_jogo(args.titulo, args.plataforma, limite)
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}' agora está Jogando.")

def finalizar(args):
    usuarios = cadastro.carregar()
    usuario = achar_usuario(usuarios, args.usuario)
    jogo = usuario.buscar_jogo(args.titulo, args.plataforma)
    jogo.finalizar_jogo(nota=args.nota)
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}' finalizado.")
    avisar_meta(usuario)

def avaliar(args):
    usuarios = cadastro.carregar()
    jogo = achar_usuario(usuarios, args.usuario).buscar_jogo(args.titulo, args.plataforma)
    jogo.nota = args.nota
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}' avaliado com nota {jogo.nota}.")

def relatorio(args):
    usuario = achar_usuario(cadastro.carregar(), args.usuario)
    print(gera_relatorio(usuario))
    avisar_meta(usuario)

# Argparse

def main():
    parser = argparse.ArgumentParser(description="Catálogo de Jogos Digitais")
    sub = parser.add_subparsers(dest="comando", required=True)

    # Opção -u para os comandos que precisam de um usuário
    com_usuario = argparse.ArgumentParser(add_help=False) # Precisa desse add_help para não dar conflito com o parser 
    com_usuario.add_argument("-u", "--usuario", required=True, help="nome do usuário")

    # Opção -p opcional para localizar um jogo (necessária quando o mesmo título existe em 2 plataformas)
    com_plataforma = argparse.ArgumentParser(add_help=False)
    com_plataforma.add_argument("-p", "--plataforma", help="plataforma do jogo")

    p_criar_usuario = sub.add_parser("criar-usuario", help="cria um usuário")
    p_criar_usuario.add_argument("nome")
    p_criar_usuario.set_defaults(func=criar_usuario)

    p_criar_colecao = sub.add_parser("criar-colecao", parents=[com_usuario], help="cria uma coleção")
    p_criar_colecao.add_argument("nome")
    p_criar_colecao.set_defaults(func=criar_colecao)

    # Não pede nota pois ela só pode ser atribuida depois do jogo finalizado
    p_adicionar = sub.add_parser("adicionar", parents=[com_usuario], help="adiciona um jogo")
    p_adicionar.add_argument("titulo")
    p_adicionar.add_argument("-c", "--colecao", required=True)
    p_adicionar.add_argument("-g", "--genero", required=True)
    p_adicionar.add_argument("-p", "--plataforma", required=True)
    p_adicionar.add_argument("-a", "--ano", type=int, required=True, help="ano de lançamento")
    p_adicionar.add_argument("-t", "--tipo", default="jogo",
                    choices=["jogo", "campanha", "competitivo", "cooperativo"])
    p_adicionar.add_argument("--missoes-totais", type=int, default=1, help="só para campanha")
    p_adicionar.add_argument("--jogadores-max", type=int, default=2, help="só para cooperativo")
    p_adicionar.set_defaults(func=adicionar)

    p_listar = sub.add_parser("listar", parents=[com_usuario], help="lista os jogos")
    p_listar.add_argument("-c", "--colecao", help="mostra só uma coleção")
    p_listar.set_defaults(func=listar)

    p_horas = sub.add_parser("horas", parents=[com_usuario, com_plataforma], help="soma horas jogadas")
    p_horas.add_argument("titulo")
    p_horas.add_argument("horas", type=float)
    p_horas.set_defaults(func=horas)

    p_finalizar = sub.add_parser("finalizar", parents=[com_usuario, com_plataforma], help="finaliza um jogo")
    p_finalizar.add_argument("titulo")
    p_finalizar.add_argument("--nota", type=float) # Agora sim pede nota, pois ela só pode ser atribuida depois do jogo finalizado
    p_finalizar.set_defaults(func=finalizar)

    p_iniciar = sub.add_parser("iniciar", parents=[com_usuario, com_plataforma], help="começa a jogar")
    p_iniciar.add_argument("titulo")
    p_iniciar.set_defaults(func=iniciar)

    p_avaliar = sub.add_parser("avaliar", parents=[com_usuario, com_plataforma], help="avalia um jogo finalizado")
    p_avaliar.add_argument("titulo")
    p_avaliar.add_argument("nota", type=float)
    p_avaliar.set_defaults(func=avaliar)

    p_relatorio = sub.add_parser("relatorio", parents=[com_usuario], help="relatório geral")
    p_relatorio.set_defaults(func=relatorio)

    args = parser.parse_args()
    try:
        args.func(args)
    except RegraDeNegocioError as erro:
        raise SystemExit(f"Erro: {erro}")

main()