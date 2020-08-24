import re,json
def readJson(filename):
    try:
        file = open(filename + '.json')
        data = json.load(file)
        
    except FileNotFoundError:
        mensaje= 'el archivo siguiente no existe: ' + filename
        print(mensaje)
    else:
        dict = data
        for elemento in dict:
            print(elemento)

repetir_bucle= True
while repetir_bucle:
    comandos= input('ingrese un comando: ')
    if re.search('CaRgar',comandos,re.IGNORECASE)!=None:
        match=re.search('CaRgar',comandos,re.IGNORECASE)
        s = match.start()
        e = match.end()
        comando1=comandos[s:e]
        espacio=" "
        archivo=comandos.replace(comando1, "")
        archivos=archivo.strip()
        filenames=archivos.split(",")
        print(filenames)
        for filename in filenames:
            readJson(filename)

    salir= input('presione 1 si desea salir si no presione enter: ')
    if salir=='1':
        repetir_bucle= False
    print(comandos)
