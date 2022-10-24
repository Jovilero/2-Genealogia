import funciones
import pandas as pd
import time
import os


apellido1="Valero"
apellido2=""

url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2)
nPages=funciones.getNpages(html)


for i in range(int(nPages)+1):
    # time.sleep(1)
    try:
        url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2, Ppagina=int(i))
        pa=pd.read_html(html)
        ruta=funciones.create_rute_to_save(apellido1,apellido2)
        if (i <1):
            print(ruta)
        print(i)
    except: pass

    funciones.registro_to_csv(pa,ruta,i)

    # if (i==1):
    #     break

#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?

print('ok')


