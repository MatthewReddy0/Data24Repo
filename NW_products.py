import statistics
import pyodbc


class NWProducts:

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        # {ODBC Driver 17 for SQL Server}
        self.docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server +
                                               ';DATABASE=' + self.database + ';UID=' + self.username +
                                               ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        query_records = self._sql_query('SELECT * FROM Products')
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        query_records = self._sql_query('SELECT AVG(UnitPrice) FROM Products')
        print('The average UnitPrice is')
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

        # Alternative Python method
        total_unit_price = []
        query_records = self._sql_query('SELECT * FROM Products')
        print('The average UnitPrice is')
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            total_unit_price.append(record.UnitPrice)
        print(statistics.mean(total_unit_price))



stuff = NWProducts()
stuff.print_average_unit_price()
