from src.configs.database import Database


class EquipeDatabase:
    database = Database()

    @staticmethod
    def insert(nome, descricao):
        try:
            EquipeDatabase.database.db_cursor.execute(
                "INSERT INTO equipe (nome, descricao) VALUES (?, ?)", (nome, descricao))
            EquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print(e)

        return EquipeDatabase.database.db_cursor.lastrowid

    @staticmethod
    def delete(id):
        try:
            EquipeDatabase.database.db_cursor.execute(
                "DELETE FROM equipe WHERE id = ?", (id))
            EquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_all():
        try:
            EquipeDatabase.database.db_cursor.execute("SELECT * FROM equipe")
            equipes = EquipeDatabase.database.db_cursor.fetchall()
            return equipes
        except Exception as e:
            print(e)

    @staticmethod
    def get_by_id(id):
        try:
            EquipeDatabase.database.db_cursor.execute(
                "SELECT * FROM equipe WHERE id = ?", (id,))
            equipe = EquipeDatabase.database.db_cursor.fetchone()
            return equipe
        except Exception as e:
            print(e)

    @staticmethod
    def update(id, nome, descricao):
        try:
            EquipeDatabase.database.db_cursor.execute(
                "UPDATE equipe SET nome = ?, descricao = ? WHERE id = ?", (nome, descricao, id))
            EquipeDatabase.database.db_connection.commit()
        except Exception as e:
            print(e)
