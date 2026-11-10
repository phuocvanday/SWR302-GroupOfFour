# Step 5 — Huy (UI UC-16, UC-17)

> Issue: #28 · Branch: `step5/huy-ui`

## Screens & PNG

| UC | Screen name | PNG file |
|----|-------------|----------|
| UC-16 | Personal Trainer Registration Form | `03_Images/UI_UC-16_RegisterPT.png` |
| UC-17 | PT Account Approval Screen (Gym Owner) | `03_Images/UI_UC-17_ApprovePT.png` |

---

## 1. UC-16 screen: PT registration form

![UI UC-16 Register PT](../../03_Images/UI_UC-16_RegisterPT.png)

---

## 2. UC-17 screen: PT account approval (Gym Owner)

![UI UC-17 Approve PT](../../03_Images/UI_UC-17_ApprovePT.png)

---

## Field table (summary)

| Screen | Field | Required | Validation / error |
|--------|-------|----------|------------------|
| UC-16 (Register PT) | Full name | Yes | Not empty, 2 - 50 characters |
| UC-16 (Register PT) | Phone number | Yes | Exactly 10 digits, valid VN format (03x, 05x, 07x, 08x, 09x), not already registered |
| UC-16 (Register PT) | Email | Yes | Must match standard email format, not already registered |
| UC-16 (Register PT) | Password | Yes | Minimum 8 characters, at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character |
| UC-16 (Register PT) | Confirm password | Yes | Must match the Password field exactly |
| UC-16 (Register PT) | Specialty | Yes | At least one specialty must be selected (Gym, Yoga, Boxing, Crossfit...) |
| UC-16 (Register PT) | Years of experience | Yes | Positive integer from 0 to 40 |
| UC-16 (Register PT) | Certificate / Degree file | Yes | PDF/JPG/PNG format, file size < 5MB per file |
| UC-17 (Approve PT) | Status filter | No | Select one of: All, Pending, Approved, Rejected |
| UC-17 (Approve PT) | Rejection reason | Yes (when Reject) | Required when clicking Reject, length 10 - 200 characters |

---

## Text Wireframe Layout Reference

### 1. Wireframe UC-16: PT registration form (`UI_UC-16_RegisterPT.png`)

```text
+-----------------------------------------------------------------------+
| GYM MANAGEMENT SYSTEM (GMS) - PERSONAL TRAINER ACCOUNT REGISTRATION  |
+-----------------------------------------------------------------------+
|                                                                       |
|  [!] Please fill in all details below to submit the PT approval form. |
|                                                                       |
|  Full name (*):      [ Nguyen Van A                         ]         |
|  Phone number (*):   [ 0912345678                           ]         |
|  Email (*):          [ pt.nguyenvana@gmail.com             ]         |
|  Password (*):       [ ••••••••••••                         ]         |
|  Confirm password (*): [ ••••••••••••                         ]         |
|                                                                       |
|  Specialty (*):      [x] Gym/Fitness  [ ] Yoga  [x] Kickboxing        |
|  Experience (*):     [ 3 ] years                                       |
|                                                                       |
|  Upload certificate(*):                                               |
|  +-----------------------------------------------------------------+  |
|  | [Choose File] Certificate_NASM.pdf (1.2 MB)                     |  |
|  +-----------------------------------------------------------------+  |
|                                                                       |
|  Personal description:                                                |
|  +-----------------------------------------------------------------+  |
|  | Specialized in fat loss, muscle gain, and rehabilitation...    |  |
|  +-----------------------------------------------------------------+  |
|                                                                       |
|         [ CANCEL ]                     [ SUBMIT REGISTRATION ]          |
+-----------------------------------------------------------------------+
```

### 2. Wireframe UC-17: PT account approval (`UI_UC-17_ApprovePT.png`)

```text
+-----------------------------------------------------------------------+
| GYM MANAGEMENT SYSTEM - PT PROFILE MANAGEMENT & APPROVAL (GYM OWNER) |
+-----------------------------------------------------------------------+
| Dashboard | Members | Book PT | [Approve PT (3)] | Reports | Logout | 
+-----------------------------------------------------------------------+
|                                                                       |
| Pending PT application list:                                          |
| Search: [ enter name/phone... ]   Status: [ Pending v ]               |
|                                                                       |
| +-------------------------------------------------------------------+ |
| | PT ID: PT004 | Nguyen Van A | Phone: 0912345678                  | |
| | Specialty: Gym/Fitness, Kickboxing | Experience: 3 years          | |
| | Certificate file: [Certificate_NASM.pdf (Download)]              | |
| | Registration date: 10/11/2026 14:30                              | |
| |                                                                   | |
| | [ VIEW PROFILE ]      [ REJECT ]      [ APPROVE ]                 | |
| +-------------------------------------------------------------------+ |
|                                                                       |
| Modal when choosing Reject:                                            |
| +-------------------------------------------------------------------+ |
| | CONFIRM REJECTION OF PROFILE PT004                                 | |
| | Enter rejection reason (*):                                        | |
| | +---------------------------------------------------------------+ | |
| | | Certificate does not meet the gym's required standards...     | | |
| | +---------------------------------------------------------------+ | |
| |              [ CANCEL ]           [ CONFIRM REJECTION ]            | |
| +-------------------------------------------------------------------+ |
+-----------------------------------------------------------------------+
```