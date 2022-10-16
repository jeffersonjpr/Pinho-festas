from src.configs.database import Database


class EquipeDatabase:
    @staticmethod
    def insert(nome, descricao):
        try:
            Database.db_cursor.execute(
                "INSERT INTO equipe (nome, descricao) VALUES (?, ?)", (nome, descricao))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def delete(id):
        try:
            Database.db_cursor.execute("DELETE FROM equipe WHERE id = ?", (id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_all():
        try:
            Database.db_cursor.execute("SELECT * FROM equipe")
            equipes = Database.db_cursor.fetchall()
            return equipes
        except Exception as e:
            print(e)

    @staticmethod
    def get_by_id(id):
        try:
            Database.db_cursor.execute(
                "SELECT * FROM equipe WHERE id = ?", (id,))
            equipe = Database.db_cursor.fetchone()
            return equipe
        except Exception as e:
            print(e)

    @staticmethod
    def update(id, nome, descricao):
        try:
            Database.db_cursor.execute(
                "UPDATE equipe SET nome = ?, descricao = ? WHERE id = ?", (nome, descricao, id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)
