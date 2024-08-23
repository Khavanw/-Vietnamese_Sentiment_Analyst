use SalesPhone;

SELECT * FROM dbo.comment;

-- Xóa dữ liệu từ bảng liên quan
DELETE FROM dbo.comment_phone WHERE id_comment IN (SELECT id FROM dbo.comment); 

DELETE FROM dbo.comment;
