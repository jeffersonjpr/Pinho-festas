from src.configs.database import Database


class PessoaEquipeDatabase:
    @staticmethod
    def insert(pessoa_id, equipe_id):
        try:
            Database.db_cursor.execute(
                "INSERT INTO pessoa_equipe (pessoa_id, equipe_id) VALUES (?, ?)", (pessoa_id, equipe_id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def delete(id):
        try:
            Database.db_cursor.execute(
                "DELETE FROM pessoa_equipe WHERE id = ?", (id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_all():
        try:
            Database.db_cursor.execute("SELECT * FROM pessoa_equipe")
            pessoa_equipes = Database.db_cursor.fetchall()
            return pessoa_equipes
        except Exception as e:
            print(e)

    @staticmethod
    def remove_by_pessoa_id(pessoa_id):
        try:
            Database.db_cursor.execute(
                "DELETE FROM pessoa_equipe WHERE pessoa_id = ?", (pessoa_id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)
