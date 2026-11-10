# Bước 5 — Phước (UI UC-05, UC-06) — DRAFT xem thử

> Issue: [#25](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/25) · Branch: `step-5`  
> Low-fidelity wireframe: bố cục + field + nút + 1 trạng thái lỗi. Không cần màu/logo.

## Màn hình & PNG

| UC | Screen ID | Tên màn hình | File PNG |
|----|-----------|--------------|----------|
| UC-05 | SCR-05 | Register Membership (at Counter) | `03_Images/UI_UC-05_RegisterMembership.png` |
| UC-05 | SCR-05-E | Register Membership — Payment error | `03_Images/UI_UC-05_RegisterMembership_Error.png` |
| UC-06 | SCR-06 | Activate Membership | `03_Images/UI_UC-06_ActivateMembership.png` |
| UC-06 | SCR-06-E | Activate Membership — Unpaid blocked | `03_Images/UI_UC-06_ActivateMembership_Error.png` |

> Bạn có thể vẽ lại bằng Figma cho đẹp hơn; nháp PNG này đủ để hiểu layout.

---

## SCR-05 — Register Membership (map UC-05 Normal Flow)

Callouts trên wireframe: ① mở form · ② nhập Customer · ③ chọn gói · ④ promo (opt) · ⑤ thanh toán · ⑥ Register & Pay

| # | Thành phần | Loại control | Dữ liệu / Nguồn | Bắt buộc | Ràng buộc / Validation | Hành động (bước UC) |
|---|------------|--------------|-----------------|----------|------------------------|---------------------|
| 1 | Full Name | Text box | Customer / nhập tại quầy | Có | Không rỗng; 2–100 ký tự | Bước 3 |
| 2 | Phone Number | Text box | Customer | Có | Định dạng SĐT VN (10 số) | Bước 3–4 |
| 3 | Email | Text box | Customer | Có | Email hợp lệ | Bước 3–4 |
| 4 | Search existing Customer | Button / link | Tra cứu theo Phone/Email | Không | — | Alt 05.2 |
| 5 | Membership Package | Radio list | MembershipPackage (ACTIVE) | Có | Phải chọn 1 gói | Bước 5 |
| 6 | Duration / Price (read-only) | Label | Theo gói đã chọn | — | Hiển thị từ catalog | Bước 6 |
| 7 | Promo Code | Text box | Mã KM (extend) | Không | Nếu nhập: phải còn hạn | Alt 05.1 |
| 8 | Apply Promo | Button | — | — | Enable khi có text promo | Alt 05.1 |
| 9 | Total Amount | Label | Fee sau promo | — | ≥ 0 VND | Bước 6 |
| 10 | Payment Method | Dropdown | Cash / Bank transfer / Card (Gateway) | Có | Bắt buộc trước Pay | Bước 9 |
| 11 | Payment reference note | Text box | Ghi chú cash/transfer | Không* | *Bắt buộc nếu Cash/Transfer | Alt 05.3 |
| 12 | Cancel | Button | — | — | Hủy form | Alt 05.4 |
| 13 | Register & Pay | Button | — | — | Enable khi đủ field bắt buộc | Bước 7–11 |

### Trạng thái lỗi (SCR-05-E)

| Lỗi | Hiện trên UI | Map Exception |
|-----|--------------|---------------|
| Payment Gateway failure / timeout | Banner đỏ: “Payment failed. Membership kept INACTIVE. Retry or cancel.” + nút Retry | 05.0.E1 |
| Invalid / expired promo | Field Promo highlight + “Promo code invalid or expired.” | 05.0.E3 |
| Persistence error | Toast/dialog: “Cannot save membership. Try again later.” | 05.0.E2 |

---

## SCR-06 — Activate Membership (map UC-06 Normal Flow)

Callouts: ① danh sách pending · ② chọn membership · ③ xem chi tiết / paid · ④ Activate · ⑤ QR preview

| # | Thành phần | Loại control | Dữ liệu / Nguồn | Bắt buộc | Ràng buộc / Validation | Hành động (bước UC) |
|---|------------|--------------|-----------------|----------|------------------------|---------------------|
| 1 | Pending memberships table | Table | Membership INACTIVE + paid | — | Chỉ hiện đủ điều kiện activate | Bước 1–2 |
| 2 | Columns: ID, Customer, Package, Amount, Status | Label | Membership + Customer + Package | — | Status = INACTIVE | Bước 2 |
| 3 | Select / View row | Button | Membership ID | Có (chọn 1) | — | Bước 3 |
| 4 | Membership ID | Label (read-only) | Selected membership | — | — | Bước 4 |
| 5 | Customer name / phone | Label | Customer | — | Phone dùng gửi SMS | Bước 4 |
| 6 | Package name + duration | Label | MembershipPackage | — | — | Bước 4 |
| 7 | Payment Status | Badge | Payment record | — | Phải = Paid (BR-02) | Bước 4, 6 |
| 8 | Activation date | Date (default today) | System date | Có | ≤ today (thường = today) | Bước 7 |
| 9 | End date (auto) | Label | activation + DurationMonths | — | BR-03, read-only | Bước 7 |
| 10 | Back | Button | — | — | Quay list / hủy | Alt 06.2 |
| 11 | Generate QR & Activate | Button | — | — | Disable nếu unpaid | Bước 5–12 |
| 12 | QR preview / Print | Image + Button | QR Service result | — | Hiện sau activate thành công | Bước 9, 12 |
| 13 | Resend SMS | Button | SMS Service | Không | Sau khi ACTIVE | Alt 06.3 |

### Trạng thái lỗi (SCR-06-E)

| Lỗi | Hiện trên UI | Map Exception / Alt |
|-----|--------------|---------------------|
| Fee not fully paid | Banner: “Cannot activate: outstanding fee …” + Activate disabled | Alt 06.1 / BR-02 |
| QR Service failure | Dialog: “QR generation failed. Membership rolled back to INACTIVE. Retry.” | 06.0.E1 |
| SMS failure (partial success) | Warning: “Activated + QR OK, but SMS failed.” + Resend SMS | 06.0.E2 |

---

## Nháp layout (text) — để vẽ lại Figma cho giống

### UC-05
```
+----------------------------------------------------------+
| GMS  | Dashboard | Membership | PT | Reports | [Owner]   |
+----------------------------------------------------------+
| REGISTER MEMBERSHIP (at Counter)              SCR-05  ①  |
|----------------------------------------------------------|
| Customer Information                              ②      |
|  Full Name [____________________]                        |
|  Phone     [____________________]  [Search existing]     |
|  Email     [____________________]                        |
|----------------------------------------------------------|
| Membership Package                                ③      |
|  ( ) Basic 1M - 500,000                                  |
|  (•) Premium 6M - 2,000,000                              |
|  ( ) VIP 12M - 3,500,000                                 |
|----------------------------------------------------------|
| Promo Code [________] [Apply]                     ④      |
| Total Amount: 2,000,000 VND                              |
| Payment Method: [Cash ▼]  Ref note [__________]   ⑤      |
|                                                          |
|              [ Cancel ]   [ Register & Pay ]      ⑥      |
+----------------------------------------------------------+
```

### UC-06
```
+----------------------------------------------------------+
| GMS  | Dashboard | Membership | PT | Reports | [Owner]   |
+----------------------------------------------------------+
| ACTIVATE MEMBERSHIP                           SCR-06  ①  |
|----------------------------------------------------------|
| Pending (INACTIVE + Paid)                                |
|  ID   | Customer      | Package  | Amount | Action       |
|  M001 | Nguyen Van A  | Premium  | 2.0M   | [Select] ②  |
|  M002 | Tran Thi B    | Basic    | 500K   | [Select]     |
|----------------------------------------------------------|
| Selected details                                  ③      |
|  Membership ID: M001                                     |
|  Customer: Nguyen Van A | Phone: 0901234567              |
|  Package: Premium (6 Months)                             |
|  Payment Status: [Paid ✓]                                |
|  Activate date: [10/11/2026]  End date: 10/05/2027 (auto)|
|                                                          |
|   [ Back ]     [ Generate QR & Activate ]         ④      |
|   QR preview: [####]  [Print] [Resend SMS]        ⑤      |
+----------------------------------------------------------+
```

---

## Checklist trước khi đóng #25

- [ ] PNG chính thức (hoặc giữ nháp này nếu GV chấp nhận low-fi)
- [ ] Bảng field đủ (file này)
- [ ] ≥1 màn lỗi / banner lỗi trên wireframe
- [ ] Callout bước UC trên ảnh
- [ ] Dán vào SRS §5.1 (khi Word không lock)
