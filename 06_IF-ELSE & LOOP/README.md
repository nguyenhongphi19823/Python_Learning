(Bắt đầu tư duy automation thật sự)

Bây giờ thêm đoạn này vào dưới code của bạn:

for user in lst:
    if user["role"] == "admin":
        print("Found admin:", user["email"])

👉 Chạy thử.

🧠 Giải thích
for user in lst:

Python sẽ lấy từng dictionary trong list.

if user["role"] == "admin":

Kiểm tra điều kiện.

Đây chính là logic bạn sẽ dùng khi:

Verify element
Verify role
Verify status
Verify API response
🧪 BÀI TẬP

1️⃣ In ra email của user có role = tester
2️⃣ Nếu không có admin thì in "No admin found"