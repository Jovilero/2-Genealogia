# Sunday, October 30, 2022 @ 01:19:59 AM
import os, sys
import psycopg2 

# Importamos los ajustes de la database.
import database as Settings

# Importamos la libreria psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

# Función para conectar con la database utilizando la libreria psycopg2.
def pgConnect():
    conn=psycopg2.connect(database = Settings.DATABASE, 
                          user = Settings.USER,
                          password = Settings.PASSWORD, 
                          host = Settings.HOST,
                          port =Settings.PORT)
    print("Connected")
    return conn

# Función para desconectar con la database 
def pgDisconnect(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()
    print("Disconnected")
