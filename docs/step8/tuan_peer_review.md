# Bước 8 — Anh Tuấn (Peer review mảng PT)

> Issue: #41 · Nhánh: `step8/tuan-peer`

## Đã review

| Artifact | OK? | Ghi chú sửa |
|----------|-----|-------------|
| UCD PT | Có | Package PT có UC-11/12 và các UC liên quan; `Process Payment` được dùng như supporting use case, `Apply Promo Code` là extension tùy chọn. Confirm/Reject được giữ là alternative flow của UC-12, không dùng `<<extend>>`. Cần bảo đảm bản export chính thức trong `GMS.vpp` khớp với tài liệu UCD. |
| AD-01 | Có | Đã bổ sung `docs/step6/tuan_ad01.md` và `03_Images/AD_BookPT.png`. Sơ đồ có 5 swimlane, validation decision, payment success/fail/timeout, tạo Booking `Pending`, fork notification/dispatch và mapping với UC-11/UC-12. |
| Đặc tả UC-11/12 | Có, cần đồng bộ nhỏ | UC-11 có main flow, alternative flows và exceptions; UC-12 có Confirm main flow, Reject alternative flow, timeout 24 giờ và refund. Cần thống nhất tên/status với ERD: `Booking`/`PTBooking`, `Member`/`Customer`, `Personal_trainer`/`Personal Trainer`, và `Payment.Status = SUCCESS/FAILED/PENDING`. |

## Kết luận

- Phần đặc tả UC và UCD PT đáp ứng nội dung nghiệp vụ chính của miền PT.
- AD-01 đã được bổ sung đầy đủ vào artifact peer review, gồm Markdown và PNG.
- Đã kiểm tra traceability giữa `UC-11`, `UC-12`, `AD-01`, `SMD-02`, ERD và UI `UI_UC11_BookPT.png`/`UI_UC12_PTBooking.png`.
- Kết luận: **Pass**.
