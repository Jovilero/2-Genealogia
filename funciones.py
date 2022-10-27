# Wednesday, October 26, 2022 @ 03:19:57 PM
#author: jjvl



# from timeit import repeat
import requests
import pandas as pd
import time
import os




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
            print("No ha sido posible obtener el número de páginas.")
            pass



def create_rute_to_save(param1,param2='',path=fr'.\Ejemplos'):
    if os.path.isdir==False:
        os.mkdir(path)
    try:
        os.mkdir(fr'{path}\{param1}')
        ruta=fr'{path}\{param1}'
        return ruta
    except: 
        ruta=fr'{path}\{param1}'
        
    try:
        os.mkdir(fr'{path}\{param1}\{param2}')
        ruta=fr'{path}\{param1}\{param2}'
        return ruta

    except:
        ruta=fr'{path}\{param1}\{param2}'
    return ruta



def registro_to_csv(pa, ruta,i):
    try:
        anyo=pa[5].loc[1,1][-4:]
        # print(pa[5].loc[1,1])
    except: anyo="x"

    pa[2].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='w', index=False, header=False)
    # pa[3].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
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
                ruta=create_rute_to_save(nombreCarpeta,nombreSubCarpeta)
                if (i <1):
                    print(ruta)
                # print(i)
            except: pass

            registro_to_csv(pa,ruta,i)

            # if (i==1):
            #     break
            #meterlo en sql o otro lugar q se vea bien rapido
            #¿pasar a gedcom?

        print('Proceso términado con éxito.')
