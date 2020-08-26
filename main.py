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
    #comando cargar
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
       #comando seleccionar  
    print(filenames)   
    select= re.findall('Seleccionar|Donde',comandos, re.IGNORECASE)
    if select :
        print("(prueba) existe seleccion o donde en el comando")
    #comando maximo
    if re.search('Maximo',comandos,re.IGNORECASE)!=None:
        print('(prueba) maximo')
    #comando minimo
    if re.search('Minimo',comandos,re.IGNORECASE)!=None:
        print('(prueba) minimo')
    #comando suma
    if re.search('Suma',comandos,re.IGNORECASE)!=None:
        print('(prueba) suma')

    #comando cuenta
    if re.search('Cuenta',comandos,re.IGNORECASE)!=None:
        print('(prueba) cuenta')
    #comando reportar
    if re.search('Reportar',comandos,re.IGNORECASE)!=None:
        print('(prueba) reportar')

    salir= input('presione 1 si desea salir, si desea utilizar otro comando presione enter: ')
    if salir=='1':
        repetir_bucle= False
    
