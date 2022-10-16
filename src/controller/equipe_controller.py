from src.database.equipe_database import EquipeDatabase


class EquipeController:
    @staticmethod
    def insert(nome, descricao):
        EquipeDatabase.insert(nome, descricao)
        print("Equipe cadastrada com sucesso")

    @staticmethod
    def delete(id):
        EquipeController.__equipe_exists(id)

        EquipeDatabase.delete(id)
        print("Equipe deletada com sucesso")

    @staticmethod
    def update(id, nome, descricao):
        EquipeController.__equipe_exists(id)

        EquipeDatabase.update(id, nome, descricao)
        print("Equipe atualizada com sucesso")

    @staticmethod
    def __equipe_exists(id):
        if not EquipeDatabase.get_by_id(id):
            raise Exception("Equipe não encontrada")

    @staticmethod
    def get_all():
        return EquipeDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        EquipeController.__equipe_exists(id)
        return EquipeDatabase.get_by_id(id)
