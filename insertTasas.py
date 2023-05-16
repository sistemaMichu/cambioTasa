import pyodbc,funciones as fun


# Datos de Conexión a SQL

server = "ARTEMISA\PROFIT"
datatest=["A_CBMICHU"]
databases=["A_RAVIADOR","A_RCFMICHU","A_RCHMICHU","A_RCLMICHO","A_RCOPMICHU","A_RCPMICHU","A_RCRMICHU","A_RGUARENAS","A_RORINOQUIA","A_RSAMBIL","AK_CMICHUBV","AK_CBMICHU","AK_CRESMICHU","AK_RADMJML","A_RCMICHU"]
username = 'profit'
password = 'profit'
driver = '{SQL Server Native Client 11.0}'

#Contadores de Intentos
fallidos=0
exitosos=0
fecha=fun.fechaTasa()
tasa=fun.tasaDelDia()

#Bucle de Conexión a Bases de Datos

for database in databases:
        cnxn_str = ';'.join([
        'DRIVER=' + driver,
        'SERVER=' + server,
        'DATABASE=' + database,
        'UID=' + username,
        'PWD=' + password
    ])

        try:
            cnxn = pyodbc.connect(cnxn_str)

            cnxn.autocommit = True

        # Crear un cursor para la conexión actual
            cursor = cnxn.cursor()
        # Ejecutar una consulta en la base de datos actual
            cursor.execute(f"""INSERT INTO [saTasa] ([co_mone],[fecha],[tasa_c],[tasa_v],[campo1],[campo2],[campo3],[campo4],[campo5],[campo6],[campo7],[campo8],[co_us_in],[co_sucu_in],[fe_us_in],[co_us_mo],[co_sucu_mo],[fe_us_mo]) VALUES ('US$','{fecha}',{tasa},{tasa},NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'PROFIT','01','{fecha}','PROFIT','01','{fecha}')""")
        
            cnxn.close()
            exitosos+=1
        except pyodbc.Error as ex:
            print('Error: ',ex)
            fallidos+=1

print("Tasa Valuada en {} insertada Satisfactoriamente en {} Bases de Datos para el día {}.".format(tasa,exitosos,fecha))
print("Proceso de Insercion de Tasas Fallido en {} Bases de Datos.".format(fallidos))


