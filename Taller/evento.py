from personas import *
from gestor_archivos import *


class Evento:

    def __init__(self) -> None:
        self.__lista_invitados:dict
        self.__taquillero:object
    
    def generar_lista_invitados(self,gestor,archivo):
        extension=gestor.determinar_extension(archivo)

        if extension[0]==".":

            if extension ==".csv":
                obj_temp=GestorDeArchivosCsv()
                invitados=obj_temp.extraer_informacion(archivo)

                
            elif extension==".txt":
                obj_temp=GestorDeArchivosTxt()
                invitados=obj_temp.extraer_informacion(archivo)
                
            elif extension==".xml":
                obj_temp=GestorDeArchivosXml()
                invitados=obj_temp.extraer_informacion(archivo)

        else:
            obj_temp=GestorDeArchivosXlsx()
            invitados=obj_temp.extraer_informacion(archivo)
        
        self.__lista_invitados=invitados
        return "Invitados agregados"

    def set_taquillero(self, taquillero:Taquillero):
        self.__taquillero=taquillero
        return "Taquillero agregado"
    
    def get_invitado(self,invitado:str):
        return self.__lista_invitados[invitado]

