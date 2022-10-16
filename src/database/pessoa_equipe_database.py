from src.configs.database import Database


class PessoaEquipeDatabase:
    database = Database()

    @staticmethod
    def insert(pessoa_id, equipe_id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "INSERT INTO pessoa_equipe (pessoa_id, equipe_id) VALUES (?, ?)", (pessoa_id, equipe_id))
            PessoaEquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaEquipeDatabase (insert)", e)

    @staticmethod
    def delete(id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "DELETE FROM pessoa_equipe WHERE id = ?", (id))
            PessoaEquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaEquipeDatabase", e)

    @staticmethod
    def get_all():
        try:
            PessoaEquipeDatabase.database.db_cursor.execute("SELECT * FROM pessoa_equipe")
            pessoa_equipes = PessoaEquipeDatabase.database.db_cursor.fetchall()
            return pessoa_equipes
        except Exception as e:
            print("PessoaEquipeDatabase", e)

    @staticmethod
    def get_by_id(id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "SELECT * FROM pessoa_equipe WHERE id = ?", (id))
            pessoa_equipe = PessoaEquipeDatabase.database.db_cursor.fetchone()
            return pessoa_equipe
        except Exception as e:
            print("PessoaEquipeDatabase", e)

    @staticmethod
    def remove_by_pessoa_id(pessoa_id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "DELETE FROM pessoa_equipe WHERE pessoa_id = ?", (pessoa_id,))
            PessoaEquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print("PessoaEquipeDatabase", e)

    @staticmethod
    def get_by_pessoa_id(pessoa_id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "SELECT * FROM pessoa_equipe WHERE pessoa_id = ?", (pessoa_id,))
            pessoa_equipe = PessoaEquipeDatabase.database.db_cursor.fetchone()
            return pessoa_equipe
        except Exception as e:
            print("PessoaEquipeDatabase", e)

    @staticmethod
    def get_by_equipe_id(equipe_id):
        try:
            PessoaEquipeDatabase.database.db_cursor.execute(
                "SELECT * FROM pessoa_equipe WHERE equipe_id = ?", (equipe_id,))
            pessoa_equipe = PessoaEquipeDatabase.database.db_cursor.fetchone()
            return pessoa_equipe
        except Exception as e:
            print("PessoaEquipeDatabase (getbyequipeid)", e)