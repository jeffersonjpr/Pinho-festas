import datetime
import time

from src.controller.brinquedo_controller import BrinquedoController
from src.controller.equipe_controller import EquipeController
from src.database.aluguel_database import AluguelDatabase
from src.database.brinquedo_database import BrinquedoDatabase
from src.database.equipe_database import EquipeDatabase
from src.database.pessoa_equipe_database import PessoaEquipeDatabase
from src.controller.cliente_controller import ClienteController

class AluguelController:
    @staticmethod
    def insert(brinquedo_id, data_montagem, data_desmontagem, id_montagem, id_desmontagem, id_cliente):
        data_montagem, data_desmontagem = AluguelController.__correct_dates(
            data_montagem, data_desmontagem)
        EquipeController.is_equipe_ready(id_montagem)
        EquipeController.is_equipe_ready(id_desmontagem)
        EquipeController.is_equipe_available(id_montagem, data_montagem)
        EquipeController.is_equipe_available(id_desmontagem, data_desmontagem)
        BrinquedoController.does_brinquedo_exists(brinquedo_id)
        BrinquedoController.is_brinquedo_available(
            brinquedo_id, data_montagem, data_desmontagem)
        ClienteController.get_by_id(id_cliente)
        
        return AluguelDatabase.insert(brinquedo_id, data_montagem,
                                      data_desmontagem, id_montagem, id_desmontagem, id_cliente)

    @staticmethod
    def __correct_dates(data_montagem, data_desmontagem):
        data_montagem = datetime.datetime.strptime(
            data_montagem, "%d/%m/%Y %H:%M")
        data_desmontagem = datetime.datetime.strptime(
            data_desmontagem, "%d/%m/%Y %H:%M")
        data_montagem = int(time.mktime(data_montagem.timetuple()))
        data_desmontagem = int(time.mktime(data_desmontagem.timetuple()))

        if data_montagem > data_desmontagem:
            raise Exception("Data de montagem maior que data de desmontagem")

        return data_montagem, data_desmontagem

    @staticmethod
    def is_equipe_available_in_this_date(equipe_id, data_fim):
        # data - 30 minutos
        data_inicio = data_fim - 1800
        data_converted = datetime.datetime.fromtimestamp(data_fim)
        if AluguelDatabase.get_by_equipe_and_data_montagem(equipe_id, data_inicio, data_fim) or AluguelDatabase.get_by_equipe_data_desmontagem(equipe_id,  data_inicio, data_fim):
            raise Exception(
                f"Equipe {equipe_id} n??o dispon??vel em {data_converted}")

    @staticmethod
    def delete(id):
        AluguelController.__aluguel_exists(id)

        AluguelDatabase.delete(id)
        print("Aluguel deletado com sucesso")

    # @staticmethod
    # def update(id, brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
    #     AluguelController.__aluguel_exists(id)

    #     AluguelDatabase.update(id, brinquedo_id, data_montagem,
    #                            data_desmontagem, equipe_montagem_id, equipe_desmontagem_id)
    #     print("Aluguel atualizado com sucesso")

    @staticmethod
    def __aluguel_exists(id):
        if not AluguelDatabase.get_by_id(id):
            raise Exception("Aluguel n??o encontrado")

    @staticmethod
    def get_all():
        alugueis = AluguelDatabase.get_all()
        AluguelController.format_alugueis(alugueis)
        return alugueis

    @staticmethod
    def format_alugueis(alugueis):
        for i in range(len(alugueis)):
            aluguel_temp = list(alugueis[i])
            data_montagem = datetime.datetime.fromtimestamp(aluguel_temp[2])
            data_desmontagem = datetime.datetime.fromtimestamp(aluguel_temp[3])
            aluguel_temp[2] = data_montagem
            aluguel_temp[3] = data_desmontagem
            aluguel_temp[4] = EquipeDatabase.get_by_id(aluguel_temp[4])[1]
            aluguel_temp[5] = EquipeDatabase.get_by_id(aluguel_temp[5])[1]
            alugueis[i] = tuple(aluguel_temp)

    @staticmethod
    def get_by_equipe_montagem_id(id):
        alugueis = AluguelDatabase.get_by_equipe_montagem_id(id)
        if not alugueis:
            raise Exception("N??o foram encontrados montagens para essa equipe.")
        AluguelController.format_alugueis(alugueis)
        return alugueis

    @staticmethod
    def get_by_equipe_desmontagem_id(id):
        alugueis = AluguelDatabase.get_by_equipe_desmontagem_id(id)
        if not alugueis:
            raise Exception("N??o foram encontrados desmontagens para essa equipe.")
        AluguelController.format_alugueis(alugueis)
        return alugueis

    @staticmethod
    def get_by_id(id):
        AluguelController.__aluguel_exists(id)
        return AluguelDatabase.get_by_id(id)
