from src.pages.page_utils import PageUtils
from src.controller.cliente_controller import ClienteController
from src.controller.aluguel_controller import AluguelController
from src.controller.equipe_controller import EquipeController
from src.controller.pessoa_equipe_controller import PessoaEquipeController
from src.pages.cliente_page import listar_clientes

CLIENTE_CABECALHO = ["id", "nome", "cpf", "telefone", "email", "cep", "bairro", "cidade", "endereco"]
ALUGUEL_CABECALHO = ["id", "brinquedo", "data montagem",
                     "data desmontagem", "equipe m", "equipe d", "cliente"]

def colaborador_login_menu():
    PageUtils.print_menu("1", "Listar serviços")
    PageUtils.print_menu("2", "Listar clientes")
    PageUtils.print_menu("3", "Consultar cliente")
    PageUtils.print_menu("0", "Sair")
    return PageUtils.int_input("Escolha uma opção:")

def colaborador_login_page(logado):
    print(PageUtils.green_text("Bem vindo administrador " + logado[1] + " !"))
    while True:
        PageUtils.titulo("colaborador")
        opcao = colaborador_login_menu()
        if opcao == 1:
            listar_sericos(logado[0])
        elif opcao == 2:
            listar_clientes()
        elif opcao == 3:
            consultar_cliente()
        elif opcao == 0:
            break
        else:
            PageUtils.print_error("Opção inválida.")
            
def listar_sericos(id_colaborador):
    pessoaequipe = PageUtils.try_catch_error(None,PessoaEquipeController.get_by_pessoa_id, id_colaborador)
    if not pessoaequipe:
        return
    
    print(PageUtils.blue_text("Serviços de montagem:"))
    
    montagens = AluguelController.get_by_equipe_montagem_id(pessoaequipe[2])
    if not montagens:
        PageUtils.print_error("Você não tem montagens")
    else:
        PageUtils.print_tabela(ALUGUEL_CABECALHO, montagens)
        
    print(PageUtils.blue_text("\nServiços de desmontagem:"))
        
    desmontagens = AluguelController.get_by_equipe_desmontagem_id(pessoaequipe[2])
    if not desmontagens:
        PageUtils.print_error("Você não tem desmontagens")
    else:
        PageUtils.print_tabela(ALUGUEL_CABECALHO, desmontagens)
        
def consultar_cliente():
    id_cliente = PageUtils.int_input("Digite o id do cliente:")
    cliente = PageUtils.try_catch_error(None, ClienteController.get_by_id, id_cliente)
    if not cliente:
        return
    PageUtils.print_tabela(CLIENTE_CABECALHO, [cliente])