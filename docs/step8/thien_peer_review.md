# Bước 8 — Thiên (Peer Review: CD-01 + SMD-01/SMD-02 + UC Check-in)

> **Issue:** [#42](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/42) · **Branch:** `step-8`  
> **Người thực hiện review:** Thiên (`@ngthien05` — `tamt2301@gmail.com`)  
> **Tiêu chuẩn đối chiếu:** `docs/HuongDan_Assignment.md` (Mục C.2, D.1, D.3, D.4, D.6, D.8 và Phần F).

---

## 1. Bảng tổng hợp kết quả Peer Review

| Artifact | Phụ trách chính | Trạng thái (`OK?`) | Ghi chú kiểm tra & Đề xuất chỉnh sửa |
|----------|-----------------|--------------------|--------------------------------------|
| **`CD-01` Context Diagram**<br>(`03_Images/CD_ContextDiagram.png`, `docs/step2/phuoc_cd.md`) | Phước | **OK** *(kèm 3 góp ý nhỏ hoàn thiện ảnh)* | **Đạt chuẩn cấu trúc:** Có duy nhất 1 tiến trình trung tâm `0 - Gym Management System (GMS)`, đủ 7 External Entities (≥ 5), không vẽ Data Store, bảng mô tả có ≥ 14 luồng dữ liệu danh từ.<br>**Góp ý chỉnh nhẹ trên ảnh `.vpp` nếu còn thời gian:**<br>1. Sửa lỗi chính tả gõ máy trên nhãn mũi tên trong ảnh `CD_ContextDiagram.png`: *"Yêu cậu thanh toán / Kết quà"* → *"Yêu cầu thanh toán / Kết quả"*, *"Nội dupg SMS"* → *"Nội dung SMS"*, *"Đang ký"* → *"Đăng ký"*.<br>2. Mũi tên giữa `Time / Scheduler` và `GMS` nên để **1 chiều** từ `Time / Scheduler → GMS` (*Sự kiện thời gian*), không cần đầu mũi tên ngược lại.<br>3. Theo mục D.1, luồng 2 chiều nên tách thành 2 mũi tên đơn 1 chiều riêng biệt nếu không gian canvas cho phép. |
| **`SMD-01` Membership Lifecycle**<br>(`03_Images/SMD_Membership.png`, `docs/step7/thien_smd.md`) | Thiên | **OK (Đạt 100%)** | - Đủ **5 trạng thái thực tế** (`Inactive`, `Active`, `Suspended`, `Expired`, `Cancelled`) + `Initial`/`Final` (đạt yêu cầu ≥ 5 states).<br>- Toàn bộ 12 transitions đều tuân thủ định dạng `event [guard] / action`.<br>- Đã bao phủ đầy đủ nhánh tự hết hạn theo thời gian `when(current_date > end_date)` (`UC-27`, `BR-11`), nhánh gia hạn `renew` (`UC-20`) và nhánh tạm khóa `suspend` (`BR-04`).<br>- Không có trạng thái chết (dead state); khớp giá trị cột `Membership.Status` trong ERD. |
| **`SMD-02` PT Booking Lifecycle**<br>(`03_Images/SMD_PTBooking.png`, `docs/step7/thien_smd.md`) | Thiên *(Tuấn review chéo)* | **OK (Đạt 100%)** | - Đủ **6 trạng thái thực tế** (`Pending`, `Confirmed`, `In Progress`, `Completed`, `Rejected`, `Cancelled`) + `Initial`/`Final` (đạt yêu cầu ≥ 5 states).<br>- Phản ánh chính xác quy tắc `BR-08` (Time event `after(24h)` tự hủy booking `Pending` và hoàn tiền), `BR-09` (từ chối phải có lý do + hoàn tiền), và `BR-10` (`recordSession` trừ dần số buổi từ `Confirmed` → `In Progress` → `Completed`).<br>- Đồng bộ hoàn toàn với đặc tả `UC-11`, `UC-12`, `UC-15` và `UC-24`. |
| **Các UC Check-in & Buổi tập liên quan**<br>(`UC-07`, `UC-08`, `UC-09`, `UC-15`, `UC-27`, Wireframe `SCR-08`, `SCR-15`) | Thiên | **OK (Đạt 100%)** | - `UC-08 (Check-in by QR)` và `UC-15 (Record Training Session)` đã viết đầy đủ theo bảng Fully Dressed chuẩn tiếng Anh như `UC-05`/`UC-06`.<br>- `UC-08` có đủ Normal Flow (9 bước), 4 Alternative Flows (bao gồm `ManualEntry` tại Extension Point khi camera lỗi — `DE-03`), 3 Exceptions, gắn kết chặt với `BR-04`, `BR-05` và chỉ số `BO-02` (phản hồi ≤ 2 giây).<br>- Wireframe `SCR-08` (`UI_UC-08_QRCheckIn.png`) và `SCR-15` (`UI_UC-15_RecordSession.png`) có đầy đủ Callouts ①–⑥ và ảnh trạng thái lỗi (`SCR-08-E`, `SCR-15-E`). |

---

## 2. Checklist rà soát chi tiết theo chuẩn Hướng dẫn (Mục D.1, D.6, D.8)

### 2.1. Kiểm tra `CD-01 Context Diagram` (Mục D.1)
- [x] Hệ thống ở giữa là **1 process duy nhất** (`0 – Gym Management System (GMS)`), không tách thành nhiều process con.
- [x] Số lượng External Entity đạt **7 thực thể** (≥ 5 theo yêu cầu): `Customer`, `Personal Trainer`, `Gym Owner`, `Payment Gateway`, `SMS Service`, `QR Service`, `Time / Scheduler`.
- [x] Không vẽ `Data Store` (CSDL) trên Context Diagram.
- [x] Tên các luồng dữ liệu trong bảng đặc tả §2.1 đều là **danh từ / cụm danh từ** (≥ 12 luồng), không dùng động từ đơn lẻ.
- [x] Mọi luồng dữ liệu liên quan đến QR & Membership (`DF-05`..`DF-14`, `DF-18`, `DF-23`) đều ánh xạ tới ít nhất 1 Use Case trong Mục 3.

### 2.2. Kiểm tra `SMD-01` & `SMD-02` (Mục D.6)
- [x] Tên trạng thái là tính từ/phân từ (`Inactive`, `Active`, `Suspended`, `Expired`, `Cancelled`, `Pending`, `Confirmed`, `In Progress`, `Completed`, `Rejected`), không nhầm lẫn với tên hành động.
- [x] Mỗi sơ đồ có **≥ 5 trạng thái** (`SMD-01` có 5 trạng thái; `SMD-02` có 6 trạng thái).
- [x] Mọi mũi tên chuyển trạng thái đều có đủ `event [guard] / action`.
- [x] Có sử dụng Time Event chuẩn UML: `when(current_date > end_date)` trên `SMD-01` và `after(24h)` trên `SMD-02`.
- [x] Mọi trạng thái đều đến được từ `Initial` và có đường thoát hợp lệ về `Final`.

### 2.3. Kiểm tra nhất quán chéo giữa các mô hình (Cross-Model Consistency — Mục D.8)
- [x] **Context Diagram ↔ Use Case Diagram:** 3 External Entity người (`Customer`, `Personal Trainer`, `Gym Owner`) khớp với 3 Primary Actors; 4 hệ thống ngoài (`Payment Gateway`, `SMS Service`, `QR Service`, `Time / Scheduler`) khớp với Actors trên `UCD-01 Overview` và `UCD-03 Membership`.
- [x] **Use Case Diagram ↔ Đặc tả UC (`UC-08`, `UC-15`):**
  - Quan hệ `<<include>> Validate QR Code` và `<<extend>> Enter Code Manually` (tại Extension Point `ManualEntry`) trên `UCD-03 Membership` khớp chính xác với Bước 3 của Normal Flow và Alternative Flow 1 trong `docs/step4/UC-08.md`.
- [x] **Đặc tả UC ↔ Wireframe (`SCR-08`, `SCR-15`):**
  - Mọi trường dữ liệu nhập/xuất trong `UC-08` và `UC-15` đều xuất hiện trên `UI_UC-08_QRCheckIn.png` và `UI_UC-15_RecordSession.png` kèm trạng thái báo lỗi `SCR-08-E`, `SCR-15-E`.
- [x] **Đặc tả UC ↔ State Machine ↔ ERD:**
  - Các trạng thái của `Membership` (`INACTIVE`, `ACTIVE`, `SUSPENDED`, `EXPIRED`, `CANCELLED`) và `PTBooking` (`PENDING`, `CONFIRMED`, `IN_PROGRESS`, `COMPLETED`, `REJECTED`, `CANCELLED`) đồng nhất giữa `UC-05`, `UC-06`, `UC-08`, `UC-12`, `UC-15`, `SMD-01`, `SMD-02` và từ điển dữ liệu ERD.

---

## 3. Kết luận

- Các mô hình và đặc tả thuộc phạm vi rà soát (`CD-01`, `SMD-01`, `SMD-02`, `UC-08`, `UC-15`, `SCR-08`, `SCR-15`) **đã đạt đầy đủ các tiêu chí về số lượng, cú pháp UML và tính nhất quán chéo** theo Rubric chấm điểm của môn học SWR302.
- Chỉ còn 1 chỉnh sửa nhỏ về mặt hiển thị (sửa vài ký tự gõ nhầm dấu tiếng Việt trên ảnh `03_Images/CD_ContextDiagram.png` của `CD-01`), hoàn toàn không ảnh hưởng đến cấu trúc logic và bảng dữ liệu trong SRS.
- **Đề xuất:** Sẵn sàng đóng gói vào bản SRS hoàn chỉnh (`01_SRS_GMS.docx`) và Ma trận truy vết (`04_Traceability_Matrix.xlsx`) để nộp cuối kỳ.
