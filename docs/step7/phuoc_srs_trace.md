# Bước 7 — Phước (SRS Mục 4 + Traceability sơ bộ)

> Issue: [#37](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/37) · Branch: `step-7`  
> Deliverables: SRS §4 (ERD + SMD refs) + Appendix C + `04_Traceability_Matrix.xlsx` / CSV

## Checklist (#37)

- [x] Chèn hình + mô tả vào SRS Mục 4 (ERD-01 từ Huy; SMD mô tả/bảng transition — PNG VP Thiên còn pending)
- [x] Rà transition SMD có UC / time event (bảng dưới + `thien_smd.md`)
- [x] Cập nhật Traceability sơ bộ (`04_Traceability_Matrix.csv` / `.xlsx` + Appendix C trong Word)
- [x] Đồng bộ entity/dict với `docs/step7/huy_erd.md` (#35)
- [ ] PNG `SMD_Membership.png` / `SMD_PTBooking.png` khi Thiên export từ VP (#34)

---

## 4. Data Requirements — nội dung SRS

### 4.1 Logical data model

**Figure 4.1 — ERD-01 Conceptual Data Model of GMS**  
File: `03_Images/ERD_Conceptual.png` (converted from Huy `Entity Relationship Diagram1.jpg`, #35).

**Core entities (Huy ERD, ≥10):** Role, Account, Gym_Owner, Personal_trainer, Member, Membership_Package, Customer_Membership, Booking, Check_In, Payment, Equipment_inventory, Maintenance_Log.

**Mapping Vision names → Huy ERD (for Traceability):**

| Vision / UC wording | Huy ERD entity |
|---------------------|----------------|
| Customer | Member (+ Account) |
| Gym Owner | Gym_Owner |
| Personal Trainer | Personal_trainer |
| MembershipPackage | Membership_Package |
| Membership | Customer_Membership |
| PTBooking | Booking |
| CheckInLog | Check_In |
| Payment | Payment |

**Key relationships (from Huy):**

| From | To | Cardinality |
|------|-----|-------------|
| Role | Account | 1 : N |
| Account | Gym_Owner / Member / Personal_trainer | 1 : 1 |
| Member | Customer_Membership | 1 : N |
| Membership_Package | Customer_Membership | 1 : N |
| Member | Booking | 1 : N |
| Personal_trainer | Booking | 1 : N |
| Member | Check_In | 1 : N |
| Member | Payment | 1 : N |
| Equipment_inventory | Maintenance_Log | 1 : N |
| Gym_Owner | Maintenance_Log | 1 : N |

Related lifecycles: **SMD-01 Membership** · **SMD-02 PT Booking** (Thiên #34).

### 4.2 Data dictionary

Full attribute tables: `docs/step7/huy_erd.md` §2 (Account, Role, Gym_Owner, Personal_trainer, Member, Membership_Package, Customer_Membership, Booking, Check_In, Payment, Equipment_inventory, Maintenance_Log).

**Stub (SRS excerpt):**

| Entity | Attribute | Meaning | Domain | Required |
|--------|-----------|---------|--------|----------|
| Customer_Membership | Status | Lifecycle state | INACTIVE/ACTIVE/SUSPENDED/EXPIRED/CANCELLED | Yes |
| Customer_Membership | EndDate | Expiry | Date (BR-03) | When ACTIVE |
| Booking | Status | PT booking lifecycle | PENDING/CONFIRMED/IN_PROGRESS/COMPLETED/REJECTED/CANCELLED | Yes |
| Check_In | DateTime | Gate entry | DateTime within open hours (BR-05) | Yes |
| Payment | Amount / Status | Fee result | SUCCESS/FAIL/PENDING | Yes |

### 4.3 Reports

| Report ID | Name | User | Data sources |
|-----------|------|------|--------------|
| RPT-01 | Revenue summary | Gym Owner | Payment, Customer_Membership, Booking |
| RPT-02 | Check-in statistics | Gym Owner | Check_In, Customer_Membership |
| RPT-03 | PT performance | Gym Owner | Booking (+ sessions when modeled) |

### 4.4 Collection, integrity, retention

- **Collection:** UC-05/06 counter; booking/QR; Payment Gateway; Scheduler UC-27/28.
- **Integrity:** BR-02, BR-04; FK Account↔profiles; Membership↔Payment.
- **Retention:** logs ≥ 12 months; archive Cancelled after policy (SMD-01 T11).

---

## SMD transition audit (UC / time event) — issue #37 item 2

Nguồn: `docs/step7/thien_smd.md`. Mọi transition có **event**; time event đánh dấu **Time**.

### SMD-01 Membership

| ID | Event | Type | Guard / Action (short) | Target | UC / BR |
|----|-------|------|------------------------|--------|---------|
| T1 | `registerMembership` | UC | create INACTIVE | Inactive | UC-05, BR-01 |
| T2 | `activate` | UC | full fee → QR + SMS | Active | UC-06, BR-02/03/04 |
| T3 | `cancelRegistration` | UC/Alt | unpaid / owner cancel | Cancelled | UC-05 Alt |
| T4 | `renew` | UC | extend EndDate | Active | UC-20, BR-02/03 |
| T5 | `when(current_date > end_date)` | **Time** | invalidate QR; SMS | Expired | UC-27, BR-04/11 |
| T6 | `suspend` | Owner/BR | disable QR | Suspended | BR-04 |
| T7 | `reactivate` | UC/BR | enable QR | Active | BR-01/04 |
| T8 | `when(current_date > end_date)` | **Time** | from Suspended | Expired | UC-27, BR-11 |
| T9 | `terminate` | Owner | revoke QR | Cancelled | BR-04 |
| T10 | `renew` | UC | from Expired → Active | Active | UC-20, BR-02/03/04 |
| T11 | `archive` | **Time** | after 365d expired | Cancelled | Retention |
| T12 | `closeRecord` | System | Final | Final | — |

### SMD-02 PT Booking

| ID | Event | Type | Guard / Action (short) | Target | UC / BR |
|----|-------|------|------------------------|--------|---------|
| T1 | `bookPTPackage` | UC | ACTIVE + pay OK | Pending | UC-11, BR-06/08 |
| T2 | `confirmBooking` | UC | within 24h | Confirmed | UC-12, BR-07/08 |
| T3 | `rejectBooking` | UC | reason → refund | Rejected | UC-12, BR-07/09 |
| T4 | `after(24h)` | **Time** | no PT response → refund | Cancelled | BR-08 |
| T5 | `cancelBooking` | UC | Customer cancel | Cancelled | UC-24 |
| T6–T7 | `recordSession` | UC | Confirmed → In Progress / Completed | … | UC-15, BR-10 |
| T8 | `cancelBooking` | UC | unused sessions | Cancelled | UC-24 |
| T9–T10 | `recordSession` | UC | progress / last session | In Progress / Completed | UC-15, BR-10 |
| T11 | `cancelBooking` | UC | partial | Cancelled | UC-24 |
| T12–T14 | `archive` / `refundSettled` | System | Final | Final | BR-08/09 |

**Kết luận rà soát:** SMD-01 có **3 time events** (T5, T8, T11) gắn UC-27 / retention; SMD-02 có **1 time event** `after(24h)` (T4 / BR-08). Các transition còn lại gắn UC-05/06/11/12/15/20/24. PNG VP chưa có — chờ Thiên export.

---

## Appendix C — Traceability Matrix (preliminary)

| BO | UC-ID | FR-ID | BR-ID | Diagram | Screen | Test (planned) |
|----|-------|-------|-------|---------|--------|----------------|
| BO-01 | UC-05 | FR-05-01 Create INACTIVE membership | BR-01, BR-02 | UCD; AD-03; SMD-01; ERD-01 | SCR-05 | TC-05-01; TC-05-02 |
| BO-01 | UC-06 | FR-06-01 ACTIVE + QR | BR-02, BR-03, BR-04 | AD-03; SMD-01; ERD-01; CD | SCR-06 | TC-06-01; TC-06-02 |
| BO-02 | UC-07 | FR-07-01 Show QR | BR-04 | UCD; ERD-01 | QR view | TC-07-01 |
| BO-02 | UC-08 | FR-08-01 Check-in | BR-04, BR-05 | UCD; SMD-01; ERD-01 | SCR-08 | TC-08-01; TC-08-02 |
| BO-02 | UC-09 | FR-09-01 Check-out | BR-04, BR-05 | UCD; ERD-01 | SCR-09 | TC-09-01 |
| BO-02 | UC-27 | FR-27-01 Auto-expire (**Time**) | BR-11, BR-04 | SMD-01 T5/T8; CD Time | — batch | TC-27-01 |
| BO-03 | UC-11 | FR-11-01 Book PT | BR-06, BR-08 | UCD PT; AD-01; SMD-02; ERD-01 | SCR-11 | TC-11-01; TC-11-02 |
| BO-03 | UC-12 | FR-12-01 Confirm/Reject | BR-07, BR-08, BR-09 | AD-01; SMD-02; ERD-01 | SCR-12 | TC-12-01; TC-12-02 |
| BO-03 | UC-15 | FR-15-01 Record session | BR-10 | UCD PT; SMD-02; ERD-01 | SCR-15 | TC-15-01 |
| BO-03 | UC-16 | FR-16-01 Register PT | BR-07 | UCD; AD-02; ERD-01 | SCR-16 | TC-16-01 |
| BO-03 | UC-17 | FR-17-01 Approve PT | BR-07 | AD-02; ERD-01 | SCR-17 | TC-17-01 |
| BO-03 | — | FR-BR08 Auto-cancel Pending (**Time**) | BR-08 | SMD-02 T4 | — | TC-BR08-01 |
| BO-04 | UC-21 | FR-21-01 Report | — | CD; ERD-01 | Report UI | TC-21-01 |
| BO-04 | UC-22 | FR-22-01 Export Excel | — | CD | Report UI | TC-22-01 |
| — | UC-02 | FR-02-01 Login | BR-01 | UCD; ERD Role/Account | Login | TC-02-01 |
| — | UC-25/26 | FR-25/26 Complaint | BR-12 | UCD Feedback | Feedback UI | TC-25-01 |

Machine-readable: `04_Traceability_Matrix.csv` / `04_Traceability_Matrix.xlsx`.

---

## Analysis models index (Appendix B)

| ID | Name | Type | SRS | Image |
|----|------|------|-----|-------|
| CD-01 | Context Diagram | Context | 2.1 | `CD_ContextDiagram.png` |
| UCD-01 | Use Case Overview | Use Case | 3.1 | `UCD_Overview.png` |
| AD-03 | Activate Membership | Activity | 3.x | `AD_ActivateMembership.jpg` |
| SMD-01 | Membership Lifecycle | State | 3.x / 4.1 | *pending* `SMD_Membership.png` |
| SMD-02 | PT Booking Lifecycle | State | 3.x | *pending* `SMD_PTBooking.png` |
| ERD-01 | Conceptual ERD | ERD | 4.1 | `ERD_Conceptual.png` ✓ |

---

## Next

1. Thiên: export SMD PNG từ VP → Phước chèn Figure SMD vào SRS.  
2. Tuấn #36: review ERD Booking–PT nếu cần bổ sung TrainingSession.  
3. Bước 8 (#40): chốt RTM + zip A.3.
