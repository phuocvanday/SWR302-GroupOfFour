# Bước 7 — Anh Tuấn (ERD Booking–PT–Session + review SMD-02)

> Issue: #36 · Nhánh: `step7/tuan-erd-review`

## Entity / quan hệ đối chiếu với ERD hiện tại

ERD hiện tại của Huy đang dùng các tên entity `Member`, `Personal_trainer`,
`Booking` và `Payment`. Trong review miền PT, quy ước:

- `Member` tương ứng với `Customer` trong UC-11/UC-12.
- `Personal_trainer` tương ứng với `Personal Trainer`.
- `Booking` tương ứng với `PTBooking`.

Các quan hệ đã có hoặc cần bổ sung được đối chiếu như sau:

| Entity | Quan hệ chính | Cardinality | Ghi chú |
|--------|---------------|-------------|---------|
| `Member` | sở hữu các `Booking` | `Member 1 — 0..* Booking` | **Đã có trong ERD** qua `Booking.MemberMember_ID`; dùng như Customer trong miền PT. |
| `Personal_trainer` | nhận các `Booking` | `Personal_trainer 1 — 0..* Booking` | **Đã có trong ERD** qua `Booking.Personal_trainerPT_ID`; chỉ PT `Approved` mới xử lý booking. |
| `PTPackage` | được dùng trong các `Booking` | `PTPackage 1 — 0..* Booking` | **Chưa thấy trong ERD hiện tại**; cần bổ sung hoặc liên kết tới bảng package tương ứng. |
| `Booking` | thuộc Member, PT và PT package | `Booking * — 1` với các entity liên quan | **Đã có một phần**; cần bổ sung `Package_ID`, lịch mong muốn, tổng tiền và rejection reason nếu dùng cho UC-11/UC-12. |
| `Payment` | thanh toán cho một `Booking` | `Booking 1 — 1 Payment` | Bảng Payment đã có, nhưng cần thêm `Booking_ID` để liên kết trực tiếp với Booking. |
| `TrainingSession` | thuộc một `Booking` | `Booking 1 — 0..* TrainingSession` | **Chưa thấy trong ERD hiện tại**; cần bổ sung để hỗ trợ UC-15. |
| `Notification` | thông báo trạng thái booking | `Booking 1 — 0..* Notification` | **Chưa thấy trong ERD hiện tại**; chỉ bổ sung nếu ERD tổng thể quản lý notification riêng. |

### Thuộc tính hiện có và thuộc tính cần bổ sung

- `Booking` hiện có: `Booking_ID`, `Datetime`, `Status`, `Personal_trainerPT_ID`, `MemberMember_ID`.
- `Booking` nên bổ sung: `Package_ID`, `PreferredDateTime`, `TotalAmount`, `CreatedAt`, `RejectionReason`.
- `Payment` hiện có: `PaymentID`, `Amount`, `Method`, `Datetime`, `Status`, `MemberMember_ID`.
- `Payment` nên bổ sung: `Booking_ID`, `GatewayReference`, `PaidAt`.
- `TrainingSession` cần bổ sung nếu chưa có entity tương ứng: `SessionID`, `Booking_ID`, `SessionDateTime`, `Status`, `Notes`.
- `PTPackage` cần bổ sung hoặc ánh xạ tới entity package đã có: `PackageID`, `PT_ID`, `Name`, `TotalSessions`, `ValidityPeriod`, `Price`.

### Giá trị trạng thái cần thống nhất

`PTBooking.Status` nên dùng:

```text
PENDING → CONFIRMED → IN_PROGRESS → COMPLETED
       ↘ REJECTED
       ↘ CANCELLED
```

`Payment.Status` cần phân biệt tối thiểu:

```text
SUCCESS, FAILED, PENDING
```

Timeout hoặc không nhận được phản hồi rõ ràng từ Payment Gateway không nên bị ghi thành `SUCCESS`; nên giữ payment ở `PENDING` để reconciliation.

## Review SMD-02

- [x] Đồng ý với mô hình trạng thái và các transition chính trong SMD-02.
- [x] `Pending → Confirmed` phản ánh PT chấp nhận booking trong UC-12.
- [x] `Pending → Rejected` yêu cầu rejection reason và khởi tạo refund khi payment đã thành công.
- [x] `Pending → Cancelled` sau 24 giờ không có phản hồi, phù hợp BR-08.
- [x] `Confirmed → In Progress → Completed` phù hợp vòng đời Training Session và UC-15.
- [x] Các trạng thái kết thúc `Rejected`/`Cancelled` có bước refund settlement hoặc đóng lifecycle.
- [ ] Cần đồng bộ SMD với ERD: tên entity hiện tại là `Booking`, `Member`, `Personal_trainer`, `Payment`.
- [ ] Cần kiểm tra trong bản ERD cuối: field, enum status và cardinality phải khớp với data dictionary.

### Nhận xét cần xử lý trước khi chốt

1. Giữ các khóa ngoại hiện có `Booking.MemberMember_ID` và `Booking.Personal_trainerPT_ID`; bổ sung khóa ngoại đến package khi entity package được xác định.
2. `TrainingSession` phải tham chiếu `Booking`, không liên kết trực tiếp chỉ với package, để kiểm soát số buổi còn lại theo từng booking.
3. `Payment` nên có `Booking_ID`, `GatewayReference` và trạng thái `PENDING` để xử lý timeout/reconciliation.
4. Khi tài liệu dùng `PTBooking`, cần ghi chú đây là entity `Booking` trong ERD hiện tại; không tạo thêm bảng trùng tên.

## Ghi chú

- Review này đối chiếu với `docs/step4/UC-11.md`, `docs/step4/UC-12.md`, UC-15 và SMD-02 trong `docs/step7/thien_smd.md`.
- Review không thay thế ERD của Huy; các entity/field ghi là “cần bổ sung” phải được thống nhất với data dictionary trước khi cập nhật ERD cuối.
