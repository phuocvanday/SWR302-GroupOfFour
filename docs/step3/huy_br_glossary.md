# Bước 3 — Huy (BR + Glossary + UCD Report/Feedback)

> Issue: #18 · Nhánh: `step3/huy-br-glossary`

## Business Rules

| BR-ID | Mô tả | Loại | Liên quan UC |
|-------|-------|------|--------------|
| BR-01 | Khách hàng chỉ được Check-in khi gói tập (Membership) ở trạng thái **ACTIVE** và còn hạn sử dụng. | Constraint | UC-08, UC-09 |
| BR-02 | Mỗi mã QR Code Check-in chỉ có hiệu lực trong **60 giây** và chỉ được sử dụng **1 lần** để tránh gian lận chụp ảnh gửi cho người khác. | Security / Constraint | UC-07, UC-08 |
| BR-03 | Mỗi tài khoản PT chỉ được duyệt bởi **Gym Owner** sau khi đã xác minh đầy đủ bằng cấp/chứng chỉ hành nghề. | Action Enabler | UC-16, UC-17 |
| BR-04 | Khách hàng chỉ được phép đặt lịch (Book PT) nếu gói Membership cá nhân đang ở trạng thái **ACTIVE**. | Constraint | UC-11 |
| BR-05 | Booking PT phải được thực hiện trước ít nhất **24 giờ** so với thời gian bắt đầu buổi tập mong muốn. | Timing / Constraint | UC-11, UC-12 |
| BR-06 | PT có tối đa **24 giờ** để phản hồi (Confirm/Reject) yêu cầu đặt lịch của khách hàng. Nếu quá 24 giờ không phản hồi, hệ thống tự động hủy booking và hoàn lại 100% tiền. | Timing / Action Enabler | UC-12 |
| BR-07 | Buổi tập PT chỉ được ghi nhận thành công (Completed) khi PT thực hiện Check-in cho hội viên và bấm "Record Session" sau khi kết thúc. | Computation / Constraint | UC-15 |
| BR-08 | Khi khách hàng gửi khiếu nại/phản hồi (Feedback), hệ thống phải gửi thông báo tới Gym Owner trong vòng **5 phút**. | Action Enabler | UC-25 |
| BR-09 | Khiếu nại của khách hàng chỉ được tạo trong vòng **7 ngày** kể từ khi xảy ra sự cố hoặc buổi tập liên quan. | Constraint | UC-25, UC-26 |
| BR-10 | Khi booking PT bị từ chối hoặc bị tự động hủy do quá hạn 24h, hệ thống hoàn **100%** tiền về đúng phương thức thanh toán ban đầu trong vòng **3 ngày làm việc**. | Action Enabler | UC-12, UC-23 |
| BR-11 | Báo cáo vận hành và doanh thu chỉ cho phép xem và xuất file đối với tài khoản có quyền **Gym Owner**. | Authorization | UC-21, UC-22, UC-24 |
| BR-12 | File báo cáo xuất ra phải đúng định dạng `.xlsx` (Microsoft Excel) và hỗ trợ tải xuống trong vòng **60 giây** đối với dữ liệu dưới 50.000 bản ghi. | System Requirement | UC-22 |

## Glossary (Thuật ngữ chuyên ngành)

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **Gym Owner** | Chủ hoặc quản lý cấp cao nhất của phòng gym, sở hữu toàn bộ quyền quản trị hệ thống, phê duyệt tài khoản PT và xem báo cáo tài chính/vận hành. |
| **Personal Trainer (PT)** | Huấn luyện viên cá nhân, người trực tiếp giảng dạy, quản lý lịch tập và ghi nhận các buổi tập với hội viên. |
| **Membership Package** | Gói tập dành cho hội viên (ví dụ: 1 tháng, 3 tháng, 1 năm), quy định quyền ra vào phòng gym và các tiện ích đi kèm. |
| **PT Package** | Gói dịch vụ huấn luyện cá nhân do PT hoặc phòng gym thiết lập (ví dụ: 8 buổi, 12 buổi), phân biệt với gói Membership ra vào phòng gym. |
| **QR Check-in / Check-out** | Quy trình quét mã QR động trên ứng dụng di động để mở cổng tự động hoặc xác nhận thời gian hội viên ra/vào phòng gym. |
| **Active Membership** | Trạng thái gói tập đã được thanh toán đầy đủ và đang trong khoảng thời gian có hiệu lực sử dụng. |
| **Pending Booking** | Trạng thái yêu cầu đặt lịch PT đã được hội viên thanh toán nhưng đang chờ PT xác nhận hoặc từ chối. |
| **Training Session** | Một buổi tập cụ thể nằm trong gói PT Package đã được đặt lịch và xác nhận giữa hội viên và PT. |
| **Operational Report** | Báo cáo tổng hợp số liệu vận hành phòng gym bao gồm: doanh thu, lượng hội viên mới, lượt Check-in/Check-out và tỷ lệ hoàn thành buổi tập PT. |
| **Feedback / Grievance** | Phản hồi, đánh giá hoặc khiếu nại từ khách hàng gửi tới ban quản lý phòng gym về chất lượng dịch vụ hoặc thái độ của PT. |

## UCD Report / Feedback (Use Case Diagram Package)

- **PNG:** `03_Images/UCD_Report_Feedback.png`
- **Ghi chú:**
  - Sơ đồ bao gồm Actor chính là **Gym Owner** tương tác trực tiếp với các Use Case: `UC-21: Generate Reports`, `UC-22: Export Excel Report`, `UC-24: View Dashboard`, và `UC-26: Process Feedback`.
  - Actor **Customer** và **PT** tương tác với `UC-25: Send Feedback / Complaint`.
  - Mối quan hệ `<<include>>`: `UC-22 (Export Excel Report)` bắt buộc phải kế thừa dữ liệu từ `UC-21 (Generate Reports)`.
  - Mối quan hệ `<<extend>>`: `UC-26 (Process Feedback)` mở rộng xử lý khi có phản hồi mới từ `UC-25 (Send Feedback)`.
  - Toàn bộ sơ đồ được thiết kế và export chuẩn PNG (≥ 150 dpi) từ phần mềm **Visual Paradigm Community** và lưu vào thư mục `02_Models/GMS.vpp`.