# Step 3 — Tuan (PT UCD package)

> Issue: #16 · Branch: `step3/tuan-ucd-pt`

## Package / UCs in the PT package

The `PT Booking` package within Tuan's assigned scope includes:

- UC-11 — Book a PT package (Customer)
- UC-12 — Confirm / Reject PT booking (Personal Trainer)

Related secondary actors:

- Payment Gateway: processes payment for UC-11 and refunds when a booking is rejected in UC-12.
- SMS Service: sends booking notifications and processing results for both UC-11 and UC-12.
- No separate notification UC is created; SMS Service is represented as a secondary actor.

## Include / extend relationships used

| Relationship | From | To | Reason |
|---------|----|-----|-------|
| `<<include>>` | UC-11 Book a PT package | UC-Pay Process payment | Online payment is mandatory when booking a PT package |
| `<<extend>>` | Apply promotion code | UC-11 Book a PT package | Occurs only when the Customer enters a promotion code |
| Alternative flow | UC-12 Confirm / Reject PT booking | Confirm / Reject | Two alternative branches; not represented by `<<extend>>` |

`UC-Pay Process payment` is drawn as a supporting technical use case and is not counted as a primary business use case.

## Exported PNG

- [ ] `03_Images/UCD_PT.png` (hoặc tên tương đương)

## Notes

- The UC and actor list is cross-checked against `docs/02_UC_List_Detailed.md`.
- This package covers only Tuan's direct Step 3 scope; other PT UCs are listed in the team's master UC document.
- In Visual Paradigm, associate Customer with UC-11; Personal Trainer with UC-12; Payment Gateway with UC-Pay; and SMS Service with both UC-11 and UC-12.
- Confirm and Reject in UC-12 are alternative flows, not an `<<extend>>` relationship.
