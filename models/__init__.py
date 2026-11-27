# Importar todos los modelos aquí hace que create_all() los vea.
from models.animal import Animal
from models.user import User

__all__ = ["Animal", "User"]
