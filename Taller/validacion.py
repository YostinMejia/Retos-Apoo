from personas import *
from gestor_archivos import *
from evento import *

class ValidacionVisitante():


    def validar_email(self,datos_lista_invitados:dict,email:str)->bool:

        if email!=datos_lista_invitados["email"]:
            return False
        else:
            return True
        

    def validar_nombre(self,evento:object,nombre:str)->bool:
        try:
            nombre=evento.get_invitado(nombre) #Se mira si el nombre si está en la lista de invitados
            return True
        except:
            return False


    def validar_id(self,datos_lista_invitados:dict,id:str)->bool:
        if id!=datos_lista_invitados["id"]:
            return False
        else:
            return True

    def validar_edad(self,datos_lista_invitados:dict,edad:int)->bool:
        if edad!=datos_lista_invitados["edad"]:
            return False
        else:
            return True

    
    def validar_invitado(self, evento:object, visitante:object):

        invitado_nombre=self.validar_nombre(evento,visitante.get_nombre()) #Se verifica que el nombre esté en la lista

        if invitado_nombre:

            datos_lista_invitados=evento.get_invitado(visitante.get_nombre()) #Estos son los datos de la lista de invitados

            #Estos son los datos registrados por el invitado
            id=self.validar_id(datos_lista_invitados,visitante.get_id())
            edad=self.validar_edad(datos_lista_invitados,visitante.get_edad())
            email=self.validar_email(datos_lista_invitados,visitante.get_email())

            if not id: #Si no concuerdan las ids
                return "La id que el invitado registro no es valida"
            elif edad:
                if visitante.get_edad()<18:
                    return "Es menor de edad no puede pasar"
                else:
                    return "La edad que el invitado registro no es valida"
            elif not email:
                return "El correo que el invitado registro no es valida"
            else:
                return f"{visitante.get_nombre().upper()} Está invitad@"

        else:
            return "No esta invitado"
