# HƯỚNG DẪN ASSIGNMENT — XÂY DỰNG TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)

_Công cụ vẽ mô hình bắt buộc: **Visual Paradigm** (Community)_
_Trình bày văn bản đúng chuẩn, mục lục tự động, đánh số tự động các đề mục, nội dung được canh chỉnh: Times New Roman, cỡ chữ 13, Multiple 1.3_

---

## Mục lục

- [Phần A – Tổng quan assignment](#phần-a--tổng-quan-assignment)
  - [A.1 Mục tiêu](#a1-mục-tiêu)
  - [A.2 Yêu cầu chung về đề tài](#a2-yêu-cầu-chung-về-đề-tài)
  - [A.3 Sản phẩm phải nộp](#a3-sản-phẩm-phải-nộp)
  - [A.4 Lộ trình thực hiện đề xuất](#a4-lộ-trình-thực-hiện-đề-xuất)
- [Phần B – Template tài liệu SRS](#phần-b--template-tài-liệu-srs)
- [Phần C – Yêu cầu tối thiểu đề xuất để phân tích](#phần-c--yêu-cầu-tối-thiểu-đề-xuất-để-phân-tích)
- [Phần D – Hướng dẫn phân tích & vẽ từng mô hình bằng Visual Paradigm](#phần-d--hướng-dẫn-phân-tích--vẽ-từng-mô-hình-bằng-visual-paradigm)
  - [D.0 Thiết lập project Visual Paradigm](#d0-thiết-lập-project-visual-paradigm)
  - [D.1 Context Diagram](#d1-context-diagram)
  - [D.2 Use Case Diagram](#d2-use-case-diagram)
  - [D.3 Đặc tả Use Case](#d3-đặc-tả-use-case)
  - [D.4 Phác thảo giao diện (Wireframe / Mockup)](#d4-phác-thảo-giao-diện-wireframe--mockup)
  - [D.5 Activity Diagram có Swimlane](#d5-activity-diagram-có-swimlane)
  - [D.6 State Machine Diagram](#d6-state-machine-diagram)
  - [D.7 ERD mức khái niệm](#d7-erd-mức-khái-niệm)
  - [D.8 Kiểm tra nhất quán giữa các mô hình](#d8-kiểm-tra-nhất-quán-giữa-các-mô-hình)
- [Phần E – Tiêu chí chấm điểm (Rubric)](#phần-e--tiêu-chí-chấm-điểm-rubric)
- [Phần F – Checklist trước khi nộp](#phần-f--checklist-trước-khi-nộp)
- [Phụ lục 1 – Gợi ý đề tài](#phụ-lục-1--gợi-ý-đề-tài)
- [Phụ lục 2 – Ví dụ minh họa ngắn (ClinicCare)](#phụ-lục-2--ví-dụ-minh-họa-ngắn-cliniccare)

---

## Phần A – Tổng quan assignment

### A.1 Mục tiêu

Sau assignment, sinh viên (theo nhóm) có thể:

1. Xác định **phạm vi & ranh giới hệ thống**, các **lớp người dùng (user classes)** và **actor**.
2. Thu thập, phân loại và viết yêu cầu theo 3 mức: **Business → User → Functional**, kèm **Business rules**, **yêu cầu phi chức năng (quality attributes)**, **yêu cầu dữ liệu**.
3. Mô hình hóa yêu cầu bằng các mô hình trực quan (Ch.12):
   - Context Diagram
   - Use Case Diagram + Đặc tả use case (fully dressed)
   - Wireframe/Mockup giao diện cho từng use case được đặc tả
   - Activity Diagram có Swimlane
   - State Machine Diagram
   - ERD mức khái niệm (Conceptual ERD)
4. Viết câu yêu cầu đạt chất lượng (Ch.11): **Complete, Correct, Feasible, Necessary, Prioritized, Unambiguous, Verifiable**; tập yêu cầu **Complete, Consistent, Modifiable, Traceable**.
5. Đảm bảo **truy vết (traceability)** giữa: Business objective ↔ Use case ↔ Functional requirement ↔ Mô hình ↔ Màn hình.

### A.2 Yêu cầu chung về đề tài

| Tiêu chí             | Yêu cầu                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quy mô nhóm          | 4–5 sinh viên                                                                                                                                                    |
| Loại hệ thống        | Hệ thống thông tin có nghiệp vụ thực tế (web / mobile / desktop), **có ít nhất 1 đối tượng nghiệp vụ có vòng đời rõ ràng** (đơn hàng, lịch hẹn, hồ sơ, yêu cầu…) |
| Số actor             | ≥ 4 actor (trong đó ≥ 3 primary actor là con người, ≥ 1 secondary actor là hệ thống bên ngoài, ví dụ cổng thanh toán, dịch vụ email/SMS, hệ thống ERP…)          |
| Số use case          | ≥ 20 use case (không tính đăng nhập/đăng xuất)                                                                                                                   |
| Đặc tả fully dressed | ≥ 2 use case / thành viên (nhóm 5 người → ≥ 10 use case), mỗi đặc tả **phải có wireframe** tương ứng                                                             |
| Không được chọn      | Đề tài đã được dùng làm ví dụ trên lớp (BookHaven, NJS Koi Farm) và hệ thống chỉ có CRUD đơn thuần                                                               |
| Ngôn ngữ             | Tiếng Việt hoặc tiếng Anh, **thống nhất trong toàn bộ tài liệu**; tên phần tử trong mô hình nên dùng tiếng Anh hoặc tiếng Việt có dấu nhất quán                  |

### A.3 Sản phẩm phải nộp

```
<MaNhom>_SWR302_Assignment/
├── 01_SRS_<TenHeThong>.docx  (hoặc .pdf)       ← Tài liệu SRS theo template Phần B
├── 02_Models/
│   └── <TenHeThong>.vpp                          ← File project Visual Paradigm (BẮT BUỘC)
├── 03_Images/                                    ← Ảnh export từ VP (PNG, ≥ 150 dpi)
│   ├── CD_ContextDiagram.png
│   ├── UCD_Overview.png, UCD_<Package>.png
│   ├── AD_<TenQuyTrinh>.png
│   ├── SMD_<TenDoiTuong>.png
│   ├── ERD_Conceptual.png
│   └── UI_<UC-ID>_<TenManHinh>.png
├── 04_Traceability_Matrix.xlsx                   ← Ma trận truy vết
└── 05_TeamWork.xlsx                              ← Phân công & tự đánh giá đóng góp
```

**Quy ước đặt tên & đánh số**

| Loại                   | Mẫu ID                               | Ví dụ       |
| ---------------------- | ------------------------------------ | ----------- |
| Business objective     | `BO-xx`                              | BO-01       |
| Business rule          | `BR-xx`                              | BR-07       |
| Use case               | `UC-xx`                              | UC-12       |
| Functional requirement | `<FEATURE>-xx` hoặc `FR-xx`          | BOOK-03     |
| Non-functional         | `NFR-<Loại>-xx`                      | NFR-PERF-01 |
| Màn hình               | `SCR-xx`                             | SCR-05      |
| Sơ đồ                  | `CD`, `UCD`, `AD`, `SMD`, `ERD` + số | AD-02       |

### A.4 Lộ trình thực hiện đề xuất

| Tuần | Công việc                                                               | Đầu ra              |
| ---- | ----------------------------------------------------------------------- | ------------------- |
| 1    | Chọn đề tài, viết Vision & Scope, xác định stakeholder, user class      | Mục 1–2 SRS         |
| 2    | **Context Diagram**, danh sách actor & use case                         | CD, UC list         |
| 3    | **Use Case Diagram**, business rules, glossary                          | UCD, BR             |
| 4–5  | **Đặc tả use case + Wireframe**                                         | Mục 3 SRS, UI       |
| 6    | **Activity Diagram swimlane** cho các quy trình chính                   | AD                  |
| 7    | **State Machine Diagram**, **ERD khái niệm**, data dictionary           | SMD, ERD, Mục 4 SRS |
| 8    | NFR, giao diện ngoài, ma trận truy vết, review chéo (peer review Ch.17) | SRS hoàn chỉnh      |

---

## Phần B – Template tài liệu SRS

> Sinh viên **giữ nguyên cấu trúc mục**, thay nội dung trong `<...>`. Mục nào không áp dụng ghi rõ **"Không áp dụng – lý do: ..."**, không được xóa mục.

---

### Trang bìa

```
ĐẶC TẢ YÊU CẦU PHẦN MỀM (Software Requirements Specification)
Hệ thống: <Tên hệ thống>
Phiên bản: <1.0>
Nhóm: <Mã nhóm> – Lớp: <Mã lớp>
Thành viên: <Họ tên – MSSV – Vai trò>
Giảng viên hướng dẫn: <...>
Ngày: <dd/mm/yyyy>
```

### Lịch sử phiên bản (Revision History)

| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi     |
| --------- | ---- | -------------- | ------------------ |
| 0.1       |      |                | Bản nháp đầu tiên  |
| 1.0       |      |                | Bản nộp chính thức |

### Mục lục

<Tự động sinh>

---

### 1. Giới thiệu (Introduction)

#### 1.1 Mục đích (Purpose)

<Tài liệu này mô tả yêu cầu cho sản phẩm nào, phiên bản nào, dành cho ai đọc (dev, tester, PM, khách hàng…).>

#### 1.2 Quy ước tài liệu (Document Conventions)

<Quy ước font, in đậm, quy ước đánh ID, mức ưu tiên (High/Medium/Low hoặc MoSCoW), từ khóa "shall / should / may".>

#### 1.3 Phạm vi dự án (Project Scope)

<Mô tả ngắn sản phẩm, lợi ích, mục tiêu kinh doanh. Tham chiếu tài liệu Vision & Scope nếu có.>

**Business objectives**

| ID    | Mục tiêu kinh doanh                          | Chỉ số đo (success metric) |
| ----- | -------------------------------------------- | -------------------------- |
| BO-01 | <Giảm 30% thời gian xử lý ... trong 6 tháng> | <...>                      |

**Phạm vi (In scope / Out of scope)**

| Trong phạm vi (Release 1) | Ngoài phạm vi / Release sau |
| ------------------------- | --------------------------- |
| <...>                     | <...>                       |

#### 1.4 Tài liệu tham chiếu (References)

<Danh sách tài liệu, chuẩn, website tham khảo: tên, tác giả, phiên bản, link.>

---

### 2. Mô tả tổng quan (Overall Description)

#### 2.1 Bối cảnh sản phẩm (Product Perspective)

<Sản phẩm mới hay thay thế hệ thống cũ? Là một phần của hệ thống lớn hơn?>

**→ Chèn Context Diagram (CD-01)** + bảng mô tả luồng dữ liệu (xem D.1).

#### 2.2 Các lớp người dùng & đặc điểm (User Classes and Characteristics)

| User class   | Mô tả | Tần suất sử dụng | Trình độ / kỹ năng | Quyền hạn chính | Mức độ quan trọng (favored?) |
| ------------ | ----- | ---------------- | ------------------ | --------------- | ---------------------------- |
| <Khách hàng> |       |                  |                    |                 |                              |

#### 2.3 Môi trường vận hành (Operating Environment)

<Hệ điều hành, trình duyệt, thiết bị di động, hạ tầng server/cloud, CSDL…>

#### 2.4 Ràng buộc thiết kế & cài đặt (Design and Implementation Constraints)

<Ngôn ngữ lập trình, framework bắt buộc, chuẩn pháp lý (Nghị định 13/2023 về bảo vệ dữ liệu cá nhân…), giới hạn ngân sách/thời gian…>

#### 2.5 Giả định & phụ thuộc (Assumptions and Dependencies)

| ID    | Giả định / Phụ thuộc | Ảnh hưởng nếu sai |
| ----- | -------------------- | ----------------- |
| AS-01 |                      |                   |
| DE-01 |                      |                   |

#### 2.6 Business Rules

| ID    | Business rule | Loại (Fact / Constraint / Action enabler / Inference / Computation) | Nguồn |
| ----- | ------------- | ------------------------------------------------------------------- | ----- |
| BR-01 |               |                                                                     |       |

---

### 3. Tính năng hệ thống (System Features)

#### 3.0 Mô hình use case tổng quan

- **Danh sách actor**

| Actor | Loại (Primary / Secondary) | Mô tả | User class tương ứng |
| ----- | -------------------------- | ----- | -------------------- |

- **Danh sách use case**

| UC-ID | Tên use case (Động từ + Danh từ) | Primary actor | Secondary actor | Ưu tiên | Feature |
| ----- | -------------------------------- | ------------- | --------------- | ------- | ------- |

- **→ Chèn Use Case Diagram tổng quan (UCD-01)** và các sơ đồ theo package (UCD-02…).

#### 3.x <Tên tính năng (Feature)> — lặp lại cho từng tính năng

##### 3.x.1 Mô tả & mức ưu tiên

<Mô tả ngắn tính năng; ưu tiên High/Medium/Low; Benefit/Penalty/Cost/Risk nếu có.>

##### 3.x.2 Chuỗi kích thích / phản hồi (Stimulus/Response)

<Tóm tắt các hành động của người dùng và phản hồi của hệ thống.>

##### 3.x.3 Đặc tả use case

<Mỗi use case thuộc tính năng: dùng template ở D.3. Use case không đặc tả đầy đủ thì viết dạng brief (1 đoạn mô tả).>

##### 3.x.4 Phác thảo giao diện

<Chèn wireframe SCR-xx cho từng use case fully dressed + bảng mô tả field (xem D.4).>

##### 3.x.5 Yêu cầu chức năng (Functional Requirements)

| ID  | Yêu cầu                       | Truy vết UC / BR | Ưu tiên |
| --- | ----------------------------- | ---------------- | ------- |
|     | <Khi ..., hệ thống shall ...> | UC-xx, BR-xx     | H       |

##### 3.x.6 Mô hình hành vi liên quan

<Chèn Activity Diagram swimlane (AD-xx) và/hoặc State Machine Diagram (SMD-xx) cho tính năng nếu có.>

---

### 4. Yêu cầu dữ liệu (Data Requirements)

#### 4.1 Mô hình dữ liệu logic

**→ Chèn ERD mức khái niệm (ERD-01)** + bảng mô tả thực thể & quan hệ (xem D.7).

#### 4.2 Từ điển dữ liệu (Data Dictionary)

| Thực thể | Thuộc tính | Ý nghĩa | Kiểu / Định dạng | Độ dài / Miền giá trị | Bắt buộc | Ví dụ |
| -------- | ---------- | ------- | ---------------- | --------------------- | -------- | ----- |

> Có thể dùng ký pháp Ch.13: `Order = OrderID + OrderDate + Customer + 1:n{OrderLine} + (Note)`

#### 4.3 Báo cáo (Reports)

<Với mỗi báo cáo: ID, tên, mục đích, người dùng, tần suất, nguồn dữ liệu, tiêu chí lọc/sắp xếp, layout phác thảo.>

#### 4.4 Thu thập, toàn vẹn, lưu giữ & hủy dữ liệu

<Dữ liệu lấy từ đâu, kiểm tra hợp lệ, sao lưu, thời gian lưu trữ, quy tắc xóa/ẩn danh.>

---

### 5. Yêu cầu giao diện ngoài (External Interface Requirements)

#### 5.1 Giao diện người dùng (User Interfaces)

<Chuẩn UI chung: style guide, bố cục, thông báo lỗi, phím tắt, responsive, accessibility (WCAG 2.1 AA). Danh sách màn hình SCR-xx và sơ đồ điều hướng (dialog map) nếu có.>

#### 5.2 Giao diện phần mềm (Software Interfaces)

| Hệ thống ngoài | Mục đích | Dữ liệu vào/ra | Giao thức / API | Ghi chú |
| -------------- | -------- | -------------- | --------------- | ------- |

#### 5.3 Giao diện phần cứng (Hardware Interfaces)

#### 5.4 Giao diện truyền thông (Communications Interfaces)

<Email, SMS, push notification, HTTPS, định dạng thông điệp…>

---

### 6. Thuộc tính chất lượng (Quality Attributes)

> Mỗi NFR phải **đo được**. Nên dùng mẫu Planguage (Ch.14) cho ≥ 2 yêu cầu quan trọng.

| ID          | Loại            | Yêu cầu | Cách kiểm chứng |
| ----------- | --------------- | ------- | --------------- |
| NFR-USA-01  | Usability       |         |                 |
| NFR-PERF-01 | Performance     |         |                 |
| NFR-SEC-01  | Security        |         |                 |
| NFR-AVL-01  | Availability    |         |                 |
| NFR-REL-01  | Reliability     |         |                 |
| NFR-SCA-01  | Scalability     |         |                 |
| NFR-MNT-01  | Maintainability |         |                 |

**Ví dụ Planguage**

```
TAG:      NFR-PERF-01 Search.ResponseTime
AMBITION: Kết quả tìm kiếm hiển thị nhanh để người dùng không bỏ đi.
SCALE:    Số giây từ khi nhấn "Tìm" đến khi trang kết quả hiển thị đầy đủ.
METER:    Kiểm thử tải với 500 người dùng đồng thời, đo 95th percentile.
MUST:     ≤ 3 giây
PLAN:     ≤ 1,5 giây
```

---

### 7. Yêu cầu quốc tế hóa & bản địa hóa

<Ngôn ngữ, định dạng ngày (dd/mm/yyyy), tiền tệ (VND), múi giờ (UTC+7)…>

### 8. Yêu cầu khác

<Pháp lý, cài đặt, đào tạo, vận hành…>

---

### Phụ lục A – Thuật ngữ (Glossary)

| Thuật ngữ | Định nghĩa | Từ đồng nghĩa / Ghi chú |
| --------- | ---------- | ----------------------- |

### Phụ lục B – Mô hình phân tích (Analysis Models)

| ID     | Tên sơ đồ | Loại                        | Mục SRS sử dụng |
| ------ | --------- | --------------------------- | --------------- |
| CD-01  |           | Context Diagram             | 2.1             |
| UCD-01 |           | Use Case Diagram            | 3.0             |
| AD-01  |           | Activity Diagram (swimlane) | 3.x.6           |
| SMD-01 |           | State Machine Diagram       | 3.x.6           |
| ERD-01 |           | Conceptual ERD              | 4.1             |

### Phụ lục C – Ma trận truy vết (Traceability Matrix)

| BO  | UC-ID | FR-ID | BR-ID | Sơ đồ | Màn hình | Test case (dự kiến) |
| --- | ----- | ----- | ----- | ----- | -------- | ------------------- |

### Phụ lục D – Danh sách vấn đề mở (TBD / Issues List)

| ID  | Vấn đề | Người phụ trách | Hạn | Trạng thái |
| --- | ------ | --------------- | --- | ---------- |

---

## Phần C – Yêu cầu tối thiểu đề xuất để phân tích

Để có đủ "chất liệu" vẽ các sơ đồ, hệ thống của nhóm **phải** có các nhóm yêu cầu sau. Đây là danh sách gợi ý — nhóm điều chỉnh theo nghiệp vụ thực tế.

### C.1 Nhóm yêu cầu bắt buộc

| #   | Nhóm yêu cầu                                                              | Gợi ý use case                                                                             | Phục vụ sơ đồ                                |
| --- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 1   | **Tài khoản & phân quyền**                                                | Đăng ký, Đăng nhập, Quên mật khẩu, Cập nhật hồ sơ, Quản lý tài khoản nhân viên, Phân quyền | UCD, ERD                                     |
| 2   | **Tra cứu / tìm kiếm** đối tượng nghiệp vụ chính                          | Tìm kiếm, Lọc, Xem chi tiết, So sánh                                                       | UCD, Wireframe                               |
| 3   | **Giao dịch nghiệp vụ chính** (đặt hàng / đặt lịch / đăng ký / nộp hồ sơ) | Tạo yêu cầu, Chỉnh sửa, Hủy, Xác nhận                                                      | UCD, **AD swimlane**, **SMD**, Wireframe     |
| 4   | **Phê duyệt / xử lý nhiều bên** (≥ 3 vai trò cùng tham gia một quy trình) | Duyệt yêu cầu, Phân công, Cập nhật tiến độ, Hoàn tất                                       | **AD swimlane**                              |
| 5   | **Thanh toán / tích hợp hệ thống ngoài**                                  | Thanh toán online, Hoàn tiền, Gửi email/SMS                                                | **Context Diagram**, UCD (secondary actor)   |
| 6   | **Thông báo**                                                             | Nhận thông báo khi trạng thái thay đổi                                                     | SMD (effect của transition)                  |
| 7   | **Quản lý danh mục / dữ liệu chủ**                                        | Quản lý sản phẩm/dịch vụ, danh mục, giá                                                    | ERD                                          |
| 8   | **Phản hồi / khiếu nại / đánh giá**                                       | Đánh giá dịch vụ, Gửi khiếu nại, Xử lý khiếu nại                                           | UCD, SMD (vòng đời khiếu nại)                |
| 9   | **Báo cáo – thống kê**                                                    | Doanh thu, Hiệu suất nhân viên, Xuất Excel/PDF                                             | Context Diagram (luồng báo cáo ra), Mục 4.3  |
| 10  | **Tác vụ tự động theo thời gian**                                         | Tự hủy đơn quá hạn, Nhắc lịch                                                              | UCD (actor Time/Scheduler), SMD (time event) |

### C.2 Yêu cầu tối thiểu cho từng mô hình

| Mô hình                   | Số lượng tối thiểu            | Điều kiện                                                                            |
| ------------------------- | ----------------------------- | ------------------------------------------------------------------------------------ |
| Context Diagram           | 1                             | ≥ 5 external entity, ≥ 12 data flow (có tên)                                         |
| Use Case Diagram          | 1 tổng quan + 1 sơ đồ/package | ≥ 20 UC, có ≥ 2 `<<include>>`, ≥ 2 `<<extend>>`, ≥ 1 generalization actor            |
| Đặc tả use case           | ≥ 2 UC / thành viên           | Fully dressed, mỗi UC có ≥ 1 alternative flow và ≥ 2 exception                       |
| Wireframe                 | 1 màn hình chính / UC đặc tả  | Ánh xạ được tới từng bước trong normal flow                                          |
| Activity Diagram swimlane | ≥ 3                           | ≥ 3 swimlane/sơ đồ, có decision, fork/join (≥ 1 sơ đồ)                               |
| State Machine Diagram     | ≥ 2                           | Mỗi sơ đồ ≥ 5 state, transition có `event [guard] / action`                          |
| ERD khái niệm             | 1                             | ≥ 10 thực thể, có quan hệ N–N được giải quyết hoặc ghi rõ, có cardinality ở cả 2 đầu |

### C.3 Câu hỏi khơi gợi yêu cầu (dùng khi phỏng vấn / workshop)

- Ai dùng hệ thống? Họ muốn **đạt được gì** (goal) chứ không chỉ "làm gì"?
- Đối tượng nghiệp vụ chính trải qua **những trạng thái nào**? Ai/sự kiện gì làm nó chuyển trạng thái? Có quay lui được không?
- Quy trình có **bao nhiêu bên tham gia**? Bước nào chạy song song? Điểm nào phải ra quyết định?
- Hệ thống **nhận dữ liệu từ đâu, gửi dữ liệu đi đâu**? Có tích hợp bên thứ ba không?
- Điều gì xảy ra khi **lỗi**: mất mạng, thanh toán thất bại, quá hạn, trùng lặp, hết hàng/hết chỗ?
- Có **quy định / chính sách** nào (giá, giảm giá, phí phạt, giới hạn số lượng, thời gian) không? → Business rules.
- Có thông tin nào phải **lưu lại / báo cáo**? → Thực thể ERD.

---

## Phần D – Hướng dẫn phân tích & vẽ từng mô hình bằng Visual Paradigm

### D.0 Thiết lập project Visual Paradigm

1. **Project → New**, đặt tên `<TenHeThong>`, lưu file `.vpp` vào `02_Models/`.
2. Trong **Model Explorer / Diagram Navigator**, tạo cấu trúc model:
   ```
    <TenHeThong>
    ├── 01 Context
    ├── 02 Use Case Model   (chia package theo feature)
    ├── 03 Wireframes
    ├── 04 Activity
    ├── 05 State Machine
    └── 06 Data Model
   ```
3. **Dùng lại phần tử** (actor, entity…) bằng cách kéo từ Model Explorer vào sơ đồ, **không vẽ lại** phần tử trùng tên → giúp đảm bảo nhất quán.
4. Đặt **Glossary**: VP có chức năng _Glossary_ (Project → Glossary / tô đậm từ trong mô tả → _Add to Glossary_) — dùng để quản lý thuật ngữ cho Phụ lục A.
5. **Export ảnh**: chuột phải nền sơ đồ → **Export → Export Diagram as Image** (PNG). Hoặc **Project → Export → Diagrams to Images** để xuất hàng loạt.
6. Có thể dùng **Doc. Composer** (Tools → Doc. Composer) để sinh nhanh phần đặc tả use case sang Word, sau đó chỉnh lại theo template.

> **Lưu ý về phiên bản:** Một số chức năng (Wireframe, Conceptual/Logical ERD, Doc. Composer đầy đủ) chỉ có ở bản Standard/Professional hoặc VP Online. Nếu dùng **Community Edition** mà thiếu chức năng, ghi rõ trong SRS công cụ thay thế đã dùng (ví dụ draw.io, Balsamiq, Figma cho wireframe), **các sơ đồ UML/DFD/ERD vẫn bắt buộc vẽ bằng VP**.

---

### D.1 Context Diagram

**Mục đích (Ch.5):** Thể hiện **ranh giới hệ thống** — hệ thống là **một process duy nhất** ở giữa, xung quanh là **external entity** (người dùng, tổ chức, hệ thống ngoài), nối với nhau bằng **data flow** có tên. **Không** thể hiện xử lý bên trong, không có data store.

**Các bước phân tích**

1. Liệt kê mọi **lớp người dùng** và **hệ thống bên ngoài** tương tác với hệ thống → external entity.
2. Với mỗi entity, hỏi: _"Entity này gửi gì vào hệ thống? Nhận gì ra từ hệ thống?"_ → data flow (danh từ: "Thông tin đặt lịch", "Hóa đơn", "Kết quả thanh toán").
3. Gộp các luồng quá chi tiết thành luồng tổng hợp (định nghĩa chi tiết trong data dictionary).
4. Kiểm tra: mỗi data flow ở Context Diagram phải xuất hiện trong ít nhất 1 use case.

**Vẽ trong Visual Paradigm**

1. **Diagram → New → Data Flow Diagram** (nằm trong nhóm _Requirements Modeling_ / _Business Modeling_ tùy phiên bản). Đặt tên `CD-01 Context Diagram`.
2. Từ thanh công cụ chọn **Process** → đặt ở giữa, đặt tên `0 – <Tên hệ thống>`.
3. Chọn **External Entity** → vẽ các entity xung quanh.
4. Dùng **Data Flow** nối entity ↔ process; nhấp đúp vào mũi tên để đặt tên luồng. Một chiều cho mỗi mũi tên; luồng hai chiều vẽ thành 2 mũi tên riêng.
5. Sắp xếp: **Layout → Auto Layout** hoặc kéo tay cho các mũi tên không cắt nhau.

**Bảng mô tả đi kèm (bắt buộc)**

| Data flow | Từ  | Đến | Nội dung (tham chiếu data dictionary) |
| --------- | --- | --- | ------------------------------------- |

**Lỗi thường gặp**

- Vẽ nhiều process bên trong (đó là DFD level 0, không phải context).
- Data flow đặt tên bằng động từ ("Đăng nhập") thay vì dữ liệu ("Thông tin đăng nhập").
- Vẽ data store (CSDL) trong context diagram.
- Bỏ sót hệ thống ngoài (cổng thanh toán, email, SMS, đơn vị vận chuyển).

---

### D.2 Use Case Diagram

**Mục đích (Ch.8):** Thể hiện **ai** (actor) dùng hệ thống để đạt **mục tiêu gì** (use case) và ranh giới hệ thống.

**Các bước phân tích**

1. **Xác định actor** từ context diagram: external entity là người → primary actor; hệ thống ngoài → secondary actor; tác vụ định kỳ → actor `Time`/`Scheduler`.
2. **Xác định use case** cho từng actor: _"Actor này muốn hệ thống giúp đạt được mục tiêu gì?"_ Đặt tên **Động từ + Danh từ** (Đặt lịch khám, Hủy lịch khám).
3. Kiểm tra mức độ: mỗi use case là **một mục tiêu hoàn chỉnh mang lại giá trị**, không phải 1 bước (✗ "Nhấn nút Lưu", ✗ "Nhập mật khẩu").
4. **Include**: hành vi dùng chung **bắt buộc** cho nhiều UC (ví dụ "Xác thực OTP" được include bởi "Thanh toán" và "Đổi mật khẩu").
5. **Extend**: hành vi **tùy chọn / có điều kiện** gắn vào điểm mở rộng của UC gốc (ví dụ "Áp mã giảm giá" extend "Thanh toán").
6. **Generalization**: giữa actor (Nhân viên ← Lễ tân, Bác sĩ) hoặc giữa UC (Thanh toán ← Thanh toán thẻ, Thanh toán ví).
7. Chia **package** theo feature nếu > 15 UC.

**Vẽ trong Visual Paradigm**

1. **Diagram → New → Use Case Diagram**, đặt tên `UCD-01 Overview`.
2. Chọn **System** (hình chữ nhật) → vẽ ranh giới, đặt tên hệ thống.
3. **Actor**: đặt bên ngoài System; primary actor bên trái, secondary actor bên phải.
4. **Use Case**: đặt bên trong System.
5. Nối bằng **Association** (actor–UC), **Include**, **Extend** (UC–UC; mũi tên extend chỉ **từ UC mở rộng về UC gốc**), **Generalization**.
6. Với extend: chọn UC gốc → chuột phải → **Open Specification → Extension Points** để khai báo điểm mở rộng; ghi điều kiện trên quan hệ extend.
7. Đánh ID: chuột phải UC → **Open Specification → General → ID** (hoặc đặt tên dạng `UC-01 Đặt lịch khám`).
8. Tạo sơ đồ con theo package: chuột phải UC/package → **Sub Diagrams → New Diagram**.

**Lỗi thường gặp**

- Vẽ use case như lưu đồ (nối UC theo thứ tự thời gian).
- Dùng include/extend để tách bước nhỏ một cách thừa.
- Đặt "Hệ thống" làm actor.
- Ghi CRUD vào Use case

---

### D.3 Đặc tả Use Case

| Trường                 | Nội dung                                                                                |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **ID & Tên**           | UC-xx: <Động từ + Danh từ>                                                              |
| **Người tạo / Ngày**   | <Họ tên> / <dd/mm/yyyy>                                                                 |
| **Primary actor**      |                                                                                         |
| **Secondary actor(s)** |                                                                                         |
| **Mô tả**              | <1–3 câu: ai, làm gì, để đạt mục tiêu gì>                                               |
| **Trigger**            | <Sự kiện khởi động UC>                                                                  |
| **Preconditions**      | PRE-1: ... ; PRE-2: ...                                                                 |
| **Postconditions**     | POST-1 (thành công): ... ; POST-2: ...                                                  |
| **Normal flow**        | xx.0 <Tên luồng chính> 1. Actor ... 2. Hệ thống ... 3. ...                              |
| **Alternative flows**  | xx.1 <Tên>: Tại bước _n_, nếu ... thì ... ; quay lại bước _m_                           |
| **Exceptions**         | xx.0.E1 <Tên>: Tại bước _n_, nếu ... thì hệ thống ... ; UC kết thúc / quay lại bước _m_ |
| **Priority**           | High / Medium / Low                                                                     |
| **Frequency of use**   | <ví dụ: ~200 lần/ngày>                                                                  |
| **Business rules**     | BR-xx, BR-yy                                                                            |
| **Other information**  | <yêu cầu hiệu năng, bảo mật riêng cho UC>                                               |
| **Assumptions**        |                                                                                         |
| **Màn hình liên quan** | SCR-xx, SCR-yy                                                                          |
| **Sơ đồ liên quan**    | AD-xx, SMD-xx                                                                           |

**Quy tắc viết luồng sự kiện**

- Mỗi bước là **một câu chủ – vị**, chủ ngữ là **Actor** hoặc **Hệ thống**, xen kẽ hành động – phản hồi.
- Không mô tả chi tiết giao diện (✗ "click nút màu xanh"), dùng ngôn ngữ nghiệp vụ (✓ "Khách hàng xác nhận đặt lịch").
- Alternative/Exception phải chỉ rõ **bước rẽ nhánh** và **điểm quay lại/kết thúc**.
- Business rule **không viết lẫn vào luồng**, chỉ tham chiếu ID.
- Mỗi UC sau khi đặc tả phải **sinh ra các Functional Requirement** ở mục 3.x.5.

**Nhập vào Visual Paradigm**

1. Chuột phải UC → **Open Use Case Details…**
2. Tab **Info**: điền Rank/Priority, Primary actor, Preconditions, Postconditions, Description.
3. Tab **Flow of Events**: nhập từng bước; dùng nút _Add Alternate Flow / Exception_ (tên nút có thể khác theo phiên bản) để thêm luồng rẽ nhánh.
4. Tab **Requirements / References**: gắn liên kết tới wireframe, sơ đồ activity.
5. Xuất bằng **Doc. Composer** hoặc copy sang Word, định dạng lại theo bảng trên.

---

### D.4 Phác thảo giao diện (Wireframe / Mockup)

**Mục đích (Ch.15 – Prototype):** Kiểm chứng đặc tả use case, phát hiện dữ liệu/bước còn thiếu. Ở mức **low-fidelity**: bố cục, trường dữ liệu, nút, thông báo — **không** cần màu sắc, logo hoàn chỉnh.

**Yêu cầu**

- Mỗi UC fully dressed có **≥ 1 màn hình chính**; nếu luồng có nhiều bước giao diện → vẽ chuỗi màn hình (storyboard).
- Có ít nhất **1 trạng thái lỗi** (exception) được thể hiện trên wireframe (thông báo lỗi, field highlight).
- Đánh số bước UC tương ứng lên wireframe (callout ①②③) để ánh xạ.

**Vẽ bằng các công cụ Google Stich, FigmaMake, ....**

Export PNG: `UI_UC-xx_<TenManHinh>.png`.

**Bảng mô tả màn hình (bắt buộc kèm mỗi wireframe)**

| #   | Thành phần     | Loại control | Dữ liệu / Nguồn       | Bắt buộc | Ràng buộc / Validation      | Hành động        |
| --- | -------------- | ------------ | --------------------- | -------- | --------------------------- | ---------------- |
| 1   | Ngày khám      | Date picker  | Lịch trống của bác sĩ | Có       | ≥ ngày hiện tại + 1 (BR-03) | —                |
| 2   | Nút "Xác nhận" | Button       | —                     | —        | Chỉ bật khi đủ field        | Bước 5 của UC-05 |

**Lỗi thường gặp**

- Wireframe có field không xuất hiện trong ERD/data dictionary (hoặc ngược lại).
- Wireframe không thể hiện nhánh lỗi.
- Thiết kế quá chi tiết về màu sắc thay vì tập trung nội dung.

---

### D.5 Activity Diagram có Swimlane

**Mục đích:** Mô tả **quy trình nghiệp vụ liên quan nhiều vai trò**, ai làm bước nào, điểm quyết định và luồng song song. Thường dùng cho quy trình xuyên suốt **nhiều use case** (ví dụ từ đặt lịch → khám → thanh toán).

**Các bước phân tích**

1. Chọn quy trình có **≥ 3 vai trò** (gồm cả "Hệ thống" và/hoặc hệ thống ngoài).
2. Liệt kê các hành động theo thứ tự, gán vào vai trò thực hiện.
3. Xác định **điểm quyết định** (điều kiện guard `[đủ hàng]`, `[không đủ hàng]`), **điểm hợp nhất**, **bước song song** (gửi email đồng thời với cập nhật kho).
4. Xác định điểm bắt đầu và (các) điểm kết thúc.
5. Đối chiếu với normal flow + alternative flow của các UC liên quan.

**Vẽ trong Visual Paradigm**

1. **Diagram → New → Activity Diagram**, tên `AD-01 <Tên quy trình>`.
2. Chọn **Vertical Swimlane** (hoặc Horizontal) → thêm partition: chuột phải swimlane → _Add Partition_; đặt tên theo actor/vai trò.
3. Thêm **Initial Node**, **Action** (tên: động từ + danh từ), **Decision Node** (ghi guard trên từng nhánh ra), **Merge Node**, **Fork / Join Node** (thanh ngang đen), **Activity Final Node**, **Flow Final Node** (nếu một nhánh kết thúc riêng).
4. Nối bằng **Control Flow**; luồng đối tượng (tùy chọn) dùng **Object Node** (ví dụ `Đơn hàng [Đã thanh toán]`) — tên trạng thái trong ngoặc vuông nên khớp SMD.
5. Đặt mỗi action đúng swimlane của người thực hiện.

**Lỗi thường gặp**

- Decision không ghi guard hoặc guard không loại trừ nhau / không bao phủ hết.
- Fork không có Join tương ứng (hoặc dùng Join cho nhánh của Decision).
- Tất cả action dồn vào lane "Hệ thống".
- Tên action là danh từ hoặc là màn hình.

---

### D.6 State Machine Diagram

**Mục đích:** Mô tả **vòng đời của một đối tượng nghiệp vụ**: các trạng thái, sự kiện gây chuyển trạng thái, điều kiện và hành động kèm theo. Giúp phát hiện chuyển trạng thái **bị thiếu hoặc không được phép**.

**Các bước phân tích**

1. Chọn đối tượng có vòng đời rõ (Đơn hàng, Lịch hẹn, Hồ sơ, Khiếu nại, Tài khoản…).
2. Liệt kê **tất cả trạng thái** (tính từ/phân từ: _Chờ xác nhận, Đã xác nhận, Đang xử lý, Hoàn tất, Đã hủy_).
3. Lập **bảng chuyển trạng thái** (state table) trước khi vẽ:

| Trạng thái hiện tại | Event                | Guard     | Action             | Trạng thái kế |
| ------------------- | -------------------- | --------- | ------------------ | ------------- |
| Chờ xác nhận        | Nhân viên xác nhận   | [còn chỗ] | Gửi email xác nhận | Đã xác nhận   |
| Chờ xác nhận        | Hết 24h (time event) | —         | Giải phóng slot    | Đã hủy        |

4. Kiểm tra: mỗi trạng thái **đến được** từ trạng thái đầu; trạng thái không phải kết thúc **đều có lối ra**; mọi cặp (state, event) được xử lý hoặc ghi rõ "bỏ qua".
5. Đối chiếu: mỗi transition phải tương ứng với **một UC hoặc một bước trong UC**, hoặc tác vụ tự động.

**Vẽ trong Visual Paradigm**

1. **Diagram → New → State Machine Diagram**, tên `SMD-01 <Tên đối tượng>`.
2. Thêm **Initial Pseudo State**, các **State**, **Final State**.
3. Nối bằng **Transition**; mở _Specification_ của transition để nhập **Trigger** (event), **Guard**, **Effect** (action) → hiển thị dạng `event [guard] / action`.
4. Hành động trong trạng thái: chuột phải State → _Add → Entry / Do / Exit_ (ví dụ `entry / gửi thông báo`).
5. Trạng thái phức hợp (composite state) nếu có trạng thái con (ví dụ _Đang giao_ gồm _Đã lấy hàng_, _Đang vận chuyển_).
6. Time event: trigger dạng `after(24h)` hoặc `when(ngày hẹn qua)`.

**Lỗi thường gặp**

- Nhầm trạng thái với hành động ("Thanh toán" là hành động; "Đã thanh toán" là trạng thái).
- Thiếu nhánh hủy/hoàn tiền/hết hạn.
- Trạng thái "chết" không có lối ra (ngoài Final).
- Tên trạng thái khác với tên trong ERD (thuộc tính `TrangThai`), wireframe, activity diagram.

---

### D.7 ERD mức khái niệm

**Mục đích:** Mô tả các **thực thể dữ liệu nghiệp vụ** và **mối quan hệ** giữa chúng, ở mức **khái niệm** — **chưa** cần kiểu dữ liệu, khóa ngoại, bảng trung gian vật lý.

**Mức khái niệm gồm**

- Thực thể (danh từ số ít: Khách hàng, Lịch hẹn, Bác sĩ…).
- Quan hệ có **tên** (động từ: _đặt_, _phụ trách_, _thuộc_).
- **Cardinality** ở 2 đầu (1..1, 0..1, 0.._, 1.._), ký pháp Crow's Foot.
- (Tùy chọn) thuộc tính định danh và một vài thuộc tính chính.

**Các bước phân tích**

1. Gạch chân **danh từ** trong use case, business rule, wireframe, báo cáo → ứng viên thực thể.
2. Loại bỏ: danh từ là actor nhưng không cần lưu thông tin, giá trị đơn lẻ (→ thuộc tính), từ đồng nghĩa (đối chiếu glossary).
3. Xác định quan hệ & cardinality bằng câu hỏi hai chiều: _"Một Khách hàng có thể có bao nhiêu Lịch hẹn? Một Lịch hẹn thuộc về bao nhiêu Khách hàng?"_
4. Quan hệ N–N: ghi rõ ở mức khái niệm, hoặc tách **thực thể kết hợp** nếu quan hệ có thuộc tính riêng (Đơn hàng – Sản phẩm → Chi tiết đơn hàng: số lượng, đơn giá).
5. Kiểm tra với CRUD matrix: mỗi thực thể phải có ít nhất 1 UC **tạo (C)** và 1 UC **đọc (R)**.

**CRUD matrix (đính kèm)**

| UC \ Entity    | Khách hàng | Lịch hẹn | Bác sĩ | Hóa đơn | ... |
| -------------- | ---------- | -------- | ------ | ------- | --- |
| UC-01 Đăng ký  | C          |          |        |         |     |
| UC-05 Đặt lịch | R          | C        | R      |         |     |

**Vẽ trong Visual Paradigm**

1. **Diagram → New → Entity Relationship Diagram**, tên `ERD-01 Conceptual`. Nếu phiên bản hỗ trợ, chọn mức **Conceptual Model** (VP Standard trở lên có tùy chọn Conceptual / Logical / Physical); nếu không, dùng ERD thường và **chỉ ghi tên thực thể + thuộc tính khóa**, không ghi kiểu dữ liệu.
2. Thêm **Entity**, đặt tên.
3. Dùng **Relationship** (One-to-One / One-to-Many / Many-to-Many); mở _Specification_ để đặt **tên quan hệ** và **cardinality** từng đầu (Zero or One / Exactly One / Zero or Many / One or Many).
4. Bật hiển thị Crow's Foot: chuột phải nền → _Presentation Options → Relationship Notation → Crow's Foot_ (nếu chưa mặc định).
5. Tránh để VP tự sinh cột khóa ngoại ở mức khái niệm (bỏ chọn các cột FK được tự thêm nếu có).

**Bảng mô tả thực thể (bắt buộc)**

| Thực thể | Mô tả | Thuộc tính chính | Liên quan BR / UC |
| -------- | ----- | ---------------- | ----------------- |

**Lỗi thường gặp**

- Vẽ actor "Hệ thống", "Admin" thành entity khi không cần lưu.
- Thiếu cardinality ở một đầu hoặc quan hệ không có tên.
- Đưa kiểu dữ liệu, FK, bảng trung gian vật lý vào mô hình khái niệm.
- Thực thể trên ERD không khớp field trên wireframe/data dictionary.

---

### D.8 Kiểm tra nhất quán giữa các mô hình

| Kiểm tra                                                       | Mô hình A        | Mô hình B           |
| -------------------------------------------------------------- | ---------------- | ------------------- |
| Mỗi external entity (người) là actor và ngược lại              | Context Diagram  | Use Case Diagram    |
| Mỗi data flow được xử lý bởi ≥ 1 UC                            | Context Diagram  | Đặc tả UC           |
| Mỗi bước tương tác của normal flow có thành phần trên màn hình | Đặc tả UC        | Wireframe           |
| Mỗi field trên màn hình có trong thực thể / data dictionary    | Wireframe        | ERD, Mục 4.2        |
| Mỗi swimlane là actor / hệ thống có trong UCD                  | Activity Diagram | Use Case Diagram    |
| Tên trạng thái trên object node trùng tên state                | Activity Diagram | State Machine       |
| Mỗi transition có UC hoặc tác vụ tự động gây ra                | State Machine    | Đặc tả UC           |
| Đối tượng có SMD là thực thể có thuộc tính trạng thái          | State Machine    | ERD                 |
| Mọi thuật ngữ dùng thống nhất                                  | Tất cả           | Glossary            |
| Mọi UC truy vết tới ≥ 1 BO và ≥ 1 FR                           | UC list          | Traceability Matrix |

---

## Phần E – Tiêu chí chấm điểm (Rubric)

| #   | Tiêu chí                                                            | Điểm   | Mức tốt (đạt tối đa)                                                           |
| --- | ------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------ |
| 1   | Giới thiệu, phạm vi, business objective, user class, business rules | 1.0    | BO đo được; phạm vi in/out rõ; BR phân loại đúng                               |
| 2   | Context Diagram                                                     | 1.0    | Đúng ký pháp, 1 process, entity & data flow đầy đủ, có bảng mô tả              |
| 3   | Use Case Diagram                                                    | 1.5    | Đủ actor/UC, tên đúng chuẩn, include/extend/generalization dùng đúng ngữ nghĩa |
| 4   | Đặc tả Use Case                                                     | 2.0    | Đủ trường template, luồng rõ ràng, alternative/exception đầy đủ, tham chiếu BR |
| 5   | Wireframe                                                           | 1.0    | Ánh xạ được với luồng UC, có trạng thái lỗi, có bảng mô tả field               |
| 6   | Activity Diagram swimlane                                           | 1.0    | Đúng ký pháp, guard đầy đủ, fork/join đúng, đúng lane                          |
| 7   | State Machine Diagram                                               | 0.75   | Đủ trạng thái, `event [guard] / action` rõ, không có trạng thái chết           |
| 8   | ERD khái niệm + Data dictionary                                     | 0.75   | Đủ thực thể, quan hệ có tên & cardinality, khớp wireframe                      |
| 9   | NFR, giao diện ngoài                                                | 0.5    | NFR đo được, có Planguage                                                      |
| 10  | Truy vết & nhất quán giữa mô hình                                   | 0.5    | Ma trận truy vết đầy đủ, qua được checklist D.8                                |
|     | **Tổng**                                                            | **10** |                                                                                |

**Trừ điểm**

- Không nộp file `.vpp` hoặc sơ đồ không vẽ bằng Visual Paradigm: **−2.0**
- Sao chép giữa các nhóm / từ nguồn khác không trích dẫn: **0 điểm** phần liên quan và xử lý theo quy chế.
- Câu yêu cầu mơ hồ (dùng từ "nhanh", "dễ dùng", "thân thiện", "v.v." mà không định lượng): **−0.1/lỗi**, tối đa −1.0.
- Thành viên không có đóng góp ghi nhận trong `05_TeamWork.xlsx`: điểm cá nhân có thể bị điều chỉnh.

---

## Phần F – Checklist trước khi nộp

**Tài liệu SRS**

- [ ] Đủ các mục 1–8 và Phụ lục A–D theo template; mục không áp dụng có ghi lý do.
- [ ] Mọi yêu cầu có ID duy nhất, có mức ưu tiên.
- [ ] Không còn từ mơ hồ (Bảng 11-2): _nhanh, dễ, linh hoạt, tối ưu, hỗ trợ, v.v., ..._ chưa định lượng.
- [ ] Mỗi NFR có cách đo / kiểm chứng.
- [ ] Glossary có đầy đủ thuật ngữ nghiệp vụ, không dùng từ đồng nghĩa lẫn lộn.

**Mô hình**

- [ ] Context Diagram: 1 process, ≥ 5 entity, data flow có tên (danh từ).
- [ ] UCD: ≥ 20 UC, tên Động từ + Danh từ, include/extend đúng hướng.
- [ ] Mỗi UC fully dressed có wireframe + bảng mô tả field.
- [ ] ≥ 3 Activity Diagram swimlane, ≥ 2 State Machine Diagram, 1 ERD khái niệm.
- [ ] Qua toàn bộ bảng kiểm tra nhất quán D.8.
- [ ] Ảnh export rõ nét, chèn đúng vị trí trong SRS, có chú thích `Hình x – <ID> <Tên>`.

**File nộp**

- [ ] Đúng cấu trúc thư mục A.3, đúng quy ước đặt tên.
- [ ] File `.vpp` mở được, chứa đầy đủ các sơ đồ.
- [ ] Ma trận truy vết & bảng phân công đã hoàn thiện.

---

## Phụ lục 1 – Gợi ý đề tài

| #   | Đề tài                               | Đối tượng có vòng đời (cho SMD)     | Quy trình nhiều bên (cho AD swimlane)                     | Hệ thống ngoài                    |
| --- | ------------------------------------ | ----------------------------------- | --------------------------------------------------------- | --------------------------------- |
| 1   | Đặt lịch khám & quản lý phòng khám   | Lịch hẹn, Hóa đơn                   | Đặt lịch → Tiếp đón → Khám → Thanh toán → Lấy thuốc       | Cổng thanh toán, SMS, Bảo hiểm    |
| 2   | Cho thuê xe tự lái                   | Hợp đồng thuê, Xe                   | Đặt xe → Kiểm tra giấy tờ → Giao xe → Trả xe → Quyết toán | eKYC, Thanh toán, GPS             |
| 3   | Quản lý ký túc xá                    | Đơn đăng ký phòng, Yêu cầu sửa chữa | Đăng ký → Duyệt → Xếp phòng → Đóng phí                    | Hệ thống SV của trường, Ngân hàng |
| 4   | Đặt sân thể thao                     | Booking, Sân                        | Đặt sân → Đặt cọc → Check-in → Thanh toán còn lại         | Ví điện tử, Bản đồ                |
| 5   | Quản lý sự kiện & bán vé             | Vé, Sự kiện                         | Tạo sự kiện → Duyệt → Mở bán → Check-in QR                | Thanh toán, Email                 |
| 6   | Tuyển dụng nội bộ                    | Hồ sơ ứng tuyển, Tin tuyển dụng     | Đăng tin → Nộp CV → Sàng lọc → Phỏng vấn → Offer          | Email, Lịch (Calendar)            |
| 7   | Giao đồ ăn cho căng tin trường       | Đơn món                             | Đặt món → Bếp nhận → Chế biến → Giao → Xác nhận           | Ví điện tử, Push notification     |
| 8   | Quản lý bảo hành – sửa chữa thiết bị | Phiếu bảo hành                      | Tiếp nhận → Chẩn đoán → Báo giá → Sửa → Trả máy           | Hãng sản xuất, SMS                |

---

## Phụ lục 2 – Ví dụ minh họa ngắn (ClinicCare)

> Chỉ minh họa **mức độ chi tiết mong đợi**, sinh viên **không** sao chép.

**Business rule**

- BR-03: Khách hàng chỉ được đặt lịch trước **tối thiểu 1 ngày** và **tối đa 30 ngày**.
- BR-04: Lịch hẹn ở trạng thái _Chờ xác nhận_ quá **24 giờ** sẽ tự động bị hủy.

**Đặc tả UC-05: Đặt lịch khám (rút gọn)**

| Trường          | Nội dung                                                                                                                                                                                                                                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary actor   | Bệnh nhân                                                                                                                                                                                                                                                                                                |
| Secondary actor | Dịch vụ SMS                                                                                                                                                                                                                                                                                              |
| Trigger         | Bệnh nhân chọn chức năng đặt lịch khám                                                                                                                                                                                                                                                                   |
| Preconditions   | PRE-1: Bệnh nhân đã đăng nhập                                                                                                                                                                                                                                                                            |
| Postconditions  | POST-1: Lịch hẹn được tạo ở trạng thái _Chờ xác nhận_; slot bác sĩ bị giữ                                                                                                                                                                                                                                |
| Normal flow     | 1. Bệnh nhân chọn chuyên khoa. 2. Hệ thống hiển thị danh sách bác sĩ của chuyên khoa. 3. Bệnh nhân chọn bác sĩ và ngày khám. 4. Hệ thống hiển thị các khung giờ còn trống (BR-03). 5. Bệnh nhân chọn khung giờ, nhập triệu chứng và xác nhận. 6. Hệ thống tạo lịch hẹn, giữ slot và gửi SMS mã lịch hẹn. |
| Alternative     | 5.1 Bệnh nhân chọn "Bác sĩ bất kỳ": hệ thống tự gán bác sĩ còn trống sớm nhất; quay lại bước 6.                                                                                                                                                                                                          |
| Exceptions      | 4.E1 Không còn khung giờ trống: hệ thống thông báo và đề xuất 3 ngày gần nhất còn trống; quay lại bước 3. 6.E1 Slot vừa bị người khác đặt: hệ thống thông báo, quay lại bước 4. 6.E2 Gửi SMS thất bại: lịch hẹn vẫn được tạo, hệ thống hiển thị mã lịch hẹn trên màn hình và thử gửi lại sau 5 phút.     |
| Business rules  | BR-03                                                                                                                                                                                                                                                                                                    |
| Màn hình        | SCR-05 Đặt lịch khám                                                                                                                                                                                                                                                                                     |

**Bảng chuyển trạng thái – Lịch hẹn (rút gọn)**

| Từ                         | Event [guard] / action                               | Đến          |
| -------------------------- | ---------------------------------------------------- | ------------ |
| ● (initial)                | Bệnh nhân đặt lịch / giữ slot                        | Chờ xác nhận |
| Chờ xác nhận               | Lễ tân xác nhận / gửi SMS                            | Đã xác nhận  |
| Chờ xác nhận               | after(24h) / giải phóng slot (BR-04)                 | Đã hủy       |
| Đã xác nhận                | Bệnh nhân hủy [trước giờ hẹn ≥ 4h] / giải phóng slot | Đã hủy       |
| Đã xác nhận                | Lễ tân check-in                                      | Đang khám    |
| Đã xác nhận                | Quá giờ hẹn 30 phút [chưa check-in]                  | Vắng mặt     |
| Đang khám                  | Bác sĩ hoàn tất / tạo hóa đơn                        | Hoàn tất     |
| Hoàn tất, Đã hủy, Vắng mặt | —                                                    | ◉ (final)    |

**Swimlane gợi ý cho AD-01 "Khám bệnh"**: _Bệnh nhân | Lễ tân | Bác sĩ | Hệ thống | Cổng thanh toán_ — có fork sau "Bác sĩ hoàn tất khám" chạy song song "Tạo hóa đơn" và "Gửi đơn thuốc sang quầy thuốc", join trước "Bệnh nhân thanh toán".

**ERD khái niệm (dạng chữ)**

```
BỆNH NHÂN  1 ──── đặt ──── 0..*  LỊCH HẸN
BÁC SĨ     1 ──── phụ trách ── 0..*  LỊCH HẸN
CHUYÊN KHOA 1 ─── gồm ──── 1..*  BÁC SĨ
LỊCH HẸN   1 ──── phát sinh ── 0..1  HÓA ĐƠN
LỊCH HẸN   1 ──── có ──── 0..1  ĐƠN THUỐC
ĐƠN THUỐC  0..* ── chứa ── 1..*  THUỐC   (N–N → CHI TIẾT ĐƠN THUỐC: liều lượng, số lượng)
```

---

_Chúc các nhóm hoàn thành tốt assignment._
