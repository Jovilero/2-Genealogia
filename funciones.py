# Sunday, October 30, 2022 @ 01:20:09 AM
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
                dataframe_to_csv(pa,ruta,i)
                # print(f"Dataframe {i} almacenado con exito")
            # except: 
            #     print(f"DATAFRAME {i} NO ALMACENADO ALERTA COBRA")
            #     pass
            # print(i)

            #meterlo en sql o otro lugar q se vea bien rapido
            #¿pasar a gedcom?

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





def registro_to_db():
    CONN= connector.pgConnect()
    """ insertar codigo aqui """

    connector.pgDisconnect(CONN)

