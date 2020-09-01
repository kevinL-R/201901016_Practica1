### 201901016_Practica1
# Manual de usuarios
## ¿Como usar el programa de consultas?
Antes de iniciar el programa primero debes saber los comandos disponible, cada uno de estos comandos 
son case insensitive esto quiere decir que no importa si se usan mayúsculas o minúsculas el programa es capaz de reconocer
el comando a utilizar esta la lista de comandos disponibles:
1. Cargar
2. Seleccionar
3. Maximo
4. Minimo
5. Suma
6. Cuenta
7. Reportar
## Comando Cargar 
Este comando permitirá la carga de diferentes archivos de tipo json a memoria, el único
parámetro que lo conforma es una lista de direcciones a los archivos que cargará a
memoria. 
A continuacion te mostrare un ejemplo de como escribir el comando

Cargar archivo1.json, archivo2.json, archivo3.json, ...... archivoN.json

## Comando Seleccionar
Permite seleccionar uno o más registros o atributos de los mismos con base en
condiciones simples donde usaremos un segundo comando "Donde" que pueden aplicarse a los atributos de los mismos.

la estructura del comando es:

SELECCIONAR nombre, edad, promedio DONDE nombre = “Kevin”
SELEcCIONAR *

Si se usa el aterisco seleccionara todos los atributos

## Comando Maximo
Te permitira encontrar el valor máximo que se encuentre en el atributo de uno de los
registros del conjunto en memoria en este caso solo se puede para promedio y edad

la estructura del comando es:

MAXiMO edad

## Comando Minimo
Permite encontrar el valor mínimo que se encuentre en el atributo de uno de los
registros del conjunto en memoria al igual que maximo solo se puede para promedio y edad.ç

la estructura del comando es:

Minimo edad

## Comando Suma

Permite obtener la suma de todos los valores de un atributo especificado en el
comando y los unicos atributos son promedio y edad

la estructura del comando es:

SuMa promedio

## Comando Cuenta
Este comando te permite contar el número de registros que se han cargado a memoria.

la estructura del comando es:

Cuenta

## Comando Reportar
Este comando permite crear un reporte en html que contiene N cantidad de
registros.

la estructura del comando es:

Reportar 2

Al colocar 2 solo se reportara 2 registros de los archivos cargados a memoria

## Instrucciones finales

Al momento de iniciar el archivo main.py te dara la bienvenida seguido de este mensaje "escriba un comando:" y escribira la linea de comandos descrito con anterioridad 
Ejemplo: escribir un comando: CaRgar archivo1.json, archivo2.json, archivo3.json

seguido de la ejecucion del comando aparecera este mensaje "presione 1 si desea salir, si desea utilizar otro comando presione enter:" si desea seguir ejecutando mas comando presione enter y de nuevo aparecera el mensaje escriba un comando pero si presiona 1 la aplicacion se detendra
