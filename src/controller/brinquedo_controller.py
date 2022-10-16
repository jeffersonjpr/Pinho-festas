from src.database.brinquedo_database import BrinquedoDatabase

class BrinquedoController:
    @staticmethod
    def insert(nome, descricao, largura, altura, comprimento):
        BrinquedoDatabase.insert(nome, descricao, largura, altura, comprimento)
        # print("Brinquedo cadastrado com sucesso")

    @staticmethod
    def delete(id):
        BrinquedoController.__brinquedo_exists(id)

        BrinquedoDatabase.delete(id)
        # print("Brinquedo deletado com sucesso")

    @staticmethod
    def update(id, nome, descricao, largura, altura, comprimento):
        BrinquedoController.__brinquedo_exists(id)

        BrinquedoDatabase.update(id, nome, descricao, largura, altura, comprimento)
        # print("Brinquedo atualizado com sucesso")

    @staticmethod
    def __brinquedo_exists(id):
        if not BrinquedoDatabase.get_by_id(id):
            raise Exception("Brinquedo não encontrado")

    @staticmethod
    def get_all():
        return BrinquedoDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        BrinquedoController.__brinquedo_exists(id)
        return BrinquedoDatabase.get_by_id(id)