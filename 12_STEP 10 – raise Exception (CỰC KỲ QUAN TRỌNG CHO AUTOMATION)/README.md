Đây là bước chuyển từ:
“Không để chương trình crash”

sang:
“Chủ động làm test fail khi cần”

🧠 1️⃣ Raise là gì?
raise = chủ động ném lỗi.

Ví dụ:
raise Exception("Something went wrong")


Chạy sẽ thấy:
Exception: Something went wrong

Chương trình dừng.
🎯 2️⃣ Khác gì với return?
❌ return
return None


→ Trả về giá trị
→ Không làm chương trình dừng  
🔥 raise
raise Exception("Email not found")


→ Dừng chương trình ngay
→ Báo lỗi rõ ràng  
🧠 3️⃣ Ứng dụng vào automation
Giả sử bạn viết:
def get_required_email(user):
    if "email" not in user:
        raise Exception("User must have email")
    return user["email"]

Test thử:
print(get_required_email({"role": "admin"}))


Sẽ fail:
Exception: User must have email
🎯 Khi nào dùng return, khi nào dùng raise?
Trường hợp	Dùng gì?
Có thể chấp nhận thiếu dữ liệu	return
Không thể chấp nhận	raise
Business rule bắt buộc	raise
Validation input	raise


🧠 Automation mindset
Automation không nên:
if not found:
    print("Fail")
Automation nên:

if not found:
    raise AssertionError("User not found")

🚀 STEP 11 – Custom Exception (nhẹ, nhưng quan trọng)
Bạn có thể tạo exception riêng:
class UserNotFoundError(Exception):
    pass
Dùng:
raise UserNotFoundError("User not found")


Sau này framework lớn thường có custom error.

🎯 BÀI TẬP
Thêm method vào UserManager:
def get_user_by_email(self, email):


Yêu cầu:
- Nếu tồn tại → return user dictionary
- Nếu không tồn tại → raise Exception("User not found")

Ví dụ:
manager.get_user_by_email("a@test.com")  # trả về user
manager.get_user_by_email("x@test.com")  # raise Exception

