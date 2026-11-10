# Bước 3 — Anh Tuấn (UCD package PT)

> Issue: #16 · Branch: `step-3`  
> Package diagram for Visual Paradigm: **UCD-04 PT** · Export: `03_Images/UCD_PT.png`

## Package / UC trong package PT

| UC-ID | Name on oval (Verb + Noun) | Primary | Secondary |
|-------|----------------------------|---------|-----------|
| UC-10 | View PT Profiles | Customer | — |
| UC-11 | Book PT Package | Customer | Payment Gateway, SMS, PT |
| UC-12 | Confirm/Reject PT Booking | Personal Trainer | SMS, Payment Gateway |
| UC-13 | Create Training Schedule | Personal Trainer | SMS |
| UC-14 | View Training Schedule | Customer, PT | — |
| UC-15 | Record Training Session | Personal Trainer | — |
| UC-16 | Register PT Account | Personal Trainer | — |
| UC-17 | Approve PT Account | Gym Owner | SMS |
| UC-18 | Manage PT Packages | Personal Trainer | — |
| UC-24 | Cancel PT Booking | Customer | Payment Gateway, SMS |

**Supporting UCs (include/extend):**

| Name | Role |
|------|------|
| Process Payment | «include» from Book / Cancel (refund) |
| Apply Promo Code | «extend» Book PT Package at `PromoApplication` |

## Include / extend đã dùng

| Quan hệ | Từ | Tới | Lý do |
|---------|----|-----|-------|
| «include» | Book PT Package | Process Payment | Always charge when booking online |
| «include» | Cancel PT Booking | Process Payment | Refund path when policy allows |
| «extend» | Apply Promo Code | Book PT Package | Optional discount at `PromoApplication` |

**Không dùng «extend» cho Confirm/Reject** — đó là **alternative flows** trong UC-12.

## Actor generalization (shared with Overview)

`User <|-- Customer`, `User <|-- Personal Trainer`, `User <|-- Gym Owner`

## PNG đã export

- [x] `03_Images/UCD_PT.png` (PlantUML draft for VP redraw if needed)
- Source: `02_Models/UCD-04_PT.puml`

## Ghi chú

Redraw/confirm in `GMS.vpp` under package **PT** so the official submission uses Visual Paradigm export.
