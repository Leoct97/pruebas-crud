import pyodbc
import os
import json

# host = os.environ["url"]
# Base = os.environ["DB"]
# user = os.environ["usr"]
# pwd = os.environ["pwd"]

host = "localhost"
Base = "crud2"
user = "sa"
pwd = "<YourStrong@Passw0rd>"


connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host};DATABASE={Base};UID={user};PWD={pwd};TrustServerCertificate=yes'

conn = pyodbc.connect(connectionString)

sql_query = "select * from articulos"
cursor = conn.cursor()
cursor.execute(sql_query)
select = cursor.fetchall()
dato2 = [dict(zip(["ïd","nombre","precio"],row)) for row in select]
datos = json.dumps(dato2)