from src.database.pessoa_database import PessoaDatabase
from src.database.pessoa_equipe_database import PessoaEquipeDatabase


class PessoaController:
    @staticmethod
    def insert(nome, cpf, telefone):
        if PessoaDatabase.get_by_cpf(cpf):
            raise Exception("CPF já cadastrado")

        PessoaDatabase.insert(nome, cpf, telefone)
        print("Pessoa cadastrada com sucesso")

    @staticmethod
    def delete(id):
        if PessoaEquipeDatabase.get_by_pessoa_id(id):
            raise Exception("Pessoa está em uma equipe")
        PessoaController.__pessoa_exists(id)

        PessoaDatabase.delete(id)
        print("Pessoa deletada com sucesso")

    @staticmethod
    def update(id, nome, cpf, telefone):
        PessoaController.__pessoa_exists(id)

        PessoaDatabase.update(id, nome, cpf, telefone)
        print("Pessoa atualizada com sucesso")

    @staticmethod
    def __pessoa_exists(id):
        if not PessoaDatabase.get_by_id(id):
            raise Exception("Pessoa não encontrada")

    @staticmethod
    def get_all():
        return PessoaDatabase.get_all()

    @staticmethod
    def get_by_id(id):
        PessoaController.__pessoa_exists(id)
        return PessoaDatabase.get_by_id(id)