# BÆ°á»›c 5 â€” Anh Tuáº¥n (UI UC-11, UC-12)

> Issue: #26 Â· NhÃ¡nh: `step5/tuan-ui`

## MÃ n hÃ¬nh & PNG

| UC | TÃªn mÃ n hÃ¬nh | File PNG |
|----|--------------|----------|
| UC-11 | Book a PT Package | `03_Images/UI_UC11_BookPT.png` |
| UC-12 | Manage PT Booking Requests | `03_Images/UI_UC12_PTBooking.png` |

### Tráº¡ng thÃ¡i file áº£nh

- UC-11: `03_Images/UI_UC11_BookPT.png` â€” áº£nh UI Ä‘Ã£ lÆ°u, kÃ­ch thÆ°á»›c 1342 Ã— 1600 px.
- UC-12: `03_Images/UI_UC12_PTBooking.png` â€” áº£nh UI Ä‘Ã£ lÆ°u, kÃ­ch thÆ°á»›c 1080 Ã— 1600 px.
- Hai áº£nh dÃ¹ng cÃ¹ng phong cÃ¡ch giao diá»‡n GMS PULSE: ná»n sÃ¡ng, tháº» ná»™i dung bo gÃ³c, mÃ u chá»§ Ä‘áº¡o xanh teal vÃ  bá»‘ cá»¥c desktop.

### Quyáº¿t Ä‘á»‹nh thiáº¿t káº¿ UI

1. UC-11 dÃ¹ng bá»‘ cá»¥c nhiá»u bÆ°á»›c: `Select PT` â†’ `Select Package` â†’ `Schedule` â†’ `Promotion` â†’ `Order Summary` â†’ `Payment`.
2. UC-12 dÃ¹ng mÃ n hÃ¬nh quáº£n lÃ½ booking má»™t trang, cÃ³ danh sÃ¡ch vÃ  pháº§n chi tiáº¿t.
3. Payment method hiá»ƒn thá»‹ cÃ¡c lá»±a chá»n cá»¥ thá»ƒ: `VNPay`, `MoMo`, `Credit Card`.
4. Rejection reason dÃ¹ng dropdown lÃ½ do cÃ³ sáºµn vÃ  lá»±a chá»n `Other` Ä‘á»ƒ nháº­p thÃªm.
5. UC-12 hiá»ƒn thá»‹ countdown/thá»i háº¡n pháº£n há»“i 24 giá», vÃ­ dá»¥: `18 hours remaining`.
6. TÃªn mÃ n hÃ¬nh giá»¯ lÃ  `Book a PT Package` vÃ  `Manage PT Booking Requests`.

## Báº£ng field (tÃ³m táº¯t)

| MÃ n hÃ¬nh | Field | Báº¯t buá»™c | Validation / lá»—i |
|----------|-------|----------|------------------|
| UC-11 â€” Book PT Package | PT / package | CÃ³ | Pháº£i chá»n PT Ä‘Ã£ Approved vÃ  package Ä‘ang hoáº¡t Ä‘á»™ng |
| UC-11 â€” Book PT Package | Preferred date/time | CÃ³ | KhÃ´ng Ä‘Æ°á»£c á»Ÿ quÃ¡ khá»©; pháº£i náº±m trong lá»‹ch cho phÃ©p |
| UC-11 â€” Book PT Package | Note | KhÃ´ng | Tá»‘i Ä‘a 500 kÃ½ tá»± |
| UC-11 â€” Book PT Package | Promotion code | KhÃ´ng | MÃ£ pháº£i há»£p lá»‡, cÃ²n háº¡n vÃ  Ã¡p dá»¥ng Ä‘Æ°á»£c |
| UC-11 â€” Book PT Package | Payment method | CÃ³ | Pháº£i Ä‘Æ°á»£c Payment Gateway há»— trá»£ |
| UC-12 â€” Booking detail | Decision | CÃ³ | Chá»n Confirm hoáº·c Reject |
| UC-12 â€” Booking detail | Rejection reason | CÃ³ khi Reject | KhÃ´ng Ä‘Æ°á»£c Ä‘á»ƒ trá»‘ng; tá»‘i Ä‘a 500 kÃ½ tá»± |

## Gá»£i Ã½ bá»‘ cá»¥c wireframe

### UC-11 â€” Book a PT Package

- Header: `Gym Management System`, Customer navigation, vÃ  tiÃªu Ä‘á» mÃ n hÃ¬nh.
- Step 1: chá»n PT, hiá»ƒn thá»‹ tÃªn, há»“ sÆ¡ tÃ³m táº¯t vÃ  tráº¡ng thÃ¡i Approved.
- Step 2: chá»n package, sá»‘ buá»•i, thá»i háº¡n vÃ  giÃ¡.
- Schedule: chá»n preferred date/time vÃ  nháº­p note.
- Promotion: nháº­p promotion code vÃ  hiá»ƒn thá»‹ káº¿t quáº£ validation.
- Order summary: PT, package, giÃ¡ gá»‘c, giáº£m giÃ¡, tá»•ng tiá»n vÃ  payment method.
- Actions: `Cancel` vÃ  `Pay & Confirm Booking`.
- ThÃ´ng bÃ¡o lá»—i pháº£i hiá»ƒn thá»‹ gáº§n field bá»‹ lá»—i; khÃ´ng cho submit khi thiáº¿u field báº¯t buá»™c.
- áº¢nh hiá»‡n táº¡i thá»ƒ hiá»‡n tráº¡ng thÃ¡i thanh toÃ¡n thÃ nh cÃ´ng táº¡o booking `Pending` vÃ  gá»­i yÃªu cáº§u Ä‘áº¿n Personal Trainer.

### UC-12 â€” Manage PT Booking Requests

- Header: `Gym Management System`, PT navigation, vÃ  tiÃªu Ä‘á» quáº£n lÃ½ booking.
- Bá»™ lá»c: Pending, Confirmed, Rejected.
- Má»—i booking hiá»ƒn thá»‹ booking ID, Customer, package, preferred time, thá»i Ä‘iá»ƒm táº¡o vÃ  thá»i háº¡n pháº£n há»“i 24 giá».
- Chi tiáº¿t booking hiá»ƒn thá»‹ note cá»§a Customer vÃ  payment status.
- Actions: `Confirm` vÃ  `Reject`.
- Khi chá»n `Reject`, hiá»ƒn thá»‹ trÆ°á»ng `Rejection reason` báº¯t buá»™c.
- Sau khi xá»­ lÃ½, hiá»ƒn thá»‹ tráº¡ng thÃ¡i má»›i vÃ  thÃ´ng bÃ¡o káº¿t quáº£.
- áº¢nh hiá»‡n táº¡i hiá»ƒn thá»‹ countdown pháº£n há»“i, tráº¡ng thÃ¡i thanh toÃ¡n `Paid`, nÃºt `Confirm Booking`, nÃºt `Reject Booking` vÃ  form rejection reason.

## LiÃªn há»‡ vá»›i Ä‘áº·c táº£ Use Case

Wireframe pháº£i Ä‘á»‘i chiáº¿u vá»›i cÃ¡c file fully dressed:

- `docs/step4/UC-11.md`
- `docs/step4/UC-12.md`

CÃ¡c field vÃ  tráº¡ng thÃ¡i trÃªn UI pháº£i há»— trá»£ main flow, alternative flows vÃ  exceptions Ä‘Ã£ mÃ´ táº£ trong hai file nÃ y.
