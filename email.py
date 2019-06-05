import imaplib, email, os

user = "m2dkcorreo@gmail.com"    #User name del correo al que queremos acceder
password = "12345678abcde"       #Contrasena del correo al que queremos acceder
imap_url = "imap.gmail.com"      #Algo que no se muy bien como funciona


connection = imaplib.IMAP4_SSL(imap_url)        #Conexion de tipo IMAP4 que provee python para poder hacer la verificacion con gmail
connection.login(user,password)                 #Conexion que toma como parametros el user creado anteriormente y la contrasena del correo
connection.list()
connection.select("inbox")
                                                #print(connection.select('INBOX')) #Print para saber si me estoy conectando
result, data = connection.uid('search',None,"ALL")
latest_email_uid = data[0].split()[-1]
result,data = connection.uid ('fetch',latest_email_uid,'(RFC822)')
#print(data[0][1])
raw_email = data[0][1]
raw = email.message_from_string(raw_email)

connection.logout()
#print(get_body(raw))