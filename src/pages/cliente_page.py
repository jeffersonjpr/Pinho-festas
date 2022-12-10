from src.pages.page_utils import PageUtils
from src.controller.cliente_controller import ClienteController

CLIENTE_CABECALHO = ["id", "nome", "cpf", "telefone", "email", "cep", "bairro", "cidade", "endereco"]

def cliente_menu():
    PageUtils.print_menu("1", "Cadastrar cliente")
    PageUtils.print_menu("2", "Listar clientes")
    PageUtils.print_menu("3", "Atualizar cliente")
    PageUtils.print_menu("4", "Deletar cliente")
    PageUtils.print_menu("5", "Voltar")
    return PageUtils.int_input("Escolha uma opção:")


def cliente_page():
    while True:
        PageUtils.titulo("administração de clientes")
        opcao = cliente_menu()

        if opcao == 1:
            cliente_cadastro()
        elif opcao == 2:
            listar_clientes()
        elif opcao == 3:
            atualizar_cliente()
        elif opcao == 4:
            deletar_cliente()
        elif opcao == 5:
            break
        else:
            PageUtils.print_error("Opção inválida.")


def cliente_cadastro():
    nome = PageUtils.str_input(PageUtils.insira_texto("nome"))
    cpf = PageUtils.str_input(PageUtils.insira_texto("cpf"))
    telefone = PageUtils.str_input(PageUtils.insira_texto("telefone"))
    email = PageUtils.str_input(PageUtils.insira_texto("email"))
    cep = PageUtils.str_input(PageUtils.insira_texto("cep"))
    bairro = PageUtils.str_input(PageUtils.insira_texto("bairro"))
    cidade = PageUtils.str_input(PageUtils.insira_texto("cidade"))
    endereco = PageUtils.str_input(PageUtils.insira_texto("endereco"))

    PageUtils.try_catch_error("Cliente cadastrado com sucesso!",
                              ClienteController.insert, nome, cpf, telefone, email, cep, bairro, cidade, endereco)

def listar_clientes():
    clientes = PageUtils.try_catch_error("",ClienteController.get_all)
    if clientes:
        PageUtils.print_tabela(CLIENTE_CABECALHO, clientes)
        return
    PageUtils.print_error("Nenhum cliente cadastrado.")

def atualizar_cliente():
    id = PageUtils.int_input(PageUtils.insira_texto("id do cliente"))
    
    cliente = PageUtils.try_catch_error("",ClienteController.get_by_id, id)
    if not cliente:
        return
    
    PageUtils.print_tabela(CLIENTE_CABECALHO, [cliente])
    
    nome = PageUtils.str_input(PageUtils.insira_texto("nome")) if PageUtils.confirma_alteracao("o", "nome") else cliente[1]
    cpf = PageUtils.str_input(PageUtils.insira_texto("cpf")) if PageUtils.confirma_alteracao("o", "cpf") else cliente[2]
    telefone = PageUtils.str_input(PageUtils.insira_texto("telefone")) if PageUtils.confirma_alteracao("o", "telefone") else cliente[3]
    email = PageUtils.str_input(PageUtils.insira_texto("email")) if PageUtils.confirma_alteracao("o", "email") else cliente[4]
    cep = PageUtils.str_input(PageUtils.insira_texto("cep")) if PageUtils.confirma_alteracao("o", "cep") else cliente[5]
    bairro = PageUtils.str_input(PageUtils.insira_texto("bairro")) if PageUtils.confirma_alteracao("o", "bairro") else cliente[6]
    cidade = PageUtils.str_input(PageUtils.insira_texto("cidade")) if PageUtils.confirma_alteracao("o", "cidade") else cliente[6]
    endereco = PageUtils.str_input(PageUtils.insira_texto("endereco")) if PageUtils.confirma_alteracao("o", "endereco") else cliente[7]

    PageUtils.try_catch_error("Cliente atualizado com sucesso!",
                              ClienteController.update, id, nome, cpf, telefone, email, cep, bairro, cidade, endereco)
    
def deletar_cliente():
    id = PageUtils.int_input(PageUtils.insira_texto("id do cliente"))
    
    cliente = PageUtils.try_catch_error("",ClienteController.get_by_id, id)
    if not cliente:
        return
    print(PageUtils.red_text("ATENÇÃO") + ": Você está prestes a remover o cliente " +
              cliente[1] + " - " + cliente[2] + " !")
    
    PageUtils.try_catch_error("Cliente deletado com sucesso!",
                              ClienteController.delete, id) if PageUtils.confirm() else print(PageUtils.green_text("Operação cancelada."))