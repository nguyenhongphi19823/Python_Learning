Mục tiêu
Biến UserManager thành một class có nhiều behavior:
- has_role()
- get_emails_by_role()
- count_users()
- add_user()
🧱 Bước 1 – Thêm method get_emails_by_role
Thêm vào class:
- ----------
class UserManager:

    def __init__(self, users):
        self.users = users

    def has_role(self, role):
        for user in self.users:
            if user["role"] == role:
                return True
        return False

    def get_emails_by_role(self, role):
        emails = []
        for user in self.users:
            if user["role"] == role:
                emails.append(user["email"])
        return emails
--------
Test thử:
-----
manager = UserManager(lst)

print(manager.get_emails_by_role("tester"))
print(manager.get_emails_by_role("manager"))
---------
🧠 Bước 2 – Thêm count_users()
---------
def count_users(self):
    return len(self.users)
--------
Test:
--------
print(manager.count_users())
---------
🧠 Bước 3 – Thêm add_user()
--------
def add_user(self, email, role):
    new_user = {"email": email, "role": role}
    self.users.append(new_user)
-------
Test:
------
manager.add_user("c@test.com", "manager")
print(manager.count_users())
print(manager.has_role("manager"))
-------
🔥 Tại sao đây là tư duy framework?
Bạn đang:
- Encapsulate data (self.users)
- Encapsulate behavior (methods)
- Không để logic rải rác bên ngoài
Sau này Playwright:
- -------
class LoginPage:
    def login(self, username, password):
        ...
---------
Giống hệt pattern bạn đang học.

🎯 BÀI TẬP CHO BẠN
Thêm method:
----
def remove_user_by_email(self, email):
------

Yêu cầu:
- Nếu tồn tại email → xóa
- Nếu không tồn tại → không lỗi
- Không dùng print
- Không return gì








