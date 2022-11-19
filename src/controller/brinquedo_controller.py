import datetime

from src.database.aluguel_database import AluguelDatabase
from src.database.brinquedo_database import BrinquedoDatabase


class BrinquedoController:
    @staticmethod
    def insert(nome, descricao, largura, altura, comprimento):
        return BrinquedoDatabase.insert(nome, descricao, largura, altura, comprimento)

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
        # data_montagem - 15 min
        data_montagem = data_montagem - 900
        # data_desmontagem + 15 min
        data_desmontagem = data_desmontagem + 900

        lista_alugueis = AluguelDatabase.get_by_brinquedo_id(brinquedo_id)
        indice_montagem = 2
        indice_desmontagem = 3

        for aluguel in lista_alugueis:
            if data_desmontagem >= aluguel[indice_montagem] and data_montagem <= aluguel[indice_desmontagem]:
                raise Exception(
                    f"Brinquedo {brinquedo_id} não disponível em {datetime.datetime.fromtimestamp(data_montagem)}")
