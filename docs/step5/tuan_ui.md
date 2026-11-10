# Bước 5 — Anh Tuấn (UI UC-11, UC-12)

> Issue: #26 · Nhánh: `step5/tuan-ui`

## Màn hình & PNG

| UC | Tên màn hình | File PNG |
|----|--------------|----------|
| UC-11 | Book a PT Package | `03_Images/UI_UC11.jpg` |
| UC-12 | Manage PT Booking Requests | `03_Images/UI_UC12.jpg` |

### Trạng thái file ảnh

- UC-11: `03_Images/UI_UC11.jpg` — ảnh UI đã lưu, kích thước 1342 × 1600 px.
- UC-12: `03_Images/UI_UC12.jpg` — ảnh UI đã lưu, kích thước 1080 × 1600 px.
- Hai ảnh dùng cùng phong cách giao diện GMS PULSE: nền sáng, thẻ nội dung bo góc, màu chủ đạo xanh teal và bố cục desktop.

### Quyết định thiết kế UI

1. UC-11 dùng bố cục nhiều bước: `Select PT` → `Select Package` → `Schedule` → `Promotion` → `Order Summary` → `Payment`.
2. UC-12 dùng màn hình quản lý booking một trang, có danh sách và phần chi tiết.
3. Payment method hiển thị các lựa chọn cụ thể: `VNPay`, `MoMo`, `Credit Card`.
4. Rejection reason dùng dropdown lý do có sẵn và lựa chọn `Other` để nhập thêm.
5. UC-12 hiển thị countdown/thời hạn phản hồi 24 giờ, ví dụ: `18 hours remaining`.
6. Tên màn hình giữ là `Book a PT Package` và `Manage PT Booking Requests`.

## Bảng field (tóm tắt)

| Màn hình | Field | Bắt buộc | Validation / lỗi |
|----------|-------|----------|------------------|
| UC-11 — Book PT Package | PT / package | Có | Phải chọn PT đã Approved và package đang hoạt động |
| UC-11 — Book PT Package | Preferred date/time | Có | Không được ở quá khứ; phải nằm trong lịch cho phép |
| UC-11 — Book PT Package | Note | Không | Tối đa 500 ký tự |
| UC-11 — Book PT Package | Promotion code | Không | Mã phải hợp lệ, còn hạn và áp dụng được |
| UC-11 — Book PT Package | Payment method | Có | Phải được Payment Gateway hỗ trợ |
| UC-12 — Booking detail | Decision | Có | Chọn Confirm hoặc Reject |
| UC-12 — Booking detail | Rejection reason | Có khi Reject | Không được để trống; tối đa 500 ký tự |

## Gợi ý bố cục wireframe

### UC-11 — Book a PT Package

- Header: `Gym Management System`, Customer navigation, và tiêu đề màn hình.
- Step 1: chọn PT, hiển thị tên, hồ sơ tóm tắt và trạng thái Approved.
- Step 2: chọn package, số buổi, thời hạn và giá.
- Schedule: chọn preferred date/time và nhập note.
- Promotion: nhập promotion code và hiển thị kết quả validation.
- Order summary: PT, package, giá gốc, giảm giá, tổng tiền và payment method.
- Actions: `Cancel` và `Pay & Confirm Booking`.
- Thông báo lỗi phải hiển thị gần field bị lỗi; không cho submit khi thiếu field bắt buộc.
- Ảnh hiện tại thể hiện trạng thái thanh toán thành công tạo booking `Pending` và gửi yêu cầu đến Personal Trainer.

### UC-12 — Manage PT Booking Requests

- Header: `Gym Management System`, PT navigation, và tiêu đề quản lý booking.
- Bộ lọc: Pending, Confirmed, Rejected.
- Mỗi booking hiển thị booking ID, Customer, package, preferred time, thời điểm tạo và thời hạn phản hồi 24 giờ.
- Chi tiết booking hiển thị note của Customer và payment status.
- Actions: `Confirm` và `Reject`.
- Khi chọn `Reject`, hiển thị trường `Rejection reason` bắt buộc.
- Sau khi xử lý, hiển thị trạng thái mới và thông báo kết quả.
- Ảnh hiện tại hiển thị countdown phản hồi, trạng thái thanh toán `Paid`, nút `Confirm Booking`, nút `Reject Booking` và form rejection reason.

## Liên hệ với đặc tả Use Case

Wireframe phải đối chiếu với các file fully dressed:

- `docs/step4/UC-11.md`
- `docs/step4/UC-12.md`

Các field và trạng thái trên UI phải hỗ trợ main flow, alternative flows và exceptions đã mô tả trong hai file này.
