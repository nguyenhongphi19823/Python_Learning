Bây giờ bạn đã hiểu:
- List
- Dict
- Loop
- Return
- Boolean logic
- Assert mindset
Chúng ta chuyển sang thứ cực quan trọng cho Playwright:
👉 CLASS & OBJECT
Automation framework = OOP.
🧱 Bài học tiếp theo
Chúng ta sẽ biến đoạn logic này thành class:
----------
class UserManager:
    def __init__(self, users):
        self.users = users

    def has_role(self, role):
        ...
--------
Đây chính là nền tảng của Page Object Model.
----------
class UserManager:

    def __init__(self, users):
        self.users = users

    def has_role(self, role):
        for user in self.users:
            if user["role"] == role:
                return True
        return False


manager = UserManager(lst)

print(manager.has_role("admin"))
print(manager.has_role("manager"))
--------

🧠 1️⃣ class UserManager:
👉 Tạo một blueprint (khuôn mẫu).

Class = bản thiết kế.
Object = sản phẩm được tạo ra từ bản thiết kế đó.

Ví dụ đời thực:
- Class = Bản thiết kế ngôi nhà
- Object = Ngôi nhà được xây
Trong automation:
- Class = LoginPage
- Object = 1 trang login cụ thể
🧠 2️⃣ def __init__(self, users):
__init__ là constructor.

Nó chạy khi bạn tạo object:

manager = UserManager(lst)
Khi dòng này chạy:
UserManager(lst)

Python tự động gọi:
__init__(self, lst)


🧠 self là gì?
self = chính object đó.

Nó cho phép object:
- Lưu dữ liệu
- Gọi method bên trong class

🧠 3️⃣ self.users = users
Dòng này nghĩa là:
Lưu danh sách users vào object.

Sau dòng này, object manager sẽ chứa:
manager.users


🧠 4️⃣ def has_role(self, role):
Đây là method của class.

Khác với function thường:
def has_role(users, role):


Method luôn có self.
🧠 5️⃣ for user in self.users:
Vì users đã được lưu vào object, nên ta truy cập bằng:
self.users


🧠 6️⃣ return True / return False
Logic giống như bạn đã học trước đó.

Nếu tìm thấy role → True
Nếu không → False  
🧠 7️⃣ manager = UserManager(lst)
Đây là tạo object.

Sau dòng này:
manager

Là một object có:
- manager.users
- manager.has_role()
🧠 8️⃣ manager.has_role("admin")
Cách Python xử lý nội bộ:
UserManager.has_role(manager, "admin")


Python tự động truyền manager vào tham số self.
🎯 Kết quả
print(manager.has_role("admin"))     # True
print(manager.has_role("manager"))   # False







