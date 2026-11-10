# Step 7 — Data Dictionary & Conceptual ERD

> Issue: #35 · Branch: `step7/erd-datadict`

## 1. Entity Relationship Diagram (Conceptual ERD)

- **PNG diagram file**: `03_Images/ERD_Conceptual.png`
- **Number of core entities**: 11 core entities.
- **Summary of relationships & cardinality**:
  - `Role` (1) ── (N) `Account`
  - `Account` (1) ── (1) `Gym_Owner` / `Member` / `Personal_trainer`
  - `Member` (1) ── (N) `Customer_Membership`
  - `Membership_Package` (1) ── (N) `Customer_Membership`
  - `Member` (1) ── (N) `Booking`
  - `Personal_trainer` (1) ── (N) `Booking`
  - `Member` (1) ── (N) `Check_In`
  - `Member` (1) ── (N) `Payment`
  - `Equipment_inventory` (1) ── (N) `Maintenance_Log`
  - `Gym_Owner` (1) ── (N) `Maintenance_Log`

---

## 2. Data Dictionary

### 2.1. Table `Account`
Description: Stores login credentials and system authorization information.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `accountID` | `INT` | PK | No | Account identifier |
| `UserName` | `VARCHAR(50)` | - | No | System username |
| `Password_Hash` | `VARCHAR(255)`| - | No | Hashed password |
| `Status` | `VARCHAR(20)` | - | No | Account status (ACTIVE, PENDING, BLOCKED) |
| `RoleID` | `INT` | FK | No | Link to `Role` table |
| `Member_ID` | `INT` | FK | Yes | Link to Member profile (if the account belongs to a member) |

### 2.2. Table `Role`
Description: Defines roles in the system (Gym Owner, Member, PT).

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `RoleID` | `INT` | PK | No | Role code |
| `RoleName` | `VARCHAR(50)` | - | No | Role name (Admin, Owner, PT, Member) |
| `Description` | `VARCHAR(255)`| - | Yes | Description of role permissions |

### 2.3. Table `Gym_Owner`
Description: Detailed information about the gym owner/manager.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Owner_ID` | `INT` | PK | No | Gym owner/manager identifier |
| `FullName` | `VARCHAR(100)`| - | No | Full name of the gym owner |
| `Authority_Level` | `VARCHAR(50)` | - | No | Authority level (Owner, SuperAdmin) |
| `Contact_info` | `VARCHAR(100)`| - | Yes | Contact information / email / phone |
| `Account_accountID`| `INT` | FK | No | Link to the login account in `Account` |

### 2.4. Table `Personal_trainer`
Description: Information about the personal trainer (PT).

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PT_ID` | `INT` | PK | No | Trainer identifier |
| `FullName` | `VARCHAR(100)`| - | No | PT full name |
| `Specialty` | `VARCHAR(100)`| - | No | Specialty (Gym, Yoga, Kickboxing...) |
| `Experience_years` | `INT` | - | No | Years of experience |
| `Gym_OwnerAccount_ID`| `INT` | FK | Yes | Manager identifier approving the profile |
| `Account_accountID` | `INT` | FK | No | Link to the login account in `Account` |

### 2.5. Table `Member`
Description: Membership profile of gym members.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Member_ID` | `INT` | PK | No | Member identifier |
| `FullName` | `VARCHAR(100)`| - | No | Member full name |
| `Phone` | `VARCHAR(15)` | - | No | Contact phone number |
| `Mail` | `VARCHAR(100)`| - | No | Email address |

### 2.6. Table `Membership_Package`
Description: List of membership packages offered by the gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Package_ID` | `INT` | PK | No | Package code |
| `PackageName` | `VARCHAR(100)`| - | No | Membership package name (Basic, VIP, Premium...) |
| `Price` | `DECIMAL(10,2)`| - | No | Package price (VND) |
| `Durations_Days` | `INT` | - | No | Validity period (days) |

### 2.7. Table `Customer_Membership`
Description: Membership package purchased/registered by a customer.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `EnrollmentID` | `INT` | PK | No | Membership registration code |
| `StartDate` | `DATE` | - | No | Package activation start date |
| `ExpireDate` | `DATE` | - | No | Membership expiration date |
| `Status` | `VARCHAR(20)` | - | No | Package status (ACTIVE, EXPIRED, CANCELLED) |
| `Membership_PackagePackage_ID` | `INT` | FK | No | Registered package code (`Membership_Package`) |
| `MemberMember_ID` | `INT` | FK | No | Owning member code (`Member`) |

### 2.8. Table `Booking`
Description: Personal training schedule between a member and PT.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Booking_ID` | `INT` | PK | No | Booking identifier |
| `DateTime` | `DATETIME` | - | No | Date and time of the training session |
| `Status` | `VARCHAR(20)` | - | No | Status (PENDING, CONFIRMED, COMPLETED, CANCELLED) |
| `Personal_trainerPT_ID` | `INT` | FK | No | Assigned PT code (`Personal_trainer`) |
| `MemberMember_ID` | `INT` | FK | No | Member who booked the session (`Member`) |

### 2.9. Table `Payment`
Description: Transaction and invoice payment log.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PaymentID` | `INT` | PK | No | Transaction / invoice code |
| `Amount` | `DECIMAL(10,2)`| - | No | Payment amount (VND) |
| `Method` | `VARCHAR(30)` | - | No | Payment method (Cash, QR, Banking) |
| `Datetime` | `DATETIME` | - | No | Transaction timestamp |
| `Status` | `VARCHAR(20)` | - | No | Payment status (SUCCESS, FAILED, PENDING) |
| `MemberMember_ID` | `INT` | FK | No | Paying member code (`Member`) |

### 2.10. Table `Check_In`
Description: Entry/exit log of member activity in the gym.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `CheckIN_ID` | `INT` | PK | No | Attendance record ID |
| `DateTime` | `DATETIME` | - | No | Time of card swipe / QR check-in |
| `Method` | `VARCHAR(30)` | - | No | Check-in method (QR Code, Fingerprint, RFID Card) |
| `MemberMember_ID` | `INT` | FK | No | Member checked in (`Member`) |

### 2.11. Table `Equipment_inventory`
Description: Inventory management of gym equipment and machines.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Equipment_ID` | `INT` | PK | No | Equipment identifier |
| `Equipment_Name` | `VARCHAR(100)`| - | No | Equipment name (Treadmill, Dumbbell...) |
| `STatus` | `VARCHAR(30)` | - | No | Machine status (OPERATIONAL, BROKEN, UNDER_MAINTENANCE) |
| `PurchaseDate` | `DATE` | - | Yes | Purchase date |

### 2.12. Table `Maintenance_Log`
Description: Maintenance and repair history for gym equipment.

| Attribute Name | Data Type | Key | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Maintenance ID` | `INT` | PK | No | Maintenance record code |
| `DateTime` | `DATETIME` | - | No | Date and time of maintenance/repair |
| `Description` | `VARCHAR(255)`| - | Yes | Details of maintenance work |
| `Cost` | `DECIMAL(10,2)`| - | Yes | Maintenance/replacement cost (VND) |
| `Status` | `VARCHAR(20)` | - | No | Work status (COMPLETED, IN_PROGRESS) |
| `Gym_OwnerOwner_ID` | `INT` | FK | No | Approver/manager of the maintenance record |
| `Equipment_inventoryEquipment_ID` | `INT` | FK | No | Equipment being maintained |