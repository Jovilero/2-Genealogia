# Wednesday, November 2, 2022 @ 12:38:41 AM
# #author: jjvl

import requests
import pandas as pd
import time
import os

import dbConnection as connector



def researcher(
    Pnom='',
    Pa1='',
    Pa2='',
    Pa2p='',
    Pa2m='',
    Pa1ap='',
    Pa1am='',
    Plnac='',
    Plins='',
    Plpa='',
    Plma='',
    Plabuopat='',
    Plabuapat='',
    Plabuomat='',
    Plabuamat='',
    Plconyuge='',
    Pltots='',
    Plevent='',
    Pcognomcj='',
    Pcognomq='',
    Pprofeq='',
    Pnompa='',
    Pnomma='',
    Pnomcon='',
    Ppagina='1',
    Pprincipio='',
    Pfinal='nnnn',
    Psexo='',
    Pprincipio_evento='',
    Pfinal_evento='nnnn',
    Pobserva='',
    Pfiltre='P',
    Porden='evento',
    PSubmit='BUSCAR'
    ):

    # print("Construyendo consulta")
    URL="https://www.arxparrvalencia.org/listados.php?"

    end_url=f"nom={Pnom}&a1={Pa1}&a2={Pa2}&a2p={Pa2p}&a2m={Pa2m}&a1ap={Pa1ap}&a1am={Pa1am}&lnac={Plnac}&lins={Plins}&lpa={Plpa}&lma={Plma}&labuopat={Plabuopat}&labuapat={Plabuapat}&labuomat={Plabuomat}&labuamat={Plabuamat}&lconyuge={Plconyuge}&ltots={Pltots}&levent={Plevent}&cognomcj={Pcognomcj}&cognomq={Pcognomq}&profeq={Pprofeq}&nompa={Pnompa}&nomma={Pnomma}&nomcon={Pnomcon}&pagina={Ppagina}&principio={Pprincipio}&final={Pfinal}&sexo={Psexo}&principio_evento={Pprincipio_evento}&final_evento={Pfinal_evento}&observa={Pobserva}&filtre={Pfiltre}&orden={Porden}&Submit={PSubmit}"
    
    # print(end_url)
    try:
        page = requests.get(URL+end_url,timeout=None)
        # print(page.text)
        return URL+end_url, page.text
    except:
        
        pass
    
    
def getNpages(html):
    # print("obteniendo paginas")
    pa=pd.read_html(html)

    for eachlist in pa[1].head().to_string().splitlines():
        # print(eachlist.split())
        splitted_header=eachlist.split()
        # print(type(splitted_header))
        try:
            position=splitted_header.index('búsqueda:')
            nPages=splitted_header[position+1]
            print(f"Descargando: {int(nPages.replace('.','').strip())} páginas.")
            # print(nPages)
            return int(nPages.replace('.',""))
        except:
            # print("No ha sido posible obtener el número de páginas.")
            pass
    return pa[3]


def create_rute_to_save(param1='',param2='',path=fr'.\Ejemplos'):
    # print("creando ruta")
    if os.path.isdir(path)==False:
        os.mkdir(path)

    try:
        os.mkdir(fr'{path}\{param1}')
        ruta=fr'{path}\{param1}'
    except: 
        ruta=fr'{path}\{param1}'
        
    try:
        os.mkdir(fr'{path}\{param1}\{param2}')
        ruta=fr'{path}\{param1}\{param2}'
    except:       
        ruta=fr'{path}\{param1}\{param2}'
    
    return ruta



def dataframe_to_csv(pa, ruta,i):
    # print("guardando csv en la ruta")
    try:
        anyo=pa[5].loc[1,1][-4:]
        # print(pa[5].loc[1,1])
    except: anyo="x"

    pa[2].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='w', index=False, header=False) #
    # pa[3].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False) #tabla1
    pa[4].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[5].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[6].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[7].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)



def search_getPages_ToCSV(  
    nombreCarpeta, nombreSubCarpeta='',
    Pnom='',
    Pa1='', 
    Pa2='',
    Pa2p='',
    Pa2m='',
    Pa1ap='',
    Pa1am='',
    Plnac='',
    Plins='',
    Plpa='',
    Plma='',
    Plabuopat='',
    Plabuapat='',
    Plabuomat='',
    Plabuamat='',
    Plconyuge='',
    Pltots='',
    Plevent='',
    Pcognomcj='',
    Pcognomq='',
    Pprofeq='',
    Pnompa='',
    Pnomma='',
    Pnomcon='',
    Ppagina='1',
    Pprincipio='',
    Pfinal='nnnn',
    Psexo='',
    Pprincipio_evento='',
    Pfinal_evento='nnnn',
    Pobserva='',
    Pfiltre='P',
    Porden='evento',
    PSubmit='BUSCAR'
):
    # print("Obteniendo las paginas y guardando el csv en el directorio")
    url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)
    
    nPages=getNpages(html)
    
    if type(nPages)==int:
        
        for i in range(nPages+1):
            # time.sleep(1)
            # print(i)
            try:
                # url,html=funciones.researcher(Pprincipio_evento=1400, Ppagina=int(i))
                url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, int(i), Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)
                
                pa=pd.read_html(html)
                
            except: pass

            ruta=create_rute_to_save(nombreCarpeta,nombreSubCarpeta)
            if (i==0):
                print(ruta)
            # registro_to_db()

            if i>0:
                dataframe_to_sql(pa)
                dataframe_to_csv(pa,ruta,i)
                # print(f"Dataframe {i} almacenado con exito")
            # except: 
            #     print(f"DATAFRAME {i} NO ALMACENADO ALERTA COBRA")
            #     pass
            # print(i)

            #meterlo en sql o otro lugar q se vea bien rapido
            #¿pasar a gedcom?

        print('Proceso términado con éxito.')

def dataframe_to_csv(pa, ruta,i):
    # print("guardando csv en la ruta")
    try:
        anyo=pa[5].loc[1,1][-4:]
        # print(pa[5].loc[1,1])
    except: anyo="x"

    pa[2].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='w', index=False, header=False) #
    # pa[3].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False) #tabla1
    pa[4].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[5].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[6].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[7].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)



def search_getPages_ToSQL(  
    Pnom='',
    Pa1='', 
    Pa2='',
    Pa2p='',
    Pa2m='',
    Pa1ap='',
    Pa1am='',
    Plnac='',
    Plins='',
    Plpa='',
    Plma='',
    Plabuopat='',
    Plabuapat='',
    Plabuomat='',
    Plabuamat='',
    Plconyuge='',
    Pltots='',
    Plevent='',
    Pcognomcj='',
    Pcognomq='',
    Pprofeq='',
    Pnompa='',
    Pnomma='',
    Pnomcon='',
    Ppagina='1',
    Pprincipio='',
    Pfinal='nnnn',
    Psexo='',
    Pprincipio_evento='',
    Pfinal_evento='nnnn',
    Pobserva='',
    Pfiltre='P',
    Porden='evento',
    PSubmit='BUSCAR'
):
    # print("Obteniendo las paginas y guardando el csv en el directorio")
    url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)
    
    nPages=getNpages(html)
    
    if type(nPages)==int:
        
        for i in range(nPages+1):
            # time.sleep(1)
            # print(i)
            try:
                # url,html=funciones.researcher(Pprincipio_evento=1400, Ppagina=int(i))
                url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, int(i), Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)
                
                pa=pd.read_html(html)
                
            except: pass

            if i>0:
                dataframe_to_sql(pa)
               
        print('Proceso términado con éxito.')




def getEveryRecordWODate(value):
    """This function return a bunch of CSVs of registers with unknown dates.
       There are 4 cases explained below:
       value == 1, it will generate a CSV for each register with unknown birth date and unknown event dates
       value == 2, it will generate a CSV for each register with unknown birth date
       value == 3, it will generate a CSV for each register with unknown event date
       value == 4, will do the other 3 options in the same execution
       
    Args:
        value (_integer_): an integer betwen 1 and 4
    """
    import string
    lista=list(string.ascii_uppercase)
    
    for each in lista:
        match value:
            case 1:
                search_getPages_ToCSV(Pnom=each,Pfinal='',Pfinal_evento='',nombreCarpeta=f'{each}_sinFechasConocidas')
            case 2: 
                search_getPages_ToCSV(Pnom=each,Pfinal='',nombreCarpeta=f'{each}_sinFNacimiento')
            case 3:
                search_getPages_ToCSV(Pnom=each,Pfinal_evento='',nombreCarpeta=f'{each}_sinFEvento')
            case 4:
                search_getPages_ToCSV(Pnom=each,Pfinal='',Pfinal_evento='',nombreCarpeta=f'{each}_sinFechasConocidas')
                search_getPages_ToCSV(Pnom=each,Pfinal='',nombreCarpeta=f'{each}_sinFNacimiento')
                search_getPages_ToCSV(Pnom=each,Pfinal_evento='',nombreCarpeta=f'{each}_sinFEvento')

def getCSV5years(
    nombreCarpeta='', nombreSubCarpeta='',
    Pnom='',
    Pa1='', 
    Pa2='',
    Pa2p='',
    Pa2m='',
    Pa1ap='',
    Pa1am='',
    Plnac='',
    Plins='',
    Plpa='',
    Plma='',
    Plabuopat='',
    Plabuapat='',
    Plabuomat='',
    Plabuamat='',
    Plconyuge='',
    Pltots='',
    Plevent='',
    Pcognomcj='',
    Pcognomq='',
    Pprofeq='',
    Pnompa='',
    Pnomma='',
    Pnomcon='',
    Ppagina='1',
    Pprincipio='',
    Pfinal='nnnn',
    Psexo='',
    Pprincipio_evento='',
    Pfinal_evento='nnnn',
    Pobserva='',
    Pfiltre='P',
    Porden='evento',
    PSubmit='BUSCAR'
):

    if Pfinal_evento-Pprincipio_evento>100:

        i=0
        hasta=Pprincipio_evento+5
        while Pprincipio_evento<hasta:
            i=i+1
            Pprincipio_evento=Pprincipio_evento+1
            try:
                if nombreCarpeta!='' and nombreSubCarpeta=='':
                    search_getPages_ToCSV(nombreCarpeta,str(Pprincipio_evento),Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, hasta, Pobserva, Pfiltre, Porden, PSubmit)
                
                if nombreCarpeta!='' and nombreSubCarpeta!='':
                    search_getPages_ToCSV(nombreCarpeta,nombreSubCarpeta,Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, hasta, Pobserva, Pfiltre, Porden, PSubmit)
                
                if nombreCarpeta=='' and nombreSubCarpeta=='':
                    search_getPages_ToCSV(Pa1,str(Pprincipio_evento),Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, hasta, Pobserva, Pfiltre, Porden, PSubmit)
            except:
                print("algo chungo ha pasao")
                pass
            Pprincipio_evento=Pprincipio_evento-1
            hasta=hasta+5
            Pprincipio_evento=Pprincipio_evento+5
            print(fr'{Pprincipio_evento}-{hasta}')
            if hasta>=Pfinal_evento:
                break
    else:
        search_getPages_ToCSV(Pa1,nombreSubCarpeta,Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)




def walkpath(ext):
    """This function looks for existin files that match the indicated extension as argument and returns a dictionary with pandas dataframes
    Args:
        ext (extension of a file): it may be the extension of a file, and the file must be stored in a folder down the .py that calls this function
    Returns:
        a dictionary containing pandas dataframe of the information contained in the filed that matched the extension indicated as argument
        also returns a list with the keys for the dictionary 
    """
    dic={}
    keys=[]
    for this_tuple in os.walk(os.path.abspath(os.curdir)):
        for each_dir in this_tuple:
            if type(each_dir)==list:
                for each_file in each_dir:
                    if each_file.endswith(f'.{ext}') or each_file.endswith(f'{ext}')  :
                        print(fr'{this_tuple[0]}\{each_file}')
                        pa=pd.read_fwf(fr'{this_tuple[0]}\{each_file}',index=False, header=None)
                        dic[each_file]=pa
                        keys.append(each_file)

    return dic, keys

def registro_to_db():
    CONN= connector.pgConnect()
    """ insertar codigo aqui """
    cursor=CONN.cursor(cursor)
    try:
        cursor.executemany(sql,values)
    except: print("failed to insert into the database")

    #DefTablaSacramentos(CONN)
    connector.pgDisconnect(CONN)


def DefTablaSacramentos():
    CONN= connector.pgConnect()
    cursor=CONN.cursor()
    try:
        sql = fr"""insert into ab."Sacramentos" values (%s, %s)"""

        values = [(1,'Bautismo'),(2,'Confirmación'),(3,''),(4,'Matrimonio'),(5,'Defunción'),(6,'Matrícula Parroquial')]

        cursor.executemany(sql, values)
    except: pass
    print("True")
    connector.pgDisconnect(CONN)



def dataframe_to_sql(pa):
    """ """
    #pa[2]
    CONN= connector.pgConnect()
    cursor=CONN.cursor()
    sql = fr"""insert into ab."Registros" values ({pa[2].loc[1,1]},{pa[2].loc[1,0]},'{pa[2].loc[1,2]}','{pa[2].loc[1,3]}','{pa[2].loc[1,4]}','{pa[2].loc[1,5]}',{pa[2].loc[1,6]})"""
    
    try:
        cursor.execute(sql)
        print("True")
        CONN.commit()
    except: 
        pass
    
    connector.pgDisconnect(CONN)
    # pa[4]
    for i in range(len(pa[4].index)):
        if i>0:
            CONN= connector.pgConnect()
            cursor=CONN.cursor()
            sql = fr"""insert into ab."Personas" (registro, relacion, nombre, apellido1, apellido2, LugarNacimiento) values ({pa[2].loc[1,1]}, '{pa[4].loc[i,0]}','{pa[4].loc[i,1]}','{pa[4].loc[i,2]}','{pa[4].loc[i,3]}','{pa[4].loc[i,4]}')"""
            
            
            # try:
                
            cursor.execute(sql)
            CONN.commit()
        # connector.pgDisconnect(CONN)
            # except: 
            #     print(sql)
            connector.pgDisconnect(CONN)
    

    #pa[5]
    CONN= connector.pgConnect()
    cursor=CONN.cursor()
    sql = fr"""insert into ab."DatosPersonales" (registro, nombre, apellido1, apellido2, fechanacimiento, fechasacramento, lugarsacramento, oficiante, profesion, profesionpadre, residencia, lugarinscripcion, notas) values ({pa[2].loc[1,1]},'{pa[4].loc[1,1]}','{pa[4].loc[1,2]}','{pa[4].loc[1,3]}','{pa[5].loc[1,0]}','{pa[5].loc[1,1]}','{pa[5].loc[1,2]}','{pa[5].loc[1,3]}','{pa[5].loc[1,4]}','{pa[5].loc[1,5]}','{pa[6].loc[1,0]}','{pa[6].loc[1,1]}', '{pa[7].loc[1,0]}')"""
    # print(sql)
    try:       
        cursor.execute(sql)
        CONN.commit()
    except: pass
    connector.pgDisconnect(CONN)