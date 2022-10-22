import funciones
import pandas as pd
import time

apellido="FORRIOL"

url,html=funciones.researcher(Pa1=apellido)
pa=pd.read_html(html)


for eachlist in pa[1].head().to_string().splitlines():
    # print(eachlist.split())
    splitted_header=eachlist.split()
    # print(type(splitted_header))
    try:
        position=splitted_header.index('búsqueda:')
        position2=splitted_header.index('registros.')
        nPages=splitted_header[position+1]
    except:
        pass
print(nPages)

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


