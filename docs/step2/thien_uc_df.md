# Bước 2 — Thiên (DF + UC Membership / QR)

> **Phạm vi phụ trách:** Luồng dữ liệu (Data Flows) trên Context Diagram `CD-01` và danh sách Use Case thuộc mảng **Membership & QR Check-in/Check-out**.
> **Quy tắc tuân thủ (theo Hướng dẫn D.1 & D.2):**
> - Tên Data Flow bắt buộc là **danh từ / cụm danh từ** (không dùng động từ), đi giữa External Entity và tiến trình trung tâm `0 – Gym Management System (GMS)`.
> - Tên Use Case bắt buộc theo cấu trúc **Động từ + Danh từ** tiếng Việt, mang lại giá trị nghiệp vụ hoàn chỉnh.

---

## 1. Data flows (Membership / QR)

Bảng dưới đây liệt kê các luồng dữ liệu giữa các tác nhân ngoài (`Customer`, `Gym Owner`, `QR Service`, `Payment Gateway`, `SMS Service`, `Time / Scheduler`) và hệ thống trung tâm **`GMS`** phục vụ mảng Membership & QR:

| ID | Tên luồng dữ liệu (Nhãn mũi tên trên CD-01) | From | To | Data (Nội dung / Cấu trúc dữ liệu tóm tắt) | UC liên quan |
|----|---------------------------------------------|------|----|--------------------------------------------|--------------|
| **DF-05** | Yêu cầu đăng ký membership | Gym Owner | GMS | `CustomerID` (hoặc thông tin khách mới: Họ tên, SĐT, Email, CCCD), `PackageID`, `StartDate` dự kiến, phương thức thanh toán | UC-05, UC-20 |
| **DF-06** | Hồ sơ & thông tin gói membership | GMS | Gym Owner / Customer | Danh mục gói tập (`PackageID`, tên gói, thời hạn, đơn giá VND) và chi tiết hồ sơ thẻ (`MembershipID`, trạng thái, `StartDate`, `EndDate`, tổng phí) | UC-04, UC-05, UC-06, UC-20, UC-23 |
| **DF-07** | Yêu cầu thanh toán phí gói tập | GMS | Payment Gateway | `TransactionID`, `MembershipID`, số tiền (VND), nội dung thanh toán đăng ký/gia hạn gói tập, `ReturnURL` | UC-05, UC-20 |
| **DF-08** | Kết quả giao dịch thanh toán | Payment Gateway | GMS | `TransactionID`, mã tham chiếu cổng (`GatewayRef`), trạng thái (`SUCCESS` / `FAILED`), thời điểm giao dịch (`PaidAt`) | UC-05, UC-06, UC-20 |
| **DF-09** | Yêu cầu kích hoạt membership | Gym Owner | GMS | `MembershipID`, xác nhận đã thu đủ 100% phí gói tập, ngày bắt đầu kích hoạt (`ActivationDate`) | UC-06 |
| **DF-10** | Yêu cầu sinh / xác thực mã QR | GMS | QR Service | Khi kích hoạt: `MembershipID` + `CustomerID` + `EndDate` để sinh token; Khi quét tại cửa: chuỗi `QRPayload` + thời điểm quét | UC-06, UC-08, UC-09 |
| **DF-11** | Kết quả sinh / xác thực mã QR | QR Service | GMS | Khi kích hoạt: chuỗi token/ảnh `QRCode`; Khi quét tại cửa: trạng thái xác thực (`VALID` / `INVALID`) + `MembershipID` giải mã được | UC-06, UC-07, UC-08, UC-09 |
| **DF-12** | Mã QR membership cá nhân | GMS | Customer | Hình ảnh mã QR 2D + mã định danh thẻ hiển thị trên giao diện hội viên kèm trạng thái `ACTIVE` và ngày hết hạn | UC-07 |
| **DF-13** | Thông tin quét QR check-in / check-out | Customer | GMS | Chuỗi mã QR hội viên (hoặc mã thẻ nhập tay khi camera lỗi), loại lượt (`CHECK_IN` / `CHECK_OUT`), thời điểm quét tại quầy/cửa | UC-08, UC-09 |
| **DF-14** | Kết quả xác nhận check-in / check-out | GMS | Customer | Trạng thái cho phép vào/ra (`ALLOWED` / `DENIED`), thông tin hội viên, số ngày còn hạn hoặc lý do từ chối (thẻ hết hạn, ngoài giờ mở cửa) | UC-08, UC-09 |
| **DF-18** | Nội dung SMS thông báo membership | GMS | SMS Service | Số điện thoại `Customer`, nội dung tin nhắn xác nhận kích hoạt thẻ thành công (`UC-06`), gia hạn (`UC-20`) hoặc cảnh báo thẻ hết hạn (`UC-27`) | UC-06, UC-20, UC-27 |
| **DF-19** | Trạng thái gửi SMS | SMS Service | GMS | `MessageID`, trạng thái chuyển phát (`DELIVERED` / `FAILED`), mã lỗi nhà mạng (nếu có) | UC-06, UC-20, UC-27 |
| **DF-23** | Sự kiện thời gian kiểm tra hạn thẻ | Time / Scheduler | GMS | Tín hiệu đồng hồ hệ thống định kỳ hằng ngày (`00:05 UTC+7`) kích hoạt tiến trình rà soát các thẻ có `EndDate < CurrentDate` | UC-27 |

> **Gợi ý cho Phước khi vẽ `CD-01`:** Nếu cần rút gọn số mũi tên trên biểu đồ để không bị rối mắt, có thể gộp:
> - `DF-05` + `DF-09` → **Yêu cầu đăng ký & kích hoạt membership** (`Gym Owner` → `GMS`)
> - `DF-06` + `DF-12` → **Hồ sơ & mã QR membership** (`GMS` → `Customer / Gym Owner`)
> - `DF-13` & `DF-14` → Giữ nguyên 2 chiều giữa `Customer` ↔ `GMS` cho sự kiện và kết quả Check-in/Check-out.

---

## 2. Use cases (Membership / QR)

Danh sách gồm **9 Use Case nghiệp vụ chính** thuộc package `Membership` (đóng góp vào chỉ tiêu ≥ 20 UC toàn hệ thống) và **3 Use Case phụ trợ (`<<include>>` / `<<extend>>`)** phục vụ vẽ Use Case Diagram ở Bước 3:

### 2.1. Các Use Case nghiệp vụ chính (Package: Membership)

| UC-ID | Tên Use Case (Động từ + Danh từ) | Actor chính (Primary) | Actor phụ (Secondary) | Ưu tiên | Mô tả ngắn (Mục tiêu nghiệp vụ) | BR liên quan |
|-------|----------------------------------|-----------------------|-----------------------|---------|---------------------------------|--------------|
| **UC-04** | Xem gói Membership | Customer | — | Medium | Hội viên tra cứu danh sách các gói tập đang mở bán (thời hạn 1, 3, 6, 12 tháng, mức giá VND, quyền lợi đi kèm) trước khi đăng ký tại quầy. | — |
| **UC-05** | Đăng ký Membership tại quầy | Gym Owner | Payment Gateway *(tùy chọn)* | High | Chủ phòng gym nhập/chọn hồ sơ Customer tại quầy, chọn gói Membership, ghi nhận thanh toán (tiền mặt hoặc cổng thanh toán) và tạo bản ghi thẻ ở trạng thái `INACTIVE`. | BR-01, BR-02 |
| **UC-06** | Kích hoạt Membership | Gym Owner | QR Service, SMS Service | High | Sau khi xác nhận thu đủ 100% phí gói, Gym Owner kích hoạt thẻ sang trạng thái `ACTIVE`, hệ thống tự động tính `EndDate`, sinh mã QR duy nhất và gửi SMS thông báo cho Customer. | BR-01, BR-02, BR-03, BR-04 |
| **UC-07** | Xem mã QR Membership | Customer | — | High | Hội viên đã đăng nhập mở ứng dụng web để hiển thị mã QR cá nhân đang `ACTIVE` cùng thông tin gói tập và số ngày còn hiệu lực để xuất trình tại cửa. | BR-04 |
| **UC-08** | Check-in bằng QR | Customer | QR Service | High | Hội viên quét mã QR tại thiết bị quầy/cửa khi đến tập; hệ thống xác thực mã QR, kiểm tra trạng thái thẻ `ACTIVE` và giờ mở cửa để ghi nhận lượt vào (`CheckInLog`). | BR-04, BR-05 |
| **UC-09** | Check-out bằng QR | Customer | QR Service | High | Hội viên quét mã QR khi rời phòng tập; hệ thống xác thực mã QR và cập nhật thời điểm kết thúc buổi tập (`CheckOutTime`) vào bản ghi `CheckInLog` trong ngày. | BR-04, BR-05 |
| **UC-20** | Gia hạn Membership | Gym Owner / Customer | Payment Gateway, SMS Service | High | Gia hạn gói tập cho thẻ sắp hết hạn hoặc đã hết hạn (`EXPIRED`); sau khi thanh toán thành công, hệ thống cộng dồn/cập nhật `EndDate`, khôi phục trạng thái `ACTIVE` và kích hoạt lại mã QR. | BR-02, BR-03, BR-04 |
| **UC-23** | Quản lý gói Membership | Gym Owner | — | High | Chủ phòng gym tạo mới, cập nhật giá/mô tả hoặc ngừng kinh doanh (deactivate) các gói tập trong danh mục sản phẩm của phòng gym. | — |
| **UC-27** | Tự hết hạn Membership | Time / Scheduler | SMS Service | High | Tiến trình tự động chạy lúc `00:05 UTC+7` hằng ngày tìm các thẻ `ACTIVE` có `EndDate < CurrentDate`, chuyển trạng thái sang `EXPIRED`, khóa hiệu lực mã QR và gửi SMS thông báo. | BR-04, BR-11 |

### 2.2. Các Use Case thành phần (`<<include>>` / `<<extend>>`) phục vụ Bước 3

| Mã phụ | Tên Use Case thành phần | Quan hệ | Gắn với UC gốc | Lý do / Điều kiện kích hoạt |
|--------|-------------------------|---------|----------------|-----------------------------|
| **UC-Sub-01** | Sinh mã QR định danh | `<<include>>` | `UC-06` (Kích hoạt Membership) | Bắt buộc thực hiện mỗi khi kích hoạt thẻ thành công để đảm bảo quy tắc mỗi thẻ `ACTIVE` có 1 mã QR duy nhất (`BR-04`). |
| **UC-Sub-02** | Xác thực mã QR | `<<include>>` | `UC-08` (Check-in), `UC-09` (Check-out) | Hành vi kiểm tra chữ ký/token mã QR và trạng thái thẻ được dùng chung bắt buộc cho cả lượt vào và lượt ra. |
| **UC-Ext-01** | Nhập mã thẻ thủ công | `<<extend>>` | `UC-08` (Check-in bằng QR) | Kích hoạt tại *Extension Point: Camera Scan Failure* khi thiết bị camera quét mờ/lỗi hoặc màn hình điện thoại khách bị hỏng (`DE-03`). |
| **UC-Ext-02** | Áp dụng mã khuyến mãi | `<<extend>>` | `UC-05` (Đăng ký Membership tại quầy) | Tùy chọn kích hoạt tại bước tính tổng tiền khi khách hàng có voucher/mã giảm giá hợp lệ trong đợt khuyến mãi. |

---

## 3. Ghi chú kiểm tra nhất quán (D.8)

1. **Khớp Actor giữa Context Diagram và Use Case list:**
   - Primary Actors: `Customer`, `Gym Owner`, `Time / Scheduler` (cho tác vụ định kỳ `UC-27`).
   - Secondary Actors: `QR Service`, `Payment Gateway`, `SMS Service`.
2. **Độ phủ Data Flow ↔ Use Case:** Toàn bộ 13 luồng dữ liệu (`DF-05` → `DF-14`, `DF-18`, `DF-19`, `DF-23`) đều ánh xạ tới ít nhất 1 Use Case trong bảng 2.1, không có luồng dữ liệu mồ côi.
3. **Đặc tả chi tiết ở Bước 4:** Trong mảng này, Thiên sẽ đặc tả fully dressed cho **`UC-08` (Check-in bằng QR)** (kèm `UC-15` ở mảng buổi tập), còn Phước sẽ đặc tả **`UC-05`** và **`UC-06`**.
