from src.database.pessoa_database import PessoaDatabase
from src.database.pessoa_equipe_database import PessoaEquipeDatabase


class PessoaController:

    @staticmethod
    def insert(nome, cpf, telefone, senha):
        if PessoaDatabase.get_by_cpf(cpf):
            raise Exception("CPF já cadastrado.")

        return PessoaDatabase.insert(nome, cpf, telefone, senha)

    @staticmethod
    def delete(id):
        if PessoaEquipeDatabase.get_by_pessoa_id(id):
            raise Exception("Pessoa está em uma equipe.")
        PessoaController.__pessoa_exists(id)

        PessoaDatabase.delete(id)

    @staticmethod
    def update(id, nome, cpf, telefone, senha):
        PessoaController.__pessoa_exists(id)

        PessoaDatabase.update(id, nome, cpf, telefone, senha)

    @staticmethod
    def __pessoa_exists(id):
        if not PessoaDatabase.get_by_id(id):
            raise Exception("Pessoa não encontrada.")

    @staticmethod
    def get_all():
        pessoas = PessoaDatabase.get_all()
        
        if pessoas: 
            for i in range(len(pessoas)):
                pessoas[i] = list(pessoas[i])
                pessoas[i].pop(4)
            return pessoas
        return None

    @staticmethod
    def get_by_id(id):
        PessoaController.__pessoa_exists(id)
        return PessoaDatabase.get_by_id(id)

    @staticmethod
    def get_by_id_clean(id):
        PessoaController.__pessoa_exists(id)
        pessoa = PessoaDatabase.get_by_id(id)
        pessoa = list(pessoa)
        pessoa.pop(4)
        return pessoa

    @staticmethod
    def login(cpf, senha):
        pessoa = PessoaDatabase.get_by_cpf(cpf)
        if not pessoa:
            raise Exception("CPF não cadastrado.")
        if pessoa[4] != senha:
            raise Exception("Senha incorreta.")
        
        return pessoa
    
    @staticmethod
    def verify_admin(cpf):
        with open('src/lista_admins.txt', 'r') as file:
            admins = file.read().splitlines()
            if cpf in admins:
                return True
            return False