# BƯỚC 1 — Vision & Scope: Gym Management System (GMS)

> **Trạng thái: NHÁP THAM KHẢO — Bước 1 chưa được nhóm hoàn thành / chốt.**  
> Mỗi thành viên làm phần trong `docs/01_PHAN_CONG_BUOC1.md`, rồi Phước ghép vào Mục 1–2 của `01_SRS_GMS.docx`.  
> Nguồn ý tưởng: `kimi2.5-project.md`. Chuẩn: `HuongDan_Assignment.md` (BO đo được, scope rõ, user class).

---

## Thông tin nhóm

| Vai trò | Họ tên | MSSV | Phụ trách chính |
|---------|--------|------|-----------------|
| Leader | **Phước** | _điền_ | Vision/Scope, CD, Traceability, UC-05/06, ghép SRS |
| Thành viên | **Anh Tuấn** | _điền_ | PT Booking UC-11/12, AD-01, UCD package PT |
| Thành viên | **Thiên** | _điền_ | QR Check-in UC-08/15, SMD-01/02 |
| Thành viên | **Huy** | _điền_ | UC-16/17, ERD, Reports, NFR, Feedback |

- Mã nhóm: `NhomXX`
- Mã lớp: `_điền_`
- Giảng viên: `_điền_`

---

## 1.1 Mục đích tài liệu

Tài liệu SRS mô tả yêu cầu phần mềm **GMS phiên bản 1.0** — hệ thống quản lý phòng gym: thành viên (membership), mã QR check-in/out, dịch vụ Personal Trainer (PT), thanh toán và báo cáo vận hành.

| Đối tượng đọc | Mục đích |
|---------------|----------|
| Gym Owner / Product Owner | Xác nhận phạm vi & nghiệp vụ |
| Nhóm BA / SWR302 | Baseline yêu cầu |
| Developer / Tester | Hiện thực & thiết kế test từ UC/FR |
| Giảng viên SWR302 | Chấm assignment |

---

## 1.2 Quy ước tài liệu

- Font: Times New Roman 13, Multiple 1.3; mục lục & đề mục tự động.
- ID: `BO-xx`, `BR-xx`, `UC-xx`, `FR-xx` / `<FEATURE>-xx`, `NFR-<Loại>-xx`, `SCR-xx`.
- Ưu tiên: High / Medium / Low.
- **shall** = bắt buộc; **should** = khuyến nghị; **may** = tùy chọn.
- Ngôn ngữ tài liệu: **tiếng Việt** (tên UC có thể giữ tiếng Anh ngắn gọn như trong bản kimi, nhưng mô tả luồng bằng tiếng Việt — **nhóm chọn 1 kiểu và thống nhất**). Khuyến nghị: tên UC dạng *Động từ + Danh từ* tiếng Việt.

---

## 1.3 Phạm vi dự án

### Tóm tắt sản phẩm

**GMS** tập trung hóa vận hành phòng gym: quản lý khách hàng & PT, gói membership, kích hoạt thẻ + QR check-in/out, đặt gói PT, lịch tập, thanh toán, thông báo SMS/in-app, và báo cáo xuất Excel.

### Business objectives

| ID | Mục tiêu kinh doanh | Chỉ số đo (success metric) |
|----|---------------------|----------------------------|
| BO-01 | Giảm thời gian đăng ký & kích hoạt thành viên tại quầy | Thời gian hoàn tất Register→Activate (đã thu đủ phí) **≤ 5 phút**/khách với ≥ 90% ca |
| BO-02 | Tăng tỷ lệ thành viên check-in đúng quy trình (không vào “lậu”) | ≥ **95%** lượt vào cửa có bản ghi check-in hợp lệ trong giờ mở cửa |
| BO-03 | Tăng doanh thu dịch vụ PT và giảm booking “treo” | ≥ **80%** PT booking chuyển khỏi _Pending_ trong **24 giờ**; tỷ lệ no-show buổi PT **≤ 15%** |
| BO-04 | Chủ gym ra quyết định vận hành dựa trên số liệu | Báo cáo doanh thu / check-in / PT hoàn tất xuất được trong **≤ 1 phút**; dùng hàng tuần bởi Owner |

### Phạm vi Release 1

| Trong phạm vi (Release 1) | Ngoài phạm vi / Release sau |
|---------------------------|-----------------------------|
| Đăng ký/đăng nhập/cập nhật hồ sơ: Customer, PT, Gym Owner | App native iOS/Android riêng (R1: web responsive) |
| Quản lý gói Membership; đăng ký tại quầy; kích hoạt; QR membership | Thiết bị turnstile phần cứng chuyên dụng (chỉ interface QR) |
| Check-in / check-out bằng QR | Wearable / vân tay |
| Hồ sơ PT; duyệt đăng ký PT; gói dịch vụ PT; đặt/xác nhận/từ chối booking | Marketplace PT ngoài phòng gym |
| Lịch tập; ghi nhận buổi tập | Chương trình dinh dưỡng / bán thực phẩm |
| Thanh toán membership & gói PT qua cổng thanh toán + tiền mặt tại quầy | Tích hợp kế toán ERP đầy đủ |
| Thông báo in-app + SMS | Chat realtime Customer–PT |
| Khiếu nại / phản hồi dịch vụ (cơ bản) | AI lộ trình tập |
| Báo cáo vận hành + xuất Excel | Chi nhánh đa quốc gia / đa tiền tệ |

---

## 2.1 Bối cảnh sản phẩm

GMS là **sản phẩm mới**, thay cho sổ giấy / Excel rời. Hệ thống độc lập, tích hợp **Payment Gateway**, **SMS Service**, và module **QR** (xác thực mã). Tác vụ định kỳ (hết hạn membership, nhắc lịch) dùng actor **Time/Scheduler**.

> **Bước 2:** chèn CD-01 (Visual Paradigm) + bảng ≥12 data flow.

**External entity dự kiến:** Customer, Personal Trainer, Gym Owner, Payment Gateway, SMS Service, QR Validator/Service, Time/Scheduler.

---

## 2.2 User classes & đặc điểm

| User class | Mô tả | Tần suất | Trình độ | Quyền hạn chính | Favored? |
|------------|-------|----------|----------|-----------------|----------|
| Customer | Hội viên tập gym | Cao | Cơ bản | Xem gói, QR, đặt PT, lịch, phản hồi | **Có** |
| Personal Trainer (PT) | HLV cá nhân | Cao | Cơ bản–TB | Gói PT, xác nhận booking, lịch, ghi buổi tập | **Có** |
| Gym Owner | Chủ/QL phòng gym | TB–Cao | TB | Duyệt PT, membership, báo cáo, cấu hình gói | **Có** |
| (Hệ thống) Payment Gateway | Thanh toán | Theo GD | — | Callback kết quả | — |
| (Hệ thống) SMS Service | Gửi SMS | Theo sự kiện | — | Gửi tin | — |
| (Hệ thống) QR Service | Xác thực QR | Theo lượt vào/ra | — | Validate mã | — |
| Time / Scheduler | Tác vụ hẹn giờ | Định kỳ | — | Hết hạn membership, nhắc lịch | — |

---

## 2.3 Môi trường vận hành

- Client: trình duyệt hiện đại, giao diện responsive; máy tablet tại quầy / cửa để quét QR.
- Server: cloud Linux, HTTPS.
- CSDL quan hệ.
- Tích hợp: REST Payment Gateway; SMS API; thư viện/module sinh & xác thực QR.

---

## 2.4 Ràng buộc thiết kế & cài đặt

- Tuân thủ **Nghị định 13/2023/NĐ-CP** (dữ liệu cá nhân: CCCD, SĐT, email).
- UI tiếng Việt; tiền tệ **VND**; múi giờ **UTC+7**; ngày **dd/mm/yyyy**.
- Sơ đồ UML/DFD/ERD bắt buộc **Visual Paradigm**; wireframe: Figma / Stitch / draw.io.

---

## 2.5 Giả định & phụ thuộc

| ID | Giả định / Phụ thuộc | Ảnh hưởng nếu sai |
|----|----------------------|-------------------|
| AS-01 | Quầy luôn có Gym Owner/nhân sự được ủy quyền trong giờ mở cửa | Đăng ký membership tại quầy bị tắc |
| AS-02 | Mỗi membership ACTIVE có đúng 1 QR ổn định đến khi hết hạn/đổi thẻ | Check-in sai thành viên |
| AS-03 | Customer phải có membership ACTIVE mới đặt gói PT | Cần luồng bán kèm / ngoại lệ walk-in |
| DE-01 | Payment Gateway có sandbox | Không test UC thanh toán end-to-end |
| DE-02 | SMS provider khả dụng | Cần fallback thông báo in-app + hiển thị mã trên UI |
| DE-03 | Thiết bị quét QR (camera điện thoại/tablet) đủ sáng & ổn định | Tăng tỷ lệ quét lỗi → cần nhập mã thủ công (extend) |

---

## 2.6 Business Rules

| ID | Business rule | Loại | Nguồn |
|----|---------------|------|-------|
| BR-01 | Chỉ Gym Owner (đã đăng nhập) được đăng ký membership tại quầy và kích hoạt thẻ | Constraint | Phân quyền |
| BR-02 | Membership chỉ chuyển **ACTIVE** khi đã ghi nhận **đủ phí** gói | Constraint | Tài chính |
| BR-03 | Ngày hết hạn = ngày kích hoạt + `DurationMonths` của gói (theo lịch, cuối ngày 23:59 UTC+7) | Computation | Gói tập |
| BR-04 | Mỗi membership ACTIVE có **một** mã QR duy nhất; QR bị vô hiệu khi status ≠ ACTIVE | Constraint | Check-in |
| BR-05 | Check-in hợp lệ chỉ trong **giờ mở cửa** cơ sở và membership đang ACTIVE | Constraint | Vận hành |
| BR-06 | Customer chỉ đặt gói PT khi có membership **ACTIVE** còn hiệu lực ≥ 1 ngày | Constraint | Upsell PT |
| BR-07 | PT chỉ thao tác booking/lịch sau khi tài khoản ở trạng thái **Approved** | Constraint | Duyệt PT |
| BR-08 | PT phải phản hồi booking _Pending_ trong **24 giờ**; quá hạn hệ thống tự **Cancel** và hoàn tiền (nếu đã thu) | Constraint / Action enabler | Trải nghiệm KH |
| BR-09 | Từ chối booking: bắt buộc nhập lý do; nếu đã thanh toán → khởi tạo hoàn tiền | Action enabler | CSKH |
| BR-10 | Ghi nhận buổi tập chỉ với booking **Confirmed** và còn buổi chưa dùng | Constraint | PT session |
| BR-11 | Scheduler: membership ACTIVE có `end_date < hôm nay` → chuyển **EXPIRED**, vô hiệu QR, gửi SMS | Action enabler | Time |
| BR-12 | Khiếu nại chỉ tạo trong **7 ngày** sau buổi tập / sự kiện liên quan | Constraint | CSKH |

---

## Danh sách Actor (chốt Bước 2)

| Actor | Loại | User class |
|-------|------|------------|
| Customer | Primary | Customer |
| Personal Trainer | Primary | PT |
| Gym Owner | Primary | Gym Owner |
| Payment Gateway | Secondary | — |
| SMS Service | Secondary | — |
| QR Service | Secondary | — |
| Time / Scheduler | Secondary | — |

> ≥ 3 primary người + secondary hệ thống: **đạt**. Generalization gợi ý: `User` ← Customer, PT, Gym Owner (cho Login / Update Profile).

---

## Danh sách Use Case đề xuất (≥20, **không tính Login**)

Giữ tinh thần bản kimi, bổ sung UC thiếu theo Phần C HuongDan (feedback, hủy/gia hạn, scheduler, quản lý gói…).

| UC-ID | Tên use case (Động từ + Danh từ) | Primary | Secondary | Ưu tiên | Package |
|-------|----------------------------------|---------|-----------|---------|---------|
| UC-01 | Đăng ký tài khoản Customer | Customer | SMS | H | Account |
| UC-02 | Đăng nhập hệ thống | Customer/PT/Owner | — | H | Account *(không tính vào quota 20)* |
| UC-03 | Cập nhật hồ sơ | Customer/PT | — | M | Account |
| UC-04 | Xem gói Membership | Customer | — | M | Membership |
| UC-05 | Đăng ký Membership tại quầy | Gym Owner | Payment (opt.) | H | Membership |
| UC-06 | Kích hoạt Membership | Gym Owner | SMS | H | Membership |
| UC-07 | Xem mã QR Membership | Customer | — | H | Membership |
| UC-08 | Check-in bằng QR | Customer | QR Service | H | Membership |
| UC-09 | Check-out bằng QR | Customer | QR Service | H | Membership |
| UC-10 | Xem hồ sơ PT | Customer | — | M | PT |
| UC-11 | Đặt gói PT | Customer | Payment, SMS, PT | H | PT |
| UC-12 | Xác nhận / Từ chối booking PT | PT | SMS, Payment | H | PT |
| UC-13 | Tạo lịch tập | PT | SMS | M | PT |
| UC-14 | Xem lịch tập | Customer, PT | — | M | PT |
| UC-15 | Ghi nhận buổi tập | PT | — | H | PT |
| UC-16 | Đăng ký tài khoản PT | PT | — | H | PT |
| UC-17 | Duyệt tài khoản PT | Gym Owner | SMS | H | PT |
| UC-18 | Quản lý gói dịch vụ PT | PT | — | M | PT |
| UC-19 | Xem thông báo | Customer, PT, Owner | — | L | Notify |
| UC-20 | Gia hạn Membership | Gym Owner / Customer | Payment, SMS | H | Membership |
| UC-21 | Tạo báo cáo vận hành | Gym Owner | — | M | Report |
| UC-22 | Xuất báo cáo Excel | Gym Owner | — | M | Report |
| UC-23 | Quản lý gói Membership (danh mục) | Gym Owner | — | H | Membership |
| UC-24 | Hủy booking PT | Customer | Payment, SMS | M | PT |
| UC-25 | Gửi phản hồi / khiếu nại | Customer | — | M | Feedback |
| UC-26 | Xử lý khiếu nại | Gym Owner | SMS | M | Feedback |
| UC-27 | Tự hết hạn Membership | Time | SMS | H | Membership |
| UC-28 | Nhắc lịch tập | Time | SMS | M | Notify |

**Đếm quota:** UC-01,03–28 trừ UC-02 ≈ **27 UC** (đạt ≥20).

### Include / Extend / Generalization (gợi ý đúng ngữ nghĩa)

| Quan hệ | Từ → Đến | Ghi chú |
|---------|----------|---------|
| include | UC-11 Đặt gói PT → UC-ProcessPayment (tách thành UC include hoặc gọi secondary) | Thanh toán bắt buộc khi book online |
| include | UC-08 Check-in → Validate QR | Bắt buộc |
| include | UC-06 Activate → Generate QR | Bắt buộc |
| extend | Nhập mã thủ công → UC-08 Check-in | Khi camera/QR lỗi (DE-03) |
| extend | Áp mã khuyến mãi → UC-05 / UC-11 | Tùy chọn |
| generalization actor | User ← Customer, PT, Gym Owner | Cho Login / View Notifications |

> Bản kimi ghi `Confirm <<extend>> Reject` là **sai ngữ nghĩa** — Confirm/Reject là **alternative flows trong cùng UC-12**, không phải extend. Nhóm làm theo bảng trên.

---

## Đối tượng vòng đời (SMD)

### SMD-01 Membership
`Inactive` → `Active` → `Expired` / `Suspended` → (Renew) `Active` → Final (Deleted/Archived)  
Time event: `when(end_date passed)` / vô hiệu QR + SMS (BR-11).

### SMD-02 PT Booking
`Pending` → `Confirmed` → `In Progress` → `Completed`  
Nhánh: `Rejected`, `Cancelled`, `Payment Failed`.

---

## Quy trình nhiều bên (AD)

1. **AD-01** Đặt gói PT & thanh toán — Customer | GMS | PT | Payment | SMS  
2. **AD-02** Đăng ký & duyệt PT — PT | GMS | Gym Owner | SMS  
3. **AD-03** Đăng ký–kích hoạt membership tại quầy — Gym Owner | GMS | Customer | SMS/(Payment)

---

## ERD khái niệm — thực thể tối thiểu (≥10)

Customer, GymOwner, PT, MembershipPackage, Membership, PTPackage, PTBooking, TrainingSession, Payment, Notification, Complaint, CheckInLog  
(+ quan hệ N–N có thuộc tính → thực thể kết hợp nếu cần).

---

## Glossary khởi đầu

| Thuật ngữ | Định nghĩa | Ghi chú |
|-----------|------------|---------|
| Membership | Quan hệ hội viên gắn Customer + gói + khoảng thời gian + trạng thái | Có SMD |
| QR Membership | Mã QR định danh membership đang ACTIVE | BR-04 |
| Check-in / Check-out | Ghi nhận vào/ra cửa bằng QR | |
| PT Package | Gói buổi tập với Personal Trainer | |
| PT Booking | Đơn đặt gói PT | Có SMD |
| Training Session | Một buổi tập thuộc booking | |
| Activate | Chuyển membership sang ACTIVE sau khi đủ phí | UC-06 |
| Pending (booking) | Chờ PT phản hồi | BR-08 |
| Gym Owner | Chủ/quản lý vận hành phòng gym | |
| Scheduler | Tiến trình tự động theo thời gian | UC-27, UC-28 |

---

## Việc tiếp theo

→ Làm theo **`docs/01_PHAN_CONG_BUOC1.md`** (chia đều 4 người).  
→ Chỉ sang Bước 2 khi checklist cuối file đó đã tick đủ.
