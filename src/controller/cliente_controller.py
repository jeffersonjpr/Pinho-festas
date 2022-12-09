from src.database.cliente_database import ClienteDatabase


class ClienteController:

    @staticmethod
    def insert(nome, cpf, telefone, email, cep, bairro, cidade, endereco):
        if ClienteDatabase.get_by_cpf(cpf):
            raise Exception("CPF já cadastrado")

        return ClienteDatabase.insert(nome, cpf, telefone, email, cep, bairro, cidade, endereco)

    @staticmethod
    def delete(id):
        ClienteController.__cliente_exists(id)

        ClienteDatabase.delete(id)

    @staticmethod
    def update(id, nome, cpf, telefone, email, cep, bairro, cidade, endereco):
        ClienteController.__cliente_exists(id)

        ClienteDatabase.update(id, nome, cpf, telefone, email, cep, bairro, cidade, endereco)

    @staticmethod
    def __cliente_exists(id):
        if not ClienteDatabase.get_by_id(id):
            raise Exception("Cliente não encontrado")

    @staticmethod
    def get_all():
        return ClienteDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        ClienteController.__cliente_exists(id)
        return ClienteDatabase.get_by_id(id)
