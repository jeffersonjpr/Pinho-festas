from src.pages.page_utils import PageUtils
from src.controller.aluguel_controller import AluguelController
from src.controller.brinquedo_controller import BrinquedoController
from src.controller.equipe_controller import EquipeController
from src.controller.brinquedo_controller import BrinquedoController
from src.controller.cliente_controller import ClienteController
import datetime

ALUGUEL_CABECALHO = ["id", "brinquedo", "data montagem",
                     "data desmontagem", "equipe m", "equipe d", "cliente"]


def aluguel_menu():
    PageUtils.print_menu("1", "Cadastrar aluguel")
    PageUtils.print_menu("2", "Listar alugueis")
    PageUtils.print_menu("3", "Deletar aluguel")
    PageUtils.print_menu("4", "Voltar")
    return PageUtils.int_input("Escolha uma opção:")


def aluguel_page():
    while True:
        PageUtils.titulo("administração de alugueis")
        option = aluguel_menu()
        if option == 1:
            aluguel_cadastro()
        elif option == 2:
            aluguel_listagem()
        elif option == 3:
            aluguel_deletar()
        elif option == 4:
            break
        else:
            PageUtils.print_error("Opção inválida.")


def verify_date(date):
    try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")
        return date
    except:
        raise Exception("Data inválida")


def aluguel_cadastro():
    brinquedo_id = PageUtils.int_input("Digite o id do brinquedo:")
    if PageUtils.try_catch_error("", BrinquedoController.get_by_id, brinquedo_id) == None:
        return
    data_montagem = PageUtils.str_input(
        "Digite a data de montagem (dd/mm/aaaa hh:mm):")
    if PageUtils.try_catch_error("", verify_date, data_montagem) == None:
        return
    data_desmontagem = PageUtils.str_input(
        "Digite a data de desmontagem (dd/mm/aaaa hh:mm):")
    if PageUtils.try_catch_error("", verify_date, data_desmontagem) == None:
        return
    id_equipe_montagem = PageUtils.int_input(
        "Digite o id da equipe de montagem:")
    if PageUtils.try_catch_error("", EquipeController.get_by_id, id_equipe_montagem) == None:
        return
    id_equipe_desmontagem = PageUtils.int_input(
        "Digite o id da equipe de desmontagem:")
    if PageUtils.try_catch_error("", EquipeController.get_by_id, id_equipe_desmontagem) == None:
        return
    id_cliente = PageUtils.int_input("Digite o id do cliente:")
    if PageUtils.try_catch_error("", ClienteController.get_by_id, id_cliente) == None:
        return

    PageUtils.try_catch_error("Aluguel cadastrado com sucesso.", AluguelController.insert, brinquedo_id,
                              data_montagem, data_desmontagem, id_equipe_montagem, id_equipe_desmontagem, id_cliente)


def aluguel_listagem():
    alugueis = PageUtils.try_catch_error("", AluguelController.get_all)
    if alugueis:
        PageUtils.print_tabela(ALUGUEL_CABECALHO, alugueis)
        return
    PageUtils.print_error("Nenhum aluguel cadastrado.")


def aluguel_deletar():
    aluguel_id = PageUtils.int_input("Digite o id do aluguel:")
    aluguel = PageUtils.try_catch_error(
        "", AluguelController.get_by_id, aluguel_id)
    if aluguel:
        PageUtils.print_tabela(ALUGUEL_CABECALHO, [aluguel])
        print(PageUtils.red_text("ATENÇÃO") +
              ": Você está prestes a remover o aluguel acima.")
        PageUtils.try_catch_error("Aluguel deletado com sucesso.", AluguelController.delete,
                                  aluguel_id) if PageUtils.confirm() else print(PageUtils.green_text("Operação cancelada."))
