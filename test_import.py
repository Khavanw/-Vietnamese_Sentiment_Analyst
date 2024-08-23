import pyodbc

connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no'

try:
    with pyodbc.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Kết nối thành công:", result)
except pyodbc.Error as e:
    print("Lỗi kết nối:", e)