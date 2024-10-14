from flask import Flask, send_file
import requests
import io
from datetime import datetime

app = Flask(__name__)
datetime = datetime.now()
str_yes_format_file = datetime.strftime('%Y/%m/%d %H:%M:%S')

@app.route('/download')
def download_csv():
    url = 'https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv'  # Thay thế bằng URL thực tế
    response = requests.get(url)

    if response.status_code == 200:
        # Tạo một đối tượng BytesIO từ nội dung
        csv_file = io.BytesIO(response.content)
        # Gửi tệp CSV về client
        return send_file(csv_file, download_name=f'{str_yes_format_file}.csv', as_attachment=True)
    else:
        return f"Không thể tải tệp. Mã trạng thái: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
