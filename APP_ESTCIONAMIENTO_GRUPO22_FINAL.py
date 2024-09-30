# PROYECTO FINAL GRUPO 22 #

# Autores:  ROBERTO FIORI #  DARIO BOSQUE 

# Titulo : APLICACION ESTACIONAMIENTO MEDIDO Y PAGO #

# Breve descripcion: El presente proyecto desarrolla una aplicacion de administracion de estacionamiento en zonas centricas de una ciudad #

# Fecha : 2024

# Version : 1.0


# Requerimientos 

# - Python 3.08 o superior
# - colorama
# - datetime
# - json
# - time
# - re
# - os

import os
import json
import colorama  # pip install colorama / pip3 install colorama
import datetime
import time
import re

# Se establecen las variables globales 

registro_patentes =[]
notificaciones = ["Permitir Notificaciones","Sonidos","Vibrar","Globos en los iconos","Ver en Pantalla Bloqueada","Regresar al menu principal"]
semanaEstacionamiento = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
horarioEstacionamiento = ["1 hora","2 horas","3 horas","4 horas","5 horas","6 horas","7 horas","8 horas","9 horas","10 horas","11 horas","12 horas"]
saldo = 0
historial = []
inicio_estacionamiento = None
precio_por_hora = 300  # Precio por hora de estacionamiento
patron_patente = re.compile(r'^[a-z]{2}\d{3}[a-z]{2}$')


# Archivo .json de "usuarios"
users_file = 'usuarios.json'
patentes_file = 'patentes.json'

####### FUNCIONES ####### 

# MENU UTILIDADES #
def menuUtilidades():
    '''
    Funcion Menu Utilidades
    presenta un menu de utilidades al usuario para poder configurar en caso de ser necesario.
    Parametros: 
    No espera
    Retorna:
    Retornara la opcion seleccionada por el usuario.
    Autor: Dario Bosque
    Colaboradores:
    '''
    while True:
        limpiarPantalla()
        print(colorama.Fore.GREEN + "-MENU UTILIDADES-".center(70))
        print("="*70)
        print()
        print(colorama.Fore.BLUE + "\t1 Alarma: "+ colorama.Fore.RESET + "Configurar Alarma.")
        print(colorama.Fore.BLUE + "\t2 Administrar Patentes: "+ colorama.Fore.RESET + "Dar de alta o Baja la Patente.")
        print(colorama.Fore.BLUE + "\t3 Contactanos: "+ colorama.Fore.RESET + "Realizar Consulta.")
        print(colorama.Fore.BLUE + "\t4 Ayuda: "+ colorama.Fore.RESET + "Solicitar Asistencia.")
        print(colorama.Fore.BLUE + "\t5 Notificaciones: "+ colorama.Fore.RESET + "Configurar Notificaciones.")
        print(colorama.Fore.BLUE + "\t6 Estacionamiento Programado: "+ colorama.Fore.RESET + "Configurar Estacionamiento.")
        print(colorama.Fore.BLUE + "\t7 Volver al Menu Principal"+ colorama.Fore.RESET)
        print()
        try:
            op = int(input("Seleccione una opcion: " + colorama.Fore.BLUE))
            print()
        except ValueError:
            print(colorama.Fore.RED + "Error: Debe seleccionar una opción valida.")
            input(colorama.Fore.RESET + "Presione enter para continuar...")
            continue
        
        if op == 1:
            limpiarPantalla()
            print(colorama.Fore.LIGHTYELLOW_EX + "-CONFIGURAR ALARMA-".center(60))
            programar_alarma()
            input(colorama.Fore.RESET +"Presione enter para continuar...")
        elif op == 2:
            limpiarPantalla()
            print(colorama.Fore.LIGHTYELLOW_EX +"-ADMINISTRAR PATENTES-".center(60))
            crear_menu_administrar_patente()
            input(colorama.Fore.RESET+"Presione enter para continuar...")
        elif op == 3:
            limpiarPantalla()
            print(colorama.Fore.LIGHTYELLOW_EX +"-CONTACTANOS-".center(60))           
            contactar()
            input(colorama.Fore.RESET+"Presione enter para continuar...")
        elif op == 4:
            limpiarPantalla()
            print(colorama.Fore.LIGHTYELLOW_EX+"-AYUDA-".center(60))
            ayudar()
            input(colorama.Fore.RESET+"Presione enter para continuar...")           
        elif op == 5:
            limpiarPantalla()
            print(colorama.Fore.LIGHTYELLOW_EX + "-NOTIFICACIONES-".center(60))
            menu_notificaciones()
            input(colorama.Fore.RESET+ "Presione enter para continuar...")
        elif op == 6:
            limpiarPantalla()        
            print(colorama.Fore.LIGHTYELLOW_EX +"-ESTACIONAMIENTO PROGRAMADO-".center(60))
            programar_estacionamiento()
            input(colorama.Fore.RESET+ "Presione enter para continuar...")
        elif op == 7:
            print(colorama.Fore.LIGHTYELLOW_EX+"Regresar al menu principal!")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            break           
        else:
            print(colorama.Fore.RED + "Error: Debe seleccionar una opción valida.")
            input(colorama.Fore.LIGHTBLACK_EX + "Presione enter para continuar...")
    return menu_menues()
print(colorama.Fore.RESET+"Gracias por usar el sistema!")

#Funcion limpiar pantalla
def limpiarPantalla():
    '''
    Funcion limpiar pantalla
    limpia la consola
    Parametros: 
    no espera
    Retorno:    
    no tiene 
    Autor: Sergio Serbluk
    Colaboradores: 
        
    '''
    os.system('cls'if os.name=='nt' else 'clear')

#Funcion programar alarma
def programar_alarma():
    '''
    Funcion programar Alarma para un periodo de tiempo especifico
    Configura Alarma de alerta de fin de estacionamiento.
    Parametros: 
    no espera
    Retorno:    
    no tiene 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    while True:
        try:
            # Solicitar al usuario ingresar las horas
            print()
            horas = int(input(colorama.Fore.RESET+"Ingrese el turno de estacionamiento en horas (entre 1 y 12): "+colorama.Fore.BLUE))
            
            # Validar que las horas estén dentro del rango permitido
            if 1 <= horas <= 12:
                print(colorama.Fore.GREEN+"Alarma establecida!")
                print(colorama.Fore.LIGHTWHITE_EX+"Recibira un recordatorio"+ colorama.Fore.BLUE+" 10 minutos "+colorama.Fore.RESET+"antes de finalizacion del turno!")
                break
            else:
                print(colorama.Fore.RED +"El periodo de estacionamiento debe ser entre 1 y 12 horas. Intente nuevamente!")
        except ValueError:
            print(colorama.Fore.LIGHTRED_EX +"Entrada no válida. Por favor, ingrese un número entero!")

    # Calcular el tiempo total en minutos para la prueba rápida
    total_minutos = horas * 60
    # Calcular el tiempo total en segundos para la prueba rápida
    total_segundos = total_minutos * 60
    
    # Calcular el tiempo hasta el aviso de los 10 minutos (3590 segundos/ numero colocado para ejecutar la prueba rapido)
    aviso_segundos = total_segundos - 3590

    # Dormir hasta que queden 10 minutos para finalizar el estacionamiento
    time.sleep(aviso_segundos)
    
    # Imprimir el mensaje de alerta
    print()
    print(colorama.Fore.BLUE+"¡Quedan 10 minutos para finalizar el permiso de estacionamiento!")
    print(colorama.Fore.RESET+"Gracias por utilizar nuestros servicios!")  
    return

#Funcion contactar    
def contactar ():
    '''
    Funcion contactar
    Brinda un mensaje con los medios de contacto, para establecer comunicacion del usuario, con la empresa prestadora del servicio.
    Parametros: 
    no espera
    Retorno:    
    no tiene 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    print()
    print(colorama.Fore.BLUE+ "\tCorreo Electronico: " +colorama.Fore.LIGHTWHITE_EX+"empresa@empresa.com")
    print(colorama.Fore.BLUE+ "\tAtencion Telefonica: " +colorama.Fore.LIGHTWHITE_EX+ "0800-555-1234")
    print()
    return

#Funcion ayudar
def ayudar ():
    '''
    Funcion ayudar
    Brinda un mensaje con la Url del concesionario del servicio, en donde se encuentra el apartado preguntas frecuentes.
    Parametros: 
    no espera
    Retorno:    
    no tiene 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    print()
    print(colorama.Fore.LIGHTWHITE_EX+"Para dudas y consultas con el uso de la aplicacion, dirijase a la seccion \nde preguntas frecuentes en el siguiente link:\n", end="" )
    print(colorama.Fore.BLUE + "https://municipio.com.ar/estacionamiento-medido/faq")
    print()
    return

#MENU ADMINISTRAR PATENTE
def crear_menu_administrar_patente():
    '''
    Funcion Menu Administrar Patentes
    presenta un menu de registro de patentes, eliminacion o listado de los datos registrados por el usuario.
    Parametros: 
    No espera
    Retorna:
    Retornara la opcion seleccionada por el usuario.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    print()
    print(colorama.Fore.RESET +"1- Agregar / 2- Eliminar / 3- Listar / 4- Salir del Menu".center(60))
    print()
    try:
        op = int(input(colorama.Fore.RESET+"Seleccione una opcion: "+colorama.Fore.BLUE))
        print()    
        if op == 1:
            print(colorama.Fore.RESET +"Opcion Seleccionada: "+colorama.Fore.BLUE+ "Agregar! ")
            agregar_patente(registro_patentes)
        elif op == 2:
            print(colorama.Fore.RESET +"Opcion Seleccionada: "+colorama.Fore.BLUE+"Eliminar! ")
            eliminar_patente(registro_patentes)
        elif op == 3:
            print(colorama.Fore.RESET +"Opcion Seleccionada: "+colorama.Fore.BLUE+"Listar! ")
            listar_patentes(registro_patentes)
        elif op == 4:
            print(colorama.Fore.BLUE+"Salir del menu!")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            menuUtilidades()
    except ValueError:
        print(colorama.Fore.RED +"Error! Debe ingresar un numero!" + colorama.Fore.RESET)
        return

#Funcion leer patentes
def leer_patentes():
    '''
    Funcion leer patentes
    permite leer los datos guardados por el ususario con anterioridad.
    Parametros: 
    No espera
    Retorna:
    Retornara la opcion seleccionada por el usuario.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    try:
        with open('patentes.json', 'r') as file:
            patentes = json.load(file)
            return patentes
    except FileNotFoundError:
        print(colorama.Fore.RED+"El archivo no se encontro!"+colorama.Fore.RESET)
        return {}

#Funcion escribir patentes
def escribir_patentes(data):
    '''
    Funcion escribir patentes
    permite dar persistencia a los datos ingresados por el ususario.
    Parametros: 
    Espera
    Retorna:
    No espera.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    with open('patentes.json', 'w') as file:
        json.dump(data, file, indent=4)

#Funcion agregar patente
def agregar_patente(patente):
    '''
    Funcion agregar patentes
    permite al usuario agregar patentes para poder utilizar con la app.
    Parametros: 
    Espera
    Retorna:
    No espera.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    patentes = leer_patentes()
    usuario = input(colorama.Fore.RESET+"Ingrese su nombre de usuario: "+colorama.Fore.BLUE)

    if usuario not in patentes:
        patentes[usuario] = []

    patente = input(colorama.Fore.RESET+"Ingrese los datos de la patente (formato aa123aa): "+colorama.Fore.BLUE)
    if validar_patente(patente):
        if patente not in patentes[usuario]:
            patentes[usuario].append(patente)
            escribir_patentes(patentes)
            print(colorama.Fore.RESET+f"La patente {colorama.Fore.BLUE}{patente} {colorama.Fore.RESET}fue agregada correctamente.")
        else:
            print(colorama.Fore.RESET+f"La patente {colorama.Fore.BLUE}{patente}{colorama.Fore.RESET} ya está registrada.")
    else:
        print(colorama.Fore.RESET+f"La patente {colorama.Fore.RED}{patente}{colorama.Fore.RESET} no tiene un formato válido.")
    
    while True:
        op = input(colorama.Fore.RESET+"¿Desea cargar otra patente? (s/n): "+colorama. Fore.BLUE)

        if op.lower() == "s":
            agregar_patente(patente)
            break
        elif op.lower() == "n":
            print(colorama.Fore.GREEN+"¡Gracias por utilizar el sistema!"+colorama.Fore.RESET)
            break
        else:
            print(colorama.Fore.RED+"Opción no válida. Por favor, ingrese 's' o 'n'."+colorama.Fore.RESET)

#Funcion eliminar patente
def eliminar_patente(patente):
    '''
    Funcion eliminar patentes
    permite al usuario eliminar patentes registradas con anterioridad.
    Parametros: 
    Espera
    Retorna:
    No espera.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    patentes = leer_patentes()
    usuario = input(colorama.Fore.RESET+"Ingrese su nombre de usuario: "+colorama.Fore.BLUE)

    if usuario not in patentes or not patentes[usuario]:
        print(colorama.Fore.RED+"No hay patentes registradas para este usuario."+colorama.Fore.RESET)
        return

    patente = input(colorama.Fore.RESET+"Ingrese los datos de la patente (formato aa123aa): "+colorama.Fore.BLUE)
    if validar_patente(patente):
        if patente in patentes[usuario]:
            patentes[usuario].remove(patente)
            escribir_patentes(patentes)
            print(colorama.Fore.RESET+f"La patente {colorama.Fore.BLUE}{patente} {colorama.Fore.RESET}fue eliminada correctamente.")
        else:
            print(colorama.Fore.RESET+f"La patente {colorama.Fore.BLUE}{patente}{colorama.Fore.RESET} no está registrada.")
    else:
        print(colorama.Fore.RESET+f"La patente {colorama.Fore.RED}{patente}{colorama.Fore.RESET} no tiene un formato válido.")
    
    while True:
        op = input(colorama.Fore.RESET+"¿Desea cargar otra patente? (s/n): "+colorama. Fore.BLUE)
        if op.lower() == "s":
            eliminar_patente(patente)
            break
        elif op.lower() == "n":
            print(colorama.Fore.GREEN+"¡Gracias por utilizar el sistema!"+colorama.Fore.RESET)
            break
        else:
            print(colorama.Fore.RED+"Opción no válida. Por favor, ingrese 's' o 'n'."+colorama.Fore.RESET)
            
#Funcion listar patentes            
def listar_patentes(patente):
    '''
    Funcion listar patentes
    permite al usuario listar las patentes registradas, para decidir si desea conservarlas o no.
    Parametros: 
    Espera
    Retorna:
    No espera.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
    patentes = leer_patentes()
    usuario = input(colorama.Fore.RESET+"Ingrese su nombre de usuario: "+colorama.Fore.BLUE)

    if usuario not in patentes or not patentes[usuario]:
        print(colorama.Fore.RED+"No hay patentes registradas para este usuario."+colorama.Fore.RESET)
        return

    print(colorama.Fore.LIGHTGREEN_EX + "Listado de Patentes Registradas:")
    for patente in patentes[usuario]:
        print(colorama.Fore.BLUE + f"{patente}".center(30," "))

#Funcion validar patentes
def validar_patente(patente):
    '''
    Funcion Validar Patente
    Valida que los datos ingresados por el usuario posean el formato correcto.
    Parametros: 
    Espera
    Retorno:    
    Retornara verdadero en caso de ser correcto o false en caso de no serlo. 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    if patron_patente.fullmatch(patente.lower()):
        return True
    else:
        return False

#Funcion validar email
def validar_email(email):
    email = email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        print(colorama.Fore.BLUE + "El email no es válido.")
        return False
    return

#Funcion validar password
#falta crear

#MENU NOTIFICACIONES        
def menu_notificaciones():
    '''
    Funcion Menu Notificaciones
    Presenta un menu de opciones al usuario para poder seleccionar.
    Parametros: 
    No espera
    Retorno:    
    Retornara la opcion seleccionada por el usuario. 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    while True:    
        limpiarPantalla()
        print(colorama.Fore.LIGHTYELLOW_EX+"-NOTIFICACIONES-".center(60))
        print()
        print(colorama.Fore.BLUE+ "\t1 " + colorama.Fore.RESET+"Permitir Notificaciones")        
        print(colorama.Fore.BLUE+ "\t2 " + colorama.Fore.RESET+"Sonidos")        
        print(colorama.Fore.BLUE+ "\t3 " + colorama.Fore.RESET+"Vibrar")        
        print(colorama.Fore.BLUE+ "\t4 " + colorama.Fore.RESET+"Globos en los iconos")        
        print(colorama.Fore.BLUE+ "\t5 " + colorama.Fore.RESET+"Ver en Pantalla Bloqueada")        
        print(colorama.Fore.BLUE+ "\t6 " + colorama.Fore.RESET+"Regresar al menu principal" + colorama.Fore.RESET)
        print()        
        try:
            opcion = int(input("Seleccione una opcion: " +colorama.Fore.BLUE))
            print()
        except ValueError:
            print(colorama.Fore.RED + "Error: Debe seleccionar una opción valida.")
            input(colorama.Fore.RESET+"Presione enter para continuar...")              
            continue
        if opcion not in range(1,7):
            print(colorama.Fore.RED + "Error: Debe seleccionar una opción valida.")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            continue
        if opcion == 6:
            print(colorama.Fore.BLUE+"Salir al menu principal!")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            menu_menues()
        
        limpiarPantalla()
        print(colorama.Fore.BLUE + f"Opción elegida: {colorama.Fore.RESET + notificaciones[opcion-1]}".center(60))
        print()
        print("1- Activar / 2 Desactivar / 3 Salir del Menú".center(60))
        print()        
        try:
            activacion = int(input(colorama.Fore.RESET+ "Elija una opción: "+ colorama.Fore.BLUE))
        except ValueError:
            print(colorama.Fore.RED+"Opción no válida, debe ser un número. Intente de nuevo.")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            continue
        if activacion not in range(1,4):
            print(colorama.Fore.RED + "Error: Debe seleccionar una opción valida.")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            continue
        if activacion == 1:
            print(colorama.Fore.GREEN+"Activar!")
            activar_notificacion()
        if activacion == 2:
            print(colorama.Fore.GREEN+"Desactivar!")
            desactivar_notificacion()
        if activacion == 3:
            print(colorama.Fore.GREEN+"Salir del menu!")
            input(colorama.Fore.RESET+"Presione enter para continuar...")
            menu_notificaciones()

#Funcion activar notificacion            
def activar_notificacion():
    '''
    Funcion Activar
    Brinda la opcion de activar la notificacion elegida por el usuario.
    Parametros: 
    No espera
    Retorno:    
    Retornara la opcion seleccionada por el usuario. 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    print(colorama.Fore.LIGHTBLUE_EX+"Notificacion activada!")
    input(colorama.Fore.RESET+"Presione enter para regresar al menu anterior...")              
    return menu_notificaciones()

#Funcion desactivar notificacion
def desactivar_notificacion():
    '''
    Funcion Desactivar
    Brinda la opcion de desactivar la notificacion elegida por el usuario.
    Parametros: 
    No espera
    Retorno:    
    Retornara la opcion seleccionada por el usuario. 
    Autor: Dario Bosque.
    Colaboradores:
    '''
    print(colorama.Fore.LIGHTBLUE_EX+"Notificacion desactivada!")
    input(colorama.Fore.RESET+"Presione enter para regresar al menu anterior...")
    return menu_notificaciones() 

#Funcion programar estacionamiento        
def programar_estacionamiento():
        '''
    Funcion programar estacionamiento
    permite al usuario establecer el dia, y la duracion del turno de estacionamiento previamente.
    Parametros: 
    Espera
    Retorna:
    No espera.
    Autor: Dario Bosque.
    Colaboradores:
    
    '''
        print()
        print(colorama.Fore.BLUE+"Vigencia de estacionamiento: "+ colorama.Fore.RESET+"Lunes a Viernes en el horario de 7 a 20 horas!")
        while True:
            dia = input(colorama.Fore.RESET+"Ingrese el día de la semana que desea estacionar: "+ colorama.Fore.BLUE)
            if dia.lower() in [d.lower() for d in semanaEstacionamiento]:
                break
            else:
                print(colorama.Fore.RED+"Error, el día ingresado no es válido. Intente nuevamente")      
            
        while True:
            try:
                horaInicio = int(input(colorama.Fore.RESET+"Ingrese el horario de inicio: (entre 7 Am y 19 Pm):  "+ colorama.Fore.BLUE))
                horaFin = int(input(colorama.Fore.RESET+"Ingrese el horario de fin: (entre 8 Am y 20 Pm):  "+ colorama.Fore.BLUE))
                if 7 <= horaInicio <= 19 and 8 <= horaFin <= 20 and horaInicio < horaFin:
                    turnoEstacionamiento = horaFin - horaInicio 
                    break
                else:
                    print(colorama.Fore.RED+"Las horas deben estar dentro del rango y la hora de inicio debe ser menor que la hora de fin")
            except ValueError:
                print(colorama.Fore.RED+"Ingrese un dato valido!")
                
                    
        for d in semanaEstacionamiento:
                if dia.lower() == d.lower():
                    print()
                    print(colorama.Fore.RESET+f"Estacionamiento programado para el dia {colorama.Fore.BLUE}{d}{colorama.Fore.RESET}, duracion del turno {colorama.Fore.BLUE}{horarioEstacionamiento[turnoEstacionamiento-1]}"+colorama.Fore.RESET)
                    break


# MENU #
# con "if" se verifica que se encuentra creado el archivo 'usuarios.json' , al devolver "True" existe, en el caso de devolver "false" se lo crea
# Funcion de carga usuarios desde archivo JSON
def cargar_usuarios():
    try:
        with open(users_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Se define una función "guardar_usuarios" que toma un parámetro (users) , abre un archivo en modo de escritura ('w')
# "with" asegura que el archivo se cierre correctamente luego de la escritura
# Guardar usuarios en archivo JSON
def guardar_usuarios(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=4)

# Cargar usuarios al inicio
users = cargar_usuarios()

# LIMPIAR PANTALLA (CLS)
# Autor: Sergio Serbluk
# Funcion llama al comando "cls" para limpiar pantalla , y asi lograr ser mas amigable visualmente al usuario
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# MENU ACERCA DE
# Llama a la funcion "limpiarPantalla" y muestra una secuencia de "print" con la informacion de la aplicacion
def acerca_de():
    limpiarPantalla()
    print(colorama.Fore.GREEN + "APLICACION ESTACIONAMIENTO".center(50))
    print("=" * 50)
    print()
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " ACERCA DE ... ".center(50))
    print()
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " APLICACION ESTACIONAMIENTO ".center(50))
    print()
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " CODO A CODO INICIAL".center(50))
    print()    
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " VERSION 1.0 ".center(50))
    print()    
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " 2024 ".center(50))
    print()    
    print(colorama.Fore.BLUE + colorama.Fore.RESET + " DESARROLLADO POR  - GRUPO 22 ".center(50))
    print()


# MENU SALDOS 
# Cargar "datos" desde el archivo JSON , donde se volcaran los datos sobre saldos
try:
    with open('datos.json', 'r') as file:
        datos = json.load(file)
        saldo = datos.get('saldo', 0)
        historial = [(datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S'), mov) for fecha, mov in datos.get('historial', [])]
except FileNotFoundError:
    saldo = 0
    historial = []

# Se crea "saldo_menu" tomando las variables globales para su correcta ejecucion dentro de la funcion, contiene las opciones:
# " Comprar Creditos " -  Asigna valores en pesos a credito del usuario anteriormente logeado
# " Movimientos "      -  Muestra un historial de maximo 5 movimientos hechos
# " Saldo  "           -  Muestra saldo remanente
# " VOLVER AL MENU PRINCIPAL " - Vuelve a menu principal "menu_menues"
# Mediante colorama se agrega colores diferenciales al menu
# Se utiliza "try/except" para validar la entrada de un entero (int) y enviar un mensaje de error en el caso que no lo sea
# Opcion 1 - Compra de Creditos:
# Se utiliza "try/except" para validar la entrada de un entero (int) y enviar un mensaje de error en el caso que no lo sea
# Se llama a la lista "historial" para agregar en cada carga el dato de fecha y hora mediate "datetime", utilizado "datetime.datetime.now()"
# Al saldo se le suma la carga "saldo += carga" y se lo imprime mediante un "print"
# Opcion 2 - Movimientos:Opcion 2 - Movimientos:
# Se utiliza un bucle "for" para iterar los últimos 5 elementos de la lista "historial" y asi mostrar los ultimos 5 movimientos hechos
# Se utiliza el método "strftime" para imprimir la fecha en el formato "Año-Mes-Día Hora:Minuto
# Opcion 3 - Saldo:
# Se mmuestra la variable "saldo" mediante un "print" formateado
# Opcion 4 - VOLVER AL MENU PRINCIPAL:
# Vuelve a 'menu_menues" mediante un "break" saliendo de la funcion "saldo_menu"

def saldo_menu():
    global saldo, historial
    while True:
        limpiarPantalla()
        print(colorama.Fore.GREEN + "APLICACION ESTACIONAMIENTO".center(50))
        print("=" * 50)
        print()
        print(colorama.Fore.BLUE + colorama.Fore.RESET + " MENU SALDOS ".center(50))
        print()
        print(colorama.Fore.BLUE + "\t1 :" + colorama.Fore.RESET + " Comprar Creditos ")
        print(colorama.Fore.BLUE + "\t2 :" + colorama.Fore.RESET + " Movimientos ")
        print(colorama.Fore.BLUE + "\t3 :" + colorama.Fore.RESET + " Saldo  ")
        print(colorama.Fore.BLUE + "\t4 :" + colorama.Fore.RESET + " VOLVER AL MENU PRINCIPAL ")
        print()
        try:
            op = int(input("Seleccione una opción: " + colorama.Fore.BLUE))
        except ValueError:
            print(colorama.Fore.RED + "Opción inválida! Debe ser un número.")
            input(colorama.Fore.RED + "Presione enter para continuar...")
            continue

        print(colorama.Fore.RESET)

        if op == 1:
            print("Comprar Creditos")
            print()
            try:
                carga = int(input("Ingrese importe a cargar: "))
            except ValueError:
                print(colorama.Fore.RED + "Importe inválido! Debe ser un número.")
                input(colorama.Fore.RED + "Presione enter para continuar...")
                continue
            historial.append((datetime.datetime.now(), carga))
            print()
            print(f"Se ha cargado: ${carga}")
            saldo += carga
            # Guardar datos en el archivo JSON
            with open('datos.json', 'w') as file:
                datos = {
                    'saldo': saldo,
                    'historial': [(fecha.strftime('%Y-%m-%d %H:%M:%S'), mov) for fecha, mov in historial]
                }
                json.dump(datos, file)
            print()
            print(f"{'*' * 15} SALDO DISPONIBLE: ${saldo} {'*' * 15}")
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 2:
            print("Movimientos:")
            for fecha, mov in historial[-5:]:
                print(f"{fecha.strftime('%Y-%m-%d %H:%M:%S')} - ${mov}")
            print()
            print(f"{'*' * 15} SALDO DISPONIBLE: ${saldo} {'*' * 15}")
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 3:
            print("Saldo: ")
            print(f"{'*' * 15} SALDO DISPONIBLE: ${saldo} {'*' * 15}")
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 4:
            break
        else:
            print(colorama.Fore.RED + "Opción incorrecta!")
            input(colorama.Fore.RED + "Presione enter para continuar...")

# MENU ESTACIONAR
# Se crea "menu_estacionar" invocando las variables globales "inicio_estacionamiento" ,"saldo" y "precio_por_hora" para su correcta ejecucion dentro de la funcion 
# Contiene las opciones:
# " Microcentro " - Inicio estacionamiento en esa ubicacion
# " Centro "      - Inicio estacionamiento en esa ubicacion
# " Macrocentro " - Inicio estacionamiento en esa ubicacion
# " Terminar Estacionamiento " - termina con el estacionamiento iniciado con las 3 opciones anteriores
# " VOLVER AL MENU PRINCIPAL " - Vuelve a menu principal "menu_menues"
# Se utiliza "try/except" para validar la entrada de un entero (int) y enviar un mensaje de error en el caso que no lo sea
# Mediante un "if" anidado dentro de otro "if" se chequea que el "inicio_estacionamiento" este en "none"
# Opcion 1, 2 y 3 - : - En el caso de que "inicio_estacionamiento" este en "none" ejecuta la siguiente linea dando a la variable "inicio_estacionamiento" en valor que le asiga "datetime" 
# Opcion 4 : la linea "elif" la variable se le asigna el valor mediante "datetime" a "fin_estacionamiento" , cerrando el estacionamiento
# Restando estos dos valores ("inicio_estacionamiento" y "fin_estacionamiento") obtenemos la variable "duracion" que nos da la cantidad de tiempo que esto estacionado en vehiculo
# Se convierte a horas la duracion del estacionamiento mediante la linea "horas = duracion.total_seconds() / 3600"
# Teniendo la variable "horas" se calcula el costo total basado la variable "horas" y la variable global "precio por hora", se redondea con round (,2) para solo ver en el costo final solo 2 decimales 
# Mediante un "if" se compara "costo > saldo" y nos imprime "Saldo insuficiente para cubrir el costo de estacionamiento." en el caso que el saldo sea menor que el costo
# Con el "else" (en caso que el saldo sea suficiente) se imprime la duracion y el costo del estacionamiento mostrando 2 decimales mediante el ".2f" en el costo del estacionamiento y el saldo restante
# Opcion 5 :Vuelve a 'menu_menues" mediante un "break" saliendo de la funcion "menu_estacionar"
# Si se da entrada a un valor mayor a 5 se imprime un mensaje de "Opción incorrecta!" y un input de "Presione enter para continuar..."

# Cargar datos desde el archivo JSON ESTACIONAR
try:
    with open('datos.json', 'r') as file:
        datos = json.load(file)
        saldo = datos.get('saldo', 0)
        historial = [(datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S'), mov) for fecha, mov in datos.get('historial', [])]
except FileNotFoundError:
    saldo = 0
    historial = []

def actualizar_datos():
    with open('datos.json', 'w') as file:
        datos = {
            'saldo': saldo,
            'historial': [(fecha.strftime('%Y-%m-%d %H:%M:%S'), mov) for fecha, mov in historial]
        }
        json.dump(datos, file)

def menu_estacionar():
    global inicio_estacionamiento, saldo, precio_por_hora
    while True:
        limpiarPantalla()
        print(colorama.Fore.GREEN + "APLICACION ESTACIONAMIENTO".center(50))
        print("=" * 50)
        print()
        print(colorama.Fore.BLUE + colorama.Fore.RESET + " BIENVENIDO A LA APP DE ESTACIONAMIENTO".center(50))
        print()
        print(colorama.Fore.BLUE + colorama.Fore.RESET + "  - MENU SALDOS - ".center(50))
        print()
        print(colorama.Fore.BLUE + "\t1 :" + colorama.Fore.RESET + " Microcentro ")
        print(colorama.Fore.BLUE + "\t2 :" + colorama.Fore.RESET + " Centro ")
        print(colorama.Fore.BLUE + "\t3 :" + colorama.Fore.RESET + " Macrocentro  ")
        print(colorama.Fore.BLUE + "\t4 :" + colorama.Fore.RESET + " Terminar Estacionamiento ")
        print(colorama.Fore.BLUE + "\t5 :" + colorama.Fore.RESET + " VOLVER AL MENU PRINCIPAL ")
        print()
        try:
            op = int(input("Seleccione una opción: " + colorama.Fore.BLUE))
        except ValueError:
            print(colorama.Fore.RED + "Opción inválida! Debe ser un número.")
            input(colorama.Fore.RED + "Presione enter para continuar...")
            continue

        print(colorama.Fore.RESET)

        if op in [1, 2, 3]:
            if inicio_estacionamiento is None:
                inicio_estacionamiento = datetime.datetime.now()
                print(f"Inicio de estacionamiento en {['Microcentro', 'Centro', 'Macrocentro'][op-1]} a las {inicio_estacionamiento.strftime('%H:%M:%S')}")
            else:
                print("Ya tiene un estacionamiento en curso.")
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 4:
            if inicio_estacionamiento is not None:
                fin_estacionamiento = datetime.datetime.now()
                print(f"Terminar Estacionamiento a las {fin_estacionamiento.strftime('%H:%M:%S')}")
                duracion = fin_estacionamiento - inicio_estacionamiento
                horas = duracion.total_seconds() / 3600  # Convierte la duración a horas
                costo = round(horas * precio_por_hora, 2)
                if costo > saldo:
                    print(colorama.Fore.RED + "Saldo insuficiente para cubrir el costo de estacionamiento.")
                else:
                    saldo -= costo
                    historial.append((datetime.datetime.now(), -costo))
                    print(f"Duración del estacionamiento: {duracion}")
                    print(f"Costo del estacionamiento: ${costo:.2f}")
                    actualizar_datos()  # Guardar datos después de cada cambio
                print(f"Saldo restante: ${saldo:.2f}")
                inicio_estacionamiento = None
            else:
                print("No hay un estacionamiento en curso.")
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 5:
            break
        else:
            print(colorama.Fore.RED + "Opción incorrecta!")
            input(colorama.Fore.RED + "Presione enter para continuar...")

# MENU PRINCIPAL
# La funcion "menu_menues" es un  bucle "while" que presenta un menu con las diferentes entradas a otros menues 
# Pide con un "input" el valor de la variable (entero , int) "op" , mediante un "try/except" si entrada no es "int", se captura la excepción "ValueError"y  reinicia el bucle.
# Opcion 1 : llama a la funcion "menu_estacionar"
# Opcion 2 : llama a la funcion "saldo_menu"
# Opcion 3 : llama a la funcion ""(UTILIDADES)
# Opcion 4 : llama a la funcion ""(ACERCA DE...)
# Opcion 5 : Mediante un "Break" vuelve al menu "main" 
def menu_menues():
    while True:
        limpiarPantalla()
        print(colorama.Fore.GREEN + "APLICACION ESTACIONAMIENTO".center(50))
        print("=" * 50)
        print()
        print(colorama.Fore.BLUE + colorama.Fore.RESET + " MENU PRINCIPAL ".center(50))
        print()
        print(colorama.Fore.BLUE + "\t1 :" + colorama.Fore.RESET + " ESTACIONAR ")
        print(colorama.Fore.BLUE + "\t2 :" + colorama.Fore.RESET + " SALDOS / CARGA ")
        print(colorama.Fore.BLUE + "\t3 :" + colorama.Fore.RESET + " UTILIDADES  ")
        print(colorama.Fore.BLUE + "\t4 :" + colorama.Fore.RESET + " ACERCA DE... ")
        print(colorama.Fore.BLUE + "\t5 :" + colorama.Fore.RESET + " CERRAR SESION ")
        print()
        print()
        print(colorama.Fore.GREEN + "IMPORTANTE: SI AUN NO A CARGADO SU PATENTE".center(50))
        print(colorama.Fore.GREEN + "INGRESE A UTILIDADES (opcion 3)".center(50))
        print(colorama.Fore.GREEN + "Y LUEGO A ADMINISTRAR PATENTES (opcion 2)".center(50))
        print()
        print()
        try:
            op = int(input("Seleccione una opción: " + colorama.Fore.BLUE))
        except ValueError:
            print(colorama.Fore.RED + "Opción inválida! Debe ser un número.")
            input(colorama.Fore.RED + "Presione enter para continuar...")
            continue

        print(colorama.Fore.RESET)
        if op == 1:
            menu_estacionar()
        elif op == 2:
            saldo_menu()
        elif op == 3:
            menuUtilidades()
        elif op == 4:
            acerca_de()
            input(colorama.Fore.RED + "Presione enter para continuar...")
        elif op == 5:
            break         
            print(colorama.Fore.RED + "GRACIAS POR USAR LA APLICACION")
        
        else:
            print(colorama.Fore.RED + "Opción incorrecta!")
            input(colorama.Fore.RED + "Presione enter para continuar...")

# CREAR NUEVO USUARIO
# Se pide entrada de un nuevo nombre de usuario y mediante un "if" se lo busca en "users" y se lo valida en el caso que no exista con anterioridad
# Se pide contraseña y agrega el nombre de usuario y la contraseña como una entrada en el diccionario "users"
# Imprime indicando que el usuario ha sido creado exitosamente
# Mediante un input pide presionar cualquier tecla ("Presione enter para continuar...)
# Limpia pantalla 
def create_user():
    limpiarPantalla()
    print(colorama.Fore.GREEN + "Registro de Usuario".center(50))
    print()
    print("="*70)
    print()
    users = cargar_usuarios()
    username = input("Ingrese su nombre: ")
    if username in users:
        print(colorama.Fore.BLUE + "El usuario ya existe.")
        print()
        input(colorama.Fore.BLUE + "Presione enter para continuar...")
        return
    print()
    email = input("Ingrese su email: ")
    #validar email
    if not validar_email(email):
        input("Presione enter para continuar...")
        return    
    print()
    password = input("Introduce una contraseña: ")
    #validar password
    
    users[username] = {
        "email": email,
        "password": password
    }
    guardar_usuarios(users)
    print(colorama.Fore.BLUE+f"Usuario {username} registrado exitosamente.")
    input("Presione enter para continuar...")


# INICIAR SESION
# Se pide entrada de nombre de usuario y mediante un "if" se lo busca en "users", si no lo encuentra imprime "Usuario no encontrado.", en caso contrario lo valida 
# Pide contraseña y mediante otro "if" se fija que al "username" anteriormente ingresado haga conicida con su contraseña "password"
# De ser correcto se da mensaje de bienvenida , limpia pantalla y ejecuta funcion "menu_menues" llevandolo al "MENU PRINCIPAL"
# Con el "else" maneja la opcion de que la contraseña no sea la correcta y limpia pantalla 
def login():
    users = cargar_usuarios()
    username = input("Introduce tu nombre de usuario: ")
    if username not in users:
        print(colorama.Fore.RED + "Usuario no encontrado.")
        input(colorama.Fore.RED + "Presione enter para continuar...")
        limpiarPantalla()
        return False
    password = input("Introduce tu contraseña: ")
    if users[username]["password"] == password:
        print(f"Bienvenido {username}")
        input(colorama.Fore.GREEN + "Presione enter para continuar...")
        limpiarPantalla()
        menu_menues()
    else:
        print(colorama.Fore.RED + "Contraseña incorrecta.")
        input(colorama.Fore.RED + "Presione enter para continuar...")
        limpiarPantalla()

# MENU LOGIN
# La funcion "main" es un  bucle "while" que presenta un menu con las opciones de logeo de usuario y creacion de usuario 
# Pide con un "input" el valor de la variable (entero , int) "choice" 
# Mediante un "if" analiza la variable "choice"
# Opcion 1 : llama a la funcion "login" para entrar un usuario/contraseña ya creado, buscandolo en el archivo "usuarios.json"
# Opcion 2 : llama a la funcion "create_user" la cual pide crear un usuario/contraseña, agregandolo al archivo "usuarios.json"
# Opcion 3 : Mediante un "Break" sale de la aplicacion imprimiendo el mensaje "GRACIAS POR UTILIZAR NUESTRA APP."
# Mediante un "else" toma una opcion no valida e imprime el mensaje "Opción no válida." 
def main():
    while True:
        limpiarPantalla()
        print(colorama.Fore.GREEN + "APLICACION ESTACIONAMIENTO".center(50))
        print("=" * 50)
        print()
        print(colorama.Fore.BLUE + colorama.Fore.RESET + " BIENVENIDO ".center(50))
        print()
        print(colorama.Fore.BLUE + "\t1 :" + colorama.Fore.RESET + " Iniciar Sesión ")
        print(colorama.Fore.BLUE + "\t2 :" + colorama.Fore.RESET + " Crear usuario ")
        print(colorama.Fore.BLUE + "\t3 :" + colorama.Fore.RESET + " Salir ")
        print()
        choice = input("Selecciona una opción: ")
        if choice == '1':
            login()
        elif choice == '2':
            create_user()
        elif choice == '3':
            print("GRACIAS POR UTILIZAR NUESTRA APP.")
            break
        else:
            print(colorama.Fore.RED + "Opción no válida.")
            input(colorama.Fore.RED + "Presione cualquier tecla para continuar")
            limpiarPantalla()

# AQUI INICIA EL PROGRAMA
main()
