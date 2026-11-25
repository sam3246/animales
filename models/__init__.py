# Importar todos los modelos aquí hace que create_all() los vea.
from app.models.animal import Animal
from app.models.user import User

__all__ = ["Animal", "User"]
