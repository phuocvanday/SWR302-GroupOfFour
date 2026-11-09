# Bước 2 — Context Diagram (CD-01) + bảng data flow

> **Chưa làm Bước 2.** File này là khung tham khảo sớm — chỉ dùng sau khi Bước 1 xong và nhóm chia việc Bước 2.  
> Dùng để vẽ **Diagram → New → Data Flow Diagram** trong Visual Paradigm.  
> Process duy nhất ở giữa: **`0 – Gym Management System (GMS)`**.  
> **Không** vẽ data store / nhiều process (đó là DFD level 0).  
> Tên data flow = **danh từ / cụm danh từ** (không dùng động từ kiểu “Đăng nhập”).

---

## 1. External entities (≥ 5 — đạt 7)

| # | External entity | Loại | Ghi chú |
|---|-----------------|------|---------|
| 1 | Customer | Người (primary) | Hội viên |
| 2 | Personal Trainer | Người (primary) | HLV cá nhân |
| 3 | Gym Owner | Người (primary) | Chủ / QL phòng gym |
| 4 | Payment Gateway | Hệ thống ngoài | VNPay / MoMo / Stripe… |
| 5 | SMS Service | Hệ thống ngoài | Gửi SMS |
| 6 | QR Service | Hệ thống ngoài | Sinh / xác thực mã QR |
| 7 | Time / Scheduler | Hệ thống (time) | Hết hạn membership, nhắc lịch |

> Khi vẽ UCD: entity người → actor; Payment / SMS / QR / Time → secondary actor.

---

## 2. Bảng mô tả data flow (≥ 12 — đề xuất 18)

| ID | Data flow (nhãn trên mũi tên) | Từ | Đến | Nội dung / data dictionary (tóm tắt) | UC liên quan |
|----|-------------------------------|----|-----|--------------------------------------|--------------|
| DF-01 | Thông tin đăng ký tài khoản | Customer | GMS | Họ tên, SĐT, email, mật khẩu, CCCD (tuỳ chọn) | UC-01 |
| DF-02 | Kết quả đăng ký / OTP | GMS | Customer | Trạng thái tạo TK; mã OTP / link xác minh (nếu có) | UC-01 |
| DF-03 | Thông tin đăng nhập | Customer / PT / Gym Owner | GMS | Email/SĐT + mật khẩu (hoặc token) | UC-02 |
| DF-04 | Phiên đăng nhập | GMS | Customer / PT / Gym Owner | Token phiên, vai trò, thông tin hồ sơ cơ bản | UC-02 |
| DF-05 | Yêu cầu đăng ký membership | Gym Owner | GMS | Customer ID, gói, hình thức TT, ngày bắt đầu dự kiến | UC-05 |
| DF-06 | Hồ sơ membership | GMS | Gym Owner / Customer | Mã membership, trạng thái, hạn, số tiền | UC-05, UC-06, UC-07, UC-20 |
| DF-07 | Yêu cầu thanh toán | GMS | Payment Gateway | Số tiền VND, mã GD, mô tả (membership / PT) | UC-05, UC-11, UC-20 |
| DF-08 | Kết quả thanh toán | Payment Gateway | GMS | Success/Fail, mã tham chiếu cổng, thời điểm | UC-05, UC-11, UC-12, UC-20, UC-24 |
| DF-09 | Yêu cầu kích hoạt membership | Gym Owner | GMS | Membership ID (đã đủ phí) | UC-06 |
| DF-10 | Yêu cầu sinh / xác thực QR | GMS | QR Service | Payload membership ACTIVE / mã quét tại cửa | UC-06, UC-08, UC-09 |
| DF-11 | Kết quả QR | QR Service | GMS | QR image/token hoặc hợp lệ/không hợp lệ | UC-06–UC-09 |
| DF-12 | Mã QR membership | GMS | Customer | Ảnh/mã QR hiển thị trên app | UC-07 |
| DF-13 | Sự kiện check-in / check-out | Customer | GMS | Mã QR quét + loại IN/OUT + thời điểm thiết bị | UC-08, UC-09 |
| DF-14 | Xác nhận check-in / check-out | GMS | Customer | OK/Fail + lý do (hết hạn, ngoài giờ…) | UC-08, UC-09 |
| DF-15 | Yêu cầu đặt gói PT | Customer | GMS | PT, gói PT, lịch mong muốn, ghi chú | UC-11 |
| DF-16 | Yêu cầu booking PT | GMS | Personal Trainer | Chi tiết booking Pending | UC-11, UC-12 |
| DF-17 | Phản hồi booking | Personal Trainer | GMS | Confirm / Reject + lý do (nếu từ chối) | UC-12 |
| DF-18 | Nội dung SMS | GMS | SMS Service | SĐT + nội dung (kích hoạt, booking, nhắc lịch, hết hạn) | UC-06, UC-11, UC-12, UC-17, UC-27, UC-28 |
| DF-19 | Trạng thái gửi SMS | SMS Service | GMS | Delivered / Failed | (hỗ trợ UC thông báo) |
| DF-20 | Yêu cầu duyệt PT | Personal Trainer | GMS | Hồ sơ PT, chứng chỉ, gói dịch vụ dự kiến | UC-16 |
| DF-21 | Quyết định duyệt PT | Gym Owner | GMS | Approve / Reject + ghi chú | UC-17 |
| DF-22 | Báo cáo vận hành | GMS | Gym Owner | Doanh thu, check-in, PT hoàn tất (aggregate) | UC-21, UC-22 |
| DF-23 | Sự kiện thời gian | Time / Scheduler | GMS | Tick ngày / job hết hạn & nhắc lịch | UC-27, UC-28 |
| DF-24 | Khiếu nại dịch vụ | Customer | GMS | Nội dung, UC/booking liên quan, mức độ | UC-25 |
| DF-25 | Kết quả xử lý khiếu nại | GMS | Customer | Trạng thái xử lý + phản hồi Owner | UC-26 |

**Đếm để chấm:** ≥ 12 luồng có tên — bảng trên **25** luồng (có thể gộp DF-18/19 khi vẽ nếu sơ đồ quá dày; vẫn giữ ≥ 12 trên diagram).

### Gợi ý gộp khi vẽ cho gọn (vẫn ≥ 12 mũi tên)

Nếu mũi tên quá nhiều, ưu tiên giữ các luồng sau trên CD-01:

1. Thông tin đăng ký tài khoản  
2. Thông tin đăng nhập / phiên  
3. Yêu cầu đăng ký & kích hoạt membership  
4. Hồ sơ / mã QR membership  
5. Sự kiện & xác nhận check-in/out  
6. Yêu cầu thanh toán  
7. Kết quả thanh toán  
8. Yêu cầu đặt gói PT & phản hồi booking  
9. Nội dung SMS  
10. Yêu cầu / kết quả QR  
11. Quyết định duyệt PT  
12. Báo cáo vận hành  
13. Sự kiện thời gian  
14. Khiếu nại & kết quả xử lý  

---

## 3. Hướng dẫn vẽ nhanh trong Visual Paradigm

1. **Diagram → New → Data Flow Diagram** → tên `CD-01 Context Diagram`.
2. **Process** giữa canvas: `0 – Gym Management System (GMS)`.
3. Thêm 7 **External Entity** quanh process (Customer trái trên; PT trái dưới; Owner phải trên; Payment / SMS / QR / Time phía dưới–phải).
4. Vẽ **Data Flow** một chiều; đặt tên đúng cột *Data flow* ở trên.
5. Export PNG ≥ 150 dpi → `03_Images/CD_ContextDiagram.png`.
6. Chèn ảnh + bảng rút gọn (≥ 12 dòng) vào **SRS §2.1**.

---

## 4. Checklist D.1 / D.8

- [ ] Đúng 1 process giữa  
- [ ] ≥ 5 external entity  
- [ ] ≥ 12 data flow có tên (danh từ)  
- [ ] Không có data store  
- [ ] Mỗi DF map ≥ 1 UC (cột cuối bảng)  
- [ ] Entity người khớp actor trên UCD  
