# Bước 2 — Danh sách Actor & Use Case (chi tiết để vẽ VP)

> **Chưa làm Bước 2.** Khung tham khảo sớm — nhóm sẽ chia & chốt lại sau Bước 1.  
> Gợi ý từ nháp Vision (đã chỉnh lỗi bản kimi).  
> Quota: **≥ 20 UC không tính Login** → hiện **27 UC** (UC-01, UC-03…UC-28 trừ UC-02).  
> Ngôn ngữ tên UC: **tiếng Việt** (Động từ + Danh từ) — thống nhất toàn bộ SRS/UCD.

---

## 1. Actor

| Actor | Primary / Secondary | Generalization | Ghi chú |
|-------|---------------------|----------------|---------|
| User | Abstract | — | Cha của 3 actor người (Login, Thông báo) |
| Customer | Primary | ← User | Hội viên |
| Personal Trainer | Primary | ← User | HLV |
| Gym Owner | Primary | ← User | Chủ / QL |
| Payment Gateway | Secondary | — | Cổng TT |
| SMS Service | Secondary | — | SMS |
| QR Service | Secondary | — | QR |
| Time / Scheduler | Secondary | — | Job định kỳ |

**Đạt:** ≥ 3 primary người + ≥ 1 secondary hệ thống.

---

## 2. Package (chia UCD)

| Package | Mã gợi ý sơ đồ | UC |
|---------|----------------|----|
| Account | UCD-02 | UC-01, UC-02, UC-03 |
| Membership | UCD-03 | UC-04…UC-09, UC-20, UC-23, UC-27 |
| PT | UCD-04 | UC-10…UC-18, UC-24 |
| Notify | UCD-05 | UC-19, UC-28 |
| Report | UCD-06 | UC-21, UC-22 |
| Feedback | UCD-07 | UC-25, UC-26 |

Tổng quan: **UCD-01 Overview** (có thể chỉ hiện High + quan hệ chính; chi tiết theo package).

---

## 3. Bảng Use Case đầy đủ

| UC-ID | Tên | Primary | Secondary | Ưu tiên | Package | Mục tiêu (1 câu) | BR liên quan |
|-------|-----|---------|-----------|---------|---------|------------------|--------------|
| UC-01 | Đăng ký tài khoản Customer | Customer | SMS (opt.) | H | Account | Tạo tài khoản hội viên để dùng GMS | — |
| UC-02 | Đăng nhập hệ thống | User | — | H | Account | Xác thực và mở phiên theo vai trò | — |
| UC-03 | Cập nhật hồ sơ | Customer / PT | — | M | Account | Sửa thông tin cá nhân được phép | NĐ-13 |
| UC-04 | Xem gói Membership | Customer | — | M | Membership | Xem danh mục gói trước khi đăng ký | — |
| UC-05 | Đăng ký Membership tại quầy | Gym Owner | Payment (opt.) | H | Membership | Tạo membership cho Customer tại quầy | BR-01, BR-02 |
| UC-06 | Kích hoạt Membership | Gym Owner | SMS, QR | H | Membership | Chuyển ACTIVE + sinh QR sau khi đủ phí | BR-01–04 |
| UC-07 | Xem mã QR Membership | Customer | — | H | Membership | Hiển thị QR của membership ACTIVE | BR-04 |
| UC-08 | Check-in bằng QR | Customer | QR Service | H | Membership | Ghi nhận vào cửa hợp lệ | BR-04, BR-05 |
| UC-09 | Check-out bằng QR | Customer | QR Service | H | Membership | Ghi nhận ra cửa | BR-04, BR-05 |
| UC-10 | Xem hồ sơ PT | Customer | — | M | PT | Chọn PT trước khi đặt gói | BR-07 |
| UC-11 | Đặt gói PT | Customer | Payment, SMS, PT | H | PT | Tạo booking Pending + thanh toán | BR-06, BR-08 |
| UC-12 | Xác nhận / Từ chối booking PT | PT | SMS, Payment | H | PT | PT phản hồi trong 24h | BR-07–09 |
| UC-13 | Tạo lịch tập | PT | SMS | M | PT | Lên lịch các buổi thuộc booking Confirmed | BR-10 |
| UC-14 | Xem lịch tập | Customer, PT | — | M | PT | Xem lịch đã xếp | — |
| UC-15 | Ghi nhận buổi tập | PT | — | H | PT | Đánh dấu buổi đã tập / còn buổi | BR-10 |
| UC-16 | Đăng ký tài khoản PT | PT | — | H | PT | Nộp hồ sơ chờ duyệt | BR-07 |
| UC-17 | Duyệt tài khoản PT | Gym Owner | SMS | H | PT | Approve/Reject PT | BR-07 |
| UC-18 | Quản lý gói dịch vụ PT | PT | — | M | PT | CRUD gói buổi của PT (sau Approved) | BR-07 |
| UC-19 | Xem thông báo | User | — | L | Notify | Đọc thông báo in-app | — |
| UC-20 | Gia hạn Membership | Gym Owner / Customer | Payment, SMS | H | Membership | Gia hạn gói còn hạn / vừa hết hạn | BR-02–04 |
| UC-21 | Tạo báo cáo vận hành | Gym Owner | — | M | Report | Xem báo cáo doanh thu / check-in / PT | BO-04 |
| UC-22 | Xuất báo cáo Excel | Gym Owner | — | M | Report | Tải file Excel từ báo cáo | BO-04 |
| UC-23 | Quản lý gói Membership | Gym Owner | — | H | Membership | CRUD danh mục gói membership | — |
| UC-24 | Hủy booking PT | Customer | Payment, SMS | M | PT | Hủy theo chính sách; hoàn tiền nếu đủ ĐK | BR-09 |
| UC-25 | Gửi phản hồi / khiếu nại | Customer | — | M | Feedback | Tạo khiếu nại trong 7 ngày | BR-12 |
| UC-26 | Xử lý khiếu nại | Gym Owner | SMS | M | Feedback | Đổi trạng thái + phản hồi KH | BR-12 |
| UC-27 | Tự hết hạn Membership | Time | SMS | H | Membership | ACTIVE→EXPIRED, vô hiệu QR | BR-11 |
| UC-28 | Nhắc lịch tập | Time | SMS | M | Notify | Nhắc buổi sắp tới | — |

### Ghi chú so với bản kimi

| Bản kimi | Cách nhóm làm |
|----------|----------------|
| UC-20 = Send SMS (actor SMS) | SMS là **secondary** gắn nhiều UC — không tính 1 UC riêng kiểu “hệ thống gửi SMS” là mục tiêu user |
| UC-23 = Process Payment | Thanh toán = **include** / secondary Payment Gateway |
| Confirm `<<extend>>` Reject | **Sai** — gộp **alternative flows** trong UC-12 |
| Thiếu Feedback / Scheduler / Gia hạn | Đã thêm UC-20, UC-24–28 |

---

## 4. Include / Extend / Generalization (đúng ngữ nghĩa)

| Quan hệ | Từ | Đến | Điều kiện / lý do |
|---------|----|-----|-------------------|
| «include» | UC-11 Đặt gói PT | *(UC) Xử lý thanh toán* | Bắt buộc khi book online |
| «include» | UC-08 Check-in | *(UC) Xác thực QR* | Bắt buộc mỗi lần quét |
| «include» | UC-06 Kích hoạt | *(UC) Sinh mã QR* | Bắt buộc khi ACTIVE |
| «include» | UC-20 Gia hạn | *(UC) Xử lý thanh toán* | Khi thu phí gia hạn |
| «extend» | Nhập mã thủ công | UC-08 | Camera/QR lỗi (DE-03) |
| «extend» | Áp mã khuyến mãi | UC-05 / UC-11 | Có mã KM |
| Actor gen. | User | Customer, PT, Gym Owner | Login / Thông báo |

> Có thể tạo UC kỹ thuật nhỏ `UC-Pay Xử lý thanh toán`, `UC-QR-Val Xác thực QR`, `UC-QR-Gen Sinh mã QR` chỉ để thể hiện include trên UCD (không tính vào quota 20 nếu giảng viên chỉ tính UC nghiệp vụ — nhóm ghi chú trong SRS).

**Đạt rubric UCD:** ≥ 2 include, ≥ 2 extend, ≥ 1 generalization actor.

---

## 5. Map Actor → UC (để kéo association trên VP)

### Customer
UC-01, UC-02, UC-03, UC-04, UC-07, UC-08, UC-09, UC-10, UC-11, UC-14, UC-19, UC-20*, UC-24, UC-25  
(*gia hạn online nếu cho phép; tại quầy thì Owner)

### Personal Trainer
UC-02, UC-03, UC-12, UC-13, UC-14, UC-15, UC-16, UC-18, UC-19

### Gym Owner
UC-02, UC-05, UC-06, UC-17, UC-19, UC-20, UC-21, UC-22, UC-23, UC-26

### Payment Gateway
UC-05 (opt.), UC-11, UC-12 (refund), UC-20, UC-24

### SMS Service
UC-01 (opt.), UC-06, UC-11, UC-12, UC-13, UC-17, UC-26, UC-27, UC-28

### QR Service
UC-06, UC-08, UC-09

### Time / Scheduler
UC-27, UC-28

---

## 6. Hướng dẫn vẽ UCD (Bước 3 — chuẩn bị sẵn)

1. `UCD-01 Overview`: System boundary **GMS**; 3 actor người + 4 secondary; UC High + mũi tên quan hệ chính.
2. Từng package: `UCD-02`…`UCD-07` đủ UC trong bảng.
3. Export → `03_Images/UCD_Overview.png`, `UCD_Membership.png`, …

---

## 7. Việc tiếp theo sau khi chốt list này

1. Phước vẽ **CD-01** theo `02_Context_Diagram_DataFlows.md`.  
2. Cả nhóm rà lại tên UC / package (đặc biệt chính sách hoàn tiền BR-08/09).  
3. Sang Bước 3: Anh Tuấn dựng package PT; Phước overview + Membership.
