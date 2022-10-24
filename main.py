import funciones
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
        pa=pd.read_html(html)
        # if fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}' is False:
        ruta=fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}'
        os.mkdir(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}')
        ruta=fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}'
        
        os.mkdir(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}\{apellido2}')
        ruta=fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\{apellido1}\{apellido2}'
        print(ruta)
        
    except: pass

    funciones.registro_to_csv(pa,ruta,i)
    # # pa[4].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\dataframe{i}.csv')
    # anyo=pa[5].loc[1,1][-4:]
    # # print(anyo)
    # pa[2].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='w', index=False, header=False)
    # # pa[3].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # pa[4].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # pa[5].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # pa[6].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # pa[7].to_csv(fr'{ruta}\{i}_{anyo}.csv', mode='a', index=False, header=False)
    # print(pa[3].to_latex)
    # if (i==1):
    #     break

#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?

print('ok')


