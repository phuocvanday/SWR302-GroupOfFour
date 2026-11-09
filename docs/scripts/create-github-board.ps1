# Create SWR302 issues and add to Project #3
$ErrorActionPreference = "Continue"
$repo = "phuocvanday/SWR302-GroupOfFour"
$owner = "phuocvanday"
$projectNumber = 3

function New-Issue {
  param(
    [string]$Title,
    [string]$Body,
    [string]$MilestoneTitle,
    [string[]]$Labels
  )
  $labelArgs = @()
  foreach ($l in $Labels) { $labelArgs += @("--label", $l) }

  $url = (gh issue create --repo $repo --title $Title --body $Body --milestone $MilestoneTitle @labelArgs 2>&1 | Select-Object -Last 1).ToString().Trim()
  if ($url -notmatch "^https://") {
    Write-Host "FAIL: $Title -> $url"
    return $null
  }
  Write-Host "OK $url"
  gh project item-add $projectNumber --owner $owner --url $url | Out-Null
  return $url
}

gh project link $projectNumber --owner $owner --repo $repo 2>$null | Out-Null
gh project edit $projectNumber --owner $owner --description "Board làm bài SWR302 GMS — 8 bước + setup. Repo: SWR302-GroupOfFour" | Out-Null

$M0 = "Bước 0 — Setup"
$M1 = "Bước 1 — Vision & Scope"
$M2 = "Bước 2 — Context Diagram + UC list"
$M3 = "Bước 3 — UCD + BR + Glossary"
$M4 = "Bước 4 — Đặc tả Use Case"
$M5 = "Bước 5 — Wireframe"
$M6 = "Bước 6 — Activity Diagram"
$M7 = "Bước 7 — SMD + ERD + Data dict"
$M8 = "Bước 8 — NFR + Traceability + Nộp"

# ========== BƯỚC 0 ==========
New-Issue -MilestoneTitle $M0 -Labels @("step-0","member-all","priority-high") -Title "[Bước 0][All] Setup: clone, đọc hướng dẫn, cài Visual Paradigm" -Body @"
## Mục tiêu
Mọi người sẵn sàng làm việc trên GitHub.

## Việc cần làm
- [ ] ``git clone https://github.com/phuocvanday/SWR302-GroupOfFour.git``
- [ ] Đọc ``HUONG_DAN_NHOM.md``
- [ ] Đọc ``docs/HuongDan_Assignment.md`` (A.1–A.4)
- [ ] Đọc ``docs/kimi2.5-project.md``
- [ ] Cài Visual Paradigm Community và mở được

Xem ``HUONG_DAN_NHOM.md``.
"@

New-Issue -MilestoneTitle $M0 -Labels @("step-0","member-phuoc") -Title "[Bước 0][Phước] Điền TeamWork + mã nhóm/lớp/GV + deadline" -Body @"
## Việc cần làm
- [ ] Thu thập MSSV 4 bạn → ``05_TeamWork.xlsx``
- [ ] Điền mã nhóm / lớp / GV (khi có)
- [ ] Chốt deadline nội bộ 8 bước

## Commit
``````
[Bước 0][Phước] setup TeamWork + deadline
``````
"@

New-Issue -MilestoneTitle $M0 -Labels @("step-0","checklist","member-all") -Title "[Bước 0][Checklist nhóm] Đóng bước Setup" -Body @"
## Checklist nhóm — chỉ đóng khi đủ
- [ ] Đủ 4 MSSV trên TeamWork (đã push)
- [ ] Mọi người clone / pull được ``main``
- [ ] VP đã cài ở máy mỗi thành viên

**Đóng issue này = được sang Bước 1.**
"@

# ========== BƯỚC 1 ==========
New-Issue -MilestoneTitle $M1 -Labels @("step-1","member-phuoc","priority-high") -Title "[Bước 1][Phước] Trang bìa, §1.1–1.2, ghép BO/Scope vào SRS" -Body @"
## Việc
- [ ] Trang bìa SRS + Revision History 0.1
- [ ] Viết §1.1 Mục đích + §1.2 Quy ước
- [ ] Sau họp nhóm: ghép BO + In/Out vào ``01_SRS_GMS.docx`` Mục 1–2
- [ ] Nhật ký TeamWork Bước 1

## Commit
``````
[Bước 1][Phước] ghép Mục 1–2 SRS + TeamWork
``````
Nháp tham khảo: ``docs/01_Vision_Scope_GMS.md`` — không copy mù.
"@

New-Issue -MilestoneTitle $M1 -Labels @("step-1","member-tuan") -Title "[Bước 1][Tuấn] User class PT + scope PT + BO-03 + glossary PT" -Body @"
## Việc
- [ ] User class **Personal Trainer**
- [ ] In/Out scope mảng PT / booking / lịch
- [ ] Đề xuất metric **BO-03** (đo được)
- [ ] Glossary PT (4–6 từ)

## Nộp
``docs/step1/tuan_vision.md`` → commit + push

## Commit
``````
[Bước 1][Tuấn] user class PT + BO-03 + glossary
``````
"@

New-Issue -MilestoneTitle $M1 -Labels @("step-1","member-thien") -Title "[Bước 1][Thiên] User class Customer + scope Membership/QR + BO-01/02" -Body @"
## Việc
- [ ] User class **Customer**
- [ ] In/Out Membership + QR check-in/out
- [ ] Metric **BO-01, BO-02**
- [ ] Assumptions quầy / thiết bị QR
- [ ] Glossary membership / QR

## Nộp
``docs/step1/thien_vision.md``

## Commit
``````
[Bước 1][Thiên] user class Customer + BO-01/02 + scope QR
``````
"@

New-Issue -MilestoneTitle $M1 -Labels @("step-1","member-huy") -Title "[Bước 1][Huy] User class Owner + môi trường/ràng buộc + BO-04 + references" -Body @"
## Việc
- [ ] User class **Gym Owner**
- [ ] §2.3 Môi trường vận hành + §2.4 Ràng buộc (NĐ-13, VND, VP…)
- [ ] In/Out báo cáo / thanh toán
- [ ] Metric **BO-04**
- [ ] §1.4 References

## Nộp
``docs/step1/huy_vision.md``

## Commit
``````
[Bước 1][Huy] Owner + constraints + BO-04 + references
``````
"@

New-Issue -MilestoneTitle $M1 -Labels @("step-1","checklist","member-all") -Title "[Bước 1][Checklist nhóm] Đóng Vision & Scope" -Body @"
## Checklist nhóm
- [ ] ≥ 3 BO đo được trong SRS
- [ ] In/Out scope rõ
- [ ] Đủ 3 user class (Customer, PT, Owner)
- [ ] Trang bìa đủ tên + MSSV
- [ ] SRS Mục 1–2 không còn placeholder
- [ ] Đã push GitHub
- [ ] Mỗi người đã ghi TeamWork

**Chưa đủ → không sang Bước 2.**
"@

# ========== BƯỚC 2 ==========
New-Issue -MilestoneTitle $M2 -Labels @("step-2","member-phuoc","priority-high") -Title "[Bước 2][Phước] Vẽ CD-01 + export PNG + chèn SRS §2.1" -Body @"
## Việc
- [ ] Vẽ CD-01 trong VP (1 process ``0 – GMS``)
- [ ] ≥ 5 entity, ≥ 12 data flow (danh từ)
- [ ] Lưu ``02_Models/GMS.vpp``
- [ ] Export ``03_Images/CD_ContextDiagram.png``
- [ ] Chèn SRS §2.1 + bảng DF

## Commit
``````
[Bước 2][Phước] CD-01 + PNG + SRS §2.1
``````
Tham khảo: ``docs/02_Context_Diagram_DataFlows.md``
"@

New-Issue -MilestoneTitle $M2 -Labels @("step-2","member-tuan") -Title "[Bước 2][Tuấn] DF + UC list domain PT" -Body @"
## Việc
- [ ] Liệt kê data flow + UC PT (UC-10…18, 24…)
- [ ] Xác nhận secondary Payment / SMS

## Nộp
``docs/step2/tuan_uc_df.md``

## Commit
``````
[Bước 2][Tuấn] DF + UC domain PT
``````
"@

New-Issue -MilestoneTitle $M2 -Labels @("step-2","member-thien") -Title "[Bước 2][Thiên] DF + UC list domain Membership/QR" -Body @"
## Việc
- [ ] DF + UC Membership/QR (UC-04…09, 20, 27…)
- [ ] Entity QR Service

## Nộp
``docs/step2/thien_uc_df.md``

## Commit
``````
[Bước 2][Thiên] DF + UC Membership/QR
``````
"@

New-Issue -MilestoneTitle $M2 -Labels @("step-2","member-huy") -Title "[Bước 2][Huy] DF + UC Owner/Report/Feedback/Time" -Body @"
## Việc
- [ ] DF + UC Owner/Report/Feedback/Time (UC-16,17,21–23,25,26,28)
- [ ] Entity Payment, SMS, Time

## Nộp
``docs/step2/huy_uc_df.md``

## Commit
``````
[Bước 2][Huy] DF + UC Owner/Report/Feedback
``````
"@

New-Issue -MilestoneTitle $M2 -Labels @("step-2","checklist","member-all") -Title "[Bước 2][Checklist nhóm] Đóng CD + UC list" -Body @"
## Checklist nhóm
- [ ] CD: 1 process, ≥5 entity, ≥12 DF, không data store
- [ ] ≥3 primary actor + ≥1 secondary
- [ ] ≥20 UC (trừ Login), tên Động từ + Danh từ
- [ ] PNG CD + vpp đã push
- [ ] DF đều map ≥1 UC
"@

# ========== BƯỚC 3 ==========
New-Issue -MilestoneTitle $M3 -Labels @("step-3","member-phuoc") -Title "[Bước 3][Phước] UCD-01 Overview + Membership + ghép SRS" -Body @"
## Việc
- [ ] UCD-01 Overview + generalization User
- [ ] Package Membership (phối hợp Thiên)
- [ ] Ghép BR/Glossary vào SRS
- [ ] Export ``UCD_Overview.png``

## Commit
``````
[Bước 3][Phước] UCD Overview + SRS BR/Glossary
``````
"@

New-Issue -MilestoneTitle $M3 -Labels @("step-3","member-tuan") -Title "[Bước 3][Tuấn] UCD package PT + include/extend booking" -Body @"
## Việc
- [ ] UCD package PT
- [ ] Include/extend phía booking/thanh toán (đúng ngữ nghĩa)
- [ ] Export ``UCD_PT.png``

## Commit
``````
[Bước 3][Tuấn] UCD package PT
``````
"@

New-Issue -MilestoneTitle $M3 -Labels @("step-3","member-thien") -Title "[Bước 3][Thiên] UCD package Membership chi tiết" -Body @"
## Việc
- [ ] UCD Membership chi tiết
- [ ] Extend nhập mã thủ công → Check-in
- [ ] Export ``UCD_Membership.png``

## Commit
``````
[Bước 3][Thiên] UCD Membership
``````
"@

New-Issue -MilestoneTitle $M3 -Labels @("step-3","member-huy") -Title "[Bước 3][Huy] UCD Report/Feedback + bảng BR + Glossary" -Body @"
## Việc
- [ ] UCD Report + Feedback
- [ ] Chốt bảng BR (có loại)
- [ ] Bổ sung Glossary còn thiếu → SRS

## Commit
``````
[Bước 3][Huy] BR + Glossary + UCD Report/Feedback
``````
"@

New-Issue -MilestoneTitle $M3 -Labels @("step-3","checklist","member-all") -Title "[Bước 3][Checklist nhóm] Đóng UCD + BR + Glossary" -Body @"
## Checklist nhóm
- [ ] ≥20 UC trên UCD
- [ ] ≥2 include, ≥2 extend, ≥1 actor generalization
- [ ] Confirm/Reject không dùng extend sai
- [ ] BR có ID + loại; Glossary thống nhất
- [ ] PNG UCD đã push
"@

# ========== BƯỚC 4 ==========
New-Issue -MilestoneTitle $M4 -Labels @("step-4","member-phuoc","priority-high") -Title "[Bước 4][Phước] Đặc tả UC-05 + UC-06" -Body @"
## UC
- UC-05 Đăng ký Membership tại quầy
- UC-06 Kích hoạt Membership

## Việc
- [ ] Fully dressed đủ template
- [ ] Nháp ``docs/step4/UC-05.md``, ``UC-06.md`` → ghép SRS Mục 3

## Commit
``````
[Bước 4][Phước] đặc tả UC-05, UC-06
``````
"@

New-Issue -MilestoneTitle $M4 -Labels @("step-4","member-tuan","priority-high") -Title "[Bước 4][Tuấn] Đặc tả UC-11 + UC-12" -Body @"
## UC
- UC-11 Đặt gói PT
- UC-12 Xác nhận / Từ chối booking PT

## Nộp
``docs/step4/UC-11.md``, ``UC-12.md``

## Commit
``````
[Bước 4][Tuấn] đặc tả UC-11, UC-12
``````
"@

New-Issue -MilestoneTitle $M4 -Labels @("step-4","member-thien","priority-high") -Title "[Bước 4][Thiên] Đặc tả UC-08 + UC-15" -Body @"
## UC
- UC-08 Check-in bằng QR
- UC-15 Ghi nhận buổi tập

## Nộp
``docs/step4/UC-08.md``, ``UC-15.md``

## Commit
``````
[Bước 4][Thiên] đặc tả UC-08, UC-15
``````
"@

New-Issue -MilestoneTitle $M4 -Labels @("step-4","member-huy","priority-high") -Title "[Bước 4][Huy] Đặc tả UC-16 + UC-17" -Body @"
## UC
- UC-16 Đăng ký tài khoản PT
- UC-17 Duyệt tài khoản PT

## Nộp
``docs/step4/UC-16.md``, ``UC-17.md``

## Commit
``````
[Bước 4][Huy] đặc tả UC-16, UC-17
``````
"@

New-Issue -MilestoneTitle $M4 -Labels @("step-4","checklist","member-all") -Title "[Bước 4][Checklist nhóm] Đóng đặc tả UC" -Body @"
## Checklist nhóm
- [ ] ≥8 UC fully dressed trong SRS
- [ ] Mỗi UC: main + ≥1 alt + ≥1 exception
- [ ] ID khớp UCD; TeamWork đã ghi
"@

# ========== BƯỚC 5 ==========
New-Issue -MilestoneTitle $M5 -Labels @("step-5","member-phuoc") -Title "[Bước 5][Phước] Wireframe UC-05 + UC-06" -Body @"
## Việc
- [ ] UI quầy đăng ký / kích hoạt / hiện QR
- [ ] Có trạng thái lỗi + bảng field
- [ ] ``03_Images/UI_UC-05_*.png``, ``UI_UC-06_*.png``

## Commit
``````
[Bước 5][Phước] wireframe UC-05, UC-06
``````
"@

New-Issue -MilestoneTitle $M5 -Labels @("step-5","member-tuan") -Title "[Bước 5][Tuấn] Wireframe UC-11 + UC-12" -Body @"
## Việc
- [ ] UI đặt PT + màn confirm/reject
- [ ] ``UI_UC-11_*.png``, ``UI_UC-12_*.png``

## Commit
``````
[Bước 5][Tuấn] wireframe UC-11, UC-12
``````
"@

New-Issue -MilestoneTitle $M5 -Labels @("step-5","member-thien") -Title "[Bước 5][Thiên] Wireframe UC-08 + UC-15" -Body @"
## Việc
- [ ] UI quét QR + ghi buổi tập
- [ ] ``UI_UC-08_*.png``, ``UI_UC-15_*.png``

## Commit
``````
[Bước 5][Thiên] wireframe UC-08, UC-15
``````
"@

New-Issue -MilestoneTitle $M5 -Labels @("step-5","member-huy") -Title "[Bước 5][Huy] Wireframe UC-16 + UC-17" -Body @"
## Việc
- [ ] UI form đăng ký PT + màn duyệt Owner
- [ ] ``UI_UC-16_*.png``, ``UI_UC-17_*.png``

## Commit
``````
[Bước 5][Huy] wireframe UC-16, UC-17
``````
"@

New-Issue -MilestoneTitle $M5 -Labels @("step-5","checklist","member-all") -Title "[Bước 5][Checklist nhóm] Đóng Wireframe" -Body @"
## Checklist nhóm
- [ ] Mọi UC dressed có UI + bảng field
- [ ] Có trạng thái lỗi
- [ ] File đúng ``UI_<UC-ID>_...`` và đã push
"@

# ========== BƯỚC 6 ==========
New-Issue -MilestoneTitle $M6 -Labels @("step-6","member-tuan","priority-high") -Title "[Bước 6][Tuấn] AD-01 Đặt gói PT & thanh toán" -Body @"
## Việc
- [ ] AD-01 swimlane ≥3 lane (Customer | GMS | PT | Payment | SMS)
- [ ] Decision + fork/join đúng
- [ ] Export ``03_Images/AD_BookPT.png``

## Commit
``````
[Bước 6][Tuấn] AD-01 Book PT
``````
"@

New-Issue -MilestoneTitle $M6 -Labels @("step-6","member-huy","priority-high") -Title "[Bước 6][Huy] AD-02 Đăng ký & duyệt PT" -Body @"
## Việc
- [ ] AD-02 (PT | GMS | Owner | SMS)
- [ ] ``AD_ApprovePT.png``

## Commit
``````
[Bước 6][Huy] AD-02 Approve PT
``````
"@

New-Issue -MilestoneTitle $M6 -Labels @("step-6","member-phuoc","member-thien","priority-high") -Title "[Bước 6][Phước+Thiên] AD-03 Đăng ký–kích hoạt membership quầy" -Body @"
## Việc
- [ ] Phước vẽ AD-03 chính (Owner | GMS | Customer | SMS/Payment)
- [ ] Thiên review guard liên quan QR/membership
- [ ] ``AD_ActivateMembership.png``

## Commit
``````
[Bước 6][Phước] AD-03 Activate membership
[Bước 6][Thiên] review AD-03
``````
"@

New-Issue -MilestoneTitle $M6 -Labels @("step-6","checklist","member-all") -Title "[Bước 6][Checklist nhóm] Đóng Activity Diagram" -Body @"
## Checklist nhóm
- [ ] ≥3 AD, ≥3 lane mỗi AD
- [ ] Guard / fork-join đúng; lane khớp UCD
- [ ] PNG + vpp đã push
"@

# ========== BƯỚC 7 ==========
New-Issue -MilestoneTitle $M7 -Labels @("step-7","member-thien","priority-high") -Title "[Bước 7][Thiên] SMD-01 Membership + SMD-02 PT Booking" -Body @"
## Việc
- [ ] SMD-01 Membership (≥5 state)
- [ ] SMD-02 PT Booking
- [ ] ``SMD_Membership.png``, ``SMD_PTBooking.png``

## Commit
``````
[Bước 7][Thiên] SMD Membership + PT Booking
``````
"@

New-Issue -MilestoneTitle $M7 -Labels @("step-7","member-huy","priority-high") -Title "[Bước 7][Huy] ERD-01 + Data dictionary" -Body @"
## Việc
- [ ] ERD khái niệm ≥10 entity + cardinality
- [ ] Data dictionary
- [ ] ``ERD_Conceptual.png``

## Commit
``````
[Bước 7][Huy] ERD + data dictionary
``````
"@

New-Issue -MilestoneTitle $M7 -Labels @("step-7","member-tuan") -Title "[Bước 7][Tuấn] Bổ sung ERD Booking–PT–Session + review SMD-02" -Body @"
## Việc
- [ ] Thuộc tính/quan hệ Booking–PT–Session trên ERD
- [ ] Review SMD-02 khớp UC-11/12

## Commit
``````
[Bước 7][Tuấn] ERD booking attrs + review SMD-02
``````
"@

New-Issue -MilestoneTitle $M7 -Labels @("step-7","member-phuoc") -Title "[Bước 7][Phước] Chèn SMD/ERD vào SRS Mục 4 + Traceability sơ bộ" -Body @"
## Việc
- [ ] Chèn hình + mô tả vào SRS Mục 4
- [ ] Rà transition SMD có UC/time event
- [ ] Cập nhật Traceability sơ bộ

## Commit
``````
[Bước 7][Phước] SRS Mục 4 + traceability draft
``````
"@

New-Issue -MilestoneTitle $M7 -Labels @("step-7","checklist","member-all") -Title "[Bước 7][Checklist nhóm] Đóng SMD + ERD" -Body @"
## Checklist nhóm
- [ ] ≥2 SMD, không state chết
- [ ] ERD ≥10 entity
- [ ] Object SMD = entity có status trên ERD
- [ ] Dict khớp field wireframe chính
"@

# ========== BƯỚC 8 ==========
New-Issue -MilestoneTitle $M8 -Labels @("step-8","member-huy","priority-high") -Title "[Bước 8][Huy] Soạn NFR đo được + giao diện ngoài" -Body @"
## Việc
- [ ] NFR PERF/SEC/USAB… có cách đo
- [ ] Giao diện ngoài → SRS

## Commit
``````
[Bước 8][Huy] NFR + external interfaces
``````
"@

New-Issue -MilestoneTitle $M8 -Labels @("step-8","member-phuoc","priority-high") -Title "[Bước 8][Phước] Traceability Matrix + đóng gói zip nộp" -Body @"
## Việc
- [ ] Hoàn thiện ``04_Traceability_Matrix.xlsx``
- [ ] Revision History 1.0
- [ ] Zip ``<MaNhom>_SWR302_Assignment.zip`` đúng A.3
- [ ] (Tuỳ chọn) tag ``v1.0-submission``

## Commit
``````
[Bước 8][Phước] traceability + submission pack
``````
"@

New-Issue -MilestoneTitle $M8 -Labels @("step-8","member-tuan") -Title "[Bước 8][Tuấn] Peer review UCD PT + AD + đặc tả PT" -Body @"
## Việc
- [ ] Peer review đặc tả + AD + UCD PT
- [ ] Ghi ``docs/step8/review_tuan.md``

## Commit
``````
[Bước 8][Tuấn] peer review PT artifacts
``````
"@

New-Issue -MilestoneTitle $M8 -Labels @("step-8","member-thien") -Title "[Bước 8][Thiên] Peer review SMD + Check-in + CD membership" -Body @"
## Việc
- [ ] Peer review SMD + UC check-in + DF membership
- [ ] Ghi ``docs/step8/review_thien.md``

## Commit
``````
[Bước 8][Thiên] peer review SMD/QR
``````
"@

New-Issue -MilestoneTitle $M8 -Labels @("step-8","checklist","member-all","priority-high") -Title "[Bước 8][All] Tự đánh giá TeamWork + Checklist nộp cuối" -Body @"
## Cá nhân
- [ ] Điền % đóng góp + mô tả việc trong ``05_TeamWork.xlsx``

## Checklist nộp
- [ ] SRS đủ mục; ID + ưu tiên; không từ mơ hồ
- [ ] CD, UCD, ≥3 AD, ≥2 SMD, ERD trong ``.vpp`` + PNG
- [ ] Mỗi UC dressed có wireframe
- [ ] Traceability + TeamWork hoàn chỉnh
- [ ] ``.vpp`` mở được; zip đúng cấu trúc A.3

**Đóng issue này = sẵn sàng nộp GV.**
"@

Write-Host ""
Write-Host "DONE"
Write-Host "Project: https://github.com/users/phuocvanday/projects/3"
Write-Host "Issues:  https://github.com/phuocvanday/SWR302-GroupOfFour/issues"
Write-Host "Milestones: https://github.com/phuocvanday/SWR302-GroupOfFour/milestones"
gh issue list --repo $repo --limit 50
