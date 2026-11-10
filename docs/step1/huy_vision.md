# Bước 1 — Huy (Owner / Báo cáo / Ràng buộc)

> Issue: #8 · Milestone Bước 1 hết hạn 16/11/2026

## 1. User class — Gym Owner (SRS §2.2)

| User class | Mô tả | Tần suất sử dụng | Trình độ / kỹ năng | Quyền hạn chính | Favored? |
|---|---|---|---|---|---|
| Gym Owner | Chủ hoặc quản lý phòng gym, trực tiếp vận hành tại quầy | Trung bình–Cao: thao tác quầy nhiều lần mỗi ngày, xem báo cáo ít nhất 1 lần/tuần | Trung bình: dùng thành thạo trình duyệt và Excel, không có kiến thức kỹ thuật | Đăng ký và kích hoạt membership (UC-05, UC-06), duyệt tài khoản PT (UC-17), quản lý danh mục gói, xử lý khiếu nại, tạo và xuất báo cáo (UC-21, UC-22) | **Có**: Owner chịu trách nhiệm kinh doanh và ra quyết định, nên khi yêu cầu xung đột thì ưu tiên yêu cầu của Owner |

## 2. §2.3 Môi trường vận hành

- OE-1: Hệ thống chạy trên web, hiển thị đúng trên trình duyệt Chrome và Edge (2 phiên bản mới nhất) ở giao diện responsive.
- OE-2: Quầy dùng máy tính hoặc tablet; tablet tại cửa dùng camera để quét QR.
- OE-3: Máy chủ đặt trên cloud Linux, truy cập qua HTTPS; dữ liệu lưu trong CSDL quan hệ dùng chung cho mọi actor.
- OE-4: Tích hợp bên ngoài: Payment Gateway qua REST API, SMS Service qua API, module sinh và xác thực mã QR.

## 3. §2.4 Ràng buộc thiết kế và cài đặt

- CON-1: Tuân thủ Nghị định 13/2023/NĐ-CP khi thu thập và xử lý dữ liệu cá nhân của khách (CCCD, SĐT, email).
- CON-2: Giao diện bằng tiếng Việt; tiền tệ **VND**; múi giờ **UTC+7**; ngày hiển thị dạng **dd/mm/yyyy**.
- CON-3: Mọi sơ đồ UML, DFD, ERD vẽ bằng **Visual Paradigm** và nộp file `.vpp`; wireframe vẽ bằng Figma, Stitch hoặc draw.io.
- CON-4: Thanh toán online xử lý qua Payment Gateway bên ngoài; hệ thống không lưu số thẻ của khách.
- CON-5: Release 1 phục vụ 1 cơ sở phòng gym.
- CON-6: Mỗi bước nộp theo hạn milestone trên GitHub (Bước 1 hết hạn 16/11/2026); hạn nộp cả bài theo thông báo của giảng viên.

## 4. Scope báo cáo và thanh toán (Release 1)

| Trong phạm vi (Release 1) | Ngoài phạm vi / Release sau |
|---|---|
| Tạo báo cáo vận hành: doanh thu, lượt check-in, buổi PT hoàn tất (UC-21) | Tích hợp kế toán ERP đầy đủ |
| Xuất báo cáo ra file Excel (UC-22) | Xuất PDF; dashboard tùy biến theo người dùng |
| Thanh toán membership và gói PT qua cổng thanh toán, và thu tiền mặt tại quầy | Tự xây cổng thanh toán; lưu thông tin thẻ |
| Hoàn tiền qua cổng thanh toán khi PT từ chối hoặc quá 24 giờ không phản hồi (BR-08, BR-09) | Chi nhánh đa quốc gia, đa tiền tệ |
| Tiếp nhận và xử lý khiếu nại cơ bản (UC-25, UC-26) | Hóa đơn điện tử, kê khai thuế |

## 5. BO-04 (đo được)

| ID | Mục tiêu kinh doanh | Chỉ số đo (success metric) |
|---|---|---|
| BO-04 | Chủ gym ra quyết định vận hành dựa trên số liệu thay cho thống kê thủ công | Trong 3 tháng đầu sau khi đưa vào sử dụng: (1) ≥ 90% lượt xuất báo cáo tháng ra Excel hoàn tất trong **≤ 60 giây**; (2) Owner mở báo cáo **ít nhất 1 lần/tuần** trong ≥ 10 trên 12 tuần |

**Cách đo:**

- **Chỉ số (1) — thời gian xuất báo cáo:** chạy 20 lần trên môi trường thử với dữ liệu 1 tháng gồm 500 membership đang hoạt động, 15.000 lượt check-in và 400 booking PT. Mỗi lần bấm giờ từ lúc Owner bấm "Tạo báo cáo" đến lúc tải xong file `.xlsx`. Đạt khi có ít nhất 18 trên 20 lần ≤ 60 giây (tương đương 90%).
- **Chỉ số (2) — mức độ sử dụng:** đếm từ log hệ thống số tuần trong 12 tuần đầu có ít nhất 1 lượt Owner mở trang báo cáo. Đạt khi có ≥ 10 trên 12 tuần.

## 6. BR / CSKH (nháp, nhóm chốt chính thức ở Bước 3)

| ID | Business rule | Loại | Nguồn |
|---|---|---|---|
| BR-12 | Khiếu nại chỉ được tạo trong **7 ngày** sau buổi tập hoặc sự kiện liên quan | Constraint | CSKH |
| BR-13 | Khi booking PT bị từ chối hoặc quá 24 giờ không được phản hồi, hệ thống hoàn **100%** số tiền đã thu trong vòng **3 ngày làm việc**, về đúng phương thức thanh toán ban đầu (cổng thanh toán hoặc tiền mặt tại quầy), không khấu trừ phí giao dịch | Action enabler | CSKH / Tài chính |

## 7. References (§1.4)

1. Nhóm SWR302, `HuongDan_Assignment.md` — Hướng dẫn assignment SRS, FPT University.
2. Chính phủ Việt Nam, *Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân*, 17/04/2023.
3. Visual Paradigm Community — tài liệu hướng dẫn UML/ERD (https://www.visual-paradigm.com).
4. Wiegers, K. & Beatty, J., *Software Requirements*, 3rd Edition, Microsoft Press, 2013 — các chương 11, 12, 14, 17 được đề nhắc tới.
5. IEEE Std 830-1998, *IEEE Recommended Practice for Software Requirements Specifications*.
6. `kimi2.5-project.md` — ý tưởng ban đầu của nhóm.
