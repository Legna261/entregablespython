## Programa para calcular el IMC de una persona

nombre = input("introduce tu nombre:") #solicita el nombre de la persona.
print ("bienvenido:" ,nombre) # da la bienvenida con el nombre de usuario
edad = int(input("introduce tu edad:")) # solicitamos la edad 
altura = float(input("introduce tu altura:")) #solicitamos su altura
peso = float(input("introduce tu peso en kilogramos:")) #solicitamos su peso en kilogramos 
print ("su IMC= ", peso/altura**2) #imprimimos su indice de masa corporal


