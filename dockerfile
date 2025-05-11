# Sử dụng Python 3.9 làm base image
FROM python:3.9-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy mã nguồn ứng dụng vào container
COPY src/ .

# Cài đặt các package cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng mà Flask sẽ chạy
# Chạy ứng dụng Flask
CMD ["sh", "-c", "python app.py"]
