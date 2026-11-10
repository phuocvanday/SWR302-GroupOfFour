# Bước 2 — Anh Tuấn (DF + UC domain PT)

> Issue: #11 · Nhánh: `step2/tuan-uc-df`

## Data flows (domain PT)

| ID | From | To | Data |
|----|------|----|------|
| DF-15 | Customer | GMS | PT ID, package ID, thời gian mong muốn, ghi chú |
| DF-16 | GMS | Personal Trainer | Mã booking, Customer, package, thời gian, trạng thái Pending |
| DF-17 | Personal Trainer | GMS | Confirm/Reject, lý do từ chối, thời điểm phản hồi |
| DF-18 | GMS | SMS Service | Số điện thoại, nội dung thông báo booking và trạng thái |
| DF-19 | GMS | Customer | Mã booking, trạng thái, lịch tập, kết quả thanh toán/hoàn tiền |

## Use cases (domain PT)

| UC-ID | Tên | Actor chính | Mô tả ngắn |
|-------|-----|-------------|------------|
| UC-11 | Đặt gói PT | Customer | Chọn package, thanh toán và tạo booking Pending |
| UC-12 | Xác nhận / Từ chối booking PT | Personal Trainer | Xử lý booking Pending trong 24 giờ |
| UC-13 | Tạo lịch tập | Personal Trainer | Tạo các buổi tập cho booking Confirmed |
| UC-24 | Hủy booking PT | Customer | Hủy booking theo chính sách và yêu cầu hoàn tiền |

## Ghi chú

- Các ID DF đối chiếu với `docs/02_Context_Diagram_DataFlows.md`.
- UC-11 có Payment Gateway là actor phụ; UC-12 có SMS Service và Payment Gateway là actor phụ.
- Confirm/Reject là hai alternative flow của UC-12, không phải hai quan hệ `extend`.
