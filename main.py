import re,json

repetir_bucle= True
while repetir_bucle:
    comandos= input('ingrese un comando: ')
    #comando cargar
    if re.search('CaRgar',comandos,re.IGNORECASE)!=None:
        match=re.search('CaRgar',comandos,re.IGNORECASE)
        s = match.start()
        e = match.end()
        comando1=comandos[s:e]
        archivo=comandos.replace(comando1, "")
        archivo_n=archivo.replace(" ","")
        archivos=archivo_n.strip()
        filenames=archivos.split(",")
        print(filenames)
        for filename in filenames:
            try:
                file = open(filename + '.json')
                datos = file.read()
                data = json.loads(datos)
                dict=data
            except FileNotFoundError:
                mensaje= 'el archivo siguiente no existe: ' + filename
                print(mensaje)
            else:
                for elemento in dict:
                    print(elemento)                  
       #comando seleccionar  
     
    if re.search('Seleccionar',comandos,re.IGNORECASE)!=None:
        print('(prueba) seleccionar')
        match=re.search('Seleccionar',comandos,re.IGNORECASE)
        s = match.start()
        e = match.end()
        comando2=comandos[s:e]
        atributo= comandos.replace(comando2,"")
        atributo_n=atributo.replace(" ", "")
        atributos= atributo_n.strip()
        atributos_lista=atributos.split(",")
        for filename in filenames:
            file = open(filename + '.json')
            datos_s = file.read()
            data_s = json.loads(datos_s)
            dict=data_s
            for elemento in dict:     
                for attribute in atributos_lista:
                    if elemento['nombre']=="kevin":
                        print(f"{elemento[attribute]50}")

    #subcomando Donde

    if re.search('Maximo',comandos,re.IGNORECASE)!=None:
        print('(prueba) maximo')   
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



    
