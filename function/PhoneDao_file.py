import pyodbc
from function.Phone_file import Phone
from function.Comment_file import Comment
import pyodbc
class PhoneDao:
    # Thực hiện truy vấn SQL để lấy tất cả các hàng từ bảng 'phone'
    def get_list_phone(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phone")
        phone_row = cursor.fetchall()
        conn.close()
        return phone_row
    
    # Thực hiện truy vấn SQL để lấy thông tin của một điện thoại cụ thể dựa trên 'phone_id'
    def get_phone(self, phone_id):
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no')
        cursor = conn.cursor()
        cursor.execute("SELECT id, phone_name, specifications, photo FROM phone WHERE id = ?", (phone_id))
        phone_row = cursor.fetchone()
        conn.close()
        return phone_row
    
    # Thực hiện truy vấn SQL để lấy id của điện thoại dựa trên 'phone_name'
    def get_id_by_phone(self,phone:Phone):
        conn=pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no")
        cursor=conn.cursor()
        cursor.execute("SELECT id FROM phone WHERE phone_name = ?", (phone.getPhoneName,))
        id_phone=cursor.fetchone
        conn.close()
        return id_phone [0] if id_phone else None
    
    # Thực hiện lệnh SQL để chèn liên kết giữa 'phone' và 'comment' vào bảng 'comment_phone'
    def insert_comment_phone(self,phone:Phone,comment:Comment):
            if  phone !=None:
                conn=pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no")
                cursor=conn.cursor()
                cursor.execute("insert comment_phone(id_phone,id_comment) values (?,?)",(phone.getId,comment.getId))
                cursor.commit()
                cursor.close()
            else: 
                print("User not found")