# SWR302 - Software Requirements Specification
## Gym Management System (GMS)

**Nhóm**: [Tên nhóm của bạn]  
**Thành viên**: 
- [Họ tên - MSSV - Vai trò]
- [Họ tên - MSSV - Vai trò]
- [Họ tên - MSSV - Vai trò]
- [Họ tên - MSSV - Vai trò]

**Giảng viên hướng dẫn**: [Tên GV]  
**Ngày nộp**: [Ngày/tháng/năm]  
**Phiên bản**: 1.0

---

## Mục lục
1. [Tổng quan dự án](#1-tổng-quan-dự-án)
2. [Các Actor trong hệ thống](#2-các-actor-trong-hệ-thống)
3. [Danh sách Use Case](#3-danh-sách-use-case)
4. [Phân tích các sơ đồ](#4-phân-tích-các-sơ-đồ)
5. [Đặc tả Use Case chi tiết](#5-đặc-tả-use-case-chi-tiết)
6. [Wireframe màn hình](#6-wireframe-màn-hình)
7. [Tài liệu tham khảo](#7-tài-liệu-tham-khảo)

---

## 1. Tổng quan dự án

### 1.1. Tên dự án
**Gym Management System (GMS)** - Hệ thống Quản lý Phòng Gym

### 1.2. Mô tả
Hệ thống GMS được thiết kế để tập trung hóa các hoạt động vận hành của phòng gym, bao gồm:
- Quản lý tài khoản khách hàng (Customer)
- Quản lý tài khoản Huấn luyện viên cá nhân (Personal Trainer)
- Quản lý các gói tập (Membership Packages)
- Đăng ký và kích hoạt thành viên
- Tích hợp QR Code cho check-in/check-out
- Quản lý đặt lịch với PT (PT Booking)
- Quản lý lịch tập và ghi nhận buổi tập
- Báo cáo vận hành

### 1.3. Mục tiêu kinh doanh
1. Tập trung hóa thông tin khách hàng, PT, thành viên, đặt lịch và lịch sử tập
2. Hỗ trợ đăng ký thành viên tại quầy gym
3. Tạo mã QR ổn định cho mỗi thành viên đang hoạt động
4. Hỗ trợ check-in/check-out bằng QR Code
5. Cho phép Gym Owner duyệt yêu cầu đăng ký PT
6. Cho phép PT quản lý gói dịch vụ, đặt lịch và lịch tập
7. Gửi thông báo qua ứng dụng và SMS
8. Cung cấp báo cáo vận hành với khả năng xuất Excel

---

## 2. Các Actor trong hệ thống

### 2.1. Primary Actors (Người dùng chính)

| STT | Actor | Mô tả | Chức năng chính |
|-----|-------|-------|-----------------|
| 1 | **Customer** | Khách hàng đăng ký tập tại gym | Đăng ký tài khoản, xem gói tập, đặt PT, check-in/out bằng QR |
| 2 | **Personal Trainer (PT)** | Huấn luyện viên cá nhân | Đăng ký tài khoản PT, quản lý gói dịch vụ, xác nhận booking, tạo lịch tập |
| 3 | **Gym Owner** | Chủ phòng gym/quản lý | Duyệt tài khoản PT, quản lý gói membership, kích hoạt thẻ, xem báo cáo |

### 2.2. Secondary Actors (Hệ thống bên ngoài)

| STT | Actor | Mô tả | Tương tác |
|-----|-------|-------|-----------|
| 1 | **Payment Gateway** | Cổng thanh toán (Stripe/VNPay/Momo) | Xử lý thanh toán online cho membership và PT package |
| 2 | **SMS Service** | Dịch vụ gửi SMS (Twilio/Vonage) | Gửi thông báo xác nhận, nhắc lịch tập |
| 3 | **QR Service** | Hệ thống quét mã QR | Xác thực mã QR cho check-in/check-out |

---

## 3. Danh sách Use Case

### 3.1. Tổng quan (24 Use Cases)

| STT | Use Case ID | Tên Use Case | Actor chính | Mức độ ưu tiên |
|-----|-------------|--------------|-------------|----------------|
| 1 | UC-01 | Register Account | Customer | High |
| 2 | UC-02 | Login System | Customer, PT, Gym Owner | High |
| 3 | UC-03 | Update Profile | Customer, PT | Medium |
| 4 | UC-04 | View Membership Packages | Customer | Medium |
| 5 | UC-05 | Register Membership (at counter) | Gym Owner | High |
| 6 | UC-06 | Activate Membership | Gym Owner | High |
| 7 | UC-07 | View Membership QR Code | Customer | High |
| 8 | UC-08 | QR Check-in | Customer + QR Service | High |
| 9 | UC-09 | QR Check-out | Customer + QR Service | High |
| 10 | UC-10 | View PT Profiles | Customer | Medium |
| 11 | UC-11 | Book PT Package | Customer + Payment Gateway | High |
| 12 | UC-12 | Confirm/Reject Booking | PT | High |
| 13 | UC-13 | Create Training Schedule | PT | Medium |
| 14 | UC-14 | View Training Schedule | Customer, PT | Medium |
| 15 | UC-15 | Record Training Session | PT | High |
| 16 | UC-16 | Register PT Account | PT | High |
| 17 | UC-17 | Approve PT Account | Gym Owner | High |
| 18 | UC-18 | Manage PT Packages | PT | Medium |
| 19 | UC-19 | View Notifications | Customer, PT | Low |
| 20 | UC-20 | Send SMS Notification | SMS Service | Medium |
| 21 | UC-21 | Generate Reports | Gym Owner | Medium |
| 22 | UC-22 | Export Excel Report | Gym Owner | Medium |
| 23 | UC-23 | Process Payment | Payment Gateway | High |
| 24 | UC-24 | View Dashboard | Gym Owner | Medium |

### 3.2. Phân loại theo Package

**Package: Account Management**
- UC-01 Register Account
- UC-02 Login System
- UC-03 Update Profile

**Package: Membership Management**
- UC-04 View Membership Packages
- UC-05 Register Membership
- UC-06 Activate Membership
- UC-07 View Membership QR Code
- UC-08 QR Check-in
- UC-09 QR Check-out

**Package: PT Services**
- UC-10 View PT Profiles
- UC-11 Book PT Package
- UC-12 Confirm/Reject Booking
- UC-13 Create Training Schedule
- UC-14 View Training Schedule
- UC-15 Record Training Session
- UC-16 Register PT Account
- UC-17 Approve PT Account
- UC-18 Manage PT Packages

**Package: Payment & Reports**
- UC-19 View Notifications
- UC-20 Send SMS Notification
- UC-21 Generate Reports
- UC-22 Export Excel Report
- UC-23 Process Payment
- UC-24 View Dashboard

---

## 4. Phân tích các sơ đồ

### 4.1. Context Diagram (Sơ đồ ngữ cảnh)

**Các External Entities:**
1. **Customer**: Gửi thông tin đăng ký, yêu cầu booking; Nhận QR Code, thông báo
2. **Personal Trainer**: Gửi thông tin profile, lịch tập; Nhận yêu cầu booking
3. **Gym Owner**: Gửi cấu hình gói, phê duyệt; Nhận báo cáo
4. **Payment Gateway**: Nhận yêu cầu thanh toán, trả kết quả
5. **SMS Service**: Nhận nội dung SMS để gửi
6. **QR Service**: Gửi kết quả quét, nhận yêu cầu xác thực

**Luồng dữ liệu chính:**
Customer → GMS: Registration Data, Booking Request
Customer ← GMS: QR Code, Notification, Schedule

PT → GMS: Profile Data, Schedule Data, Booking Response
PT ← GMS: Booking Request, Approval Status

Gym Owner → GMS: Package Config, Approval Decision
Gym Owner ← GMS: Reports, Dashboard Data

GMS ↔ Payment Gateway: Payment Request/Response
GMS → SMS Service: SMS Content
GMS ↔ QR Service: QR Validation Request/Response

### 4.2. Use Case Diagram (UCD-01)

**Cấu trúc chính:**
+------------------+ +------------------+ +------------------+
| Customer | | Personal Trainer | | Gym Owner |
+------------------+ +------------------+ +------------------+
| | |
| | |
+----v-----------------------v-----------------------v----+
| GYM MANAGEMENT SYSTEM |
+----^-----------------------^-----------------------^----+
| | |
+----v----+ +----v----+ +----v----+
| Payment | | SMS | | QR |
| Gateway | | Service | | Service |
+---------+ +---------+ +---------+

**Các quan hệ:**
- `<<include>>`: 
  - Login <<include>> Verify Credentials
  - Book PT Package <<include>> Process Payment
  - QR Check-in <<include>> Validate QR
- `<<extend>>`:
  - Confirm Booking <<extend>> Reject Booking (điều kiện: không đủ slot)

### 4.3. Activity Diagram với Swimlane (AD-01: Book PT Package)

**Các Swimlane:** Customer | System | PT | Payment Gateway | SMS Service
Customer Lane:
[Start] → Chọn PT Package → Điền thông tin → Submit Request

System Lane:
← Nhận request → Validate thông tin
→ [Decision: Đủ slot?]
├── [No] → Thông báo hết slot → [End]
└── [Yes] → Tạo Booking (Pending) → Gửi notification PT
← Nhận phản hồi PT
→ [Decision: PT Accept?]
├── [No] → Cập nhật Rejected → Thông báo Customer → [End]
└── [Yes] → Tính phí → Gửi Payment Request

Payment Gateway Lane:
← Nhận request → Xử lý thanh toán
→ [Decision: Success?]
├── [No] → Trả Failed → [End]
└── [Yes] → Trả Success

System Lane (tiếp):
← Nhận Success → Cập nhật Booking (Confirmed)
→ [Fork]
├── Gửi SMS Content → SMS Service Lane → Gửi SMS → [Join]
└── Gửi Notification → Customer & PT → [Join]
→ [End]

SMS Service Lane:
← Nhận content → Gửi SMS xác nhận

### 4.4. State Machine Diagram (SMD-01: Membership Lifecycle)
[Initial]
|
v
[INACTIVE] ←--register-- [Customer]
|
| activate [payment verified] / send SMS
v
[ACTIVE] ←------------------+
| |
| | renew [payment received] / extend end_date
| expire [date > end] |
v |
[EXPIRED] |
| |
| delete |
v |
[SUSPENDED] --reactivate-->--+
|
v
[Final]

**Các Transition:**
| Từ Trạng thái | Sự kiện | Guard | Hành động | Đến Trạng thái |
|---------------|---------|-------|-----------|----------------|
| Initial | register | - | Tạo record | INACTIVE |
| INACTIVE | activate | payment verified | send SMS, generate QR | ACTIVE |
| ACTIVE | expire | current_date > end_date | notify customer | EXPIRED |
| ACTIVE | suspend | violation detected | notify customer | SUSPENDED |
| EXPIRED | renew | payment received | extend end_date | ACTIVE |
| SUSPENDED | reactivate | admin approval | send SMS | ACTIVE |
| Any | delete | - | archive data | Final |

### 4.5. State Machine Diagram (SMD-02: PT Booking Lifecycle)
[Initial]
|
v
[PENDING] ←--book-- [Customer]
|
| confirm [PT accepted & payment success]
v
[CONFIRMED]
|
| complete [all sessions done]
v
[COMPLETED]
|
| cancel [customer request]
v
[CANCELLED]
|
v
[Final]

### 4.6. ERD Conceptual (ERD-01)

**Các thực thể chính:**
+----------------+ +-------------------+ +----------------+
| Customer | | MembershipPackage | | GymOwner |
+----------------+ +-------------------+ +----------------+
| - CustomerID | | - PackageID | | - OwnerID |
| - FullName | | - Name | | - FullName |
| - Email | | - DurationMonths | | - Email |
| - Phone | | - Price | +----------------+
| - DOB | | - Description |
| - JoinDate | +-------------------+
+----------------+ |
| |
| 1 | 1
| |
| * | *
v v
+----------------+ +----------------+
| Membership | | PT |
+----------------+ +----------------+
| - MembershipID| | - PTID |
| - StartDate | | - FullName |
| - EndDate | | - Specialty |
| - Status | | - Experience |
| - QRCode | | - Status |
+----------------+ +----------------+
| |
| |
| * | 1
| |
v v
+----------------+ +----------------+
| PTBooking |<----->| PTPackage |
+----------------+ +----------------+
| - BookingID | | - PackageID |
| - BookingDate | | - Name |
| - Status | | - Sessions |
| - TotalAmount | | - PricePerSession
+----------------+ +----------------+
|
| *
|
v
+----------------+
|TrainingSession |
+----------------+
| - SessionID |
| - Date |
| - Time |
| - Status |
| - Notes |
+----------------+
|
| 1
|
v
+----------------+
| Payment |
+----------------+
| - PaymentID |
| - Amount |
| - Method |
| - Status |
| - GatewayRef |
+----------------+

**Các mối quan hệ:**
- Customer **1** — **0..*** Membership
- MembershipPackage **1** — **0..*** Membership
- PT **1** — **0..*** PTPackage
- Customer **1** — **0..*** PTBooking
- PT **1** — **0..*** PTBooking (là người được book)
- PTPackage **1** — **0..*** PTBooking
- PTBooking **1** — **0..*** TrainingSession
- PTBooking **1** — **1** Payment

---

## 5. Đặc tả Use Case chi tiết (Fully Dressed)

### 5.1. UC-05: Register Membership (Gym Owner)

**Use Case ID:** UC-05  
**Tên:** Register Membership  
**Actor chính:** Gym Owner  
**Actor phụ:** Customer (cung cấp thông tin), Payment Gateway (nếu thanh toán online)  
**Mức độ ưu tiên:** High  
**Loại:** Primary

**Mô tả tóm tắt:**  
Gym Owner đăng ký gói tập cho khách hàng tại quầy gym, nhập thông tin và chọn gói tập phù hợp.

**Luồng sự kiện chính:**
1. Gym Owner chọn chức năng "Register Membership"
2. Hệ thống hiển thị form nhập thông tin khách hàng
3. Gym Owner nhập thông tin: Họ tên, SĐT, Email, CCCD (nếu cần)
4. Hệ thống kiểm tra SĐT/Email chưa tồn tại
5. Gym Owner chọn Membership Package từ danh sách
6. Hệ thống tính toán phí và hiển thị tổng tiền
7. Gym Owner xác nhận thông tin
8. Hệ thống tạo Membership record với trạng thái INACTIVE
9. Gym Owner nhận thanh toán (tiền mặt hoặc chuyển khoản)
10. Hệ thống ghi nhận thanh toán và chuyển sang UC-06 Activate

**Luồng sự kiện thay thế:**
- 4a. SĐT/Email đã tồn tại: Hệ thống hiển thị thông báo và yêu cầu cập nhật thông tin
- 7a. Gym Owner hủy: Quay về màn hình chính

**Luồng ngoại lệ:**
- 8a. Lỗi kết nối DB: Hiển thị lỗi, cho phép thử lại

**Điều kiện tiên quyết:**
- Gym Owner đã đăng nhập
- Có ít nhất 1 Membership Package đang hoạt động

**Điều kiện sau:**
- Membership record được tạo với trạng thái INACTIVE
- Thông tin khách hàng được lưu (nếu là khách mới)

**Yêu cầu đặc biệt:**
- QR Code chỉ được tạo sau khi Activate (UC-06)

---

### 5.2. UC-06: Activate Membership (Gym Owner)

**Use Case ID:** UC-06  
**Tên:** Activate Membership  
**Actor chính:** Gym Owner  
**Actor phụ:** SMS Service  
**Mức độ ưu tiên:** High  
**Loại:** Primary

**Mô tả tóm tắt:**  
Gym Owner kích hoạt membership sau khi đã nhận đủ phí, hệ thống tạo QR Code và gửi thông báo.

**Luồng sự kiện chính:**
1. Gym Owner chọn membership cần activate từ danh sách chờ
2. Hệ thống hiển thị chi tiết membership và trạng thái thanh toán
3. Gym Owner xác nhận đã nhận đủ phí
4. Hệ thống cập nhật trạng thái membership thành ACTIVE
5. Hệ thống tính toán ngày hết hạn (start_date + duration)
6. Hệ thống tạo QR Code duy nhất cho membership
7. Hệ thống gửi nội dung SMS đến SMS Service
8. SMS Service gửi SMS xác nhận kích hoạt đến khách hàng
9. Hệ thống hiển thị thông báo thành công

**Luồng sự kiện thay thế:**
- 3a. Chưa đủ phí: Hiển thị cảnh báo, yêu cầu hoàn tất thanh toán

**Điều kiện tiên quyết:**
- Membership tồn tại với trạng thái INACTIVE
- Đã hoàn tất thanh toán

**Điều kiện sau:**
- Membership chuyển sang trạng thái ACTIVE
- QR Code được tạo và liên kết với membership
- SMS xác nhận được gửi

---

### 5.3. UC-11: Book PT Package (Customer)

**Use Case ID:** UC-11  
**Tên:** Book PT Package  
**Actor chính:** Customer  
**Actor phụ:** Payment Gateway, SMS Service, PT (nhận notification)  
**Mức độ ưu tiên:** High  
**Loại:** Primary

**Mô tả tóm tắt:**  
Customer chọn và đặt gói tập với PT, thanh toán online, hệ thống tạo booking và gửi yêu cầu đến PT.

**Luồng sự kiện chính:**
1. Customer đăng nhập và xem danh sách PT
2. Customer chọn PT và xem các gói dịch vụ
3. Customer chọn gói phù hợp và nhấn "Book Now"
4. Hệ thống kiểm tra membership còn hiệu lực
5. Hệ thống hiển thị form xác nhận: PT, gói, số buổi, tổng tiền
6. Customer xác nhận và chọn phương thức thanh toán
7. Hệ thống gửi request đến Payment Gateway
8. Payment Gateway xử lý và trả kết quả SUCCESS
9. Hệ thống tạo PTBooking với trạng thái CONFIRMED
10. Hệ thống gửi notification đến PT
11. Hệ thống gửi SMS xác nhận đến Customer
12. Hệ thống hiển thị booking confirmation

**Luồng sự kiện thay thế:**
- 4a. Membership hết hạn: Chuyển đến trang gia hạn
- 8a. Thanh toán thất bại: Hiển thị lỗi, cho phép thử lại
- 8b. Customer hủy thanh toán: Quay về trang chọn gói

**Luồng ngoại lệ:**
- 7a. Timeout kết nối Payment Gateway: Hiển thị lỗi, lưu booking PENDING payment

**Điều kiện tiên quyết:**
- Customer đã đăng nhập
- Có membership ACTIVE
- PT có gói dịch vụ đang mở

**Điều kiện sau:**
- PTBooking được tạo với trạng thái CONFIRMED
- Payment record được tạo và liên kết
- PT nhận được notification
- Customer nhận SMS xác nhận

---

### 5.4. UC-12: Confirm/Reject Booking (PT)

**Use Case ID:** UC-12  
**Tên:** Confirm/Reject Booking  
**Actor chính:** PT  
**Actor phụ:** Customer (nhận notification), SMS Service  
**Mức độ ưu tiên:** High  
**Loại:** Primary

**Mô tả tóm tắt:**  
PT xem yêu cầu booking từ customer và quyết định xác nhận hoặc từ chối.

**Luồng sự kiện chính (Confirm):**
1. PT nhận notification có booking mới
2. PT mở danh sách booking chờ xác nhận
3. PT chọn booking để xem chi tiết
4. PT kiểm tra lịch trống và quyết định
5. PT nhấn "Confirm"
6. Hệ thống cập nhật booking thành CONFIRMED
7. Hệ thống gửi notification đến Customer
8. Hệ thống cho phép PT tạo Training Schedule

**Luồng sự kiện thay thế (Reject):**
- 5b. PT nhấn "Reject"
- 6b. Hệ thống yêu cầu lý do từ chối
- 7b. PT nhập lý do và xác nhận
- 8b. Hệ thống cập nhật booking thành REJECTED
- 9b. Hệ thống hoàn tiền qua Payment Gateway
- 10b. Hệ thống gửi SMS thông báo từ chối đến Customer

**Điều kiện tiên quyết:**
- PT đã đăng nhập và được approve
- Có booking ở trạng thái PENDING

**Điều kiện sau:**
- Booking chuyển sang CONFIRMED hoặc REJECTED
- Customer nhận thông báo kết quả

---

## 6. Wireframe màn hình

### 6.1. Màn hình UC-05: Register Membership
+----------------------------------------------------------+
| GYM MANAGEMENT SYSTEM [Gym Owner] |
+----------------------------------------------------------+
| Dashboard | Membership | PT Management | Reports | Logout|
+----------------------------------------------------------+
| |
| +----------------------------------------------------+ |
| | REGISTER NEW MEMBERSHIP | |
| +----------------------------------------------------+ |
| | | |
| | Customer Information: | |
| | +----------------+ +-----------------------------+ | |
| | | Full Name: | | [] | | |
| | +----------------+ +-----------------------------+ | |
| | | Phone Number: | | [] | | |
| | +----------------+ +-----------------------------+ | |
| | | Email: | | [] | | |
| | +----------------+ +-----------------------------+ | |
| | | ID Card: | | [] | | |
| | +----------------+ +-----------------------------+ | |
| | | |
| | Membership Package: | |
| | +-----------------------------------------------+ | |
| | | ( ) Basic - 1 Month - 500,000 VND | | |
| | | ( ) Standard - 3 Months - 1,200,000 VND | | |
| | | (*) Premium - 6 Months - 2,000,000 VND | | |
| | | ( ) VIP - 12 Months - 3,500,000 VND | | |
| | +-----------------------------------------------+ | |
| | | |
| | Total Amount: [2,000,000 VND] | |
| | | |
| | Payment Method: | |
| | [Cash ▼] [Bank Transfer ▼] [Credit Card ▼] | |
| | | |
| | [ CANCEL ] [ REGISTER & PAY ] | |
| | | |
| +----------------------------------------------------+ |
| |
+----------------------------------------------------------+

### 6.2. Màn hình UC-06: Activate Membership
+----------------------------------------------------------+
| GYM MANAGEMENT SYSTEM [Gym Owner] |
+----------------------------------------------------------+
| Dashboard | Membership | PT Management | Reports | Logout|
+----------------------------------------------------------+
| |
| +----------------------------------------------------+ |
| | ACTIVATE MEMBERSHIP | |
| +----------------------------------------------------+ |
| | | |
| | Pending Memberships: | |
| | +------------------------------------------------+ |
| | | ID | Customer | Package | Amount | Action| |
| | |------|-------------|-----------|--------|-------| |
| | | M001 | Nguyen Van A| Premium | 2.0M |[View] | |
| | | M002 | Tran Thi B | Basic | 500K |[View] | |
| | | M003 | Le Van C | VIP | 3.5M |[View] | |
| | +------------------------------------------------+ |
| | | |
| | Selected Membership Details: | |
| | +------------------------------------------------+ |
| | | Membership ID: M001 | |
| | | Customer: Nguyen Van A | |
| | | Phone: 0901234567 | |
| | | Package: Premium (6 Months) | |
| | | Start Date: [01/12/2024 ▼] | |
| | | End Date: 01/06/2025 (auto-calculated) | |
| | | Payment Status: [✓] Paid | |
| | +------------------------------------------------+ |
| | | |
| | [ BACK ] [ GENERATE QR & ACTIVATE ] | |
| | | |
| +----------------------------------------------------+ |
| |
+----------------------------------------------------------+

### 6.3. Màn hình UC-11: Book PT Package
+----------------------------------------------------------+
| GYM MANAGEMENT SYSTEM [Customer] |
+----------------------------------------------------------+
| Home | My Membership | PT | Schedule | Notifications |
+----------------------------------------------------------+
| |
| +----------------------------------------------------+ |
| | BOOK PERSONAL TRAINER | |
| +----------------------------------------------------+ |
| | | |
| | Step 1: Select PT | |
| | +------------------------------------------------+ |
| | | [Photo] John Smith - Fitness - ★★★★★ - $50/session| |
| | | [Photo] Jane Doe - Yoga - ★★★★☆ - $40/session| |
| | | [Photo] Mike Johnson - Boxing - ★★★★★ - $60/session| |
| | +------------------------------------------------+ |
| | | |
| | Step 2: Select Package | |
| | +------------------------------------------------+ |
| | | ( ) 4 Sessions - $200 (Save $0) | |
| | | (*) 8 Sessions - $360 (Save $40) | |
| | | ( ) 12 Sessions - $480 (Save $120) | |
| | +------------------------------------------------+ |
| | | |
| | Order Summary: | |
| | +------------------------------------------------+ |
| | | PT: Jane Doe | |
| | | Package: 8 Sessions | |
| | | Total: $360 | |
| | | Your Balance: [500 Points] | |
| | +------------------------------------------------+ |
| | | |
| | Payment Method: [Credit Card ▼] [Momo ▼] [VNPay ▼] | |
| | | |
| | [ CANCEL ] [ PAY & CONFIRM BOOKING ] | |
| | | |
| +----------------------------------------------------+ |
| |
+----------------------------------------------------------+

### 6.4. Màn hình UC-12: Confirm/Reject Booking
+----------------------------------------------------------+
| GYM MANAGEMENT SYSTEM [PT] |
+----------------------------------------------------------+
| Dashboard | My Packages | Bookings | Schedule | Profile |
+----------------------------------------------------------+
| |
| +----------------------------------------------------+ |
| | MANAGE BOOKING REQUESTS | |
| +----------------------------------------------------+ |
| | | |
| | Pending Requests: | |
| | +------------------------------------------------+ |
| | | Booking #BK001 | |
| | | From: Nguyen Van A (Member since 2024) | |
| | | Package: 8 Sessions | |
| | | Preferred Time: Morning (6AM-12PM) | |
| | | Message: "I want to focus on weight loss" | |
| | | | |
| | | [ VIEW PROFILE ] | |
| | | | |
| | | [ REJECT ] [ CONFIRM ] | |
| | +------------------------------------------------+ |
| | | |
| | +------------------------------------------------+ |
| | | Booking #BK002 | |
| | | From: Tran Thi B | |
| | | Package: 4 Sessions | |
| | | Preferred Time: Evening (5PM-9PM) | |
| | | | |
| | | [ REJECT ] [ CONFIRM ] | |
| | +------------------------------------------------+ |
| | | |
| +----------------------------------------------------+ |
| |
| Reject Reason (if selected): |
| +----------------------------------------------------+ |
| | [Not available at preferred time ▼] | |
| | [Fully booked this month ▼] | |
| | [Other: _________________________] | |
| +----------------------------------------------------+ |
| |
+----------------------------------------------------------+

---

## 7. Tài liệu tham khảo

1. **GitHub Repository**: https://github.com/RyugaWork/SWR---Gym-Management-System
2. **Course Materials**: SWR302 - Software Requirements, FPT University
3. **IEEE Std 830-1998**: IEEE Recommended Practice for Software Requirements Specifications
4. **UML 2.5 Specification**: Object Management Group

---

## Phụ lục: Phân công công việc nhóm

| Thành viên | MSSV | Phụ trách | Công việc cụ thể |
|------------|------|-----------|------------------|
| [Tên 1] | [MSSV] | Team Lead + SRS | Tổng hợp SRS, UC-05, UC-06, Context Diagram |
| [Tên 2] | [MSSV] | Use Case Analyst | UC-11, UC-12, Use Case Diagram, Activity Diagram |
| [Tên 3] | [MSSV] | State Analyst | UC-08, UC-15, State Machine Diagrams |
| [Tên 4] | [MSSV] | Data Analyst | UC-16, UC-17, ERD, Database Design |
| [Tên 5] | [MSSV] | UI/UX Designer | Wireframes, UC-21, UC-22, UI Review |
