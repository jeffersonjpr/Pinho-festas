from src.configs.database import Database


class PessoaDatabase:
    database = Database()

    @staticmethod
    def insert(nome, cpf, telefone):
        try:
            PessoaDatabase.database.db_cursor.execute(
                "INSERT INTO pessoa (nome, cpf, telefone) VALUES (?, ?, ?)", (nome, cpf, telefone))
            PessoaDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaDatabase", e)

    @staticmethod
    def delete(id):
        try:
            PessoaDatabase.database.db_cursor.execute(
                "DELETE FROM pessoa WHERE id = ?", (id,))
            PessoaDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaDatabase", e)

    @staticmethod
    def get_all():
        try:
            PessoaDatabase.database.db_cursor.execute("SELECT * FROM pessoa")
            pessoas = PessoaDatabase.database.db_cursor.fetchall()
            return pessoas
        except Exception as e:
            print("PessoaDatabase", e)

    @staticmethod
    def get_by_id(id):
        try:
            PessoaDatabase.database.db_cursor.execute(
                "SELECT * FROM pessoa WHERE id = ?", (id,))
            pessoa = PessoaDatabase.database.db_cursor.fetchone()
            return pessoa
        except Exception as e:
            print("PessoaDatabase", e)

    @staticmethod
    def update(id, nome, cpf, telefone):
        try:
            PessoaDatabase.database.db_cursor.execute(
                "UPDATE pessoa SET nome = ?, cpf = ?, telefone = ? WHERE id = ?", (nome, cpf, telefone, id))
            PessoaDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaDatabase", e)

    @staticmethod
    def get_by_cpf(cpf):
        try:
            PessoaDatabase.database.db_cursor.execute(
                "SELECT * FROM pessoa WHERE cpf = ?", (cpf,))
            pessoa = PessoaDatabase.database.db_cursor.fetchone()
            return pessoa
        except Exception as e:
            print("PessoaDatabase", e)
