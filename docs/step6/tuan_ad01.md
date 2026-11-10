# BÆ°á»›c 6 â€” Anh Tuáº¥n â€” AD-01

> Issue: #30 Â· NhÃ¡nh: `step6/tuan-ad01`

## Swimlanes (â‰¥3)

Activity Diagram AD-01 sá»­ dá»¥ng cÃ¡c swimlane sau:

1. **Customer** â€” chá»n PT package, lá»‹ch mong muá»‘n, promotion code vÃ  phÆ°Æ¡ng thá»©c thanh toÃ¡n; xÃ¡c nháº­n hoáº·c há»§y.
2. **GMS** â€” kiá»ƒm tra Ä‘iá»u kiá»‡n booking, táº¡o payment request, ghi nháº­n káº¿t quáº£, táº¡o booking vÃ  gá»­i thÃ´ng bÃ¡o.
3. **Payment Gateway** â€” tiáº¿p nháº­n yÃªu cáº§u thanh toÃ¡n vÃ  tráº£ vá» káº¿t quáº£ `Success`, `Fail` hoáº·c khÃ´ng pháº£n há»“i.
4. **Personal Trainer** â€” nháº­n booking request á»Ÿ tráº¡ng thÃ¡i `Pending` Ä‘á»ƒ xá»­ lÃ½ theo UC-12.
5. **SMS Service** â€” gá»­i thÃ´ng bÃ¡o tráº¡ng thÃ¡i booking/payment cho Customer vÃ  thÃ´ng bÃ¡o booking má»›i cho PT.

## Luá»“ng hoáº¡t Ä‘á»™ng chÃ­nh

1. Customer má»Ÿ há»“ sÆ¡ cá»§a Personal Trainer Ä‘Ã£ `Approved`.
2. Customer chá»n PT package Ä‘ang hoáº¡t Ä‘á»™ng.
3. Customer nháº­p preferred date/time, note tÃ¹y chá»n vÃ  promotion code náº¿u cÃ³.
4. GMS kiá»ƒm tra membership `ACTIVE`, PT, package, lá»‹ch vÃ  giÃ¡ hiá»‡n táº¡i.
5. Náº¿u dá»¯ liá»‡u há»£p lá»‡, GMS tÃ­nh tá»•ng tiá»n vÃ  táº¡o payment request.
6. Customer chá»n payment method vÃ  xÃ¡c nháº­n thanh toÃ¡n.
7. Payment Gateway xá»­ lÃ½ payment request.
8. GMS nháº­n káº¿t quáº£ tá»« Payment Gateway.
9. Náº¿u thanh toÃ¡n thÃ nh cÃ´ng, GMS ghi nháº­n payment vÃ  táº¡o PT booking vá»›i status `Pending`.
10. GMS gá»­i booking request cho Personal Trainer.
11. GMS gá»­i thÃ´ng bÃ¡o cho Customer vÃ  Personal Trainer qua SMS/in-app.
12. PT tiáº¿p tá»¥c xá»­ lÃ½ booking theo UC-12.

## Quyáº¿t Ä‘á»‹nh / nhÃ¡nh song song

### Decision D1 â€” Dá»¯ liá»‡u booking cÃ³ há»£p lá»‡ khÃ´ng?

- **CÃ³:** tiáº¿p tá»¥c táº¡o payment request.
- **KhÃ´ng:** hiá»ƒn thá»‹ lá»—i, yÃªu cáº§u Customer sá»­a PT/package, membership, lá»‹ch hoáº·c giÃ¡; káº¿t thÃºc luá»“ng hiá»‡n táº¡i.

### Decision D2 â€” Payment Gateway tráº£ káº¿t quáº£ gÃ¬?

- **Success:** ghi nháº­n payment, táº¡o booking `Pending` vÃ  dispatch request cho PT.
- **Fail:** ghi nháº­n payment tháº¥t báº¡i, khÃ´ng táº¡o booking há»£p lá»‡, cho phÃ©p Customer retry hoáº·c cancel.
- **Timeout/Unknown:** ghi nháº­n payment `Pending` hoáº·c `Unknown` Ä‘á»ƒ reconciliation; khÃ´ng tá»± coi lÃ  paid vÃ  khÃ´ng Ä‘Ã¡nh dáº¥u booking `Confirmed`.

### Decision D3 â€” Customer cÃ³ há»§y trÆ°á»›c khi payment hoÃ n táº¥t khÃ´ng?

- **CÃ³:** há»§y payment request náº¿u cÃ³, khÃ´ng táº¡o booking há»£p lá»‡.
- **KhÃ´ng:** tiáº¿p tá»¥c chá» vÃ  xá»­ lÃ½ káº¿t quáº£ payment.

### NhÃ¡nh song song sau payment thÃ nh cÃ´ng

Sau khi GMS ghi nháº­n payment thÃ nh cÃ´ng vÃ  táº¡o booking `Pending`, cÃ¡c hoáº¡t Ä‘á»™ng sau cÃ³ thá»ƒ Ä‘Æ°á»£c thá»±c hiá»‡n song song:

- GMS gá»­i booking request Ä‘áº¿n Personal Trainer.
- GMS gá»­i thÃ´ng bÃ¡o tráº¡ng thÃ¡i Ä‘áº¿n Customer.
- SMS Service gá»­i notification Ä‘áº¿n Customer vÃ  Personal Trainer.

CÃ¡c hoáº¡t Ä‘á»™ng nÃ y pháº£i hoÃ n táº¥t hoáº·c Ä‘Æ°á»£c ghi nháº­n retry theo cÆ¡ cháº¿ notification; viá»‡c gá»­i notification khÃ´ng Ä‘Æ°á»£c lÃ m thay Ä‘á»•i payment thÃ nh cÃ´ng thÃ nh payment tháº¥t báº¡i.

## Luá»“ng ngoáº¡i lá»‡

- **E1 â€” Package hoáº·c schedule khÃ´ng cÃ²n kháº£ dá»¥ng:** GMS tá»« chá»‘i request vÃ  yÃªu cáº§u Customer chá»n láº¡i.
- **E2 â€” Membership khÃ´ng ACTIVE:** GMS khÃ´ng cho tiáº¿p tá»¥c thanh toÃ¡n.
- **E3 â€” Payment timeout/uncertain:** payment giá»¯ á»Ÿ `Pending`/`Unknown`, chá» reconciliation.
- **E4 â€” Notification failure:** GMS ghi nháº­n lá»—i gá»­i vÃ  retry; payment/booking Ä‘Ã£ ghi nháº­n khÃ´ng bá»‹ rollback chá»‰ vÃ¬ notification lá»—i.

## Mapping vá»›i Use Case vÃ  Business Rules

- AD-01 bao phá»§ main flow vÃ  cÃ¡c alternative/exception flow chÃ­nh cá»§a `docs/step4/UC-11.md`.
- Sau khi táº¡o booking `Pending`, PT xá»­ lÃ½ theo `docs/step4/UC-12.md`.
- `BR-06`: Customer pháº£i cÃ³ membership `ACTIVE` Ä‘á»ƒ Ä‘áº·t PT package.
- `BR-08`: PT pháº£i pháº£n há»“i booking `Pending` trong 24 giá».
- Payment timeout khÃ´ng tá»± Ä‘á»™ng táº¡o tráº¡ng thÃ¡i paid hoáº·c `Confirmed`.

## PNG

- [x] `03_Images/AD_BookPT.png`

> PNG sáº½ Ä‘Æ°á»£c export tá»« Visual Paradigm sau khi ná»™i dung swimlane vÃ  cÃ¡c decision Ä‘Æ°á»£c review.
