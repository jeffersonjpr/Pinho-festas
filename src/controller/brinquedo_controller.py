from src.database.brinquedo_database import BrinquedoDatabase
import datetime
from src.database.aluguel_database import AluguelDatabase


class BrinquedoController:
    @staticmethod
    def insert(nome, descricao, largura, altura, comprimento):
        BrinquedoDatabase.insert(nome, descricao, largura, altura, comprimento)
        # print("Brinquedo cadastrado com sucesso")

    @staticmethod
    def delete(id):
        BrinquedoController.does_brinquedo_exists(id)

        BrinquedoDatabase.delete(id)
        # print("Brinquedo deletado com sucesso")

    @staticmethod
    def update(id, nome, descricao, largura, altura, comprimento):
        BrinquedoController.does_brinquedo_exists(id)

        BrinquedoDatabase.update(
            id, nome, descricao, largura, altura, comprimento)
        # print("Brinquedo atualizado com sucesso")

    @staticmethod
    def does_brinquedo_exists(id):
        if not BrinquedoDatabase.get_by_id(id):
            raise Exception("Brinquedo não encontrado")

    @staticmethod
    def get_all():
        return BrinquedoDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        BrinquedoController.does_brinquedo_exists(id)
        return BrinquedoDatabase.get_by_id(id)

    def is_brinquedo_available(brinquedo_id, data_montagem, data_desmontagem):
        # data_montagem - 5 min
        data_montagem_inicio = data_montagem - 300
        # data_desmontagem + 5 min
        data_desmontagem_fim = data_desmontagem + 300

        if AluguelDatabase.get_by_brinquedo_datas(brinquedo_id, data_montagem_inicio, data_desmontagem_fim):
            data_montagem_converted = datetime.datetime.fromtimestamp(
                data_montagem)
            data_desmontagem_converted = datetime.datetime.fromtimestamp(
                data_desmontagem)
            raise Exception(
                f"Brinquedo {brinquedo_id} não disponível entre {data_montagem_converted} e {data_desmontagem_converted}")
