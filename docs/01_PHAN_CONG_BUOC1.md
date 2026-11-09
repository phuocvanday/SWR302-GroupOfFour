# Bước 1 — Phân công (mỗi người làm phần của mình)

> **Nguyên tắc:** AI chỉ tạo khung / gợi ý. Mỗi thành viên **tự viết / tự chốt** phần được giao, ghi tên vào cột “Người làm”, tick Done khi xong.  
> **Leader (Phước)** chỉ ghép & review — **không** viết thay phần của người khác.  
> File nháp tham khảo: `docs/01_Vision_Scope_GMS.md` (chưa phải bản nhóm đã chốt).

**Deadline nội bộ Bước 1:** _điền ngày_  
**Đầu ra chung:** Mục 1–2 trong `01_SRS_GMS.docx` + cập nhật `05_TeamWork.xlsx`

---

## A. Việc chung cả nhóm (ai cũng phải làm)

| # | Việc | Done |
|---|------|------|
| 1 | Điền **họ tên + MSSV** của mình vào bảng thông tin nhóm & `05_TeamWork.xlsx` | ☐ |
| 2 | Đọc `docs/HuongDan_Assignment.md` mục A.1–A.4, B §1–2 | ☐ |
| 3 | Đọc `docs/kimi2.5-project.md` (đề đã chốt GMS) | ☐ |
| 4 | Comment / duyệt phần mình phụ trách trên Vision (đồng ý hoặc sửa) | ☐ |

---

## B. Chia việc Bước 1 theo thành viên

### 1) Phước — Leader (điều phối, không làm hộ)

| Việc | Chi tiết | Done |
|------|----------|------|
| Trang bìa SRS | Thu thập MSSV/mã nhóm/lớp/GV từ 3 bạn → điền trang bìa + Revision History 0.1 | ☐ |
| §1.1–1.2 | Mục đích tài liệu + quy ước (font, ID, shall/should) — **tự viết** sau khi nhóm thống nhất | ☐ |
| §1.3 BO | Tổng hợp BO-01…BO-04 sau khi cả nhóm chốt số đo | ☐ |
| Scope In/Out | Ghép bảng phạm vi từ góp ý 3 bạn | ☐ |
| `05_TeamWork` | Tạo dòng phân công Bước 1 + nhật ký họp | ☐ |
| Review | Rà soát bản ghép, **không** tự sửa phần chuyên môn của người khác nếu chưa hỏi | ☐ |

### 2) Anh Tuấn — mảng PT / booking (góc nhìn nghiệp vụ)

| Việc | Chi tiết | Done |
|------|----------|------|
| User class **Personal Trainer** | Tự viết mô tả, tần suất, trình độ, quyền hạn, favored? | ☐ |
| Scope PT | Liệt kê **In / Out** liên quan PT, booking, lịch tập (Release 1) | ☐ |
| BO liên quan PT | Đề xuất / chỉnh metric BO-03 (booking Pending 24h, no-show…) — phải **đo được** | ☐ |
| BR mảng PT | Tự soạn nháp BR-06…BR-10 (đặt PT, duyệt PT, 24h, từ chối, ghi buổi) — nhóm sẽ chốt ở Bước 3 | ☐ |
| Glossary | 4–6 thuật ngữ: PT Package, PT Booking, Pending, Training Session… | ☐ |

### 3) Thiên — mảng Membership / QR check-in

| Việc | Chi tiết | Done |
|------|----------|------|
| User class **Customer** | Tự viết đặc điểm user class | ☐ |
| Scope Membership + QR | In/Out: đăng ký quầy, kích hoạt, QR, check-in/out, **không** turnstile phần cứng… | ☐ |
| BO liên quan vận hành cửa | Đề xuất / chỉnh BO-01, BO-02 (thời gian đăng ký; % check-in hợp lệ) | ☐ |
| BR mảng membership/QR | Nháp BR-01…BR-05, BR-11 (ACTIVE đủ phí, 1 QR, giờ mở cửa, hết hạn) | ☐ |
| Assumptions | AS/DE liên quan quầy, thiết bị quét QR, SMS fallback | ☐ |
| Glossary | Membership, QR Membership, Check-in/out, Activate… | ☐ |

### 4) Huy — mảng Owner / báo cáo / ràng buộc / feedback

| Việc | Chi tiết | Done |
|------|----------|------|
| User class **Gym Owner** | Tự viết đặc điểm | ☐ |
| §2.3–2.4 | Môi trường vận hành + ràng buộc (NĐ-13, VND, UTC+7, VP bắt buộc) — **tự viết** | ☐ |
| Scope báo cáo & thanh toán | In/Out: báo cáo Excel, payment gateway; Out: ERP, đa tiền tệ… | ☐ |
| BO-04 | Metric báo cáo (≤ 1 phút, dùng hàng tuần…) | ☐ |
| BR / CSKH | Nháp BR-12 (khiếu nại 7 ngày) + ghi chú chính sách hoàn tiền cần Owner chốt | ☐ |
| References §1.4 | Liệt kê tài liệu tham chiếu (HuongDan, NĐ-13, VP…) | ☐ |

---

## C. Thứ tự làm trong nhóm

```
Mỗi người làm phần B của mình (song song)
        ↓
Họp ngắn 15–30' chốt: BO số đo, In/Out, ngôn ngữ tài liệu (Việt)
        ↓
Phước ghép vào 01_SRS_GMS.docx Mục 1–2
        ↓
Cả nhóm đọc lại 1 lần → tick xong Bước 1 trên 00_LO_TRINH.md
        ↓
Mới sang Bước 2 (CD + UC list) — cũng chia đều, không một người làm hết
```

---

## D. File Bước 2 hiện có trong repo

`02_Context_Diagram_DataFlows.md` và `02_UC_List_Detailed.md` chỉ là **khung tham khảo sớm** — **chưa phải việc đang làm**.  
Khi xong Bước 1, sẽ mở Bước 2 và **chia lại** (ví dụ: mỗi người phụ trách DF + UC thuộc domain của mình, Phước vẽ CD tổng).

---

## E. Checklist “xong Bước 1”

- [ ] 4 MSSV + mã nhóm/lớp/GV đã điền  
- [ ] ≥ 3 BO có chỉ số đo  
- [ ] Bảng In scope / Out of scope đủ rõ  
- [ ] ≥ 3 user class người (Customer, PT, Owner)  
- [ ] Assumptions / Constraints có trong SRS  
- [ ] Mỗi thành viên có dòng đóng góp Bước 1 trong `05_TeamWork.xlsx`  
- [ ] `01_SRS_GMS.docx` Mục 1–2 đã cập nhật (không để trống `<...>`)  
