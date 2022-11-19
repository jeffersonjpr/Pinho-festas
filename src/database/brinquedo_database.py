from src.configs.database import Database


class BrinquedoDatabase:
    database = Database()

    @staticmethod
    def insert(nome, descricao, largura, altura, comprimento):
        try:
            BrinquedoDatabase.database.db_cursor.execute(
                "INSERT INTO brinquedo (nome, descricao, largura, altura, comprimento) VALUES (?, ?, ?, ?, ?)", (nome, descricao, largura, altura, comprimento))
            BrinquedoDatabase.database.db_connection.commit()
        except Exception as e:
            print("Brinquedo insert" + str(e))

        return BrinquedoDatabase.database.db_cursor.lastrowid

    @staticmethod
    def delete(id):
        try:
            BrinquedoDatabase.database.db_cursor.execute(
                "DELETE FROM brinquedo WHERE id = ?", (id))
            BrinquedoDatabase.database.db_connection.commit()
        except Exception as e:
            print("Brinquedo database", e)

    @staticmethod
    def get_all():
        try:
            BrinquedoDatabase.database.db_cursor.execute(
                "SELECT * FROM brinquedo")
            brinquedos = BrinquedoDatabase.database.db_cursor.fetchall()
            return brinquedos
        except Exception as e:
            print("Brinquedo database", e)

    @staticmethod
    def get_by_id(id):
        try:
            BrinquedoDatabase.database.db_cursor.execute(
                "SELECT * FROM brinquedo WHERE id = ?", (id,))
            brinquedo = BrinquedoDatabase.database.db_cursor.fetchone()
            return brinquedo
        except Exception as e:
            print("Brinquedo database", e)

    @staticmethod
    def update(id, nome, descricao, largura, altura, comprimento):
        try:
            BrinquedoDatabase.database.db_cursor.execute(
                "UPDATE brinquedo SET nome = ?, descricao = ?, largura = ?, altura = ?, comprimento = ? WHERE id = ?", (nome, descricao, largura, altura, comprimento, id))
            BrinquedoDatabase.database.db_connection.commit()
        except Exception as e:
            print("Brinquedo database", e)
