from evento import *
from gestor_archivos import *
from personas import *
from validacion import *


gestor=GestorDeArchivo()  
evento=Evento()
evento.generar_lista_invitados(gestor,"Taller_herencia.csv")

visitante1=Visitante("Biel","0jfd2H8f2@hotmail.com",38,65454615)
# visitante1=Visitante("semenko","0jfd2H8f2@hotmail.com",38,65454615)


validar=ValidacionVisitante()

taquillero=Taquillero("thor","askdasgmail.com",34,312323)

print(taquillero.validar_visitante(evento,validar,visitante1))
# print(validar.validar_invitado(evento,visitante1))


# # extraer=GestorDeArchivosXlsx()
# # print(extraer.extraer_informacion("Taller_herencia.xlsx"))
# # print()
# # print()
# # print()
# # print()
# # print()
# # print()
# # print()
# # print()
# # extraer=GestorDeArchivosCsv()
# # print(extraer.extraer_informacion("Taller_herencia_.csv"))
# # print()
# # print()
# # print()
# # print()
# # print()
# # print()
# # print()
# # extraer=GestorDeArchivosXml()
# # print(extraer.extraer_informacion("Taller_herencia.xml"))
# # extraer.extraer_informacion("Taller_herencia.xml")
# # print(extraer.datos)
