import pyodbc
from function.Comment_file import Comment
from function.User_file import User

class CommentDao:
    def __init__(self):
        self.connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-U1FN3SK1\\MSSQLSERVER1;DATABASE=SalesPhone;Trusted_Connection=yes;Encrypt=no'

    # Thêm bình luận mới vào bảng 'comment'
    def insert_comment(self, user: User, comment: Comment):
        if user.getUserId is not None:
            try:
                with pyodbc.connect(self.connection_string) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute("INSERT INTO comment (user_id, comment) VALUES (?, ?)", (user.getUserId, comment.getComment))
                        conn.commit()
            except pyodbc.Error as e:
                print("Error inserting comment: ", e)
        else:
            print("User not found.")

    # Lấy tất cả các bình luận từ bảng 'comment'
    def get_comment_by_user(self):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT id, comment FROM comment")
                    comments = cursor.fetchall()
                    return comments
        except pyodbc.Error as e:
            print("Error fetching comments: ", e)
            return []

    #  Lấy ID của bình luận mới nhất.
    def get_comment_id_by_user(self):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT TOP 1 id FROM comment ORDER BY id DESC")
                    comment_id = cursor.fetchone()
                    return comment_id[0] if comment_id else None
        except pyodbc.Error as e:
            print("Error fetching comment ID: ", e)
            return None
    # Lấy thống kê về số lượng bình luận theo cảm xúc (Positive, Negative, Neutral) cho từng loại điện thoại.
    def statistical(self):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        SELECT 
                            phone.phone_name,
                            COUNT(CASE WHEN comment.predict = 2 THEN 1 END) AS number_of_positives,
                            COUNT(CASE WHEN comment.predict = 0 THEN 1 END) AS number_of_negatives,
                            COUNT(CASE WHEN comment.predict = 1 THEN 1 END) AS number_of_neutrals
                        FROM 
                            phone 
                        JOIN 
                            comment_phone ON phone.id = comment_phone.id_phone 
                        JOIN 
                            comment ON comment.id = comment_phone.id_comment
                        GROUP BY 
                            phone.phone_name;
                    """)
                    result = cursor.fetchall()
                    return result
        except pyodbc.Error as e:
            print("Error fetching statistics: ", e)
            return []
    # Cập nhật cảm xúc của bình luận.
    def update_comment(self, comment: Comment):
        if comment is not None:
            try:
                with pyodbc.connect(self.connection_string) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute("UPDATE comment SET predict = ? WHERE id = ?", (comment.getPredict, comment.getId))
                        conn.commit()
            except pyodbc.Error as e:
                print("Error updating comment: ", e)
        else:
            print("Comment not found.")
