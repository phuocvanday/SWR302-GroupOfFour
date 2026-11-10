# Bước 5 — Thiên (UI UC-08, UC-15)

> Issue: [#27](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/27) · Branch: `step-5`  
> Low-fidelity wireframe: bố cục + field + nút + callouts ①②③ + trạng thái lỗi (Exception/Alternative). Đồng bộ chuẩn trình bày với `phuoc_ui.md`.

## Màn hình & PNG

| UC | Screen ID | Tên màn hình | File PNG |
|----|-----------|--------------|----------|
| UC-08 | SCR-08 | Check-in by QR | `03_Images/UI_UC-08_QRCheckIn.png` |
| UC-08 | SCR-08-E | Check-in by QR — Expired / Invalid QR Error | `03_Images/UI_UC-08_QRCheckIn_Error.png` |
| UC-15 | SCR-15 | Record Training Session | `03_Images/UI_UC-15_RecordSession.png` |
| UC-15 | SCR-15-E | Record Training Session — Validation / No Sessions Error | `03_Images/UI_UC-15_RecordSession_Error.png` |

---

## SCR-08 — Check-in by QR (map UC-08 Normal Flow & Alternative Flows)

Callouts trên wireframe: ① mở màn hình quét QR · ② vùng camera quét mã QR · ③ khu vực nhập mã thủ công (*ManualEntry* — «extend») · ④ nút xác thực Check-in · ⑤ bảng kết quả thông tin hội viên & trạng thái thẻ (`ACTIVE`) · ⑥ thông báo xác nhận lượt vào cửa hợp lệ

| # | Thành phần | Loại control | Dữ liệu / Nguồn | Bắt buộc | Ràng buộc / Validation | Hành động (bước UC) |
|---|------------|--------------|-----------------|----------|------------------------|---------------------|
| 1 | Check-in Mode Selector | Radio / Toggle | `CHECK-IN` (default) / `CHECK-OUT` | Có | Mặc định chọn `CHECK-IN` cho UC-08 | Bước 1 |
| 2 | Facility Operating Hours Badge | Label (read-only) | Cấu hình giờ mở cửa (`05:30 – 22:00 UTC+7`) | — | Phải nằm trong khung giờ mở cửa (`BR-05`) | Bước 7 |
| 3 | QR Camera Scanner Viewport | Camera / Video box | Luồng camera thiết bị quầy/cửa | Có* | *Tự động bắt khung QR 2D; timeout 3s (`DE-03`) | Bước 1–2 |
| 4 | Manual Code Input (`MembershipID` / Phone) | Text box | Nhập tay khi camera không quét được | Không* | *Bắt buộc khi dùng nhánh `ManualEntry` (6–15 ký tự) | Alt 08.1 (`ManualEntry`) |
| 5 | Verify Manual Code | Button | — | — | Bật khi ô Manual Code không rỗng | Alt 08.1 |
| 6 | Membership ID & Customer Name | Label (read-only) | `Membership` + `Customer` (sau khi giải mã QR) | — | Khớp token trả về từ `QR Service` | Bước 4–5 |
| 7 | Package & Expiration Date | Label (read-only) | `MembershipPackage.Name`, `Membership.EndDate` | — | `CurrentDate <= EndDate` (`BR-03`, `BR-05`) | Bước 6 |
| 8 | Membership Status Badge | Badge | `ACTIVE` / `EXPIRED` / `SUSPENDED` / `INACTIVE` | — | Bắt buộc `= ACTIVE` mới cho phép Check-in (`BR-04`) | Bước 6 |
| 9 | Remaining Validity Days | Label (read-only) | `EndDate - CurrentDate` (ngày) | — | Hiển thị số ngày còn lại (≥ 0 ngày) | Bước 9 |
| 10 | Check-in Timestamp | Label (read-only) | Đồng hồ hệ thống (`dd/mm/yyyy HH:mm:ss UTC+7`) | — | Tự động ghi nhận khi tạo `CheckInLog` | Bước 8–9 |
| 11 | Reset / Scan Next | Button | — | — | Làm mới màn hình cho hội viên tiếp theo | Bước 9 |

### Trạng thái lỗi (SCR-08-E)

| Lỗi | Hiện trên UI | Map Exception / Alt |
|-----|--------------|---------------------|
| Membership not ACTIVE (`EXPIRED` / `SUSPENDED` / `INACTIVE`) | Banner đỏ: `"DENIED: Membership M004 is EXPIRED (ended 01/11/2026). QR invalidated (BR-04, BR-05)."` + nút `[Go to Renew (UC-20)]` | Alt 08.2 / BR-04, BR-05 |
| Forged / Invalid QR token | Banner đỏ: `"ERROR: Invalid or unrecognized QR Code. Please retry or use Manual Entry."` | Exception 08.0.E1 |
| Outside opening hours | Banner cảnh báo: `"DENIED: Check-in is only allowed during opening hours (05:30 - 22:00 UTC+7)."` | Alt 08.3 / BR-05 |
| QR Service timeout | Toast / Banner: `"QR Service timeout. Please retry scanning or enter Membership ID manually."` | Exception 08.0.E2 |

---

## SCR-15 — Record Training Session (map UC-15 Normal Flow & Alternative Flows)

Callouts trên wireframe: ① mở danh sách buổi tập đã xếp lịch · ② chọn buổi tập thuộc Booking `Confirmed` / `In Progress` · ③ kiểm tra số buổi còn lại (`Remaining Sessions >= 1`) · ④ chọn trạng thái buổi tập (`Completed` / `No-Show`) & nhập ghi chú · ⑤ nút `Save Session Record`

| # | Thành phần | Loại control | Dữ liệu / Nguồn | Bắt buộc | Ràng buộc / Validation | Hành động (bước UC) |
|---|------------|--------------|-----------------|----------|------------------------|---------------------|
| 1 | Scheduled Sessions List | Table | `TrainingSession` + `PTBooking` + `Customer` | — | Chỉ hiển thị lịch của PT đang đăng nhập (`BR-07`) | Bước 1–2 |
| 2 | Select Session Row | Button (`[Select]`) | `SessionID` | Có (chọn 1) | Chỉ bật với buổi tập chưa ghi nhận (`SCHEDULED`) | Bước 3 |
| 3 | Booking ID & Status | Label / Badge | `PTBooking.BookingID`, `PTBooking.Status` | — | Phải là `Confirmed` hoặc `In Progress` (`BR-10`) | Bước 4 |
| 4 | Customer Name & Package | Label (read-only) | `Customer.FullName`, `PTPackage.Name` | — | — | Bước 4 |
| 5 | Session Balance (`Used / Total / Remaining`) | Label (read-only) | `PTBooking` (`used_sessions`, `remaining_sessions`) | — | `remaining_sessions >= 1` (`BR-10`) | Bước 4, 8 |
| 6 | Session Date & Time | DateTime (read-only / picker) | `TrainingSession.Date`, `Time` | Có | Không được lớn hơn thời điểm hiện tại (`<= now()`) | Bước 5, 7 |
| 7 | Attendance Outcome | Radio list | `Completed` (default) / `Customer No-Show` | Có | Chọn đúng 1 trạng thái | Bước 5 / Alt 15.2 |
| 8 | Workout Metrics (Weight / Duration) | Text box | Cân nặng học viên (kg), thời lượng tập (phút) | Không | Số dương hợp lệ (VD: `30–180` phút) | Bước 5 |
| 9 | Training Summary & PT Notes | Textarea | Nội dung bài tập, mức tạ, nhận xét của PT | Có | Không rỗng; 10–500 ký tự | Bước 5, 7 |
| 10 | Cancel | Button | — | — | Hủy thay đổi, quay về lịch tập | Alt 15.3 |
| 11 | Save Session Record | Button | — | — | Disable nếu `remaining_sessions == 0` hoặc thiếu ghi chú | Bước 6–10 |

### Trạng thái lỗi (SCR-15-E)

| Lỗi | Hiện trên UI | Map Exception / Alt |
|-----|--------------|---------------------|
| Missing required workout notes / Future timestamp | Viền đỏ quanh ô `Training Summary & PT Notes` + Banner: `"ERROR: Training notes are required and session time cannot be in the future."` | Exception 15.0.E3 |
| No remaining sessions (`remaining_sessions == 0`) | Banner đỏ: `"BLOCKED: Booking BK001 has 0 remaining sessions (BR-10). Cannot record additional session."` + nút `Save` bị khóa | Exception 15.0.E1 / BR-10 |
| Duplicate submission (Concurrent update) | Dialog / Banner: `"This training session was already recorded. Refreshing schedule..."` | Exception 15.0.E2 |

---

## Nháp layout (text) — Đồng bộ với file PNG

### UC-08 (`SCR-08`)
```
+--------------------------------------------------------------------+
| GMS  | Home | My Membership | QR Check-in | Schedule  [Customer/ Gate]|
+--------------------------------------------------------------------+
| CHECK-IN BY QR                           Hours: 05:30-22:00  SCR-08 ①|
|--------------------------------------------------------------------|
| QR Scanner (Camera)        ②   | Membership Verification        ⑤  |
| +----------------------------+ |  Membership ID:  M001             |
| |                            | |  Customer:       Nguyen Van A     |
| |      [  [#]  [#]  ]        | |  Package:        Premium (6M)     |
| |      [    QR      ]        | |  Status:         [ ACTIVE ✓ ]     |
| |      [  [#]  [ ]  ]        | |  Valid Until:    10/05/2027       |
| |   Scanning QR payload...   | |  Remaining:      181 days         |
| +----------------------------+ |  Check-in Time:  10/11/2026 18:05 |
|--------------------------------|-----------------------------------|
| Manual Entry (if camera fails) ③| CHECK-IN ALLOWED — Welcome!    ⑥ |
| Code/Phone [M001______] [Verify]④|           [ Scan Next ]         |
+--------------------------------------------------------------------+
```

### UC-15 (`SCR-15`)
```
+--------------------------------------------------------------------+
| GMS  | Dashboard | My Packages | Bookings | Schedule          [PT] |
+--------------------------------------------------------------------+
| RECORD TRAINING SESSION                                   SCR-15 ① |
|--------------------------------------------------------------------|
| Today's Scheduled Sessions (Approved PT — BR-07)                   |
| SessID | Booking | Customer     | Time        | Rem. | Action      |
| S-104  | BK001   | Nguyen Van A | 10/11 18:00 | 3/8  | [Select] ②  |
| S-105  | BK004   | Tran Thi B   | 10/11 19:30 | 7/12 | [Select]    |
|--------------------------------------------------------------------|
| Session Recording Form — S-104 (Booking BK001: IN PROGRESS)     ③  |
| Customer: Nguyen Van A | Package: 8 Sessions | Remaining: 3 -> 2   |
| Session Date/Time: [10/11/2026 18:00]   Duration (min): [60]       |
| Outcome: (•) Completed    ( ) Customer No-Show (BO-03)          ④  |
| Training Summary & PT Notes (*required):                           |
| [ Squat 4x10 (60kg), Bench press 4x8, Core 15m. Good form.       ] |
|                                                                    |
|                           [ Cancel ]    [ Save Session Record ] ⑤  |
+--------------------------------------------------------------------+
```

---

## Checklist trước khi đóng #27

- [x] File PNG trạng thái chuẩn & trạng thái lỗi cho `UC-08` và `UC-15` trong `03_Images/`
- [x] Bảng mô tả đầy đủ các field, kiểu control, nguồn dữ liệu, validation và bước UC
- [x] Có ≥ 1 trạng thái lỗi / exception được thể hiện trực tiếp trên wireframe (`SCR-08-E`, `SCR-15-E`)
- [x] Có đánh số Callout ①②③④⑤⑥ khớp với các bước trong `UC-08.md` và `UC-15.md`
