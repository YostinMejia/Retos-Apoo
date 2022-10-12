import pywhatkit
from termcolor import colored 
import random
from dataclasses import dataclass

lista_palabras=["hogar","apodo","bucle","cacao","costo","pizza","jueza","niñez","chuzo","capaz","zombi","cazar"]


def convObjPalabra(eleccion):

    @dataclass
    class ObjPalabra:
        palabra=[]

        def __repr__(self) -> str:
            return f"{self.palabra}"

        def __ne__(self, other: str) -> bool:
            return len(self.palabra)!=len(other)
    
    @dataclass
    class ObjLetras: 
        letra:str
        
        def __repr__(self) -> str:
            return f"{self.letra}"
        
        def __eq__(self, other: object) -> bool:
            return self.letra==other.letra
        
        def __ne__(self, other: str) -> bool:
            return self.letra!=other.letra


    objpalabra=ObjPalabra()

    for letra in eleccion:
        letra=ObjLetras(letra)     #Se convierte cada letra en un objeto 
        objpalabra.palabra.append(letra) #se agrega el objeto letra a la lista de letras

    return objpalabra

#---------------------Inicio------------

print("¿Qué se dice socio?")

print("Si desea iniciar el juego ingrese 'si' de lo contrario ingrese cualquier otra cosa")
inicio=input("¿Quiere iniciar el juego?: ")

intentos=0

if inicio=="si":
    while True:

        #Aleatoriamente se escoge la palabra 
        if intentos==0:
           palabra_random=random.choice(lista_palabras)
           palabra_random=convObjPalabra(palabra_random)
           print("lista de letras",palabra_random)

        #EL usuario ingresa la palabra con la que intenta adivinar
        usuario_palabra=input("Ingrese una palabra de 5 letras: ").lower()
        while usuario_palabra!=palabra_random : #El dunder method mira si el len() es diferente
            usuario_palabra=input("Ingrese una palabra de 5 letras: ").lower()

        usuario_palabra=convObjPalabra(usuario_palabra) #Se covierten las letras en objetos y se ponen en la lista Palabra   

        #Contamos las letras y le restamos, si el número es  entonces no se colorea
        cantidad_letras={}

        acierto=0
        perdio=""

        mostrar=[]
        #Se debe de poner primero la cantidad porque depues se miran todas las verdes
        for i in range(len(palabra_random.palabra)):
            #Se guarda la cantidad de letras en el diccionario
            if f"{usuario_palabra.palabra[i]}" not in cantidad_letras: 
                cantidad_letras[f"{usuario_palabra.palabra[i]}"]=palabra_random.palabra.count(usuario_palabra.palabra[i]) #Se cuentan las veces que esta esta letra en la palabra random
            mostrar.append(None)
            
        
        for j in range(len(palabra_random.palabra)):
            
            if usuario_palabra.palabra[j]==palabra_random.palabra[j] and (cantidad_letras[f"{usuario_palabra.palabra[j]}"]>0) :
                # print(colored(usuario_palabra.palabra[j],"green"))
                mostrar[j]=(colored(usuario_palabra.palabra[j],"green"))
                cantidad_letras[f"{usuario_palabra.palabra[j]}"]-=1 #Se resta en la cantidad de letras para que no siga contando 
                acierto+=1

        for i in range(len(palabra_random.palabra)):

            #Guardo cada letra en color rojo para mostrarlo cuando pierda
            perdio=perdio+colored(usuario_palabra.palabra[i],"red")


            if mostrar[i]==None:

                if usuario_palabra.palabra[i] in palabra_random.palabra and (cantidad_letras[f"{usuario_palabra.palabra[j]}"]>0):
                    #Se mira si esta en distinta posicion
                    mostrar[i]=(colored(usuario_palabra.palabra[i],"yellow"))
                    cantidad_letras[f"{usuario_palabra.palabra[i]}"]-=1 #Se resta en la cantidad de letras para que no siga contando 
                else:
                    # print(colored(usuario_palabra.palabra[i],"grey"))
                    mostrar[i]=(colored(usuario_palabra.palabra[i],"grey"))

        mostrar="".join(mostrar)


            #Gana o pierde
        if acierto==len(palabra_random.palabra):
            print(mostrar)
            print(colored("ESOOOOOOO MOSTRO GANOOOOOOOOOOOOOOO","green"))
            pywhatkit.playonyt("https://youtu.be/KXw8CRapg7k?t=39")
            break

        elif intentos==6:
            print(perdio)
            print(colored("NO PA USTED ES MUY MALO YA NO TIENE MAS INTENTOS, EN POCAS PALABRAS, PERDISTES DE ÑENGO FLOW","red"))
            pywhatkit.playonyt("https://www.youtube.com/watch?v=UumOtQ9v0GM&ab_channel=TusefectosdeSonido")
            break 
        else:
            print(mostrar)  

        intentos+=1

#Si no quiere inicar el juego
else:
    print("Vaya a dormir entonces")







