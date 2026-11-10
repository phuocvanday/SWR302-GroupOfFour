# Hướng dẫn làm bài SWR302 — Gym Management System (GMS)

> **Gửi cả nhóm:** Phước · Anh Tuấn · Thiên · Huy  
> Đọc file này + mở link GitHub của mình → biết ngay việc phải làm.

|                          | Link                                                                          |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Repo**                 | https://github.com/phuocvanday/SWR302-GroupOfFour                             |
| **Clone**                | `git clone https://github.com/phuocvanday/SWR302-GroupOfFour.git`             |
| **Project board**        | https://github.com/users/phuocvanday/projects/3                               |
| **Issues (tất cả)**      | https://github.com/phuocvanday/SWR302-GroupOfFour/issues                      |
| **Việc của TÔI**         | https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/            |
| **Milestones**           | https://github.com/phuocvanday/SWR302-GroupOfFour/milestones                  |
| **File này trên GitHub** | https://github.com/phuocvanday/SWR302-GroupOfFour/blob/main/HUONG_DAN_NHOM.md |

**Đề tài:** Gym Management System (GMS)  
**Công cụ vẽ bắt buộc:** Visual Paradigm Community  
**Chuẩn chữ SRS:** Times New Roman 13, Multiple 1.3  
**Đề / rubric:** `docs/HuongDan_Assignment.md`  
**Ý tưởng gốc:** `docs/kimi2.5-project.md`

**Tiến độ hiện tại:** đang **Bước 0 → Bước 1** (Vision & Scope). Chưa sang Bước 2.

---

## 0. Đọc 5 phút — làm ngay hôm nay

1. Mở **[Việc của tôi](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/)** (đăng nhập đúng tài khoản GitHub của mình).
2. Làm issue **Bước 0** trước (setup), rồi **Bước 1**.
3. Commit trên nhánh **`step-0` / `step-1`** (một nhánh / bước — xem §4.2), rồi **đóng issue**.
4. Khi cả nhóm xong: đóng issue `[Checklist nhóm]` → Leader **merge vào `main`** → mới sang bước sau.

### Tài khoản GitHub đã gán issue

| Thành viên         | GitHub            | Link việc của bạn                                                                                   |
| ------------------ | ----------------- | --------------------------------------------------------------------------------------------------- |
| **Phước** (Leader) | `@phuocvanday`    | [Issues assigned](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/phuocvanday)    |
| **Anh Tuấn**       | `@teafromhand-vn` | [Issues assigned](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/teafromhand-vn) |
| **Thiên**          | `@ngthien05`      | [Issues assigned](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/ngthien05)      |
| **Huy**            | `@Huyd06`         | [Issues assigned](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/Huyd06)         |

Issue **Checklist nhóm** / **All** được gán **cả 4 người**.  
Issue **AD-03** gán Phước + Thiên.

---

## 1. Tổng số bước hoàn thành bài

|                  | Số           | Ghi chú                                |
| ---------------- | ------------ | -------------------------------------- |
| **Nội dung bài** | **8 bước**   | Theo đề HuongDan §A.4 — làm đủ mới nộp |
| Setup            | + **Bước 0** | Clone, đọc đề, điền MSSV, cài VP       |

```
Bước 0  Setup GitHub + Visual Paradigm
Bước 1  Vision & Scope                 → Mục 1–2 SRS
Bước 2  Context Diagram + UC list
Bước 3  Use Case Diagram + BR + Glossary
Bước 4  Đặc tả Use Case (fully dressed)
Bước 5  Wireframe / Mockup
Bước 6  Activity Diagram (swimlane)
Bước 7  State Machine + ERD + Data dictionary
Bước 8  NFR + Traceability + peer review + đóng gói nộp
```

Trên GitHub đã có **9 milestones** (Bước 0→8) và **42 issues** (mỗi bước: việc từng người + checklist nhóm).

---

## 2. Phân công cố định cả kỳ

| Thành viên   | GitHub            | Domain                                      | UC fully dressed | Sơ đồ chủ trì                 |
| ------------ | ----------------- | ------------------------------------------- | ---------------- | ----------------------------- |
| **Phước**    | `@phuocvanday`    | Membership quầy, ghép SRS, CD, Traceability | **UC-05, UC-06** | CD-01, Traceability, đóng gói |
| **Anh Tuấn** | `@teafromhand-vn` | PT Booking                                  | **UC-11, UC-12** | UCD package PT, AD-01         |
| **Thiên**    | `@ngthien05`      | QR Check-in, buổi tập                       | **UC-08, UC-15** | SMD-01, SMD-02                |
| **Huy**      | `@Huyd06`         | Duyệt PT, báo cáo, NFR, Feedback            | **UC-16, UC-17** | ERD-01, AD-02, NFR            |

### Nguyên tắc nhóm

1. **Mỗi người tự làm phần được giao** — không nhờ một người / AI làm hết rồi đứng tên.
2. Leader **ghép & review**, không viết thay phần chuyên môn của người khác.
3. Mọi đóng góp ghi vào `05_TeamWork.xlsx` (không ghi → điểm cá nhân có thể bị trừ).
4. File trong `docs/` = nháp làm việc; **bản nộp chính** = SRS + Models + Images + xlsx.

---

## 3. Cấu trúc repo & sản phẩm nộp cuối

```
SWR302-GroupOfFour/
├── HUONG_DAN_NHOM.md              ← File hướng dẫn này
├── 01_SRS_GMS.docx                ← SRS chính (nộp)
├── 02_Models/
│   └── GMS.vpp                    ← Visual Paradigm (BẮT BUỘC)
├── 03_Images/                     ← PNG ≥ 150 dpi export từ VP
├── 04_Traceability_Matrix.xlsx
├── 05_TeamWork.xlsx
└── docs/                          ← Nháp / nguồn tham khảo
    ├── step1/ … step8/            ← Mỗi người nộp nháp theo bước
    ├── HuongDan_Assignment.md
    ├── kimi2.5-project.md
    └── 01_Vision_Scope_GMS.md     ← NHÁP tham khảo (chưa chốt)
```

**Zip nộp GV (cuối Bước 8):** `<MaNhom>_SWR302_Assignment.zip` đúng cấu trúc A.3.

---

## 4. Quy trình GitHub (bắt buộc)

### 4.1 Lần đầu

```bash
git clone https://github.com/phuocvanday/SWR302-GroupOfFour.git
cd SWR302-GroupOfFour
git pull
```

Mở folder trong Cursor / VS Code. Cài **Visual Paradigm Community**.

### 4.2 Chiến lược nhánh (bắt buộc theo nhóm)

**Một nhánh cho một bước** — không tạo nhánh theo từng issue / từng người sống dài (dễ rối).

| Loại | Tên nhánh | Ai dùng |
|------|-----------|---------|
| Chính | `main` | Bản đã chốt từng bước (sau khi đóng checklist nhóm) |
| Theo bước | `step-0` … `step-8` | **Cả 4 người** commit phần mình vào **cùng** nhánh bước đang làm |

**Không làm:** nhánh kiểu `step1/huy-vision`, `step2/tuan-uc-df`… (đã bỏ trên remote).

#### Bắt đầu một bước (Leader tạo 1 lần)

```bash
git checkout main
git pull
git checkout -b step-1
git push -u origin step-1
```

(Đổi `step-1` thành `step-2` … khi sang bước mới. Bước 0 dùng `step-0`.)

#### Thành viên làm việc trên nhánh bước

```bash
git fetch
git checkout step-1
git pull
# ... sửa file của mình ...
git add <file-của-mình>
git commit -m "[Bước 1][Tên] mô tả ngắn"
git push
```

#### Đóng bước → về `main` (Leader hoặc người được cử)

Khi issue **Checklist nhóm** đã đóng:

```bash
git checkout main
git pull
git merge step-1
git push
# (tuỳ chọn) xóa nhánh bước trên remote sau khi merge ổn
git push origin --delete step-1
```

**Word / Excel:** nhánh **không** tránh được conflict `.docx`/`.xlsx`. Trước khi sửa SRS hoặc TeamWork → **báo nhóm chat**; một lúc chỉ **một người** sửa file đó.

### 4.3 Làm 1 issue như thế nào?

1. Mở issue được **assign** cho mình → đọc checklist.
2. Checkout đúng nhánh bước đang làm (`step-N`), rồi `git pull`.
3. Làm phần mình (`docs/stepN/` hoặc sơ đồ VP).
4. **Báo nhóm** trước khi sửa `01_SRS_GMS.docx` / Excel.
5. Commit + push lên **`step-N`** (không tạo nhánh riêng lung tung).
6. Tick checklist trong issue → **Close issue**.
7. Cả nhóm xong → đóng **`[Checklist nhóm]`** → Leader **merge `step-N` → `main`**.

### 4.4 Message commit (đúng mẫu)

```
[Bước N][Tên] mô tả ngắn

Ví dụ:
[Bước 0][Thiên] điền MSSV TeamWork
[Bước 1][Tuấn] user class PT + BO-03 + glossary
[Bước 2][Phước] CD-01 + export PNG
[Bước 4][Huy] đặc tả UC-16, UC-17
```

---

## 5. Chi tiết từng bước + issue GitHub

> Chi tiết đầy đủ cũng nằm **trong từng issue** trên GitHub. Dưới đây là bản tóm để đọc offline.

---

### Bước 0 — Setup

**Milestone:** [Bước 0 — Setup](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/1)

| Ai    | Việc                                 | Issue (mở trên GitHub)                                                     |
| ----- | ------------------------------------ | -------------------------------------------------------------------------- |
| Cả 4  | Clone, đọc hướng dẫn + đề, cài VP    | [#2 All Setup](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/2) |
| Phước | TeamWork + mã nhóm/lớp/GV + deadline | [#3](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/3)           |
| Cả 4  | Checklist đóng bước                  | [#4](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/4)           |

**Checklist cá nhân:** clone OK · đọc HuongDan A.1–A.4 · điền MSSV + push · VP mở được  
**Checklist nhóm:** đủ 4 MSSV · `git pull` được

---

### Bước 1 — Vision & Scope (Mục 1–2 SRS)

**Milestone:** [Bước 1](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/2)  
**Nháp tham khảo:** `docs/01_Vision_Scope_GMS.md` (phải tự viết/chốt phần mình, không copy mù)

| Ai        | Việc                                                                | Nộp                          | Issue                                                            |
| --------- | ------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------- |
| **Phước** | Trang bìa, §1.1–1.2, ghép BO/Scope vào SRS                          | `01_SRS_GMS.docx`, TeamWork  | [#5](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/5) |
| **Tuấn**  | User class PT, scope PT, **BO-03**, glossary PT                     | `docs/step1/tuan_vision.md`  | [#6](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/6) |
| **Thiên** | User class Customer, scope Membership/QR, **BO-01/02**, assumptions | `docs/step1/thien_vision.md` | [#7](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/7) |
| **Huy**   | User class Owner, §2.3–2.4, **BO-04**, references                   | `docs/step1/huy_vision.md`   | [#8](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/8) |
| Cả 4      | Checklist đóng Vision                                               | —                            | [#9](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/9) |

**Cách nộp Bước 1:** mỗi người push file `docs/step1/...` → họp 15–30' chốt số đo BO → Phước ghép SRS Mục 1–2.

**⛔ Chưa đóng #9 → không sang Bước 2.**

---

### Bước 2 — Context Diagram + UC list

**Milestone:** [Bước 2](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/3)

| Ai        | Việc                                                           | Issue                                                              |
| --------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Phước** | Vẽ CD-01 (≥5 entity, ≥12 DF), `GMS.vpp`, PNG, SRS §2.1         | [#10](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/10) |
| **Tuấn**  | DF + UC domain PT → `docs/step2/tuan_uc_df.md`                 | [#11](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/11) |
| **Thiên** | DF + UC Membership/QR → `docs/step2/thien_uc_df.md`            | [#12](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/12) |
| **Huy**   | DF + UC Owner/Report/Feedback/Time → `docs/step2/huy_uc_df.md` | [#13](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/13) |
| Cả 4      | Checklist                                                      | [#14](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/14) |

Tham khảo khung (chưa phải bản chốt): `docs/02_Context_Diagram_DataFlows.md`, `docs/02_UC_List_Detailed.md`.

---

### Bước 3 — UCD + BR + Glossary

**Milestone:** [Bước 3](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/4)

| Ai        | Việc                                             | Issue                                                              |
| --------- | ------------------------------------------------ | ------------------------------------------------------------------ |
| **Phước** | UCD-01 Overview + Membership + ghép SRS          | [#15](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/15) |
| **Tuấn**  | UCD package PT + include/extend                  | [#16](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/16) |
| **Thiên** | UCD Membership chi tiết                          | [#17](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/17) |
| **Huy**   | UCD Report/Feedback + bảng BR + Glossary         | [#18](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/18) |
| Cả 4      | Checklist (≥2 include, ≥2 extend, ≥1 actor gen.) | [#19](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/19) |

> Confirm/Reject là **alternative flow trong UC-12**, **không** dùng `<<extend>>`.

---

### Bước 4 — Đặc tả Use Case (≥2 UC / người)

**Milestone:** [Bước 4](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/5)

| Ai        | UC           | Issue                                                              |
| --------- | ------------ | ------------------------------------------------------------------ |
| **Phước** | UC-05, UC-06 | [#20](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/20) |
| **Tuấn**  | UC-11, UC-12 | [#21](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/21) |
| **Thiên** | UC-08, UC-15 | [#22](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/22) |
| **Huy**   | UC-16, UC-17 | [#23](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/23) |
| Cả 4      | Checklist    | [#24](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/24) |

Nộp nháp: `docs/step4/UC-xx.md` → ghép SRS Mục 3. Mỗi UC: main + ≥1 alt + ≥1 exception.

---

### Bước 5 — Wireframe

**Milestone:** [Bước 5](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/6)

| Ai        | UI cho UC    | Issue                                                              |
| --------- | ------------ | ------------------------------------------------------------------ |
| **Phước** | UC-05, UC-06 | [#25](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/25) |
| **Tuấn**  | UC-11, UC-12 | [#26](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/26) |
| **Thiên** | UC-08, UC-15 | [#27](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/27) |
| **Huy**   | UC-16, UC-17 | [#28](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/28) |
| Cả 4      | Checklist    | [#29](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/29) |

File: `03_Images/UI_UC-xx_TenManHinh.png` + bảng field + trạng thái lỗi.

---

### Bước 6 — Activity Diagram

**Milestone:** [Bước 6](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/7)

| Ai                | Sơ đồ                           | Issue                                                              |
| ----------------- | ------------------------------- | ------------------------------------------------------------------ |
| **Tuấn**          | AD-01 Đặt gói PT & thanh toán   | [#30](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/30) |
| **Huy**           | AD-02 Đăng ký & duyệt PT        | [#31](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/31) |
| **Phước + Thiên** | AD-03 Kích hoạt membership quầy | [#32](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/32) |
| Cả 4              | Checklist (≥3 AD, ≥3 lane)      | [#33](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/33) |

---

### Bước 7 — SMD + ERD + Data dictionary

**Milestone:** [Bước 7](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/8)

| Ai        | Việc                                           | Issue                                                              |
| --------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| **Thiên** | SMD-01 Membership + SMD-02 PT Booking          | [#34](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/34) |
| **Huy**   | ERD-01 ≥10 entity + data dictionary            | [#35](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/35) |
| **Tuấn**  | Bổ sung ERD Booking–PT–Session + review SMD-02 | [#36](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/36) |
| **Phước** | Chèn SRS Mục 4 + Traceability sơ bộ            | [#37](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/37) |
| Cả 4      | Checklist                                      | [#38](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/38) |

---

### Bước 8 — NFR + Traceability + nộp

**Milestone:** [Bước 8](https://github.com/phuocvanday/SWR302-GroupOfFour/milestone/9)

| Ai        | Việc                                     | Issue                                                              |
| --------- | ---------------------------------------- | ------------------------------------------------------------------ |
| **Huy**   | NFR đo được + giao diện ngoài            | [#39](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/39) |
| **Phước** | Traceability Matrix + zip nộp A.3        | [#40](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/40) |
| **Tuấn**  | Peer review PT (UCD/AD/đặc tả)           | [#41](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/41) |
| **Thiên** | Peer review SMD + Check-in + CD          | [#42](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/42) |
| Cả 4      | TeamWork % đóng góp + checklist nộp cuối | [#43](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/43) |

---

## 6. Bảng tiến độ (tick khi đóng checklist nhóm)

| Bước | Tên                 | Checklist issue                                                    | Done? |
| ---- | ------------------- | ------------------------------------------------------------------ | ----- |
| 0    | Setup               | [#4](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/4)   | ☐     |
| 1    | Vision & Scope      | [#9](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/9)   | ☐     |
| 2    | CD + UC list        | [#14](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/14) | ☐     |
| 3    | UCD + BR + Glossary | [#19](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/19) | ☐     |
| 4    | Đặc tả UC           | [#24](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/24) | ☑     |
| 5    | Wireframe           | [#29](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/29) | ☐     |
| 6    | Activity            | [#33](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/33) | ☐     |
| 7    | SMD + ERD           | [#38](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/38) | ☐     |
| 8    | NFR + nộp           | [#43](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/43) | ☐     |

---

## 7. Trừ điểm cần tránh

| Lỗi                                              | Mức                          |
| ------------------------------------------------ | ---------------------------- |
| Không nộp `.vpp` / không vẽ bằng Visual Paradigm | **−2.0**                     |
| Thành viên không ghi đóng góp TeamWork           | Điểm cá nhân bị điều chỉnh   |
| Câu mơ hồ không định lượng (“nhanh”, “dễ dùng”…) | **−0.1 / lỗi** (tối đa −1.0) |
| Sao chép không trích dẫn                         | 0 điểm phần liên quan        |

---

## 8. Tin nhắn gửi nhóm (copy/paste)

```
Mọi người vào làm SWR302 GMS giúp mình:

1) Repo: https://github.com/phuocvanday/SWR302-GroupOfFour
2) Hướng dẫn: HUONG_DAN_NHOM.md (trong repo)
3) Board: https://github.com/users/phuocvanday/projects/3
4) Việc của từng người (đã assign):
   - Phước: @phuocvanday
   - Tuấn: @teafromhand-vn
   - Thiên: @ngthien05
   - Huy: @Huyd06
   Link nhanh: https://github.com/phuocvanday/SWR302-GroupOfFour/issues/assigned/

Làm Bước 0 trước → rồi Bước 1.
Git: cả nhóm commit trên nhánh step-0 / step-1 (một nhánh/bước), xong checklist thì merge vào main.
Xong phần mình: commit + push + đóng issue.
Đủ checklist nhóm mới sang bước sau.
```

---

**Tóm lại:** **8 bước** (+ Bước 0). Việc đã **gán sẵn trên GitHub**. Git: **một nhánh `step-N` / bước**. Mỗi người: **issue → làm trên `step-N` → commit → đóng issue → checklist nhóm → merge `main` → bước tiếp.**
