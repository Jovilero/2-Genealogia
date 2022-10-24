import funciones
import funciones2
import pandas as pd
import time
import os

apellido1="Lanzuela"
apellido2=""

url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2)
nPages=funciones.getNpages(html)

#este es mas elegante, pero no guarda el primer csv que se genera
for i in range(int(nPages)+1):
    print(i)
    # time.sleep(1)
    try:
        url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2, Ppagina=int(i))
        print(i)
        pa=pd.read_html(html)
        print(i)

    except: pass
    ruta=funciones2.create_rute_to_save(apellido1,apellido2)
    print(i)
    funciones.registro_to_csv(pa,ruta,i)
    print("csv creado")


    # if (i==1):
    #     break

#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?

print('ok')


