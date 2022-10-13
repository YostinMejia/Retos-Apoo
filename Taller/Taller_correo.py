from dataclasses import dataclass
import pandas as pd

import csv

#nombre id email edad
"""Hay que mirar la extensión del archivo para saber como leerlo """




@dataclass
class Persona:
    __nombre:str
    __email:str
    __edad:int
    __id:int

    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
    def get_edad(self):
        return self.__edad
    def get_id(self):
        return self.__id

class Visitante(Persona):
    pass

class Taquillero(Persona):

    # def validar_visitante(self, validador:ValidacionVisitante, visitante:Visitante):
        pass

class Evento:
    def __init__(self) -> None:
        self.__lista_invitados:list
        self.__taquillero:object
    
    # def generar_lista_invitados(gestor:GestorArchivo):
        pass

    # def set_taquillero(self, taquillero:Taquillero):
        pass


class GestorArchivo:

    def cargar_archivo(archivo):
        pass

    def determinar_extension(archivo):
        pass

    def extraer_informacion(archivo):
        pass


class  GestoDeArchivosXml:
    def __init__(self) -> None:
        self.datos={}

    def extraer_informacion(self,archivo)-> dict:
        
        pass


class GestoDeArchivosXlsx:
    
    def __init__(self) -> None:
        self.datos={}

    def extraer_informacion(self,archivo)-> dict:
        columns = ['Nombre','Id','Email','Edad']
        df2 = pd.read_excel(archivo, header=None,names=columns,skiprows=1)
        valores=df2.values
        for row in valores:
            self.datos.update({f"{row[0]}":{f"id":int(row[1]), f"email":row[2], f"edad":int(row[3])}})
        return self.datos
        

class GestoDeArchivosTxt:

    def __init__(self) -> None:
        self.datos={}

    def extraer_informacion(self,archivo)-> dict:
        with open("Taller_herencia.txt","r") as txt:
            for _ in txt:
                valores=txt.readline().split()
                if valores[0]!="Nombre": 
                    self.datos.update({f"{valores[0]}":{f"id":int(valores[1]), f"email":valores[2], f"edad":int(valores[3])}})
        
        return self.datos
            

class GestorDeArchivosCsv:
    
    def __init__(self) -> None:
        self.datos={}

    def extraer_informacion(self,archivo)-> dict:

        with open(archivo,"r") as csv_file:
            csvreader=csv.reader(csv_file)

            for row in csvreader:

                valores=row[0].split("**")

                if len(valores)==1:
                    if valores[0]!="Nombre": #No guarda la primera fila que indica los datos de las columnas
                        
                        valores=row #Se separa por comas
                                     #   NOMBRE              ID                      EMAIL               EDAD
                        self.datos.update({f"{valores[0]}":{f"id":int(valores[1]), f"email":valores[2], f"edad":int(valores[3])}})

                else:

                    if valores[0]!="Nombre": #No guarda la primera fila que indica los datos de las columnas
                        valores=row[0].split("**")
                         #En la primera fila está el indicativo de las columnas por lo que no se guarda

                                #   NOMBRE              ID                      EMAIL               EDAD
                        self.datos.update({f"{valores[0]}":{f"id":int(valores[1]), f"email":valores[2], f"edad":int(valores[3])}})

        return self.datos

extraer=GestoDeArchivosXlsx()
print(extraer.extraer_informacion("Taller_herencia.xlsx"))
print()
print()
print()
print()
print()
print()
print()
print()
extraer=GestorDeArchivosCsv()
print(extraer.extraer_informacion("Taller_herencia_.csv"))
print()
print()
print()
print()
print()
print()
print()
extraer=GestorDeArchivosCsv()
print(extraer.extraer_informacion("Taller_herencia.csv"))
# print(extraer.datos)