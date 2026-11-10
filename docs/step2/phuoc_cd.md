# Bước 2 — Phước (Leader) · CD-01 Context Diagram

> Issue: **#10** · Nhánh: `step-2`  
> Chỉ phần Leader. UC/DF chi tiết theo domain: Tuấn #11 · Thiên #12 · Huy #13.  
> Checklist nhóm **#14** → để sau khi cả nhóm xong.

## Mục tiêu

- Context Diagram đúng ký pháp: **1 process** giữa, **≥5 external entity**, **≥12 data flow** (tên = danh từ).
- Lưu Visual Paradigm: `02_Models/GMS.vpp` (**bắt buộc** — không thay bằng tool khác khi nộp).
- Export: `03_Images/CD_ContextDiagram.png` (≥150 dpi).
- Chèn SRS **§2.1** + bảng mô tả data flow.

## External entities (7)

| # | Entity | Loại |
|---|--------|------|
| 1 | Customer | Người |
| 2 | Personal Trainer | Người |
| 3 | Gym Owner | Người |
| 4 | Payment Gateway | Hệ thống ngoài |
| 5 | SMS Service | Hệ thống ngoài |
| 6 | QR Service | Hệ thống ngoài |
| 7 | Time / Scheduler | Time |

Process giữa: **`0 – Gym Management System (GMS)`**

## Data flow vẽ trên CD-01 (≥12 — dùng bản gọn 14 mũi tên)

| # | Data flow (nhãn mũi tên) | Từ | Đến |
|---|--------------------------|----|-----|
| 1 | Thông tin đăng ký tài khoản | Customer | GMS |
| 2 | Thông tin đăng nhập / phiên | Customer / PT / Owner | GMS *(và chiều ngược phiên)* |
| 3 | Yêu cầu đăng ký & kích hoạt membership | Gym Owner | GMS |
| 4 | Hồ sơ / mã QR membership | GMS | Customer / Gym Owner |
| 5 | Sự kiện & xác nhận check-in/out | Customer ↔ GMS | |
| 6 | Yêu cầu thanh toán | GMS | Payment Gateway |
| 7 | Kết quả thanh toán | Payment Gateway | GMS |
| 8 | Yêu cầu đặt gói PT & phản hồi booking | Customer / PT ↔ GMS | |
| 9 | Nội dung SMS | GMS | SMS Service |
| 10 | Yêu cầu / kết quả QR | GMS ↔ QR Service | |
| 11 | Quyết định duyệt PT | Gym Owner | GMS |
| 12 | Báo cáo vận hành | GMS | Gym Owner |
| 13 | Sự kiện thời gian | Time / Scheduler | GMS |
| 14 | Khiếu nại & kết quả xử lý | Customer ↔ GMS | |

> Bảng đầy đủ DF-01…DF-25: `docs/02_Context_Diagram_DataFlows.md` (dùng khi viết SRS chi tiết).

## Việc Leader đã chuẩn bị trong repo

| File | Trạng thái |
|------|------------|
| `docs/step2/phuoc_cd.md` | Bảng DF + hướng dẫn VP |
| `03_Images/CD_ContextDiagram_DRAFT.png` | **Nháp bố cục** (không thay PNG nộp từ VP) |
| `02_Models/CD-01_Context.puml` | PlantUML tham khảo khi vẽ lại trên VP |
| `01_SRS_GMS.docx` §2.1 | Đã chèn bảng DF (≥12) + ghi chú chờ PNG từ VP |

## Việc Phước còn phải làm tay trong Visual Paradigm

1. Mở / tạo `02_Models/GMS.vpp`.
2. Diagram → New → **Data Flow Diagram** → tên `CD-01 Context Diagram`.
3. Vẽ theo bảng 14 luồng ở trên (1 process, không data store).
4. Export PNG → ghi đè / đặt tên chính thức `03_Images/CD_ContextDiagram.png`.
5. Chèn hình vào SRS §2.1 (thay dòng TODO ảnh).

## Checklist cá nhân #10

- [x] Chốt entity + ≥12 data flow (danh từ)
- [x] Cập nhật SRS §2.1 (bảng DF)
- [x] File hướng dẫn + nháp bố cục
- [ ] **Vẽ xong trong Visual Paradigm → `GMS.vpp` + `CD_ContextDiagram.png`**
