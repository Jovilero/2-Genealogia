import funciones
import pandas as pd
import time

apellido="FORRIOL"

url,html=funciones.researcher(Pa1=apellido)
nPages=funciones.getNpages


for i in range(int(nPages)+1):
    print(i)
    # time.sleep(1)
    try:
        url,html=funciones.researcher(Pa1=apellido,Ppagina=int(i))
        pa=pd.read_html(html)
        pa[4].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\dataframe{i}.csv')
    except:
        pass

#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?




print('ok')


