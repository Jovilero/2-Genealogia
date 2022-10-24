import funciones
import funciones2
import pandas as pd
import time
import os

apellido1="Lanzuela"
apellido2=""

url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2)
nPages=funciones.getNpages(html)


for i in range(int(nPages)+1):
    print(i)
    # time.sleep(1)
    try:
        url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2, Ppagina=int(i))
        print(i)
        pa=pd.read_html(html)
        print(i)
        ruta=funciones2.create_rute_to_save(apellido1,apellido2)
        print(i)
        funciones.registro_to_csv(pa,ruta,i)
        print("csv creado")
    except: pass



    # if (i==1):
    #     break

#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?

print('ok')


