🎯 1️⃣ Cơ bản
Thử viết:
x = 10 / 0


Chạy thử.

Bạn sẽ thấy:
ZeroDivisionError

Chương trình dừng.
🎯 2️⃣ Bắt lỗi với try/except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

Giờ chương trình không crash nữa.

try:
    # code có thể lỗi
except SomeError:
    # xử lý khi lỗi xảy ra
finally:
    # luôn chạy

🎯 Ví dụ thực tế cho automation
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

🚀 STEP 8 – Bắt nhiều loại lỗi
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
🚀 STEP 9 – Bắt mọi lỗi (cẩn thận khi dùng)
try:
    something
except Exception as e:
    print("Error:", e)

e chứa message lỗi.

Automation thường log lỗi này.

🎯 BÀI TẬP
Viết function:
def safe_get_email(user):

Yêu cầu:
- Trả về user["email"] nếu tồn tại
- Nếu không có key "email" → return None
- Không để chương trình crash
Gợi ý:

try:
    ...
except KeyError:
    ...