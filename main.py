import re,json,webbrowser

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
    #comando maximo               
    if re.search('Maximo',comandos,re.IGNORECASE)!=None:
        match=re.search('Maximo',comandos,re.IGNORECASE)
        s= match.start()
        e= match.end()
        comando3=comandos[s:e+1]
        atributo_max=comandos.replace(comando3,"")
        lista_c=[]
        for filename in filenames:
            file = open(filename)
            datos_s = file.read()
            data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
            dict=data_s
            for elemento in dict: 
                maximo= f"{elemento[atributo_max]}"
                lista_c.append(maximo)
        print("-----------------------------") 
        print("Estas son todos los atributos de tipo "+atributo_max + " encontradas en los registros: " )
        print(lista_c)
        print("El/la "+ atributo_max+" maximo es: " + max(lista_c))
        print("------------------------------")


    #comando minimo
    if re.search('Minimo',comandos,re.IGNORECASE)!=None:
        match=re.search('Minimo',comandos,re.IGNORECASE)
        s= match.start()
        e= match.end()
        comando3=comandos[s:e+1]
        atributo_min=comandos.replace(comando3,"")
        lista_c=[]
        for filename in filenames:
            file = open(filename)
            datos_s = file.read()
            data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
            dict=data_s
            for elemento in dict: 
                minimo= f"{elemento[atributo_min]}"
                lista_c.append(minimo)
        print("-----------------------------") 
        print("Estas son todos los atributos de tipo "+atributo_min + " encontradas en los registros: " )
        print(lista_c)
        print("El/la "+ atributo_min+" minimo es: " + min(lista_c))
        print("------------------------------")
        
    #comando suma
    if re.search('Suma',comandos,re.IGNORECASE)!=None:
        match=re.search('Suma',comandos,re.IGNORECASE)
        s= match.start()
        e= match.end()
        comando3=comandos[s:e+1]
        atributo_sum=comandos.replace(comando3,"")
        lista_c=[]
        for filename in filenames:
            file = open(filename)
            datos_s = file.read()
            data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
            dict=data_s
            for elemento in dict: 
                suma= f"{elemento[atributo_sum]}"
                lista_c.append(suma)
        print("-----------------------------") 
        print("Estas son todos los atributos de tipo "+atributo_sum + " encontradas en los registros: " )
        print(lista_c)
        print("la suma de los atributos de tipo "+ atributo_sum+" es: " )
        print(sum(float(i) for i in lista_c))
        print("------------------------------")
        

    #comando cuenta
    if re.search('Cuenta',comandos,re.IGNORECASE)!=None:
        cuenta=0
        registro=0
        for filename in filenames:
            file = open(filename)
            datos_s = file.read()
            data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
            dict=data_s
            for elemento in dict: 
                cuenta= cuenta+len(elemento)
                
        registro=cuenta/4
        print("Este es el numero de atributos cargados a memoria:")
        print(cuenta)
        print("Este es el numero de registros cargados a memoria:")
        print(int(registro))
        
    #comando reportar
    if re.search('Reportar',comandos,re.IGNORECASE)!=None:
        match=re.search('Reportar',comandos,re.IGNORECASE)
        s= match.start()
        e= match.end()
        comandoR=comandos[s:e+1]
        num_registro=comandos.replace(comandoR,"")
        num_registros=int(num_registro)
        lista_nombre=[]
        lista_edades=[]
        lista_activo=[]
        lista_promedio=[]
        registros_condicion=1
        
        for filename in filenames:
            file = open(filename)
            datos_s = file.read()
            data_s = json.loads(datos_s)            #imprimimos los atributos segun las condiciones establecidas
            dict=data_s
           
            for elemento in dict: 
                if registros_condicion<=num_registros:
                    nombres= f"{elemento['nombre']}"
                    lista_nombre.append(nombres)
                    edades= f"{elemento['edad']}"
                    lista_edades.append(edades)
                    activos= f"{elemento['activo']}"
                    lista_activo.append(activos)
                    promedios= f"{elemento['promedio']}"
                    lista_promedio.append(promedios)
                    registros_condicion=registros_condicion+1

        with open('reporte.html', 'w') as myFile:
            myFile.write('<!DOCTYPE html>')
            myFile.write('<html>')
            myFile.write('<head>')
            myFile.write('<meta charset="utf-8">')
            myFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
            myFile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
            myFile.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
            myFile.write('</head>')
            myFile.write('<body>')
            myFile.write('<center>')
            myFile.write('<h1>REPORTE</h1>')
            myFile.write('<table border="1" class="table table-striped">')
            myFile.write('<tr>')
            myFile.write('<td>Nombres</td>')
            for nom in lista_nombre:
                myFile.write('<td>')
                myFile.write(nom)
                myFile.write('</td>')
            myFile.write('</tr>')
            myFile.write('<tr>')
            myFile.write('<td>Edades</td>')
            for eda in lista_edades:
                myFile.write('<td>')
                myFile.write(eda)
                myFile.write('</td>')
            myFile.write('</tr>')
            myFile.write('<tr>')
            myFile.write('<td>Activo</td>')
            for act in lista_activo:
                myFile.write('<td>')
                myFile.write(act)
                myFile.write('</td>')
            myFile.write('</tr>')
            myFile.write('<tr>')
            myFile.write('<td>Promedios</td>')
            for pro in lista_promedio:
                myFile.write('<td>')
                myFile.write(pro)
                myFile.write('</td>')
            myFile.write('</tr>')
            myFile.write('</table>')
            myFile.write('</center>')
            myFile.write('</body>')
            myFile.write('</html>')
        webbrowser.open('reporte.html', new=2, autoraise=True)
            


            
            
                
            





        

    salir= input('presione 1 si desea salir, si desea utilizar otro comando presione enter: ')
    if salir=='1':
        repetir_bucle= False



    
