Tras descargar el repositorio:
Abrir main.py y elegir los parametros de busqueda. p.e.: apellido1='Roger'

Main.py crea en el mismo directorio donde se ejecute una subcarpeta para cada uno de los parametros de busqueda elegidos
Los parametros de busqueda estan definidos en la función researcher, y son los siguientes:

    Pnom=''               - nombre
    Pa1=''                - apellido 1
    Pa2=''                - apellido 2
    Pa2p=''               - apellido 2 del padre
    Pa2m=''               - apellido 2 de la madre
    Pa1ap=''              - apellido 1 del abuelo paterno
    Pa1am=''              - apellido 1 del abuelo materno
    Plnac=''              - Lugar de nacimiento del interesado
    Plins=''              - Lugar de inscripción del evento
    Plpa=''               - Lugar de nacimiento del padre
    Plma=''               - Lugar de nacimiento de la madre
    Plabuopat=''          - Lugar de nacimiento del abuelo paterno
    Plabuapat=''          - Lugar de nacimiento de la abuela paterna
    Plabuomat=''          - Lugar de nacimiento de la abuelo materno
    Plabuamat=''          - Lugar de nacimiento de la abuela materno
    Plconyuge=''          - Lugar de nacimiento del conyuge
    Pltots=''             - Lugar de nacimiento de cualquiera que conste en el registro
    Plevent=''            - Lugar del evento
    Pcognomcj=''          - Apellido del conyuge
    Pcognomq=''           - Apellido de cualquiera del registro
    Pprofeq=''            - Profesion del interesado 
    Pnompa=''             - Nombre del padre
    Pnomma=''             - Nombre de la madre
    Pnomcon=''            - Nombre del conyuge
    Ppagina='1'           - Número de página /** se recomienda no modificar este parametro 
    Pprincipio=''         - Año de nacimiento inicio del rango de busqueda
    Pfinal='nnnn'         - Año de nacimiento final del rango de busqueda
    Psexo=''              - Sexo del interesado
    Pprincipio_evento=''  - Año del evento inicio del rango de  busqueda
    Pfinal_evento='nnnn'  - Año del evento final del rango de busqueda
    Pobserva=''           - Observación que conste en el registro
    Pfiltre=['P','F','C'] - 3 Opciones de filtrado para las cadenas de texto: Coincide principio, Coincide final, contiene 
    Porden='evento'       - Orden de respuesta del resultado: 4º Opciones - Por apellido, por año de evento, año de nacimiento o por lugar de inscripcion
    PSubmit='BUSCAR'      - Parametro por defecto
    
    
Para buscar registros sin fechas Pfinal = '' y/o Pfinal_evento=''
