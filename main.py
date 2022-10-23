# from signal import pause
import funciones
import pandas as pd
import time

apellido1="ROCH"

url,html=funciones.researcher(Pa1=apellido1)
nPages=funciones.getNpages(html)


for i in range(int(nPages)+1):
    print(i)
    # time.sleep(1)
    try:
        url,html=funciones.researcher(Pa1=apellido1,Ppagina=int(i))
        pa=pd.read_html(html)
    except:
        pass
    # pa[4].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\dataframe{i}.csv')
    print(pa[5].loc[1,1][-4:])
    pa[2].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='w')
    pa[3].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='a')
    pa[4].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='a')
    pa[5].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='a')
    pa[6].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='a')
    pa[7].to_csv(fr'D:\OneDrive - UPV\3-Ocio\4-Programacion\2-Genealogia\df{apellido1}{i}.csv',mode='a')
    
    if (i>10): 
        break



#meterlo en sql o otro lugar q se vea bien rapido
#¿pasar a gedcom?

print('ok')


