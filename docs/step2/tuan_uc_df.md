# Step 2 — Tuan (DF + PT-domain UCs)

> Issue: #11 · Branch: `step2/tuan-uc-df`

## Data flows (PT domain)

| ID | From | To | Data |
|----|------|----|------|
| DF-15 | Customer | GMS | PT, PT package, preferred schedule, notes |
| DF-16 | GMS | Personal Trainer | Pending booking details |
| DF-17 | Personal Trainer | GMS | Confirm / Reject + reason if rejected |
| DF-18 | GMS | SMS Service | Phone number + SMS content |
| DF-19 | SMS Service | GMS | Delivered / Failed |

## Use cases (PT domain)

| UC-ID | Name | Primary actor | Short description |
|-------|-----|-------------|------------|
| UC-11 | Book a PT package | Customer | Create a Pending booking and make payment |
| UC-12 | Confirm / Reject PT booking | Personal Trainer | The PT responds to the booking within 24 hours |

## Notes

- DF-15 to DF-19 are cross-checked against `docs/02_Context_Diagram_DataFlows.md`.
- UC-11 has Payment Gateway, SMS Service, and Personal Trainer as secondary actors.
- UC-12 has SMS Service and Payment Gateway as secondary actors.
- DF-07 and DF-08 are shared payment data flows; UC-11 uses both flows.
- Confirm and Reject are alternative flows within UC-12, not two `<<extend>>` use cases.
