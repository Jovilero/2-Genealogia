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
        except:
            pass
    print(int(nPages.replace('.','').strip()))
    return int(nPages.replace('.',""))


def create_rute_to_save(apellido1,apellido2='',path=fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia'):
    try:

        os.mkdir(fr'{path}\{apellido1}')
        #si no existe la ruta y la ha creado antes, la asigna ahora
        ruta=fr'{path}\{apellido1}'
        try:
            #si hay segundo apellido, crea la ruta para el segundo apellido
            os.mkdir(fr'{path}\{apellido1}\{apellido2}')
            #y asigna la ruta con la subcarpeta del segundo apellido
            ruta=fr'{path}\{apellido1}\{apellido2}'
            print(ruta)
        except: pass
    except:
        return ruta

def registro_to_csv(pa, ruta,i):
    # try:
    # print(pa[0])
    # print(pa[1])
    # print(pa[2])
    # print(pa[3])
    # print(pa[4])
    # print(pa[5])
    # pa[4].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\dataframe{i}.csv')
    anyo=pa[5].loc[1,1][-4:]
    print(anyo)
    
    pa[2].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='w', index=False, header=False)
    # pa[3].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[4].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[5].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[6].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    pa[7].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # except:
    #     pass
    # except: pass 


def getRegisterfrom_toCSV(
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

    url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina, Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit, 
)
    nPages=getNpages(html)
    # print(nPages)

    for i in range(int(nPages)+1):
        
        # time.sleep(1)
        try:
            
            url,html=researcher(Pnom, Pa1, Pa2, Pa2p, Pa2m, Pa1ap, Pa1am, Plnac, Plins, Plpa, Plma, Plabuopat, Plabuapat, Plabuomat, Plabuamat, Plconyuge, Pltots, Plevent, Pcognomcj, Pcognomq, Pprofeq, Pnompa, Pnomma, Pnomcon, Ppagina==i, Pprincipio, Pfinal, Psexo, Pprincipio_evento, Pfinal_evento, Pobserva, Pfiltre, Porden, PSubmit)
            
            
            pa=pd.read_html(html)
            # print(pa)
            ruta=create_rute_to_save(apellido1=Pa1,apellido2=Pa2)
            print(i)
            
        except: pass
        registro_to_csv(pa,ruta,i)
        print(i)