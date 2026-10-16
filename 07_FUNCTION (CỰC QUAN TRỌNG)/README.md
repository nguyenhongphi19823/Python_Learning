Bây giờ chúng ta nâng cấp level.
Hiện tại code của bạn đang viết trực tiếp trong file.
Automation chuyên nghiệp sẽ không viết logic rải rác như vậy.
Chúng ta sẽ gom logic lại thành function.
🧱 Viết function kiểm tra role
Thêm vào file:
def check_role(users, role):
    found = False

    for user in users:
        if user["role"] == role:
            print(f"Found {role}: {user['email']}")
            found = True

    if not found:
        print(f"No {role} found")
Sau đó gọi:
check_role(lst, "admin")
check_role(lst, "tester")


🧠 Vì sao function quan trọng?
Automation framework = 80% function + class.
Sau này bạn sẽ có:
login()
logout()
create_user()
delete_user()
check_error_message()

Tất cả đều là function hoặc method trong class.
🎯 BÀI TẬP
1️⃣ Viết function:
def get_emails_by_role(users, role):


Yêu cầu:
- Trả về list email theo role
- Không print
- Dùng return
Ví dụ:
get_emails_by_role(lst, "tester")

Phải trả về:
["b@test.com"]