import argparse
from repositories.cadastroJson import CadastroJson
from domain import Usuario, Colecao, Jogo, JogoCampanha, JogoCompetitivo, JogoCooperativo, gera_relatorio

cadastro = CadastroJson("arquivos.json")

def achar_usuario(usuarios, nome):
    for u in usuarios:
        if u == Usuario(nome):
            return u
    raise SystemExit(f"Usuário '{nome}' não existe.")

def achar_jogo(usuario, titulo):
    for colecao in usuario.colecoes.values():
        for jogo in colecao.jogos:
            if jogo.titulo.lower() == titulo.lower():
                return jogo
    raise SystemExit(f"Jogo '{titulo}' não encontrado.")

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
    if args.colecao not in usuario.colecoes:
        raise SystemExit(f"Coleção '{args.colecao}' não existe.")
 
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
 
    usuario.colecoes[args.colecao].jogos.append(jogo)
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
    jogo = achar_jogo(achar_usuario(usuarios, args.usuario), args.titulo)
    jogo.adiciona_horas(args.horas)  # método de Jogo
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}': {jogo.horas_jogadas}h jogadas.")

def finalizar(args):
    usuarios = cadastro.carregar()
    jogo = achar_jogo(achar_usuario(usuarios, args.usuario), args.titulo)
    jogo.finalizar_jogo(nota=args.nota)  # define data de término e status "Finalizado"
    cadastro.salvar(usuarios)
    print(f"'{jogo.titulo}' finalizado.")

def relatorio(args):
    usuario = achar_usuario(cadastro.carregar(), args.usuario)
    print(gera_relatorio(usuario))  

# Argparse

def main():
    parser = argparse.ArgumentParser(description="Catálogo de Jogos Digitais")
    sub = parser.add_subparsers(dest="comando", required=True)
 
    # Opção -u para os comandos que precisam de um usuário
    com_usuario = argparse.ArgumentParser(add_help=False) # Precisa desse add_help para não dar conflito com o parser 
    com_usuario.add_argument("-u", "--usuario", required=True, help="nome do usuário")
 
    p_criar_usuario = sub.add_parser("criar-usuario", help="cria um usuário")
    p_criar_usuario.add_argument("nome")
    p_criar_usuario.set_defaults(func=criar_usuario)
 
    p_criar_colecao = sub.add_parser("criar-colecao", parents=[com_usuario], help="cria uma coleção")
    p_criar_colecao.add_argument("nome")
    p_criar_colecao.set_defaults(func=criar_colecao)
 
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
 
    p_horas = sub.add_parser("horas", parents=[com_usuario], help="soma horas jogadas")
    p_horas.add_argument("titulo")
    p_horas.add_argument("horas", type=float)
    p_horas.set_defaults(func=horas)
 
    p_finalizar = sub.add_parser("finalizar", parents=[com_usuario], help="finaliza um jogo")
    p_finalizar.add_argument("titulo")
    p_finalizar.add_argument("--nota", type=float)
    p_finalizar.set_defaults(func=finalizar)
 
    p_relatorio = sub.add_parser("relatorio", parents=[com_usuario], help="relatório geral")
    p_relatorio.set_defaults(func=relatorio)
 
    args = parser.parse_args()
    args.func(args)

main()