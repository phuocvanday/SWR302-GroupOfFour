# Bước 1 — Thiên (Membership / QR Check-in)

## 1. User class — Customer (Hội viên / Khách hàng)

- **Mô tả:** Cá nhân có nhu cầu rèn luyện sức khỏe tại phòng gym; thực hiện đăng ký tài khoản trên hệ thống, mua gói hội viên (Membership) tại quầy, sử dụng mã QR cá nhân để ra/vào phòng tập (check-in/check-out), cũng như tra cứu, đặt gói tập với Huấn luyện viên cá nhân (PT), theo dõi lịch tập và gửi phản hồi dịch vụ.
- **Tần suất sử dụng:** Cao — trung bình **3–6 lần/tuần** (mỗi lần đến phòng tập đều mở hệ thống lấy mã QR để check-in/check-out và xem lịch tập trong tuần).
- **Trình độ / kỹ năng:** Cơ bản — quen sử dụng trình duyệt web trên điện thoại thông minh (smartphone), biết thao tác đăng nhập, hiển thị mã QR trên màn hình hoặc đưa mã QR vào vùng camera quét tại quầy; không yêu cầu kiến thức chuyên môn về CNTT.
- **Quyền hạn chính:**
  - Đăng ký tài khoản hội viên, đăng nhập và cập nhật hồ sơ cá nhân (`UC-01`, `UC-02`, `UC-03`).
  - Xem danh mục gói tập Membership (`UC-04`) và xem mã QR Membership đang hoạt động của bản thân (`UC-07`).
  - Thực hiện check-in và check-out tại quầy/cửa bằng mã QR (`UC-08`, `UC-09`).
  - Xem hồ sơ PT, đặt gói PT, xem lịch tập, hủy booking PT theo quy định (`UC-10`, `UC-11`, `UC-14`, `UC-24`).
  - Nhận thông báo in-app/SMS và gửi phản hồi/khiếu nại dịch vụ trong vòng 7 ngày sau sự kiện (`UC-19`, `UC-25`).
- **Favored? (có/không + lý do):** **Có (Favored User Class)**.
  - *Lý do:* Customer là nguồn doanh thu trực tiếp của phòng gym (từ phí gói Membership và gói PT) và là nhóm người dùng có số lượng lớn nhất, tương tác hàng ngày ở điểm chạm критический (check-in/out giờ cao điểm). Giao diện dành cho Customer bắt buộc phải tối ưu số bước thao tác (mở mã QR trong ≤ 2 thao tác từ màn hình chính) để tránh ùn tắc tại quầy lễ tân.

---

## 2. Scope Membership + QR (Release 1)

| Trong phạm vi (In scope — Release 1) | Ngoài phạm vi (Out of scope — Release sau) |
|--------------------------------------|--------------------------------------------|
| Quản lý danh mục gói Membership (CRUD gói tập: thời hạn theo tháng, mức giá VND, mô tả quyền lợi) bởi Gym Owner (`UC-23`). | Gói tập đa chi nhánh (multi-branch roaming) hoặc gói tập tính phí theo số giờ lẻ. |
| Đăng ký gói Membership mới cho Customer trực tiếp tại quầy lễ tân bởi Gym Owner, hỗ trợ thu tiền mặt hoặc qua cổng thanh toán (`UC-05`). | Khách hàng tự mua mới gói Membership lần đầu hoàn toàn online không qua xác minh tại quầy. |
| Kích hoạt thẻ tập (`Activate`) sau khi xác nhận thu đủ 100% phí gói, tự động tính ngày hết hạn và sinh mã QR định danh duy nhất (`UC-06`). | Phát hành thẻ cứng từ tính NFC / RFID vật lý hoặc nhận diện sinh trắc học (vân tay, khuôn mặt FaceID). |
| Hiển thị mã QR Membership trên giao diện web responsive của Customer và gửi thông báo SMS xác nhận kích hoạt (`UC-07`). | Ứng dụng di động gốc (Native iOS / Android App) và lưu thẻ vào Apple Wallet / Google Wallet. |
| Quét và xác thực mã QR để ghi nhận lượt vào/ra (`Check-in` / `Check-out`) kèm kiểm tra trạng thái `ACTIVE` và khung giờ mở cửa; hỗ trợ nhập mã thủ công khi camera lỗi (`UC-08`, `UC-09`). | Tích hợp điều khiển phần cứng cổng xoay tự động (turnstile barrier / khóa từ cửa tự động) — Release 1 chỉ xác thực phần mềm trên thiết bị tại quầy/cửa. |
| Gia hạn gói Membership (`Renew`) cho thẻ sắp hết hạn hoặc đã hết hạn (`UC-20`). | Chuyển nhượng gói tập (transfer) giữa hai hội viên hoặc bảo lưu/đóng băng (freeze) tự động trên app của Customer. |
| Tác vụ tự động hàng ngày (`Time/Scheduler`) kiểm tra `end_date`, chuyển thẻ quá hạn sang `EXPIRED`, vô hiệu hóa mã QR và gửi SMS thông báo (`UC-27`). | Tự động trích nợ gia hạn định kỳ (auto-renewal recurring billing qua thẻ tín dụng). |

---

## 3. BO-01, BO-02 (Mục tiêu kinh doanh — Đo lường được)

### BO-01: Rút ngắn thời gian đăng ký và kích hoạt hội viên tại quầy lễ tân
- **Vấn đề hiện tại:** Ghi sổ giấy hoặc nhập file Excel rời rạc tại quầy mất trung bình 10–15 phút/khách, dễ sai sót ngày hết hạn và gây chờ đợi vào khung giờ cao điểm (17:00–20:00).
- **Mục tiêu (Goal):** Chuẩn hóa quy trình từ lúc tạo hồ sơ Membership (`UC-05`) đến khi kích hoạt và cấp mã QR (`UC-06`) trên cùng một luồng xử lý.
- **Chỉ số đo (Success Metric):** Thời gian hoàn tất trọn vẹn quy trình **Register → Activate** (khi khách đã thanh toán đủ phí) đạt **≤ 5 phút/khách hàng** đối với **≥ 90%** số giao dịch tại quầy trong vòng **1 tháng** kể từ khi vận hành chính thức.
- **Cách đo lường:** Đo bằng chênh lệch thời gian hệ thống (`timestamp` tạo bản ghi Membership `INACTIVE` đến `timestamp` chuyển sang `ACTIVE` trong CSDL).

### BO-02: Kiểm soát chặt chẽ lượt ra/vào phòng tập và ngăn chặn tình trạng tập không hợp lệ
- **Vấn đề hiện tại:** Kiểm tra thẻ giấy bằng mắt thường không phát hiện kịp thời thẻ đã hết hạn hoặc mượn thẻ của người khác, không thống kê được lưu lượng khách theo khung giờ.
- **Mục tiêu (Goal):** Bắt buộc xác thực trạng thái hội viên bằng mã QR điện tử trước khi vào khu vực tập luyện.
- **Chỉ số đo (Success Metric):**
  - Đạt **≥ 95%** tổng số lượt hội viên vào phòng tập trong giờ mở cửa được ghi nhận bản ghi `CheckInLog` hợp lệ trên hệ thống sau **1 tháng** triển khai.
  - **100%** lượt quét mã QR của thẻ có trạng thái khác `ACTIVE` (`INACTIVE`, `EXPIRED`, `SUSPENDED`) bị hệ thống từ chối và cảnh báo trên màn hình quét trong thời gian **≤ 2 giây**.
- **Cách đo lường:** Đối chiếu số lượng bản ghi `CheckInLog` hợp lệ trên hệ thống với số lượt kiểm đếm thực tế định kỳ tại quầy và nhật ký từ chối quét mã.

---

## 4. Assumptions & Dependencies (AS / DE mảng Membership & QR)

| ID | Loại | Nội dung Giả định / Phụ thuộc | Ảnh hưởng nếu không đảm bảo & Hướng xử lý |
|----|------|-------------------------------|-------------------------------------------|
| **AS-01** | Assumption | Tại quầy lễ tân luôn có ít nhất 01 Gym Owner (hoặc nhân sự được ủy quyền sử dụng tài khoản quản lý quầy) trực trong suốt khung giờ mở cửa (05:30–22:00). | Nếu không có người trực quầy, khách hàng mới không thể hoàn tất `UC-05` (Đăng ký tại quầy) và `UC-06` (Kích hoạt thẻ). |
| **AS-02** | Assumption | Mỗi hội viên có ít nhất 01 thiết bị di động cá nhân có màn hình hiển thị được mã QR (từ trình duyệt web hoặc ảnh chụp màn hình mã QR) khi đến phòng tập. | Nếu khách quên điện thoại hoặc hết pin, nhân viên tại quầy sử dụng luồng mở rộng nhập mã định danh hội viên/SĐT thủ công trong `UC-08`. |
| **AS-03** | Assumption | Mỗi hội viên tại một thời điểm chỉ sở hữu tối đa 01 gói Membership ở trạng thái `ACTIVE`, gắn với duy nhất 01 mã QR ổn định suốt chu kỳ hiệu lực. | Tránh xung đột khi quét mã QR không biết trừ/ghi nhận vào gói tập nào. |
| **DE-02** | Dependency | Dịch vụ SMS Gateway bên thứ ba hoạt động ổn định (uptime ≥ 99%) để gửi tin nhắn xác nhận kích hoạt thẻ và cảnh báo hết hạn. | Nếu SMS Service lỗi hoặc trễ, hệ thống vẫn phải hoàn tất kích hoạt thẻ, lưu thông báo in-app (`UC-19`) và hiển thị trực tiếp mã QR trên màn hình cho khách. |
| **DE-03** | Dependency | Thiết bị quét tại quầy/cửa (tablet hoặc webcam/máy quét 2D nối máy tính quầy) có kết nối mạng Internet ổn định và đủ ánh sáng để đọc mã QR. | Nếu camera mờ/hỏng hoặc mất góc quét, hệ thống cung cấp chức năng **Nhập mã Membership thủ công** (`<<extend>>` của `UC-08`) để không làm gián đoạn việc vào cửa. |

---

## 5. Nháp Business Rules mảng Membership / QR (Chuẩn bị cho Bước 3)

| ID | Quy tắc nghiệp vụ (Business Rule) | Loại | Nguồn / UC áp dụng |
|----|-----------------------------------|------|--------------------|
| **BR-01** | Chỉ tài khoản có vai trò **Gym Owner** (đã xác thực đăng nhập) mới được phép tạo mới hồ sơ đăng ký Membership tại quầy và thực hiện lệnh kích hoạt (`Activate`). | Constraint | Phân quyền (`UC-05`, `UC-06`) |
| **BR-02** | Một bản ghi Membership chỉ được chuyển từ trạng thái `INACTIVE` sang `ACTIVE` khi tổng số tiền thanh toán đã ghi nhận thành công bằng **100% giá niêm yết** của gói tập (trừ khuyến mãi hợp lệ nếu có). | Constraint | Chính sách tài chính (`UC-05`, `UC-06`, `UC-20`) |
| **BR-03** | Ngày hết hạn (`EndDate`) của Membership được tính theo công thức: `EndDate = StartDate + DurationMonths` (tính theo tháng lịch, hiệu lực đến **23:59:59 UTC+7** của ngày cuối cùng). Nếu gia hạn khi thẻ còn hạn, thời gian mới được cộng nối tiếp vào `EndDate` hiện tại. | Computation | Quy định gói tập (`UC-06`, `UC-20`) |
| **BR-04** | Mỗi Membership ở trạng thái `ACTIVE` được cấp **duy nhất 01 mã QR** định danh. Khi trạng thái Membership chuyển sang `EXPIRED` hoặc `SUSPENDED`, mã QR đó lập tức bị vô hiệu hóa khi quét tại cửa. | Constraint | Kiểm soát ra vào (`UC-06`, `UC-07`, `UC-08`, `UC-09`) |
| **BR-05** | Hệ thống chỉ cho phép ghi nhận **Check-in hợp lệ** khi thỏa mãn đồng thời 2 điều kiện: (1) Membership gắn với mã QR đang ở trạng thái `ACTIVE` (`CurrentDate <= EndDate`), và (2) Thời điểm quét nằm trong **khung giờ mở cửa** của phòng gym (mặc định **05:30 – 22:00 UTC+7**). | Constraint | Quy định vận hành (`UC-08`, `UC-09`) |
| **BR-11** | Vào lúc **00:05 UTC+7** hằng ngày, tiến trình `Time / Scheduler` tự động quét toàn bộ Membership có `Status = ACTIVE` nhưng `EndDate < CurrentDate` để chuyển trạng thái sang `EXPIRED`, khóa hiệu lực mã QR và kích hoạt gửi SMS thông báo hết hạn cho Customer. | Action enabler | Tự động hóa vận hành (`UC-27`) |

---

## 6. Glossary Membership / QR (6 thuật ngữ)

| Thuật ngữ | Định nghĩa | Ghi chú / Đồng nghĩa |
|-----------|------------|----------------------|
| **Membership (Thẻ hội viên)** | Bản ghi thể hiện hợp đồng/quyền tập luyện của một `Customer` đối với một `Membership Package` cụ thể trong khoảng thời gian từ `StartDate` đến `EndDate`, đi kèm trạng thái vòng đời (`INACTIVE`, `ACTIVE`, `EXPIRED`, `SUSPENDED`). | Đối tượng có SMD-01 |
| **Membership Package (Gói tập)** | Sản phẩm dịch vụ cơ bản do phòng gym cung cấp, quy định rõ tên gói, thời hạn sử dụng (`DurationMonths` — ví dụ: 1, 3, 6, 12 tháng), mức giá (VND) và quyền lợi sử dụng cơ sở vật chất. | Danh mục gói hội viên |
| **QR Membership (Mã QR hội viên)** | Mã vạch ma trận 2 chiều (2D QR Code) chứa chuỗi định danh duy nhất (token/payload) được sinh ra khi Membership chuyển sang `ACTIVE`, dùng để xác thực danh tính và quyền vào cửa của hội viên. | BR-04 |
| **Activate (Kích hoạt thẻ)** | Hành động nghiệp vụ của Gym Owner xác nhận hội viên đã hoàn tất thanh toán phí gói tập để chuyển trạng thái Membership từ `INACTIVE` sang `ACTIVE`, thiết lập `StartDate`/`EndDate` và sinh mã QR. | `UC-06` |
| **Check-in / Check-out** | Sự kiện hệ thống quét, xác thực mã QR của hội viên và ghi nhận thời điểm bắt đầu vào phòng tập (`Check-in`) hoặc thời điểm rời phòng tập (`Check-out`) vào bảng nhật ký `CheckInLog`. | `UC-08`, `UC-09` |
| **Grace / Expiry Job (Tác vụ hết hạn tự động)** | Tiến trình chạy định kỳ hằng đêm bởi actor `Time / Scheduler` nhằm tự động chuyển các thẻ đã quá ngày `EndDate` từ `ACTIVE` sang `EXPIRED` và thu hồi quyền quét QR. | `UC-27`, `BR-11` |

---

## 7. Ghi chú / Câu hỏi thống nhất với nhóm

1. **Khung giờ mở cửa chuẩn (BR-05):** Đề xuất chốt khung giờ mở cửa mặc định trong SRS là **05:30 – 22:00 (UTC+7)** tất cả các ngày trong tuần để dùng thống nhất trong điều kiện kiểm tra của `UC-08 (Check-in bằng QR)`.
2. **Quy tắc Check-out quên quét mã (`UC-09`):** Nếu hội viên đã `Check-in` nhưng lúc về quên `Check-out`, đề xuất cuối ngày (23:59) hệ thống tự động đóng phiên tập đó với trạng thái `Auto-Closed` để không chặn lượt `Check-in` vào ngày hôm sau.
3. **Gia hạn Membership (`UC-20`):** Nhóm xác nhận lại xem ở Release 1 chỉ cho phép gia hạn tại quầy (Actor: Gym Owner) hay cho phép cả Customer tự bấm gia hạn online qua Payment Gateway để đồng bộ với sơ đồ `UCD_Membership` ở Bước 3.
