import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Tải biến môi trường từ tệp .env
load_dotenv()

# Thông tin email
sender_email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
receiver_email = "huy.daoquang@vti.com.vn"

# Tạo đối tượng MIMEMultipart
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Thông báo quan trọng từ Công ty ABC"  
html = """
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .header, .footer {
            background-color: #007BFF;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .body {
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
        a {
            color: #1a73e8;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="color: white;">Tiêu đề Email</h1>
        </div>
        <div class="body">
            <p>Xin chào!</p>
            <p>Đây là nội dung chính của email. Bạn có thể thêm bất kỳ thông tin nào bạn muốn ở đây.</p>
            <p>Bạn có thể <a href="https://www.example.com">truy cập vào đây</a> để biết thêm thông tin.</p>
        </div>
        <div class="footer">
            <p style="color: white;">&copy; 2024 Công ty của bạn. Tất cả quyền được bảo lưu.</p>
            <p><a href="https://www.example.com/privacy-policy" style="color: white;">Chính sách bảo mật</a> | <a href="https://www.example.com/unsubscribe" style="color: white;">Hủy đăng ký</a></p>
        </div>
    </div>
</body>
</html>
"""

# Đính kèm nội dung HTML vào email
msg.attach(MIMEText(html, 'html'))

# Gửi email
try:
    # Kết nối đến server SMTP
    with smtplib.SMTP('smtp.tutorialspoint.com', 25) as server:
        server.starttls()  # Bắt đầu mã hóa TLS
        server.login(sender_email, password)  # Đăng nhập
        server.send_message(msg)  # Gửi email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
