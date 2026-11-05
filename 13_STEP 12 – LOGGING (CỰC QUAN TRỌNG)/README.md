Automation không dùng print().

Automation chuyên nghiệp dùng logging.
🎯 1️⃣ Vì sao không dùng print?
print("User created")


Vấn đề:
- Không có level (INFO, ERROR…)
- Không có timestamp
- Không ghi vào file
- Khó debug khi test lớn
🎯 2️⃣ Dùng logging cơ bản

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Test started")
logging.warning("This is a warning")
logging.error("Something went wrong")

Output sẽ như:
INFO:root:Test started
WARNING:root:This is a warning
ERROR:root:Something went wrong

🧠 3️⃣ Logging level
Level	Khi dùng
DEBUG	Debug chi tiết
INFO	Thông tin bình thường
WARNING	Có vấn đề nhẹ
ERROR	Lỗi
CRITICAL	Lỗi nghiêm trọng


Automation thường dùng:
- INFO
- ERROR
- DEBUG
🚀 STEP 13 – Logging chuyên nghiệp hơn
Thay vì dùng root logger, ta tạo logger riêng:

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("User created")
logger.error("Login failed")

__name__ giúp biết log đến từ file nào.
🎯 BÀI TẬP
Thêm logging vào UserManager.

Ví dụ:

def add_user(self, email, role):
    logger.info(f"Adding user {email}")
    self.users.append({"email": email, "role": role})

Và trong get_user_by_email:
logger.error(f"User {email} not found")


📌 Mục tiêu bài này
- Không dùng print nữa
- Thay bằng logging
- Hiểu level log
