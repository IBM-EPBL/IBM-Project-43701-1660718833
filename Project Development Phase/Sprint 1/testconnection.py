import ibm_db

try:
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=vsv60334;PWD=JAWPs1gz8WWAbsMX;", "", "")
     print("connected to database")
except:
       print("Error in connection")     
server = ibm_db.server_info(conn)
print("DBMS_NAME:", server.DBMS_NAME)
print("DBMS_VER:", server.DBMS_VER)
print("DB_NAME:", server.DB_NAME)
