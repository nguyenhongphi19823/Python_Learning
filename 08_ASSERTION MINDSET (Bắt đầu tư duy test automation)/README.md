Bây giờ thêm:
result = get_emails_by_role(lst, "tester")

assert len(result) > 0
print("Test passed")


🧠 Nếu đổi thành:
result = get_emails_by_role(lst, "manager")

assert len(result) > 0
print("Test passed")


👉 Chạy thử.
Bạn sẽ thấy lỗi kiểu:
AssertionError

Đây chính là cách test automation fail.
🧠 Vì sao assert quan trọng?
Automation framework (pytest) hoạt động dựa trên:
assert actual == expected

Không cần:
if ... print("fail")

🎯 BÀI TẬP
Viết:
def has_role(users, role):


Yêu cầu:
- Trả về True nếu tồn tại role
- False nếu không
Gợi ý:
return True
return False


Sau đó:
assert has_role(lst, "admin") is True
assert has_role(lst, "manager") is False