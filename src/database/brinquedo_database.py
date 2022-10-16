from src.configs.database import Database


class BrinquedoDatabase:
    @staticmethod
    def insert(nome, descricao, largura, altura, comprimento):
        try:
            Database.db_cursor.execute(
                "INSERT INTO brinquedo (nome, descricao, largura, altura, comprimento) VALUES (?, ?, ?, ?, ?)", (nome, descricao, largura, altura, comprimento))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def delete(id):
        try:
            Database.db_cursor.execute(
                "DELETE FROM brinquedo WHERE id = ?", (id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_all():
        try:
            Database.db_cursor.execute("SELECT * FROM brinquedo")
            brinquedos = Database.db_cursor.fetchall()
            return brinquedos
        except Exception as e:
            print(e)

    @staticmethod
    def get_by_id(id):
        try:
            Database.db_cursor.execute(
                "SELECT * FROM brinquedo WHERE id = ?", (id,))
            brinquedo = Database.db_cursor.fetchone()
            return brinquedo
        except Exception as e:
            print(e)

    @staticmethod
    def update(id, nome, descricao, largura, altura, comprimento):
        try:
            Database.db_cursor.execute(
                "UPDATE brinquedo SET nome = ?, descricao = ?, largura = ?, altura = ?, comprimento = ? WHERE id = ?", (nome, descricao, largura, altura, comprimento, id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)
