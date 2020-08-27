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
                file = open(filename)
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
        match=re.search('Seleccionar',comandos,re.IGNORECASE)  #obtendra el match de la palabra seleccionar
        match2=re.search('Donde',comandos,re.IGNORECASE)      #obtendra el match de la palabra donde
        s = match.start()                               #con s e s2 y e 2 definira de donde a donde estan seleccionar y donde
        e = match.end()
        s2 = match2.start()
        e2 = match2.end()
        comando2=comandos[s:e]                          #obtendremos la palabra por medio de los indices 
        comando_d=comandos[e2:e2]
        parte_1=comandos[s:s2]
        parte_d=comandos[e2+1:len(comandos)]     #dividiremos el string esta parte contiene desde el final de "donde" hasta el final de la cadena
        x = re.search("nombre|edad|promedio|activo", parte_d)  #buscara si existe alguna de estas condiciones a buscar
        sx=x.start()                                            # obtendremos de donde a donde estan segun el indice
        ex=x.end()
        atributo_d=parte_d[sx:ex]                       #se obtendra el atributo condicion
        atributo_p2= parte_d.replace(atributo_d,"")          #quitaremos esa palabra de la segunda parte de la cadena
        atributo_condi=atributo_p2.replace("=", "")  #atributo que define la condicion de donde ="" quitando el signo igual
        atributo= parte_1.replace(comando2,"") #en la primera parte de la cadena quitaremos el seleccionar
        atributo_n=atributo.replace(" ", "") #quitaremos los espacios en blanco
        atributos= atributo_n.strip()     #se quitara algun espacio entre palabras
        atributos_lista=atributos.split(",") #se dividira en una lista con el delimitador ,
        z=re.findall("nombre|edad|promedio|activo", parte_d)
        
        if atributo_d == "nombre":
            condicion1="nombre"
        if atributo_d == "promedio":
            condicion1="promedio"
        if atributo_d == "activo":
            condicion1="activo"
        if atributo_d == "promedio":
            condicion1="promedio"
        if atributo_d =="edad":
            condicion1="edad"
        
        
        atributocondi= atributo_condi[1:len(atributo_condi)-1]
        x = re.findall("\d", atributo_condi)
        if x:
            atributocondi=float(atributo_condi)
        
        if atributo_n =="*":        #si nuestra variable donde contiene los atributos a buscar tiene * seleccionara todos los atributos automaticamente
            for filename in filenames:
                file = open(filename)
                datos_s = file.read()
                data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
                dict=data_s
                for elemento in dict: 
                    condicion_atributo=elemento.get(condicion1)
                    condicion2=atributocondi
                    if condicion_atributo==condicion2:  #si la condicion del atributo coincide con la entrada imprimira el atributo a buscar
                        print("-------------------------------------")
                        
                        print("nombre: "+ f"{elemento['nombre']:5} \n"
                            "edad: "+ f"{elemento['edad']:5} \n"
                            "promedio: "+ f"{elemento['promedio']:5} \n" 
                            "activo: "+ f"{elemento['activo']:5} \n")
                        print("------------------------------------")
                    
        else:              
            for filename in filenames:
                file = open(filename)
                datos_s = file.read()
                data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
                dict=data_s
                for elemento in dict: 
                    condicion_atributo=elemento.get(condicion1)
                    condicion2=atributocondi
                    
                    if condicion_atributo==condicion2:  #si la condicion del atributo coincide con la entrada imprimira el atributo a buscar
                        print("-------------------------------------")
                        for attribute in atributos_lista:
                            print(attribute +":"+ " " + f"{elemento[attribute]:5}")
                        print("------------------------------------")
                    

    

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



    
