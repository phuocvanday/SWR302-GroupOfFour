# Bước 7 — Phước (SRS Mục 4 + Traceability sơ bộ)

> Issue: [#37](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/37) · Branch: `step-7`  
> Deliverables: SRS §4 scaffold + Appendix C draft + `04_Traceability_Matrix.xlsx` / CSV

## Checklist

- [x] Khung **Mục 4 Data Requirements** (nháp Markdown — dán Word khi ERD của Huy sẵn)
- [x] **Traceability sơ bộ** (bảng dưới + `04_Traceability_Matrix.csv`)
- [ ] Dán vào `01_SRS_GMS.docx` §4 + Appendix C (khi Word free + ERD PNG có)
- [ ] Bổ sung hàng còn thiếu sau khi Huy (#35) / Tuấn (#36) chốt ERD

---

## 4. Data Requirements — nội dung dán SRS (English draft)

### 4.1 Logical data model

Insert **Figure 4.1 — ERD-01 Conceptual Data Model of GMS** (`03_Images/ERD_Conceptual.png`, owner: Huy #35).

**Minimum entities (Release 1):** Customer, GymOwner, PersonalTrainer, MembershipPackage, Membership, PTPackage, PTBooking, TrainingSession, Payment, Notification, Complaint, CheckInLog (≥10).

**Key relationships (draft):**

| From | To | Cardinality | Note |
|------|-----|-------------|------|
| Customer | Membership | 1 : 0..* | A customer may hold multiple memberships over time |
| MembershipPackage | Membership | 1 : 0..* | Package defines duration/fee |
| Membership | CheckInLog | 1 : 0..* | Only ACTIVE membership should create valid check-ins (BR-04/05) |
| Customer | PTBooking | 1 : 0..* | Requires ACTIVE membership (BR-06) |
| PersonalTrainer | PTPackage | 1 : 0..* | After PT Approved (BR-07) |
| PTPackage | PTBooking | 1 : 0..* | |
| PTBooking | TrainingSession | 1 : 0..* | Sessions under Confirmed booking (BR-10) |
| Membership / PTBooking | Payment | 1 : 0..* | Fee, renew, refund |
| Customer / PT / Owner | Notification | 1 : 0..* | SMS / in-app |
| Customer | Complaint | 1 : 0..* | Within 7 days (BR-12) |

Related lifecycle: **SMD-01 Membership** (Thiên) — states Inactive → Active → Expired / Suspended / Cancelled.

### 4.2 Data dictionary (stub — fill from Huy)

| Entity | Attribute | Meaning | Type / Format | Length / Domain | Required | Example |
|--------|-----------|---------|---------------|-----------------|----------|---------|
| Membership | membershipId | Unique membership id | String | PK | Yes | M001 |
| Membership | status | Lifecycle state | Enum | INACTIVE/ACTIVE/SUSPENDED/EXPIRED/CANCELLED | Yes | ACTIVE |
| Membership | startDate | Activation date | Date | UTC+7 | When ACTIVE | 10/11/2026 |
| Membership | endDate | Expiry date | Date | start + DurationMonths (BR-03) | When ACTIVE | 10/05/2027 |
| Membership | qrToken | Unique QR payload | String | Unique while ACTIVE (BR-04) | When ACTIVE | qr_… |
| Payment | amountVnd | Amount charged | Integer | ≥ 0 | Yes | 2000000 |
| Payment | result | Gateway/cash result | Enum | SUCCESS/FAIL/PENDING | Yes | SUCCESS |
| PTBooking | status | Booking lifecycle | Enum | PENDING/CONFIRMED/REJECTED/CANCELLED | Yes | PENDING |
| CheckInLog | checkInAt | Gate entry time | DateTime | Within open hours (BR-05) | Yes | 2026-11-10 18:00 |

> Full dictionary: wait for Huy `docs/step7/huy_erd.md` + sheet.

### 4.3 Reports

| Report ID | Name | Purpose | User | Frequency | Data sources | Filters |
|-----------|------|---------|------|-----------|--------------|---------|
| RPT-01 | Revenue summary | Track membership/PT fee | Gym Owner | Weekly | Payment, Membership, PTBooking | Date range, type |
| RPT-02 | Check-in statistics | Gate usage / BO-02 | Gym Owner | Weekly | CheckInLog, Membership | Date, status |
| RPT-03 | PT performance | Sessions completed / no-show | Gym Owner | Weekly | TrainingSession, PTBooking | PT, date |

Export: UC-21 / UC-22 (Excel).

### 4.4 Collection, integrity, retention

- **Collection:** Counter (UC-05/06), Customer self-service (booking/QR), Payment Gateway callbacks, Scheduler jobs (UC-27/28).
- **Integrity:** BR-02 (no ACTIVE without full fee); BR-04 (one QR per ACTIVE); referential integrity Customer↔Membership↔Payment.
- **Retention (draft):** operational logs ≥ 12 months; cancelled membership archive after 365 days expired (see SMD-01 T11); anonymize PII on request (ND-13 / profile).

---

## Appendix C — Traceability Matrix (preliminary)

Columns per assignment: **BO | UC-ID | FR-ID | BR-ID | Diagram | Screen | Test (planned)**

| BO | UC-ID | FR-ID | BR-ID | Diagram | Screen | Test (planned) |
|----|-------|-------|-------|---------|--------|----------------|
| BO-01 | UC-05 | FR-05-01 Create INACTIVE membership | BR-01, BR-02 | UCD Overview/Membership; AD-03; SMD-01 | SCR-05 Register Membership | TC-05-01 register cash; TC-05-02 payment fail |
| BO-01 | UC-06 | FR-06-01 Set ACTIVE; FR-06-03 Generate QR | BR-02, BR-03, BR-04 | AD-03; SMD-01; CD (QR/SMS) | SCR-06 Activate Membership | TC-06-01 activate; TC-06-02 unpaid block |
| BO-02 | UC-07 | FR-07-01 Show membership QR | BR-04 | UCD Membership | (Customer QR view) | TC-07-01 show QR when ACTIVE |
| BO-02 | UC-08 | FR-08-01 Validate QR check-in | BR-04, BR-05 | UCD; SMD-01 | SCR-08 QR Check-in | TC-08-01 valid; TC-08-02 invalid/manual |
| BO-02 | UC-09 | FR-09-01 Check-out by QR | BR-04, BR-05 | UCD Membership | SCR-09 | TC-09-01 checkout |
| BO-02 | UC-27 | FR-27-01 Auto-expire membership | BR-11, BR-04 | SMD-01; CD (Time, SMS) | — (batch) | TC-27-01 expire job |
| BO-03 | UC-11 | FR-11-01 Book PT + pay | BR-06, BR-08 | UCD PT; AD-01; SMD-02 | SCR-11 | TC-11-01 book; TC-11-02 no ACTIVE membership |
| BO-03 | UC-12 | FR-12-01 Confirm/Reject booking | BR-07, BR-08, BR-09 | AD-01; SMD-02 | SCR-12 | TC-12-01 confirm; TC-12-02 reject+refund |
| BO-03 | UC-15 | FR-15-01 Record training session | BR-10 | UCD PT; SMD-02 | SCR-15 Record Session | TC-15-01 record session |
| BO-03 | UC-16 | FR-16-01 Register PT account | BR-07 | UCD; AD-02 | SCR-16 Register PT | TC-16-01 submit |
| BO-03 | UC-17 | FR-17-01 Approve/Reject PT | BR-07 | AD-02 | SCR-17 Approve PT | TC-17-01 approve |
| BO-04 | UC-21 | FR-21-01 Generate operational report | — | CD (Owner) | Report UI | TC-21-01 gen report ≤1 min |
| BO-04 | UC-22 | FR-22-01 Export report Excel | — | CD | Report UI | TC-22-01 export xlsx |
| — | UC-02 | FR-02-01 Login by role | BR-01 | UCD (User gen.) | Login | TC-02-01 owner login |
| — | UC-25/26 | FR-25/26 Complaint | BR-12 | UCD Feedback | Feedback UI | TC-25-01 within 7 days |

Machine-readable copy: `04_Traceability_Matrix.csv` (open in Excel → save as `04_Traceability_Matrix.xlsx` if needed).

---

## Analysis models index (Appendix B — update)

| ID | Name | Type | SRS section |
|----|------|------|-------------|
| CD-01 | GMS Context Diagram | Context | 2.1 |
| UCD-01 | Use Case Overview | Use Case | 3.1 |
| AD-03 | Activate Membership at Counter | Activity | 3.x / App.B |
| SMD-01 | Membership Lifecycle | State | 3.x / 4.1 |
| SMD-02 | PT Booking Lifecycle | State | 3.x |
| ERD-01 | Conceptual ERD | ERD | 4.1 *(pending Huy)* |

---

## Next actions

1. Huy: fill ERD PNG + dictionary → Phước paste §4.1–4.2 into Word.  
2. Phước: open CSV in Excel, format, replace/overwrite `04_Traceability_Matrix.xlsx`.  
3. Sync Appendix B/C in `01_SRS_GMS.docx`.  
4. Close #37 when Word paste done.
