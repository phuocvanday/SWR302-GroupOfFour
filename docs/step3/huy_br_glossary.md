# Step 3 — Huy (BR + Glossary + UCD Report/Feedback)

> Issue: #18 · Branch: `step3/huy-br-glossary`

## Business Rules

| BR-ID | Description | Type | Related UC |
|-------|-------------|------|------------|
| BR-01 | A customer can only check in when the membership is in **ACTIVE** status and still within its valid period. | Constraint | UC-08, UC-09 |
| BR-02 | Each QR check-in code is valid for only **60 seconds** and can be used **once** to prevent fraud through screenshots shared with others. | Security / Constraint | UC-07, UC-08 |
| BR-03 | Each PT account can only be approved by the **Gym Owner** after full verification of professional qualifications and certificates. | Action Enabler | UC-16, UC-17 |
| BR-04 | A customer can only book PT sessions if their personal membership is in **ACTIVE** status. | Constraint | UC-11 |
| BR-05 | PT bookings must be made at least **24 hours** before the desired session start time. | Timing / Constraint | UC-11, UC-12 |
| BR-06 | A PT has up to **24 hours** to respond (confirm/reject) to a customer's booking request. If no response is received within 24 hours, the system automatically cancels the booking and refunds 100% of the amount. | Timing / Action Enabler | UC-12 |
| BR-07 | A PT session is only recorded as **Completed** when the PT performs check-in for the member and clicks "Record Session" after finishing. | Computation / Constraint | UC-15 |
| BR-08 | When a customer submits feedback/complaints, the system must notify the Gym Owner within **5 minutes**. | Action Enabler | UC-25 |
| BR-09 | Customer complaints can only be created within **7 days** of the related incident or training session. | Constraint | UC-25, UC-26 |
| BR-10 | If a PT booking is rejected or automatically canceled due to the 24-hour timeout, the system refunds **100%** of the amount to the original payment method within **3 working days**. | Action Enabler | UC-12, UC-23 |
| BR-11 | Operational and revenue reports can only be viewed and exported by accounts with **Gym Owner** privileges. | Authorization | UC-21, UC-22, UC-24 |
| BR-12 | Exported report files must be in `.xlsx` format (Microsoft Excel) and must support download within **60 seconds** for datasets below 50,000 records. | System Requirement | UC-22 |

## Glossary (Technical terms)

| Term | Definition |
|------|------------|
| **Gym Owner** | The owner or highest-level manager of the gym, with full administrative rights over the system, approval of PT accounts, and access to financial/operational reports. |
| **Personal Trainer (PT)** | A personal trainer who directly teaches, manages training schedules, and records sessions with members. |
| **Membership Package** | A training package for members (e.g., 1 month, 3 months, 1 year) that defines access to the gym and the associated benefits. |
| **PT Package** | A personal training service package created by the PT or gym (e.g., 8 sessions, 12 sessions), distinct from the gym membership package. |
| **QR Check-in / Check-out** | The process of scanning a dynamic QR code in the mobile app to open the gate automatically or confirm the member's entry/exit time. |
| **Active Membership** | A membership status where the package has been fully paid for and is still within the valid usage period. |
| **Pending Booking** | A PT booking request that has been paid for by the member but is awaiting PT confirmation or rejection. |
| **Training Session** | A specific training session planned and confirmed within a PT package between the member and PT. |
| **Operational Report** | A summary report of gym operations including revenue, new member numbers, check-in/out counts, and PT session completion rates. |
| **Feedback / Grievance** | Responses, evaluations, or complaints from customers sent to the gym management regarding service quality or PT behavior. |

## UCD Report / Feedback (Use Case Diagram Package)

- **PNG:** `03_Images/UCD_Report_Feedback.png`
- **Notes:**
  - The diagram includes **Gym Owner** as the main actor interacting directly with the use cases: `UC-21: Generate Reports`, `UC-22: Export Excel Report`, `UC-24: View Dashboard`, and `UC-26: Process Feedback`.
  - The **Customer** and **PT** actors interact with `UC-25: Send Feedback / Complaint`.
  - The `<<include>>` relationship: `UC-22 (Export Excel Report)` must inherit data from `UC-21 (Generate Reports)`.
  - The `<<extend>>` relationship: `UC-26 (Process Feedback)` expands handling when new feedback arrives from `UC-25 (Send Feedback)`.
  - The full diagram is designed and exported as a PNG image (≥ 150 dpi) from **Visual Paradigm Community** and saved in the folder `02_Models/GMS.vpp`.