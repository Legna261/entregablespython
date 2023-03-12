## Programa para calcular el IMC de una persona

nombre = input("introduce tu nombre: ") #solicita el nombre de la persona.
if not nombre:
        print("Este campo es obligatorio, favor de llenarlo")

apellidopaterno= input("introduce tu apellido paterno: ") # solicita el apellido paterno del usuario
if not apellidopaterno:        
        print("Este campo es obligatorio, favor de llenarlo")
        
apellidomaterno= input("introduce tu apellido materno: ") # solicita el apellido materno del usuario
if not apellidomaterno:
        print("Este campo es obligatorio, favor de llenarlo")

print ("bienvenido:" ,nombre , apellidopaterno , apellidomaterno)  # da la bienvenida con el nombre de usuario

edad = int(input("introduce tu edad:")) # solicitamos la edad        
altura = float(input("introduce tu altura:")) #solicitamos su altura
peso = float(input("introduce tu peso en kilogramos:")) #solicitamos su peso en kilogramos 
print ( nombre , apellidopaterno , apellidomaterno , "su IMC= ", peso/altura**2) #imprimimos el nombre del usuario acompañado del calculo de su IMC.
