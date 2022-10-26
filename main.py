# Wednesday, October 26, 2022 @ 03:20:25 PM
#ctrl+shift+t
#JJVL

import funciones
import pandas as pd
import time
import os


apellido1="Quintanilla"
apellido2=""

# 
url,html=funciones.researcher(Pa1=apellido1, Pa2=apellido2)
# url,html=funciones.researcher(Pprincipio_evento=1400)
nPages=funciones.getNpages(html)

if type(nPages)==int:
    for i in range(nPages+1):
        # time.sleep(1)
        print(i)
        try:
            # url,html=funciones.researcher(Pprincipio_evento=1400, Ppagina=int(i))
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

    print('Proceso términado con éxito.')


