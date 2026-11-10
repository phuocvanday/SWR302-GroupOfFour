# Step 2 — Huy (DF + UC Owner / Report / Feedback / Time)

> Issue: #13 · Branch: `step2/huy-uc-df`

## 1. External entities in charge (for the Context Diagram)

| Entity Name | Type | Interaction description |
|---|---|---|
| **Payment Gateway** | External System | Payment gateway (VNPay/Momo/Stripe) processes online transactions and sends payment/refund confirmations back to the system |
| **SMS Service** | External System | SMS service (Twilio/Vonage) receives content from GMS to send OTP codes, activation notifications, and schedule reminders |
| **Timer / Time Event** | Temporal Event | Time-based trigger that automatically activates system tasks: membership expiration, automatic booking cancellation after 24 hours |

---

## 2. Data flows

| ID | From | To | Data Flow Content |
|---|---|---|---|
| DF-01 | PT | GMS | PT account registration information (full name, certificates, experience, specialization) |
| DF-02 | Gym Owner | GMS | Decision to approve/reject a PT account and the rejection reason (if any) |
| DF-03 | GMS | PT | Notification of PT account approval result |
| DF-04 | Gym Owner | GMS | Report filtering criteria (time range, report type: revenue/check-in/PT) |
| DF-05 | GMS | Gym Owner | Report data displayed on screen and exported file in `.xlsx` format |
| DF-06 | Customer / PT | GMS | Complaint/feedback content about service quality |
| DF-07 | GMS | Gym Owner | List of feedback/complaints requiring review and resolution |
| DF-08 | GMS | Payment Gateway | Refund request when PT rejects or exceeds the 24-hour response window |
| DF-09 | Payment Gateway | GMS | Refund status: successful or failed |
| DF-10 | GMS | SMS Service | SMS content to be sent to Customer/PT |

---

## 3. Responsible use cases (complete according to Issue #13)

| UC-ID | Use Case Name | Primary Actor | Short description |
|---|---|---|---|
| **UC-16** | Register PT Account | Personal Trainer | The PT submits a PT account registration with competency profile information to the system. |
| **UC-17** | Approve PT Account | Gym Owner | The Owner reviews the profile and approves or rejects the PT account. |
| **UC-21** | Generate Reports | Gym Owner | The system consolidates revenue, check-in, and PT training data to display reports. |
| **UC-22** | Export Excel Report | Gym Owner | Export operational report data to an Excel file (`.xlsx`). |
| **UC-23** | Process Payment & Refund | Payment Gateway | Handle online payment transactions and automatic refunds when bookings are canceled. |
| **UC-25** | Submit Feedback/Complaint | Customer / PT | The user submits feedback or complaints about issues/training sessions. |
| **UC-26** | Process Complaint | Gym Owner | The Owner views the list, updates the handling status, and responds to complaints. |
| **UC-28** | Auto-Cancel Pending Booking | Timer | The system automatically cancels a booking and triggers a refund if the PT does not respond within 24 hours. |

---