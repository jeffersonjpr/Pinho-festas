from ast import Delete
from src.configs.database import Database
from src.database.pessoa_database import PessoaDatabase
from src.controller.equipe_controller import EquipeController
from src.controller.pessoa_controller import PessoaController
from src.controller.aluguel_controller import AluguelController
from src.controller.brinquedo_controller import BrinquedoController
from src.controller.pessoa_equipe_controller import PessoaEquipeController
# from colorama import Fore

print("Testes básicos")

# CADASTRANDO BRINQUEDOS
try: 
    BrinquedoController.insert("PulaPula", "cama eslatica", 3.0, 3.0, 3.0) # 1
    BrinquedoController.insert("PulaPula 2", "cama eslatica", 3.0, 3.0, 3.0) # 2
    print("Brinquedos cadastrados com sucesso")
except Exception as e:
    print("Esse erro não deve aparecer:", e)

# CADASTRANDO EQUIPE 1
try:
    
    PessoaController.insert("jef", "123", "322323") # 1
    EquipeController.insert("Equipe 1", "EQUIPE CIDADE 1") # 1
    PessoaEquipeController.insert(1, 1)
    print("Equipe 1 cadastrada com sucesso")
except Exception as e:
    print("Esse erro não deve aparecer:", e)

# CADASTRANDO EQUIPE 2
try:
    PessoaController.insert("isa", "321", "322323") # 2
    EquipeController.insert("Equipe 2", "EQUIPE CIDADE 2") # 2
    PessoaEquipeController.insert(2, 2)
    print("Equipe 2 cadastrada com sucesso")
except Exception as e:
    print("Esse erro não deve aparecer:", e)

# CADASTRO ALUGUEL 1
try:
    AluguelController.insert(1, "01/01/2022 18:30", "01/01/2022 20:30", 1, 1)
    print("Aluguel 1 cadastrado com sucesso")
except Exception as e:
    print("Esse erro não deve aparecer:", e)

# CADASTRO PESSOA REPETIDA
try:
    PessoaController.insert("jef", "123", "322323")
    print("Esse teste não deveria passar")
except Exception as e:
    print("Esse erro deve aparecer (CPF já cadastrado):", e)

# CADASTRO BRINQUEDO INDISPONIVEL
try:
    AluguelController.insert(1, "01/01/2022 18:30", "01/01/2022 22:30", 2, 2)
    print("Esse teste não deveria passar")
except Exception as e:
    print("Esse erro deve aparecer (Brinquedo 1 não disponível):", e)

# CADASTRO EQUIPE OCUPADA
try:
    AluguelController.insert(2, "01/01/2022 18:30", "01/01/2022 22:30", 1, 1)
    print("Esse teste não deveria passar")
except Exception as e:
    print("Esse erro deve aparecer (Equipe 1 não disponível):", e)
