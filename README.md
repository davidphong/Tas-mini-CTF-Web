# SQL to SSRF Challenge

Đây là một challenge CTF về SQL Injection và Server-Side Request Forgery (SSRF). Challenge này mô phỏng một ứng dụng blog đơn giản với các chức năng cơ bản như xem bài viết, đăng nhập admin và thêm bài viết mới.

## Mô tả Challenge

Ứng dụng web này có các chức năng chính:
- Xem danh sách bài viết
- Xem chi tiết bài viết
- Đăng nhập vào trang admin
- Thêm bài viết mới (yêu cầu quyền admin)

## Các lỗ hổng tiềm ẩn

1. SQL Injection:
   - Có thể khai thác thông qua tham số ID trong URL khi xem chi tiết bài viết
   - Không có prepared statements cho một số truy vấn SQL

2. SSRF (Server-Side Request Forgery):
   - Chức năng thêm bài viết cho phép nhập URL hình ảnh
   - Server sẽ thực hiện request đến URL được cung cấp
   - Có thể khai thác để truy cập các dịch vụ nội bộ

## Cách chạy challenge

1. Đảm bảo đã cài đặt Docker và Docker Compose
2. Clone repository này
3. Chạy lệnh:
```bash
docker-compose up --build
```
4. Truy cập ứng dụng tại http://localhost:5000

## Cấu trúc ứng dụng

- `src/`: Chứa mã nguồn chính của ứng dụng
  - `app.py`: File chính chứa logic của ứng dụng
  - `templates/`: Chứa các file template HTML
  - `static/`: Chứa các file tĩnh (CSS, JS, images)
- `init/`: Chứa các file khởi tạo database
- `dockerfile`: Cấu hình Docker cho ứng dụng
- `docker-compose.yaml`: Cấu hình Docker Compose

## Mục tiêu

Tìm và khai thác các lỗ hổng trong ứng dụng để:
1. Truy cập được vào tài khoản admin
2. Đọc được thông tin nhạy cảm từ database
3. Thực hiện SSRF để truy cập các dịch vụ nội bộ

## Lưu ý

- Challenge này chỉ dành cho mục đích học tập và thực hành
- Không sử dụng các kỹ thuật tấn công vào các hệ thống thực tế
- Tuân thủ các quy định và điều khoản của cuộc thi CTF 