import pandas as pd
import xml.etree.ElementTree as ET
import csv
from abc import abstractproperty


class Gestor_De_Archivo:
    @abstractproperty
    def cargar_archivo(self, archivo):
        pass

    @abstractproperty
    def determinar_extension(self, archivo):
        pass
        
    @abstractproperty
    def extraer_informacion(self,archivo)-> dict:
        pass


class GestorDeArchivo(Gestor_De_Archivo):

    def __init__(self) -> None:
        self.datos={}

    def cargar_archivo(self):
        print("Cargando archivo............")
        print("Archivo cargado")
        
    def determinar_extension(self, archivo):

        extension=archivo[-4:]

        return extension
        
    def extraer_informacion(self,archivo)-> dict:
        pass

    def ordenar_por_nombres(self, datos:dict):
        ordenados=sorted(datos)
        return ordenados
    
    def ordenar_por_edades(self,datos:dict):

        ordenados = dict(sorted(datos.items(), key=lambda item:item[1]["edad"]))
        return ordenados
    
    def determinar_promedio(self,datos:dict):
        total_edades=0
        for i in datos:
            total_edades+=datos[i]["edad"]

        promedio=total_edades/len(datos)
        
        return promedio
        



class  GestorDeArchivosXml(GestorDeArchivo):

    
    def extraer_informacion(self,archivo)-> dict:
        self.cargar_archivo()

        tree=ET.parse(archivo)
        root=tree.getroot()
        
        temp=[]
        for i in root.findall(".//{urn:schemas-microsoft-com:office:spreadsheet}Cell/"):
            # print(i.text)
            dato=i.text
            # print(dato)
            temp.append(dato)
            if len(temp)==4:
                if temp[0]=="Nombre":
                    temp=[]
                else:
                    self.datos.update({f"{temp[0].lower()}":{f"id":temp[1], f"email":temp[2], f"edad":int(temp[3])}})
                    temp=[]

        return self.datos
        

class GestorDeArchivosXlsx(GestorDeArchivo):

    def extraer_informacion(self,archivo)-> dict:
        self.cargar_archivo()


        columns = ['Nombre','Id','Email','Edad']
        df2 = pd.read_excel(archivo, header=None,names=columns,skiprows=1)
        valores=df2.values
        
        for row in valores:
            self.datos.update({f"{row[0].lower()}":{f"id":row[1], f"email":row[2], f"edad":int(row[3])}})

        return self.datos
        

class GestorDeArchivosTxt(GestorDeArchivo):

    def extraer_informacion(self,archivo)-> dict:
        self.cargar_archivo()

        with open("Taller_herencia.txt","r") as txt:
            for _ in txt:
                valores=txt.readline().split()
                if valores[0]!="Nombre": 
                        self.datos.update({f"{valores[0].lower()}":{f"id":valores[1], f"email":valores[2], f"edad":int(valores[3])}})
        
        return self.datos
            

class GestorDeArchivosCsv(GestorDeArchivo):

    def extraer_informacion(self,archivo)-> dict:
        self.cargar_archivo()

        with open(archivo,"r") as csv_file:
            csvreader=csv.reader(csv_file)

            for row in csvreader:

                valores=row[0].split("**")

                if len(valores)==1:
                    if valores[0]!="Nombre": #No guarda la primera fila que indica los datos de las columnas
                        
                        valores=row #Se separa por comas
                                     #   NOMBRE              ID                      EMAIL               EDAD
                        self.datos.update({f"{valores[0].lower()}":{f"id":valores[1], f"email":valores[2], f"edad":int(valores[3])}})

                else:

                    if valores[0]!="Nombre": #No guarda la primera fila que indica los datos de las columnas
                        valores=row[0].split("**")
                         #En la primera fila está el indicativo de las columnas por lo que no se guarda

                                #   NOMBRE              ID                      EMAIL               EDAD
                        self.datos.update({f"{valores[0].lower()}":{f"id":valores[1], f"email":valores[2], f"edad":int(valores[3])}})

        return self.datos