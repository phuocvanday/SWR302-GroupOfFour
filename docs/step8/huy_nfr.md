# Step 8 — Huy (NFR)

> Issue: #39 · Branch: `step8/huy-nfr`

## Measurable Non-Functional Requirements (NFR)

| NFR-ID | Description | Measurement Method | Target Metric |
|--------|-------------|-------------------|---------------|
| **NFR-PERF-01** | **System Response Time:** Member lookup and check-in operations must respond quickly during peak hours. | Measure API Response Time via performance testing tools (JMeter) or browser Network tab under 100 concurrent requests. | Average response time $\le 1.5$ seconds; no request shall exceed 3 seconds. |
| **NFR-SEC-01** | **Password Security:** User passwords (Member, PT, Owner) must be securely encrypted before storing in the database. | Direct inspection of the `Account` table in SQL Server Management Studio to verify no plain-text passwords exist. | Standard password hashing algorithm (e.g., BCrypt with work factor $\ge 10$). |
| **NFR-SEC-02** | **Session Timeout Control:** The system must automatically invalidate user sessions after a prolonged period of inactivity. | Track active session/token status after maintaining an idle screen state for 15 minutes. | Automatically log out and redirect to the login page after exactly 15 minutes of inactivity. |
| **NFR-USAB-01** | **Usability:** The management interface must be intuitive, enabling new receptionists to complete member check-ins or package registrations quickly. | Conduct User Acceptance Testing (UAT) with 5 new users, timing member check-in execution. | 100% of users complete core tasks in under 30 seconds without requiring complex documentation. |
| **NFR-REL-01** | **Availability & Data Backup:** Gym management data must be protected against loss using automated scheduled backups. | Verify automatic script execution (Backup Schedule) within the database engine. | Automated daily full database backups executed at the end of each operating day. |

## External Interfaces & Technical Constraints

- **External Interfaces:**
  - **Barcode / Check-in Scanner:** Interface integrates with barcode scanners or cameras for scanning member QR codes during check-in operations.
  - **Payment Gateway:** Invoice recording interface supports flexible payment methods (Cash, Bank Transfer, E-Wallets, or online payment gateways).
  - **Browser Compatibility:** Web interface is fully responsive across standard modern browsers (Google Chrome, Microsoft Edge, Firefox, Safari) on desktop computers and reception tablets.

### System User Interface Wireframes:

* **Register Membership (UC-05):**
  ![Register Membership](../03_Images/UI_UC-05_RegisterMembership.png)

* **Activate Membership (UC-06):**
  ![Activate Membership](../03_Images/UI_UC-06_ActivateMembership.png)

* **QR Check-in (UC-08):**
  ![QR Check-In](../03_Images/UI_UC-08_QRCheckIn.png)

* **Record PT Session (UC-15):**
  ![Record Session](../03_Images/UI_UC-15_RecordSession.png)

* **Register PT Schedule (UC-16):**
  ![Register PT](../03_Images/UI_UC-16_RegisterPT.png)

* **Approve PT Schedule (UC-17):**
  ![Approve PT](../03_Images/UI_UC-17_ApprovePT.png)

- **Technical Constraints:**
  - **Core Technology Stack:** Backend developed using Java / Spring Framework, paired with Microsoft SQL Server Management Studio, deployed on an Apache Tomcat web server environment.
  - **Transmission Security:** All data exchanged between client and server must use HTTPS/TLS encryption protocols.
  - **Version Control Guidelines:** Strict adherence to team Git branching strategy, maintaining clean commit histories and submitting Pull Requests with Code Reviews prior to merging into main development branches.