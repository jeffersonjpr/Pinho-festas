from src.database.pessoa_equipe_database import PessoaEquipeDatabase
from src.database.aluguel_database import AluguelDatabase
from src.database.brinquedo_database import BrinquedoDatabase
from src.database.equipe_database import EquipeDatabase
import datetime
import time


class AluguelController:
    @staticmethod
    def insert(brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        data_montagem, data_desmontagem = AluguelController.__correct_dates(
            data_montagem, data_desmontagem)
        AluguelController.__equipe_exists(equipe_montagem_id)
        AluguelController.__equipe_exists(equipe_desmontagem_id)
        AluguelController.__brinquedo_exists(brinquedo_id)
        AluguelController.__verify_equipe_available(
            equipe_montagem_id, data_montagem)
        AluguelController.__verify_equipe_available(
            equipe_desmontagem_id, data_desmontagem)
        AluguelController.__verify_brinquedo_available(
            brinquedo_id, data_montagem, data_desmontagem)

        AluguelDatabase.insert(brinquedo_id, data_montagem,
                               data_desmontagem, equipe_montagem_id, equipe_desmontagem_id)

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

    staticmethod

    def __verify_equipe_available(equipe_id, data_fim):
        #data - 30 minutos
        data_inicio = data_fim - 1800
        data_converted = datetime.datetime.fromtimestamp(data_fim)
        if AluguelDatabase.get_by_equipe_and_data_montagem(equipe_id, data_inicio, data_fim) or AluguelDatabase.get_by_equipe_data_desmontagem(equipe_id,  data_inicio, data_fim):
            raise Exception(
                f"Equipe {equipe_id} não disponível em {data_converted}")

    def __verify_brinquedo_available(brinquedo_id, data_montagem, data_desmontagem):
        #data_montagem - 5 min
        data_montagem_inicio = data_montagem - 300
        #data_desmontagem + 5 min
        data_desmontagem_fim = data_desmontagem + 300

        if AluguelDatabase.get_by_brinquedo_datas(brinquedo_id, data_montagem_inicio, data_desmontagem_fim):
            data_montagem_converted = datetime.datetime.fromtimestamp(
                data_montagem)
            data_desmontagem_converted = datetime.datetime.fromtimestamp(
                data_desmontagem)
            raise Exception(
                f"Brinquedo {brinquedo_id} não disponível entre {data_montagem_converted} e {data_desmontagem_converted}")

    @staticmethod
    def delete(id):
        AluguelController.__aluguel_exists(id)

        AluguelDatabase.delete(id)
        print("Aluguel deletado com sucesso")

    @staticmethod
    def update(id, brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        AluguelController.__aluguel_exists(id)

        AluguelDatabase.update(id, brinquedo_id, data_montagem,
                               data_desmontagem, equipe_montagem_id, equipe_desmontagem_id)
        print("Aluguel atualizado com sucesso")

    @staticmethod
    def __aluguel_exists(id):
        if not AluguelDatabase.get_by_id(id):
            raise Exception("Aluguel não encontrado")

    @staticmethod
    def get_all():
        alugueis = AluguelDatabase.get_all()
        for aluguel in alugueis:
            aluguel_temp = list(aluguel)
            data_montagem = datetime.datetime.fromtimestamp(aluguel_temp[2])
            data_desmontagem = datetime.datetime.fromtimestamp(aluguel_temp[3])
            aluguel_temp[2] = data_montagem
            aluguel_temp[3] = data_desmontagem
            aluguel = tuple(aluguel_temp)
        
        return alugueis

    @staticmethod
    def get_by_id(id):
        AluguelController.__aluguel_exists(id)
        return AluguelDatabase.get_by_id(id)

    @staticmethod
    def __brinquedo_exists(id):
        if not BrinquedoDatabase.get_by_id(id):
            raise Exception("Brinquedo não encontrado")

    @staticmethod
    def __equipe_exists(id):
        if not EquipeDatabase.get_by_id(id):
            raise Exception("Equipe não encontrada")
        if not PessoaEquipeDatabase.get_by_equipe_id(id):
            raise Exception("Equipe sem pessoas")
