# Step 1 — Huy (Owner / Reporting / Constraints)

> Issue: #8 · Milestone: Step 1 due 16/11/2026

## 1. User class — Gym Owner (SRS §2.2)

| User class | Description | Frequency of use | Level / skills | Main privileges | Favored? |
|---|---|---|---|---|---|
| Gym Owner | Owner or manager of the gym, directly operating at the front desk | Medium–High: front-desk operations multiple times a day, report review at least once a week | Intermediate: proficient with browsers and Excel, no technical background | Register and activate memberships (UC-05, UC-06), approve PT accounts (UC-17), manage package catalog, handle complaints, create and export reports (UC-21, UC-22) | **Yes**: the Owner is responsible for business operations and decision-making, so when requirements conflict, Owner requirements take priority |

## 2. §2.3 Operating environment

- OE-1: The system runs on the web and displays correctly in Chrome and Edge (latest 2 versions) with a responsive interface.
- OE-2: Front desk uses a computer or tablet; the tablet at the entrance uses a camera to scan QR codes.
- OE-3: The server is hosted on a Linux cloud, accessed via HTTPS; data is stored in a shared relational database for all actors.
- OE-4: External integrations: Payment Gateway via REST API, SMS Service via API, QR generation and verification module.

## 3. §2.4 Design and implementation constraints

- CON-1: Comply with Decree 13/2023/NĐ-CP when collecting and processing personal data of customers (ID card, phone number, email).
- CON-2: Interface in Vietnamese; currency is **VND**; time zone is **UTC+7**; dates are displayed in **dd/mm/yyyy** format.
- CON-3: All UML, DFD, and ERD diagrams are created using **Visual Paradigm** and submitted as `.vpp` files; wireframes are created in Figma, Stitch, or draw.io.
- CON-4: Online payments are processed through an external Payment Gateway; the system does not store customers' card numbers.
- CON-5: Release 1 serves one gym location.
- CON-6: Each submission step follows the milestone deadline on GitHub (Step 1 due 16/11/2026); the final assignment submission deadline follows the lecturer's announcement.

## 4. Reporting and payment scope (Release 1)

| In scope (Release 1) | Out of scope / Future release |
|---|---|
| Create operational reports: revenue, check-ins, completed PT sessions (UC-21) | Full ERP accounting integration |
| Export reports to Excel files (UC-22) | PDF export; user-customizable dashboard |
| Process membership and PT package payments through a payment gateway, and collect cash at the front desk | Build the payment gateway internally; store card information |
| Refund via payment gateway when PT rejects or no response within 24 hours (BR-08, BR-09) | Multi-branch, multi-currency operations |
| Receive and process basic complaints (UC-25, UC-26) | Electronic invoices, tax declaration |

## 5. BO-04 (measurable)

| ID | Business goal | Measurement metric |
|---|---|---|
| BO-04 | The gym owner makes operational decisions based on data instead of manual statistics | In the first 3 months after deployment: (1) ≥ 90% of monthly report exports to Excel are completed within **≤ 60 seconds**; (2) the Owner opens the report **at least once a week** in ≥ 10 out of 12 weeks |

**Measurement method:**

- **Metric (1) — report export time:** run 20 times in a test environment with data for 1 month including 500 active memberships, 15,000 check-ins, and 400 PT bookings. Measure the time from when the Owner clicks "Create report" to when the `.xlsx` file is downloaded. Success is achieved when at least 18 out of 20 runs are ≤ 60 seconds (equivalent to 90%).
- **Metric (2) — usage level:** count from system logs the number of weeks in the first 12 weeks with at least one report page open by the Owner. Success is achieved when there are ≥ 10 out of 12 weeks.

## 6. BR / Customer service (draft; official key group finalized in Step 3)

| ID | Business rule | Type | Source |
|---|---|---|---|
| BR-12 | Complaints can only be created within **7 days** after the training session or related event | Constraint | CSKH |
| BR-13 | When a PT booking is rejected or no response is received within 24 hours, the system refunds **100%** of the collected amount within **3 working days**, back to the original payment method (payment gateway or cash at the front desk), without deducting transaction fees | Action enabler | CSKH / Finance |

## 7. References (§1.4)

1. SWR302 Team, `HuongDan_Assignment.md` — SRS assignment guide, FPT University.
2. Government of Vietnam, *Decree 13/2023/NĐ-CP on personal data protection*, 17/04/2023.
3. Visual Paradigm Community — UML/ERD tutorial documents (https://www.visual-paradigm.com).
4. Wiegers, K. & Beatty, J., *Software Requirements*, 3rd Edition, Microsoft Press, 2013 — chapters 11, 12, 14, and 17 are referenced.
5. IEEE Std 830-1998, *IEEE Recommended Practice for Software Requirements Specifications*.
6. `kimi2.5-project.md` — initial project idea of the team.
