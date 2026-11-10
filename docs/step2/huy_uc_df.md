# Bước 2 — Huy (DF + UC Owner / Report / Feedback / Time)

> Issue: #13 · Nhánh: `step2/huy-uc-df`

## 1. External Entities phụ trách (cho Context Diagram)

| Entity Name | Loại | Mô tả tương tác |
|---|---|---|
| **Payment Gateway** | External System | Cổng thanh toán (VNPay/Momo/Stripe) xử lý giao dịch online và gửi lại xác nhận thanh toán/hoàn tiền |
| **SMS Service** | External System | Dịch vụ gửi SMS (Twilio/Vonage) nhận nội dung từ GMS để gửi mã OTP, thông báo kích hoạt, nhắc lịch |
| **Timer / Time Event** | Temporal Event | Động cơ đếm thời gian hệ thống tự động kích hoạt tác vụ: hết hạn membership, hủy booking tự động sau 24h |

---

## 2. Data flows (Luồng dữ liệu)

| ID | From | To | Data Flow Content |
|---|---|---|---|
| DF-01 | PT | GMS | Thông tin đăng ký tài khoản PT (Họ tên, chứng chỉ, kinh nghiệm, chuyên môn) |
| DF-02 | Gym Owner | GMS | Quyết định duyệt/từ chối tài khoản PT & Lý do отказ (nếu có) |
| DF-03 | GMS | PT | Thông báo kết quả duyệt tài khoản |
| DF-04 | Gym Owner | GMS | Tiêu chí lọc báo cáo (Khoảng thời gian, loại báo cáo doanh thu/check-in/PT) |
| DF-05 | GMS | Gym Owner | Dữ liệu báo cáo hiển thị trên màn hình & File xuất dạng `.xlsx` |
| DF-06 | Customer / PT | GMS | Nội dung gửi khiếu nại / phản hồi chất lượng dịch vụ |
| DF-07 | GMS | Gym Owner | Danh sách phản hồi/khiếu nại cần tiếp nhận và xử lý |
| DF-08 | GMS | Payment Gateway | Yêu cầu hoàn tiền (Refund request) khi PT từ chối/quá hạn 24h |
| DF-09 | Payment Gateway | GMS | Trạng thái hoàn tiền thành công/thất bại |
| DF-10 | GMS | SMS Service | Nội dung tin nhắn SMS cần gửi đến Customer/PT |

---

## 3. Use Cases phụ trách (Đầy đủ theo Issue #13)

| UC-ID | Tên Use Case | Actor chính | Mô tả ngắn |
|---|---|---|---|
| **UC-16** | Register PT Account | Personal Trainer | PT gửi đăng ký tài khoản kèm thông tin hồ sơ năng lực lên hệ thống. |
| **UC-17** | Approve PT Account | Gym Owner | Owner xem xét hồ sơ và phê duyệt hoặc từ chối tài khoản PT. |
| **UC-21** | Generate Reports | Gym Owner | Hệ thống tổng hợp số liệu doanh thu, lượt check-in và buổi tập PT để hiển thị báo cáo. |
| **UC-22** | Export Excel Report | Gym Owner | Xuất dữ liệu báo cáo vận hành ra file định dạng Excel (`.xlsx`). |
| **UC-23** | Process Payment & Refund | Payment Gateway | Xử lý giao dịch thanh toán online và hoàn tiền tự động khi hủy booking. |
| **UC-25** | Submit Feedback/Complaint | Customer / PT | Người dùng gửi ý kiến đóng góp hoặc khiếu nại về sự cố/buổi tập. |
| **UC-26** | Process Complaint | Gym Owner | Owner xem danh sách, cập nhật trạng thái xử lý và phản hồi khiếu nại. |
| **UC-28** | Auto-Cancel Pending Booking | Timer | Hệ thống tự động hủy booking và kích hoạt hoàn tiền nếu PT không phản hồi sau 24h. |

---