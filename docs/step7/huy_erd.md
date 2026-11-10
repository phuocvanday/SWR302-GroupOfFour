# Bước 7 — Data Dictionary & Conceptual ERD

> Issue: #35 · Nhánh: `step7/erd-datadict`

## 1. Sơ đồ Thực thể Mối quan hệ (Conceptual ERD)

- **File sơ đồ PNG**: `03_Images/ERD_Conceptual.png`
- **Số lượng thực thể (Entities)**: 11 thực thể cốt lõi.
- **Tóm tắt mối quan hệ & Cardinality**:
  - `Role` (1) ── (N) `Account`
  - `Account` (1) ── (1) `Gym_Owner` / `Member` / `Personal_trainer`
  - `Member` (1) ── (N) `Customer_Membership`
  - `Membership_Package` (1) ── (N) `Customer_Membership`
  - `Member` (1) ── (N) `Booking`
  - `Personal_trainer` (1) ── (N) `Booking`
  - `Member` (1) ── (N) `Check_In`
  - `Member` (1) ── (N) `Payment`
  - `Equipment_inventory` (1) ── (N) `Maintenance_Log`
  - `Gym_Owner` (1) ── (N) `Maintenance_Log`

---

## 2. Từ điển Dữ liệu (Data Dictionary)

### 2.1. Bảng `Account`
Mô tả: Lưu trữ thông tin tài khoản đăng nhập và phân quyền hệ thống.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `accountID` | `INT` | PK | No | Mã định danh tài khoản |
| `UserName` | `VARCHAR(50)` | - | No | Tên đăng nhập hệ thống |
| `Password_Hash` | `VARCHAR(255)`| - | No | Mật khẩu đã được mã hóa (Hash) |
| `Status` | `VARCHAR(20)` | - | No | Trạng thái tài khoản (ACTIVE, PENDING, BLOCKED) |
| `RoleID` | `INT` | FK | No | Liên kết đến bảng `Role` |
| `Member_ID` | `INT` | FK | Yes | Liên kết hồ sơ Member (nếu là Member) |

### 2.2. Bảng `Role`
Mô tả: Định nghĩa các vai trò trong hệ thống (Gym Owner, Member, PT).

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `RoleID` | `INT` | PK | No | Mã vai trò |
| `RoleName` | `VARCHAR(50)` | - | No | Tên vai trò (Admin, Owner, PT, Member) |
| `Description` | `VARCHAR(255)`| - | Yes | Mô tả quyền hạn của vai trò |

### 2.3. Bảng `Gym_Owner`
Mô tả: Thông tin chi tiết chủ/quản lý phòng gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Owner_ID` | `INT` | PK | No | Mã quản lý / chủ phòng gym |
| `FullName` | `VARCHAR(100)`| - | No | Họ và tên chủ phòng gym |
| `Authority_Level` | `VARCHAR(50)` | - | No | Cấp độ thẩm quyền (Owner, SuperAdmin) |
| `Contact_info` | `VARCHAR(100)`| - | Yes | Thông tin liên lạc / Email / Số điện thoại |
| `Account_accountID`| `INT` | FK | No | Liên kết tài khoản đăng nhập `Account` |

### 2.4. Bảng `Personal_trainer`
Mô tả: Thông tin huấn luyện viên cá nhân (PT).

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PT_ID` | `INT` | PK | No | Mã huấn luyện viên |
| `FullName` | `VARCHAR(100)`| - | No | Họ và tên PT |
| `Specialty` | `VARCHAR(100)`| - | No | Chuyên môn (Gym, Yoga, Kickboxing...) |
| `Experience_years` | `INT` | - | No | Số năm kinh nghiệm |
| `Gym_OwnerAccount_ID`| `INT` | FK | Yes | Mã quản lý duyệt hồ sơ |
| `Account_accountID` | `INT` | FK | No | Liên kết tài khoản đăng nhập `Account` |

### 2.5. Bảng `Member`
Mô tả: Hồ sơ hội viên tập luyện tại phòng gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Member_ID` | `INT` | PK | No | Mã định danh hội viên |
| `FullName` | `VARCHAR(100)`| - | No | Họ và tên hội viên |
| `Phone` | `VARCHAR(15)` | - | No | Số điện thoại liên lạc |
| `Mail` | `VARCHAR(100)`| - | No | Địa chỉ email |

### 2.6. Bảng `Membership_Package`
Mô tả: Danh mục gói tập do phòng gym cung cấp.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Package_ID` | `INT` | PK | No | Mã gói tập |
| `PackageName` | `VARCHAR(100)`| - | No | Tên gói hội viên (Basic, VIP, Premium...) |
| `Price` | `DECIMAL(10,2)`| - | No | Giá tiền của gói (VND) |
| `Durations_Days` | `INT` | - | No | Thời hạn sử dụng (tính theo ngày) |

### 2.7. Bảng `Customer_Membership`
Mô tả: Gói hội viên mà khách hàng đã mua/đăng ký sử dụng.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `EnrollmentID` | `INT` | PK | No | Mã đăng ký gói |
| `StartDate` | `DATE` | - | No | Ngày bắt đầu kích hoạt gói |
| `ExpireDate` | `DATE` | - | No | Ngày hết hạn gói tập |
| `Status` | `VARCHAR(20)` | - | No | Trạng thái gói (ACTIVE, EXPIRED, CANCELLED) |
| `Membership_PackagePackage_ID` | `INT` | FK | No | Mã gói tập đăng ký (`Membership_Package`) |
| `MemberMember_ID` | `INT` | FK | No | Mã hội viên sở hữu (`Member`) |

### 2.8. Bảng `Booking`
Mô tả: Lịch đặt buổi tập cá nhân giữa Hội viên và PT.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Booking_ID` | `INT` | PK | No | Mã lượt đặt lịch |
| `DateTime` | `DATETIME` | - | No | Ngày giờ diễn ra buổi tập |
| `Status` | `VARCHAR(20)` | - | No | Trạng thái (PENDING, CONFIRMED, COMPLETED, CANCELLED) |
| `Personal_trainerPT_ID` | `INT` | FK | No | Mã PT đảm nhận (`Personal_trainer`) |
| `MemberMember_ID` | `INT` | FK | No | Mã hội viên đặt lịch (`Member`) |

### 2.9. Bảng `Payment`
Mô tả: Nhật ký giao dịch và thanh toán hóa đơn.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PaymentID` | `INT` | PK | No | Mã giao dịch / Hóa đơn |
| `Amount` | `DECIMAL(10,2)`| - | No | Số tiền thanh toán (VND) |
| `Method` | `VARCHAR(30)` | - | No | Phương thức thanh toán (Cash, QR, Banking) |
| `Datetime` | `DATETIME` | - | No | Thời gian thực hiện giao dịch |
| `Status` | `VARCHAR(20)` | - | No | Trạng thái giao dịch (SUCCESS, FAILED, PENDING) |
| `MemberMember_ID` | `INT` | FK | No | Mã hội viên thanh toán (`Member`) |

### 2.10. Bảng `Check_In`
Mô tả: Nhật ký ra vào phòng tập của hội viên.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CheckIN_ID` | `INT` | PK | No | Mã lượt điểm danh |
| `DateTime` | `DATETIME` | - | No | Thời điểm quẹt thẻ / QR check-in |
| `Method` | `VARCHAR(30)` | - | No | Phương thức check-in (QR Code, Fingerprint, RFID Card) |
| `MemberMember_ID` | `INT` | FK | No | Mã hội viên check-in (`Member`) |

### 2.11. Bảng `Equipment_inventory`
Mô tả: Quản lý danh mục thiết bị, máy móc trong phòng gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Equipment_ID` | `INT` | PK | No | Mã định danh thiết bị |
| `Equipment_Name` | `VARCHAR(100)`| - | No | Tên thiết bị (Máy chạy bộ, Tạ đơn...) |
| `STatus` | `VARCHAR(30)` | - | No | Tình trạng máy (OPERATIONAL, BROKEN, UNDER_MAINTENANCE) |
| `PurchaseDate` | `DATE` | - | Yes | Ngày nhập mua thiết bị |

### 2.12. Bảng `Maintenance_Log`
Mô tả: Lịch sử bảo trì và sửa chữa trang thiết bị phòng gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Maintenance ID` | `INT` | PK | No | Mã lượt bảo trì |
| `DateTime` | `DATETIME` | - | No | Ngày giờ tiến hành bảo trì/sửa chữa |
| `Description` | `VARCHAR(255)`| - | Yes | Chi tiết nội dung công việc bảo trì |
| `Cost` | `DECIMAL(10,2)`| - | Yes | Chi phí bảo trì/thay linh kiện (VND) |
| `Status` | `VARCHAR(20)` | - | No | Trạng thái công việc (COMPLETED, IN_PROGRESS) |
| `Gym_OwnerOwner_ID` | `INT` | FK | No | Người phê duyệt/quản lý lượt bảo trì |
| `Equipment_inventoryEquipment_ID` | `INT` | FK | No | Mã thiết bị được bảo trì |