from src.configs.database import Database


class ClienteDatabase:
    database = Database()

    @staticmethod
    def insert(nome, cpf, telefone, email, cep, bairro, cidade, endereco):
        try:
            ClienteDatabase.database.db_cursor.execute(
                "INSERT INTO cliente (nome, cpf, telefone, email, cep, bairro, cidade, endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, email, cep, bairro, cidade, endereco))
            ClienteDatabase.database.db_connection.commit()
        except Exception as e:
            print("ClienteDatabase", e)

        return ClienteDatabase.database.db_cursor.lastrowid

    @staticmethod
    def delete(id):
        try:
            ClienteDatabase.database.db_cursor.execute(
                "DELETE FROM cliente WHERE id = ?", (id,))
            ClienteDatabase.database.db_connection.commit()
        except Exception as e:
            print("ClienteDatabase", e)

    @staticmethod
    def get_all():
        try:
            ClienteDatabase.database.db_cursor.execute("SELECT * FROM cliente")
            clientes = ClienteDatabase.database.db_cursor.fetchall()
            return clientes
        except Exception as e:
            print("ClienteDatabase", e)

    @staticmethod
    def get_by_id(id):
        try:
            ClienteDatabase.database.db_cursor.execute(
                "SELECT * FROM cliente WHERE id = ?", (id,))
            cliente = ClienteDatabase.database.db_cursor.fetchone()
            return cliente
        except Exception as e:
            print("ClienteDatabase", e)

    @staticmethod
    def update(id, nome, cpf, telefone, email, cep, bairro, cidade, endereco):
        try:
            ClienteDatabase.database.db_cursor.execute(
                "UPDATE cliente SET nome = ?, cpf = ?, telefone = ?, email = ?, cep = ?, bairro = ?, cidade = ?, endereco = ? WHERE id = ?", (nome, cpf, telefone, email, cep, bairro, cidade, endereco, id))
            ClienteDatabase.database.db_connection.commit()
        except Exception as e:
            print("ClienteDatabase", e)

    @staticmethod
    def get_by_cpf(cpf):
        try:
            ClienteDatabase.database.db_cursor.execute(
                "SELECT * FROM cliente WHERE cpf = ?", (cpf,))
            cliente = ClienteDatabase.database.db_cursor.fetchone()
            return cliente
        except Exception as e:
            print("ClienteDatabase", e)
