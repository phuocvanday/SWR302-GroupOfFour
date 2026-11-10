# Step 3 — Phuoc (Leader): UCD-01 Overview (reference sample)

> Issue **#15** · Branch `step-3`  
> This is a **draft to redraw in Visual Paradigm**. Official submission = diagrams inside `02_Models/GMS.vpp`.

## Files for reference

| File | Purpose |
|------|---------|
| `02_Models/UCD-01_Overview.puml` | PlantUML source (open in VS Code / plantuml.com) |
| `03_Images/UCD_Overview_DRAFT.png` | Layout draft (if generated) |
| `docs/02_UC_List_Detailed.md` | Full UC list (translate names to English Verb+Noun) |

## What to draw in Visual Paradigm (`GMS.vpp`)

1. **Diagram → New → Use Case Diagram** → name: `UCD-01 Overview`
2. System boundary rectangle: **GMS**
3. Actors + generalization:

```text
User  <|--  Customer
User  <|--  Personal Trainer
User  <|--  Gym Owner
```

Secondary (outside / linked as needed): `Payment Gateway`, `SMS Service`, `QR Service`, `Time / Scheduler`

4. **High-priority use cases (English Verb + Noun)** inside GMS:

| ID | Name on diagram |
|----|-----------------|
| UC-01 | Register Customer Account |
| UC-02 | Login |
| UC-05 | Register Membership (at Counter) |
| UC-06 | Activate Membership |
| UC-07 | View Membership QR |
| UC-08 | Check-in by QR |
| UC-09 | Check-out by QR |
| UC-11 | Book PT Package |
| UC-12 | Confirm/Reject PT Booking |
| UC-15 | Record Training Session |
| UC-16 | Register PT Account |
| UC-17 | Approve PT Account |
| UC-19 | View Notifications |
| UC-20 | Renew Membership |
| UC-21 | Generate Operational Report |
| UC-23 | Manage Membership Packages |
| UC-25 | Submit Complaint/Feedback |
| UC-26 | Handle Complaint |
| UC-27 | Expire Membership (auto) |

5. **Supporting UCs (for include/extend only)** — still inside boundary:

| Name | Role |
|------|------|
| Process Payment | «include» from UC-11, UC-20 |
| Generate QR Code | «include» from UC-06 |
| Validate QR Code | «include» from UC-08, UC-09 |
| Enter Code Manually | «extend» → UC-08 |
| Apply Promo Code | «extend» → UC-05 / UC-11 |

6. **Must-have relationships (rubric)**

| Type | From | To |
|------|------|-----|
| «include» | Book PT Package | Process Payment |
| «include» | Renew Membership | Process Payment |
| «include» | Activate Membership | Generate QR Code |
| «include» | Check-in by QR | Validate QR Code |
| «extend» | Enter Code Manually | Check-in by QR |
| «extend» | Apply Promo Code | Register Membership / Book PT Package |
| generalization | User | Customer, Personal Trainer, Gym Owner |

7. **Do NOT** draw Confirm «extend» Reject — both are alternative flows **inside UC-12**.

8. Export PNG → `03_Images/UCD_Overview.png`  
   Caption in SRS:
```text
Figure 3.1 – UCD-01 Use Case Overview of the Gym Management System (GMS)
```

## Note

Overview can stay “High UCs only”. Detail packages (Membership / PT / Report / Feedback) are separate diagrams for Tuan / Thien / Huy (#16–#18).
