from timeit import repeat
import requests
import pandas as pd

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
    print(nPages)
    return nPages