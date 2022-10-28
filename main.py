# Wednesday, October 26, 2022 @ 03:20:25 PM
#ctrl+shift+t
#JJVL

import funciones


apellido1="Carratala"
apellido2=""
desde=1500
hasta=1950
# funciones.search_getPages_ToCSV(
#     nombreCarpeta=apellido1,
#     nombreSubCarpeta='', 
#     Pa1=apellido1,
#     Pprincipio=desde
# )

if hasta-desde>100:
    # nVeces=desde/10
    # print(nVeces)
    i=0
    hasta=desde+5
    while desde<hasta:
        i=i+1
        print("mamahuevo")
        desde=desde+1
        funciones.search_getPages_ToCSV(
        nombreCarpeta=1400,
        nombreSubCarpeta='', 
        # Pa1=apellido1,
        Pprincipio_evento=desde,
        Pfinal_evento=hasta
        )
        desde=desde-1
        hasta=hasta+5
        desde=desde+5
        print(fr'{desde}-{hasta}')
        if hasta>=1550:
            break
else:
    funciones.search_getPages_ToCSV(
    nombreCarpeta=apellido1,
    nombreSubCarpeta='', 
    Pa1=apellido1,
    Pprincipio=desde
    )
# nombreCarpeta=apellido1
# nombreSubCarpeta=''
# Pnom=''
# # Pa1=''
# Pa2=''
# Pa2p=''
# Pa2m=''
# Pa1ap=''
# Pa1am=''
# Plnac=''
# Plins=''
# Plpa=''
# Plma=''
# Plabuopat=''
# Plabuapat=''
# Plabuomat=''
# Plabuamat=''
# Plconyuge=''
# Pltots=''
# Plevent=''
# Pcognomcj=''
# Pcognomq=''
# Pprofeq=''
# Pnompa=''
# Pnomma=''
# Pnomcon=''
# Ppagina='1'
# Pprincipio=''
# Pfinal='nnnn'
# Psexo=''
# Pprincipio_evento=''
# Pfinal_evento='nnnn'
# Pobserva=''
# # Pfiltre='P'
# # Porden='evento'
# # PSubmit='BUSCAR'


