Thay vì log chỉ ra console, ta ghi vào file.

Ví dụ:
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

Sau đó chạy lại test → sẽ tạo file app.log.
🎯 BÀI TẬP
1. Cấu hình logging để ghi ra file automation.log
2. Format phải có:
   - Timestamp
   - Level
   - Message
Sau đó chạy thử get_user_by_email với email không tồn tại.