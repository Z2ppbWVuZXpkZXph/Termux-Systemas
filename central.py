from sympy.crypto.crypto import encipher_affine, decipher_affine

from sympy.crypto.crypto import encipher_shift, decipher_shift
                                                                 >
import os

import traceback


os.system("clear")

#COLORES
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

print (M+"==============================")

print (R+"SYSTEMA DE INCRIPTACION")

print (M+"==============================")

print (" ")

print (M+"A continuacion escribe tu nombre para continuar")

print (" ")

resultado = input("ESCRIBE TU NOMBRE: ")

if resultado == resultado:
   print ("Bienvenido al systema de incriptacion")
print (resultado)

print (" ")

print (M+"A CONTINUACION ELIGE UNA OPCION")

print (" ")

print ("1)  Si quieres salir")

print (" ")

print ("2) incriptacion")

print (" ")

resultado = input("ELIGE UNA OPCION: ")
print (R+"AGUARDE UN MOMENTO A ESPERAR QUE SE CARGUE LA  ENCRIPTA>
                                                                 >
if resultado == "1":
        print ("Saliendo")

elif resultado == "2":
        def cifrado():
                print ("cifrar")
                mensaje = input("ESCRIBE UNA PALABRA: ")
                llave = (7,26)
                cifrado = encipher_affine(mensaje, llave)
                print (cifrado)
        cifrado()

print (" ")

print (YY+" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")

print (YY+"SYSTEMA DE DESCRIPTACION")

print (" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")

print (" ")

respuesta = input("DIME TU NOMBRE: ")

if respuesta == respuesta:
   print ("Bienvenid@ A Systema de descriptacion")
   print (respuesta)

print (" ")

print (YY+"ELIGE UNA DE LAS SIGUIENTES OPCIONES")

print (" ")

print ("1) Desencriptar palabra")

print (" ")

print ("2) salir")

print (" ")

respuesta = input("ELIGE UNA RESPUESTA: ")

if respuesta == "1":
        def desencriptar():
                print ("descifrar")
                mensaje = input("Escribe un palabra: ")
                llave = (3, 26)
                desencriptar = decipher_affine(mensaje, llave)
                print (desencriptar)
desencriptar()

elif respuesta == "2":
     print ("Saliendo...")



print (" ")


print (YY+"+++++++++++++++++++++++++++++++")

print (RR+"RECOPILADOR DE DATOS PERSONALES")

print (YY+"+++++++++++++++++++++++++++++++")

print (" ")

print (W+"Bienvenido a el recopilador de datos")

print (" ")

print (W+"para empezar ponga su nombre")

print (" ")

resultado = input("ESCRIBE TU NOMBRE: ")

if resultado == resultado:

   print (" ")

   print ("Nombre")

   print (" ")


print (" ")

print (W+"Siguiente pon tu apellido")

print (" ")

resultado_2 = input("ESCRIBE TU APELLIDO: ")


if resultado_2 == resultado_2:

   print (" ")

   print ("Apellido")

   print (" ")

   print (resultado_2)

   print (" ")

   print (W+"Siguiente escribe tu edad: ")

   print (" ")

respuesta_3 = input("ESCRIBE  TU EDAD: ")

if respuesta_3 == respuesta_3:

   print (" ")

   print ("Edad")

   print (" ")

   print (respuesta_3)

print (" ")

print (W+"Siguiente Escribe tu signo zodiacal")

if respuesta_4 == respuesta_4:

   print (" ")

   print ("Signo zodiacal")

   print (" ")

   print (respuesta_4)

   print (" ")

print (W+"Siguiente escribe  tu altura")

print (" ")

respuesta_5 = input("ESCRIBE TU ALTURA: ")

if respuesta_5 == respuesta_5:

print (" ")

   print ("Altura")

   print (" ")

   print (respuesta_5)

   print (" ")

print (W+"Siguiente escribe tu peso corporal")

print (" ")

respuesta_6 = input("ESCRIBE TU PESO CORPORAL: ")

if respuesta_6 == respuesta_6:

   print (" ")

   print ("peso")

   print (" ")

   print (respuesta_6)

   print (" ")

print (W+"Siguoente escribe tu color de piel")

print (" ")

respuesta_7 = input("ESCRIBE TU COLOR DE PIEL: ")

if respuesta_7 == respuesta_7:

   print (" ")

print ("color de piel")

   print (" ")

   print (respuesta_7)

   print (" ")

print (W+" Siguiente escribe tu color de ojos")

print (" ")

respuesta_8 = input("ESCRIBE TU COLOR DE OJOS: ")

if respuesta_8 == respuesta_8:

   print (" ")

   print ("Color de ojos")

   print (" ")

   print (respuesta_8)

   print (" ")

print (W+"Siguiente escribe tu color de cabello")

print (" ")

resultado_9 = input("ESCRIBE TU COLOR DE CABELLO: ")

if resultado_9 == resultado_9:

   print (" ")

   print ("color de cabello")

   print (" ")

print (resultado_9)

   print (" ")

print (W+"Siguiente eecribe tu pais")

print (" ")

resultado_10 = input("ESCRIBE TU PAIS: ")

if resultado_10 == resultado_10:

   print (" ")

   print ("pais")

   print (" ")

   print (resultado_10)

print (" ")

print (W+" Siguiente escribe tu  sexo")

print (" ")

resultado_11 = input("ESCRIBE TU SEXO: ")

if resultado_11 == resultado_11:
   print (" ")


   print ("sexo")

   print (" ")

   print (resultado_11)

print (" ")

print (R+"-----------------------------")
print (W+"CALCULADORA == TERMUX")

print (R+"-----------------------------")

print (" ")

print (R+"CARGANDO CALCULADORA...")

print (" ")

primero = int(input("PON EL PRIMER NUMERO: "))

print (" ")

segundo = int(input("PON EL SEGUNDO NUMERO: "))

print (" ")

print ("RESULTADO DE LA SUMA")

print (" ")

print (primero + segundo)

print (" ")

print (B+"###################################")

print (Y+"ENCRIPTAR Y DESENCRIPTADOR ROT13")

print ("######################################")

print (" ")

print (B+"Bienvenid@ Al systema de encriptacion y desencriptacion>

print (" ")

print (Y+"CARGANDO OPCIONES")

print (" ")

print (B+"ELIGE UNA OPCION")

print (" ")

print ("1) Si quieres encriptar una palabra")

print (" ")

print ("2) Si quieres desencriptar una palabra")

print (" ")

respuesta = input("ELIGE UNA OPCION: ")

print (" ")

if respuesta == "1":
        def encriptado():
                print ("cifrar")
                mensaje = input("ESCRIBE UN MENSAJE: ")
                llave = int(input("QUE ROT ELIGES: "))
                cifrado = encipher_shift(mensaje,llave)
                print (cifrado)
        encriptado()

elif respuesta == "2":
        def desencriptado():
                print ("descifrar")
                mensaje = input("ESCRIBE UN MENSAJE: ")
                llave = int(input("QUE ROT ELIGES: "))
                descifrado = decipher_shift(mensaje,-llave)
                print (descifrado)
        desencriptado()


print (" ")

print (R+"GRACIAS POR USAR EL SCRIP")

print (" ")

print ("LUCI@ MODZ")

print (" ")

print (Y+"SALIENDO ......")


os.system(" toilet -f mono12 -F gay LUCIA")

os.system(" toilet -f mono12 -F gay MODZ")
