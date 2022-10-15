from evento import *
from gestor_archivos import *
from validacion import *
from personas import *

from dataclasses import dataclass

@dataclass
class Persona:
    __nombre:str
    __email:str
    __edad:int
    __id:int

    def get_nombre(self):
        return self.__nombre.lower()

    def get_email(self):
        return self.__email

    def get_edad(self):
        return self.__edad

    def get_id(self):
        return self.__id

class Visitante(Persona):
    pass

class Taquillero(Persona):

    def validar_visitante(self, evento:object,validador:object, visitante:object):
        return validador.validar_invitado(evento,visitante)

