import sqlite3
from sqlite3 import Error

from src.controller.database_controller import DatabaseController
from src.models import aluguel, brinquedo, equipe, pessoa, pessoa_equipe


class Database:
    db_connection = None
    db_cursor = None

    def __init__(self):
        self.db_connection = self.create_connection(
            DatabaseController.get_database_name())
        self.db_cursor = self.db_connection.cursor()
        self.initialize_tables()

    def create_connection(self, db_file):
        connection = None
        try:
            connection = sqlite3.connect(db_file)

        except Error as e:
            print(e)

        # print("Connection to SQLite DB successful")

        return connection

    def create_table(self, create_table_sql):
        try:
            c = self.db_connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

        # print("Table created successfully")

    def initialize_tables(self):
        self.create_table(pessoa.pessoa)
        self.create_table(equipe.equipe)
        self.create_table(pessoa_equipe.pessoa_equipe)
        self.create_table(brinquedo.brinquedo)
        self.create_table(aluguel.aluguel)
        # print("Tables created")
