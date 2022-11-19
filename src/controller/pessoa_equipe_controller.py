from src.controller.equipe_controller import EquipeController
from src.controller.pessoa_controller import PessoaController
from src.database.pessoa_equipe_database import PessoaEquipeDatabase


class PessoaEquipeController:
    @staticmethod
    def insert(pessoa_id, equipe_id):
        PessoaEquipeController.__pessoa_exists(pessoa_id)
        PessoaEquipeController.__equipe_exists(equipe_id)

        if PessoaEquipeDatabase.get_by_pessoa_id(pessoa_id):
            raise Exception("Pessoa já está em uma equipe")

        PessoaEquipeDatabase.insert(pessoa_id, equipe_id)
        # print("Pessoa adicionada a equipe com sucesso")

    @staticmethod
    def delete(id):
        PessoaEquipeController.__pessoa_equipe_exists(id)

        PessoaEquipeDatabase.delete(id)
        # print("Pessoa removida da equipe com sucesso")

    @staticmethod
    def __pessoa_equipe_exists(id):
        if not PessoaEquipeDatabase.get_by_id(id):
            raise Exception("Pessoa não encontrada na equipe")

    @staticmethod
    def get_all():
        return PessoaEquipeDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        PessoaEquipeController.__pessoa_equipe_exists(id)
        return PessoaEquipeDatabase.get_by_id(id)

    @staticmethod
    def __pessoa_exists(id):
        if not PessoaController.get_by_id(id):
            raise Exception("Pessoa não encontrada")

    @staticmethod
    def __equipe_exists(id):
        if not EquipeController.get_by_id(id):
            raise Exception("Equipe não encontrada")

    @staticmethod
    def get_by_pessoa_id(pessoa_id):
        PessoaEquipeController.__pessoa_exists(pessoa_id)
        return PessoaEquipeDatabase.get_by_pessoa_id(pessoa_id)

    @staticmethod
    def get_by_equipe_id(equipe_id):
        PessoaEquipeController.__equipe_exists(equipe_id)
        return PessoaEquipeDatabase.get_by_equipe_id(equipe_id)
