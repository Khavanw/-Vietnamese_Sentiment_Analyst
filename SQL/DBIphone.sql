-- Tạo cơ sở dữ liệu SalesPhone
CREATE DATABASE SalesPhone;
GO

-- Sử dụng cơ sở dữ liệu SalesPhone
USE SalesPhone;
GO

-- Tạo bảng users
CREATE TABLE users (
    id INT IDENTITY PRIMARY KEY,
    username VARCHAR(255) unique,
    full_name NVARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
GO

-- Tạo bảng phone
CREATE TABLE phone (
    id INT IDENTITY PRIMARY KEY,
    phone_name NVARCHAR(MAX),
    specifications NVARCHAR(MAX),
	photo NVARCHAR(MAX)
);
GO

-- Tạo bảng comment
CREATE TABLE comment (
    id INT IDENTITY PRIMARY KEY,
    user_id INT,
    comment NVARCHAR(MAX),
    predict NVARCHAR(MAX)
    FOREIGN KEY (user_id) REFERENCES users(id)
);
GO

-- Tạo bảng comment_phone
CREATE TABLE comment_phone (
    id_phone INT NOT NULL, 
    id_comment INT NOT NULL,
    PRIMARY KEY (id_phone, id_comment),
    FOREIGN KEY (id_phone) REFERENCES phone(id),
    FOREIGN KEY (id_comment) REFERENCES comment(id)
);
GO

INSERT INTO users (username, full_name, password) VALUES
('user1', N'Nguyễn Văn A', '123'),
('user2', N'Trần Thị B', '123'),
('user3', N'Lê Văn C', '123'),
('user4', N'Phạm Thị D', '123');
GO

INSERT INTO phone (phone_name, specifications, photo) VALUES
(N'iPhone 11', '[12MP, 4GB, 64GB, 3110mAh, Iphone(Apple)]', 'https://cdn.tgdd.vn/Products/Images/42/153856/iphone-11-trang-200x200.jpg'),
(N'iPhone 12', '[12MP, 4GB, 64GB, 2815mAh, Iphone(Apple)]', 'https://cdn.tgdd.vn/Products/Images/42/213031/iphone-12-trang-13-600x600.jpg'),
(N'iPhone 12 Pro', '[12MP, 6GB, 128GB, 2815mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2020/10/thumb_IP12Pro_3.jpg'),
(N'iPhone 12 Pro Max', '[12MP, 6GB, 128GB, 3687mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2020/10/thumb_IP12Pro_3.jpg'), 
(N'iPhone 13', '[12MP, 4GB, 128GB, 3240mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/x/media/catalog/product/1/5/15_2_8_1.jpg'),
(N'iPhone 13 Pro', '[12MP, 6GB, 128GB, 3095mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/4/_/4_36_3_2_1_5.jpg'),
(N'iPhone 13 Pro Max', '[12MP, 6GB, 128GB, 4352mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/4/_/4_36_3_2_1_9.jpg'),
(N'iPhone 14', '[12MP, 6GB, 128GB, 3279mAh, Iphone(Apple)]', 'https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/2222.png'),
(N'iPhone 14 Pro', '[48MP, 6GB, 128GB, 3200mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2023/10/4.jpg'),
(N'iPhone 14 Pro Max', '[48MP, 6GB, 512GB, 4323mAh, Iphone(Apple)]','https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg');