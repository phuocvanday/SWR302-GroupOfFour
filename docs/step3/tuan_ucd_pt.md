# Bước 3 — Anh Tuấn (UCD package PT)

> Issue: #16 · Nhánh: `step3/tuan-ucd-pt`

## Package / UC trong package PT

Package `PT Booking` trong phạm vi Tuấn phụ trách gồm:

- UC-11 — Đặt gói PT (Customer)
- UC-12 — Xác nhận / Từ chối booking PT (Personal Trainer)

Các actor phụ liên quan:

- Payment Gateway: xử lý thanh toán cho UC-11 và hoàn tiền khi booking bị từ chối trong UC-12.
- SMS Service: gửi thông báo booking và kết quả xử lý cho cả UC-11 và UC-12.
- Không tạo UC riêng cho việc gửi thông báo; SMS Service được biểu diễn là actor phụ.

## Các quan hệ include / extend

| Quan hệ | Từ | Tới | Lý do |
|---------|----|-----|-------|
| `<<include>>` | UC-11 Đặt gói PT | UC-Pay Xử lý thanh toán | Thanh toán online là bắt buộc khi đặt gói PT |
| `<<extend>>` | UC-Promo Áp mã khuyến mãi | UC-11 Đặt gói PT | Chỉ xảy ra khi Customer nhập mã khuyến mãi hợp lệ |
| Alternative flow | UC-12 Xác nhận / Từ chối booking PT | Confirm / Reject | Hai nhánh thay thế; không biểu diễn bằng `<<extend>>` |

`UC-Pay Xử lý thanh toán` và `UC-Promo Áp mã khuyến mãi` được vẽ là các UC hỗ trợ với mã chức năng; không tính là UC nghiệp vụ chính.

## PNG đã export

- [x] `03_Images/UCD02.png`

## Ghi chú

- Danh sách UC và actor được đối chiếu với `docs/02_UC_List_Detailed.md`.
- Package này chỉ mô tả phạm vi Bước 3 do Tuấn phụ trách; các UC PT khác nằm trong tài liệu UC tổng của nhóm.
- Khi vẽ bằng Visual Paradigm, nối Customer với UC-11 và UC-Promo; Personal Trainer với UC-12; Payment Gateway với UC-Pay; SMS Service với cả UC-11 và UC-12.
- `UC-Promo` mở rộng UC-11 chỉ khi Customer nhập mã khuyến mãi hợp lệ.
- Extension point nằm trong UC-11 với tên `Apply promotion code`.
- Confirm và Reject trong UC-12 là alternative flow, không phải quan hệ `<<extend>>`.
- File nguồn Visual Paradigm được cập nhật trong `02_Models/GMS.vpp`.
