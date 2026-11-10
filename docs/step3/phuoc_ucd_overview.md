# Step 3 — UCD Overview (Phước / #15)

## Deliverables

| Item | Path |
|------|------|
| PlantUML source (FULL associations) | `02_Models/UCD-01_Overview.puml` |
| Draft PNG | `03_Images/UCD_Overview_DRAFT.png` |
| Official diagram | Draw in Visual Paradigm → `GMS.vpp` → export `03_Images/UCD_Overview.png` |
| SRS | §3.1 figure + short description |

## What is drawn (Overview)

### Actors

| Actor | Type |
|-------|------|
| User | Generalized parent |
| Customer, Personal Trainer, Gym Owner | Specialize User |
| Payment Gateway, SMS Service, QR Service | Secondary |
| Time / Scheduler | System clock (UC-27, UC-28) |

### Actor → Use Case associations (full)

**User:** Login, View Notifications  

**Customer:** Register Account, Update Profile, View Packages, View Membership QR, Check-in/out, View PT Profiles, Book PT Package, View Training Schedule, Renew Membership, Cancel PT Booking, Submit Complaint  

**PT:** Update Profile, Confirm/Reject Booking, Create/View Schedule, Record Session, Register PT Account, Manage PT Packages  

**Owner:** Register Membership (counter), Activate Membership, Approve PT, Renew (assist), Operational Report, Export Excel, Manage Packages, Handle Complaint  

**Time:** Expire Membership, Remind Training Schedule  

**Secondary:** Payment Gateway ↔ Process Payment (+ dashed to UC-05/12/20/24); SMS on notify UCs; QR Service on Generate/Validate QR  

### Include / Extend

| Relation | From (base / extender) | To | Note |
|----------|------------------------|-----|------|
| `<<include>>` | Book PT Package, Renew, Cancel PT Booking, Register Membership | Process Payment | Always needed when money moves |
| `<<include>>` | Activate Membership | Generate QR Code | Always create QR |
| `<<include>>` | Check-in / Check-out | Validate QR Code | Always validate |
| `<<extend>>` | Enter Code Manually | Check-in by QR | Optional when camera fails |
| `<<extend>>` | Apply Promo Code | Register Membership / Book PT Package | Optional discount |

**Do NOT model Confirm/Reject as extend** — those are alternative flows inside UC-12.

### Actor generalization

`User <|-- Customer`, `User <|-- Personal Trainer`, `User <|-- Gym Owner`

## Visual Paradigm redraw checklist

1. Open `02_Models/GMS.vpp` → new diagram **UCD-01 Use Case Overview**.
2. Actors + generalization as above.
3. Place High UCs + supporting UCs (Process Payment, Generate/Validate QR, Enter Code Manually, Apply Promo).
4. Draw **all** associations listed above (solid lines actor→UC).
5. Draw `<<include>>` / `<<extend>>` dashed arrows with stereotypes (**direction matters**):
   - include: base → included
   - extend: extending → base
6. Export PNG → `03_Images/UCD_Overview.png` (replace DRAFT when done).
7. Paste into SRS §3.1; caption: *Figure 3.1 — Use Case Overview Diagram of GMS*.

## Naming

English **Verb + Noun** (e.g. `Book PT Package`, not `Booking`).
