import pyodbc
from pprint import pprint

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# {ODBC Driver 17 for SQL Server}
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='
                                  + username+';PWD=' + password)
cursor = docker_Northwind.cursor()

cursor.execute('SELECT * FROM Customers')
row = cursor.fetchone()
print(row)

cursor.execute('SELECT AVG(p.UnitsOnOrder) AS \'Average Units on Order\', s.CompanyName FROM Products p INNER JOIN '
               'Suppliers s ON p.SupplierID = s.SupplierID GROUP BY p.SupplierID, s.CompanyName')
row = cursor.fetchone()
print(row)

# Problem: fetchall() stores all the rows in memory. Dangerous.
# rows = cursor.execute('SELECT * FROM Products').fetchall()
# Instead:
rows = cursor.execute('SELECT * FROM Products')
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

