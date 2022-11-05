import ibm_db
try:
     ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=vsv60334;PWD=JAWPs1gz8WWAbsMX;", "", "")
     print("connected to database")
except:
       print("Error in connection")     