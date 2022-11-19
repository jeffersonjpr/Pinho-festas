import os
import unittest

from src.controller.database_controller import DatabaseController
from src.controller.pessoa_controller import PessoaController
from src.controller.brinquedo_controller import BrinquedoController
from src.controller.equipe_controller import EquipeController
from src.controller.pessoa_equipe_controller import PessoaEquipeController
from src.controller.aluguel_controller import AluguelController


def remove_db():
    if os.path.exists("test.db"):
        os.remove("test.db")


class TestAluguelController(unittest.TestCase):
    brinquedo1 = BrinquedoController.insert(
        "PulaPula", "cama eslatica", 3.0, 3.0, 3.0)
    brinquedo2 = BrinquedoController.insert(
        "PulaPula 2", "cama eslatica", 3.0, 3.0, 3.0)
    pessoa1 = PessoaController.insert("jef", "123", "322323")
    equipe1 = EquipeController.insert("Equipe 1", "EQUIPE CIDADE 1")
    PessoaEquipeController.insert(pessoa1, equipe1)

    pessoa2 = PessoaController.insert("isa", "321", "322323")
    equipe2 = EquipeController.insert("Equipe 2", "EQUIPE CIDADE 2")
    PessoaEquipeController.insert(pessoa2, equipe2)

    @classmethod
    def setUpClass(cls) -> None:
        DatabaseController.set_database_name('test.db')

        if os.path.exists('teste.db'):
            os.remove('test.db')

    @classmethod
    def tearDownClass(cls):

        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_insert(self):
        self.assertIsInstance(AluguelController.insert(
            self.brinquedo1, "01/01/2022 18:30", "01/01/2022 20:30", self.equipe1, self.equipe2, "Rua x"), int)

    def test_insert_invalid_equipe_montagem(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "02/02/2022 18:30", "02/02/2022 20:30", 31321, self.equipe1, "Rua x")

    def test_insert_invalid_equipe_desmontagem(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "02/02/2022 18:30", "02/02/2022 20:30", self.equipe1, 31321, "Rua x")

    def test_insert_invalid_brinquedo(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                31321, "02/02/2022 18:30", "02/02/2022 20:30", self.equipe1, self.equipe2, "Rua x")

    def test_insert_invalid_data_montagem(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "oi", "02/02/2022 18:29", self.equipe1, self.equipe2, "Rua x")

    def test_insert_invalid_data_desmontagem(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "02/02/2022 18:30", "oi", self.equipe1, self.equipe2, "Rua x")

    def test_insert_invalid_data_montagem_maior_que_desmontagem(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "02/02/2023 18:30", "02/02/2023 18:29", self.equipe1, self.equipe2, "Rua x")

    def test_insert_invalid_local(self):
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo1, "02/02/2023 18:00", "02/02/2023 18:29", self.equipe1, self.equipe2, "")

    def test_equipe_unavailable_before(self):
        AluguelController.insert(
            self.brinquedo1, "02/02/2024 18:00", "02/02/2024 23:00", self.equipe1, self.equipe1, "Rua x")
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo2, "02/02/2024 15:00", "02/02/2024 18:01", self.equipe1, self.equipe1, "Rua x")

    def test_equipe_unavailable_after(self):
        AluguelController.insert(
            self.brinquedo1, "02/02/2025 18:00", "02/02/2025 23:00", self.equipe1, self.equipe1, "Rua x")
        with self.assertRaises(Exception):
            AluguelController.insert(
                self.brinquedo2, "02/02/2025 23:15", "03/02/2025 23:50", self.equipe1, self.equipe1, "Rua x")

    def test_get_all(self):
        self.assertIsInstance(AluguelController.get_all(), list)

    def test_get_by_id(self):
        aluguel = AluguelController.insert(
            self.brinquedo1, "02/02/2026 18:00", "02/02/2026 23:00", self.equipe1, self.equipe1, "Rua x")
        self.assertIsInstance(AluguelController.get_by_id(aluguel), tuple)

    def test_brinquedo_unavailable(self):
        AluguelController.insert(
            self.brinquedo1, "02/02/2027 18:00", "02/02/2027 23:00", self.equipe1, self.equipe1, "Rua x")
        with self.assertRaises(Exception):
            AluguelController.insert(self.brinquedo1, "02/02/2027 18:20",
                                     "02/02/2027 22:40", self.equipe1, self.equipe1, "Rua x")


if __name__ == '__main__':
    unittest.main()
