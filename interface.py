from src.controller.aluguel_controller import AluguelController
from src.controller.brinquedo_controller import BrinquedoController
from src.controller.cliente_controller import ClienteController
from src.controller.equipe_controller import EquipeController
from src.controller.pessoa_controller import PessoaController
from src.controller.pessoa_equipe_controller import PessoaEquipeController
from src.pages.cliente_page import cliente_page
from src.pages.aluguel_page import aluguel_page
from src.pages.colaborador_page import colaborador_login_page
from colorama import Fore, Back, Style

# variaveis
logado = None
BRINQUEDO_CABECALHO = ["id", "nome", "descrição",
                       "largura", "altura", "comprimento"]
PESSOA_CABECALHO = ["id", "nome", "cpf", "telefone"]
PESSOA_EQUIPE_CABECALHO = ["id", "pessoa_id", "equipe_id"]
EQUIPE_CABECALHO = ["id", "nome", "descrição"]


def red_text(msg):
    return Fore.RED + msg + Style.RESET_ALL


def green_text(msg):
    return Fore.GREEN + msg + Style.RESET_ALL


def blue_text(msg):
    return Fore.BLUE + msg + Style.RESET_ALL


def bright_text(msg):
    return Style.BRIGHT + msg + Style.RESET_ALL


def back_white(msg):
    return Back.WHITE + msg + Style.RESET_ALL


def print_error(msg):
    print(red_text("ERRO") + ": " + str(msg) + "\n")


def print_sucesso(msg):
    print(green_text("SUCESSO") + ": " + str(msg) + "\n")


def print_menu(num, msg):
    print(green_text(num) + " - " + msg)


def titulo(msg: str):
    dece = "---: "
    decd = " :---"
    msg = dece + msg.upper() + decd
    print("\n" + bright_text(back_white(green_text(msg))))


def insira_texto(msg):
    return green_text("Insira ") + msg + ": "


def confirm():
    return input("Confirmar? (s/n): ").lower() == "s"


def try_catch_error(msg, func, *args):
    try:
        result = func(*args)
        print_sucesso(msg) if msg else None
        return result
    except Exception as e:
        print_error(e)

    return None


def float_input(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print_error("Digite um número flutuante.")


def int_input(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print_error("Digite um número inteiro.")


def login_menu():
    print_menu("1", "Login")
    print_menu("2", "Cadastrar")
    print_menu("0", "Sair")
    return int_input("Escolha uma opção: ")


def initial_page():
    global logado
    while True:
        titulo("PINHO FESTAS")

        opcao = login_menu()
        if opcao == 1:
            logado = login_form()
            if logado:
                if PessoaController.verify_admin(logado[2]):
                    admin_page()
                else:
                    colaborador_login_page(logado)
                    logado = None
        elif opcao == 2:
            cadastro_pessoa_form()
        elif opcao == 0:
            break
        else:
            print(red_text("ERRO") + ": Opção inválida.")


def admin_menu():
    print_menu("1", "Administrar brinquedos")
    print_menu("2", "Administrar colaboradores")
    print_menu("3", "Administrar equipes")
    print_menu("4", "Administrar clientes")
    print_menu("5", "Administrar aluguéis")
    print_menu("0", "Sair")
    return int_input("Escolha uma opção:")


def brinquedo_menu():
    print_menu("1", "Cadastrar brinquedo")
    print_menu("2", "Listar brinquedos")
    print_menu("3", "Editar brinquedo")
    print_menu("4", "Remover brinquedo")
    print_menu("5", "Voltar")


def brinquedo_page():
    while True:
        titulo("administração de brinquedos")
        brinquedo_menu()
        opcao = int_input("Escolha uma opção: ")
        if opcao == 1:
            cadastro_brinquedo_form()
        elif opcao == 2:
            listar_brinquedos()
        elif opcao == 3:
            editar_brinquedo_form()
        elif opcao == 4:
            remover_brinquedo_form()
        elif opcao == 5:
            break
        else:
            print_error("Opção inválida.")


def editar_brinquedo_form():
    id = int_input(insira_texto("id do brinquedo"))
    brinquedo = try_catch_error(None, BrinquedoController.get_by_id, id)
    if not brinquedo:
        return
    print_tabela(BRINQUEDO_CABECALHO, [brinquedo])

    nome = input(insira_texto("nome")) if input(
        "Deseja alterar o nome? (s/n): ") == "s" else brinquedo[1]
    descricao = input(insira_texto("descrição")) if input(
        "Deseja alterar a descrição? (s/n): ") == "s" else brinquedo[2]
    largura = float_input(insira_texto("largura")) if input(
        "Deseja alterar a largura? (s/n): ") == "s" else brinquedo[3]
    altura = float_input(insira_texto("altura")) if input(
        "Deseja alterar a altura? (s/n): ") == "s" else brinquedo[4]
    comprimento = float_input(insira_texto("comprimento")) if input(
        "Deseja alterar o comprimento? (s/n): ") == "s" else brinquedo[5]

    try_catch_error("Brinquedo editado com sucesso.", BrinquedoController.update,
                    id, nome, descricao, largura, altura, comprimento)


def remover_brinquedo_form():
    id = int_input(insira_texto("id do brinquedo"))
    brinquedo = try_catch_error(None, BrinquedoController.get_by_id, id)
    if brinquedo:
        print(red_text("ATENÇÃO") + ": Você está prestes a remover o brinquedo " +
              brinquedo[1] + " - " + brinquedo[2] + " !")
        try_catch_error("Brinquedo removido com sucesso.", BrinquedoController.delete,
                        id) if confirm() else print(green_text("Operação cancelada."))


def cadastro_brinquedo_form():
    titulo("Cadastro de brinquedo")

    nome = input(insira_texto("nome"))
    descricao = input(insira_texto("descrição"))
    largura = float_input(insira_texto("largura"))
    altura = float_input(insira_texto("altura"))
    comprimento = float_input(insira_texto("comprimento"))

    try_catch_error("Brinquedo cadastrado com sucesso!",
                    BrinquedoController.insert, nome, descricao, largura, altura, comprimento)


def listar_brinquedos():
    titulo("Lista de brinquedos")
    brinquedos = BrinquedoController.get_all()
    print_tabela(BRINQUEDO_CABECALHO, brinquedos) if brinquedos else print_error(
        "Nenhum brinquedo cadastrado.")


def colaborador_menu():
    print_menu("1", "Listar colaboradores")
    print_menu("2", "Inserir colaborador na equipe")
    print_menu("3", "Remover colaborador da equipe")
    print_menu("4", "Voltar")


def colaborador_page():
    while True:
        titulo("administração de colaboradores")
        colaborador_menu()
        opcao = int_input("Escolha uma opção: ")
        if opcao == 1:
            listar_colaboradores()
        elif opcao == 2:
            inserir_colaborador_equipe_form()
        elif opcao == 3:
            remover_colaborador_equipe_form()
        elif opcao == 4:
            break
        else:
            print_error("Opção inválida.")


def listar_colaboradores():
    colaboradores = PessoaController.get_all()
    print_tabela(PESSOA_CABECALHO, colaboradores) if colaboradores else print_error(
        "Nenhum colaborador cadastrado.")


def inserir_colaborador_equipe_form():
    id_colaborador = int_input(insira_texto("id do colaborador"))

    colaborador = try_catch_error(
        None, PessoaController.get_by_id, id_colaborador)
    if not colaborador:
        return
    elif PessoaController.verify_admin(colaborador[2]):
        print_error("Não é possível inserir administradores em equipes.")
        return

    id_equipe = int_input(insira_texto("id da equipe"))
    try_catch_error("Colaborador inserido na equipe com sucesso!",
                    PessoaEquipeController.insert, id_colaborador, id_equipe)


def remover_colaborador_equipe_form():
    id_colaborador = int_input(insira_texto("id do colaborador"))
    try_catch_error("Colaborador removido da equipe com sucesso!",
                    PessoaEquipeController.delete_with_pessoa_id, id_colaborador)


def equipe_menu():
    print_menu("1", "Listar equipes")
    print_menu("2", "Inserir equipe")
    print_menu("3", "Remover equipe")
    print_menu("4", "Colaboradores da equipe")
    print_menu("5", "Voltar")


def equipe_page():
    while True:
        titulo("administração de equipes")
        equipe_menu()
        opcao = int_input("Escolha uma opção: ")
        if opcao == 1:
            listar_equipes()
        elif opcao == 2:
            inserir_equipe_form()
        elif opcao == 3:
            remover_equipe_form()
        elif opcao == 4:
            listar_colaboradores_equipe_form()
        elif opcao == 5:
            break
        else:
            print_error("Opção inválida.")


def listar_equipes():
    equipes = EquipeController.get_all()
    print_tabela(EQUIPE_CABECALHO, equipes) if equipes else print_error(
        "Nenhuma equipe cadastrada.")


def inserir_equipe_form():
    nome = input(insira_texto("nome"))
    descricao = input(insira_texto("descrição"))
    try_catch_error("Equipe cadastrada com sucesso!",
                    EquipeController.insert, nome, descricao)


def remover_equipe_form():
    id = int_input(insira_texto("id da equipe"))
    equipe = try_catch_error(None, EquipeController.get_by_id, id)
    if equipe:
        print(red_text("ATENÇÃO") + ": Você está prestes a remover a equipe " +
              equipe[1] + " - " + equipe[2] + " !")
        try_catch_error("Equipe removida com sucesso!", EquipeController.delete,
                        id) if confirm() else print(green_text("Operação cancelada."))


def listar_colaboradores_equipe_form():
    id_equipe = int_input(insira_texto("id da equipe"))
    lista_ids = try_catch_error(
        None, PessoaEquipeController.get_pessoa_ids_from_equipe, id_equipe)
    if not lista_ids:
        return
    lista_colaboredores = []
    for id in lista_ids:
        lista_colaboredores.append(try_catch_error(
            None, PessoaController.get_by_id_clean, id))
    print_tabela(PESSOA_CABECALHO, lista_colaboredores) if lista_colaboredores else print_error(
        "Nenhum colaborador cadastrado nessa equipe.")


def admin_page():
    global logado
    print(green_text("Bem vindo administrador " + logado[1] + " !"))
    while True:
        titulo("administração")
        opcao = admin_menu()
        if opcao == 1:
            brinquedo_page()
        elif opcao == 2:
            colaborador_page()
        elif opcao == 3:
            equipe_page()
        elif opcao == 4:
            cliente_page()
        elif opcao == 5:
            aluguel_page()
        elif opcao == 0:
            logado = None
            break
        else:
            print_error("Opção inválida.")


def print_tabela(nomes, conteudos):
    espacos_colunas = [0] * len(nomes)
    offset = 5

    for conteudo in conteudos:
        for i in range(len(conteudo)):
            if len(str(conteudo[i])) + offset > espacos_colunas[i]:
                espacos_colunas[i] = len(str(conteudo[i])) + offset
            if len(nomes[i]) + offset > espacos_colunas[i]:
                espacos_colunas[i] = len(nomes[i]) + offset

    cabeçalho = ""
    for i in range(len(nomes)):
        cabeçalho += nomes[i].ljust(espacos_colunas[i])
    print(blue_text(cabeçalho))

    for conteudo in conteudos:
        linha = ""
        for i in range(len(conteudo)):
            linha += str(conteudo[i]).ljust(espacos_colunas[i])
        print(linha)


def user_page():
    pass


def cadastro_pessoa_form():
    titulo("Cadastro de conta")

    nome = input(insira_texto("nome"))
    cpf = input(insira_texto("CPF"))
    telefone = input(insira_texto("telefone"))
    senha = input(insira_texto("senha"))

    try_catch_error("Conta cadastrada com sucesso!",
                    PessoaController.insert, nome, cpf, telefone, senha)

def login_form():
    titulo("login")

    cpf = input(insira_texto("CPF"))
    senha = input(insira_texto("senha"))

    return try_catch_error("Login realizado com sucesso!",
                           PessoaController.login, cpf, senha)


def main():
    initial_page()


if __name__ == "__main__":
    main()
