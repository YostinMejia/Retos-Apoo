# """Desarrolle una calculadora para operaciones sencillas interactiva. 
# Una operación sencilla es una operación que tiene dos operandos numéricos y un operador (+,-,* o /) todos separados por un espacio, por ejemplo, "5 + 5".
# Este programa deberá solicitar al usuario expresiones hasta que el usuario ingrese la palabra "terminar" y deberá evaluarlas de acuerdo al operador, es decir, si el usuario ingresa "5 + 5", el programa deberá imprimir por pantalla 10.
# Definir una excepción personalizada para cada tipo de error que puede ocurrir. Cuáles identifican?
# Controlar los casos problemáticos lanzando estas excepciones y atrapándolas con el bloque except para que se le informe al usuario del error y se le solicite una nueva entrada.
# El programa nunca debe parar a menos que el usuario ingrese "terminar", incluso si ingresa una sentencia no válida.
# 0.3 para el primero, 0.2 para el segundo, 0.1 para el resto que lo termine dentro de la clase."""

# def calculadora():

#     def sumar(num1,num2):
#         return num1 + num2

#     def restar(num1,num2):
#         return num1 - num2

#     def multiplicar(num1,num2):
#         return num1 * num2
    
#     def dividir(num1,num2):
#         try:
#             div= num1 / num2
#             return div
#         except ZeroDivisionError:
#             print(f"división por cero -> {num1} / {num2}")
#             calculadora()

#     def mirarNumeros(num,pos):
#         try: 
#             numero= int(num[pos])
#             return numero
#         except:
#             print(f"Donde escribio {num[pos]} debe ir un número")
#             calculadora()


#     while True:
#         print("ingrese la operacion con espacios, por ejemplo '5 + 5' notese los espacios entre numeros y operadores")
#         dato=input("Ingrese el dato con espacios: ").split()
#         if (dato[0])=="terminar":
#             break
#         else:
#             operadores=["+","-","*","/"]



#             num1=mirarNumeros(dato,0)
#             num2=mirarNumeros(dato,2)

#             cont_operadores=0
#             operador=""
#             for i in dato:
#                 if i in operadores:
#                     cont_operadores+=1
#                     operador=i

#             if cont_operadores==1:
#                 if operador=="+":
#                     print(sumar(num1,num2))
#                 elif operador=="-":
#                     print(restar(num1,num2))
#                 elif operador=="*":
#                     print(multiplicar(num1,num2))
#                 elif operador=="/":
#                     print(dividir(num1,num2))
#             elif cont_operadores>1:
#                 print("Sobrepaso la cantidad de operadores")
#             else:
#                 print("Le hace falta un operador")
            


# calculadora()

