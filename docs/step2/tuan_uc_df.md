# Bước 2 — Anh Tuấn (DF + UC domain PT)

> Issue: #11 · Nhánh: `step2/tuan-uc-df`

## Data flows (domain PT)

| ID | From | To | Data |
|----|------|----|------|
| DF-15 | Customer | GMS | PT, gói PT, lịch mong muốn, ghi chú |
| DF-16 | GMS | Personal Trainer | Chi tiết booking Pending |
| DF-17 | Personal Trainer | GMS | Confirm / Reject + lý do nếu từ chối |
| DF-18 | GMS | SMS Service | SDT + nội dung SMS |
| DF-19 | SMS Service | GMS | Delivered / Failed |

## Use cases (domain PT)

| UC-ID | Tên | Actor chính | Mô tả ngắn |
|-------|-----|-------------|------------|
| UC-11 | Đặt gói PT | Customer | Tạo booking Pending và thanh toán |
| UC-12 | Xác nhận / Từ chối booking PT | Personal Trainer | PT phản hồi booking trong 24 giờ |

## Ghi chú

- DF-15 đến DF-19 được đối chiếu với `docs/02_Context_Diagram_DataFlows.md`.
- UC-11 có Payment Gateway, SMS Service và Personal Trainer là secondary actor.
- UC-12 có SMS Service và Payment Gateway là secondary actor.
- DF-07 và DF-08 là các data flow thanh toán dùng chung; UC-11 sử dụng hai flow này.
- Confirm và Reject là hai alternative flow trong UC-12, không phải hai use case `<<extend>>`.
