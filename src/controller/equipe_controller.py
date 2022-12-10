import datetime

from src.database.aluguel_database import AluguelDatabase
from src.database.equipe_database import EquipeDatabase
from src.database.pessoa_equipe_database import PessoaEquipeDatabase


class EquipeController:
    @staticmethod
    def insert(nome, descricao):
        return EquipeDatabase.insert(nome, descricao)

    @staticmethod
    def delete(id):
        EquipeController.equipe_exists(id)

        EquipeDatabase.delete(id)
        # print("Equipe deletada com sucesso")

    @staticmethod
    def update(id, nome, descricao):
        EquipeController.equipe_exists(id)

        EquipeDatabase.update(id, nome, descricao)
        # print("Equipe atualizada com sucesso")

    @staticmethod
    def get_all():
        return EquipeDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        EquipeController.equipe_exists(id)
        return EquipeDatabase.get_by_id(id)

    @staticmethod
    def equipe_exists(id):
        if not EquipeDatabase.get_by_id(id):
            raise Exception("Equipe não encontrada")

    @staticmethod
    def is_equipe_ready(id):
        if not EquipeDatabase.get_by_id(id):
            raise Exception("Equipe não encontrada")
        if not PessoaEquipeDatabase.get_by_equipe_id(id):
            raise Exception("Equipe sem pessoas")
        
    def is_equipe_available(equipe_id, data):
        # |~~~mont~~~|data|~~~desm~~~|
        data_inicio = data - 900
        data_fim = data + 900

        data_converted = datetime.datetime.fromtimestamp(data)

        if AluguelDatabase.get_by_equipe_and_data_montagem(equipe_id, data_inicio, data_fim):
            raise Exception(
                f"Equipe {equipe_id} não disponível em {data_converted}")

        if AluguelDatabase.get_by_equipe_data_desmontagem(equipe_id,  data_inicio, data_fim):
            raise Exception(
                f"Equipe {equipe_id} não disponível em {data_converted}")
