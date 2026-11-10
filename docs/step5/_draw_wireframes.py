"""Low-fi academic wireframes for UC-05 / UC-06 (DRAFT)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("03_Images")
W, H = 1100, 780
BG = (255, 255, 255)
FG = (20, 20, 20)
MUTED = (90, 90, 90)
ERR = (160, 30, 30)
FILL_BOX = (245, 245, 245)


def font(size=16, bold=False):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


def rect(d, xy, outline=FG, width=2, fill=None):
    d.rectangle(xy, outline=outline, width=width, fill=fill)


def text(d, xy, s, size=15, bold=False, fill=FG):
    d.text(xy, s, font=font(size, bold), fill=fill)


def input_box(d, x, y, w, h, label, value=""):
    text(d, (x, y - 20), label, 13, fill=MUTED)
    rect(d, (x, y, x + w, y + h), fill=FILL_BOX)
    if value:
        text(d, (x + 8, y + 8), value, 14)


def button(d, x, y, w, h, label, primary=False):
    fill = (230, 230, 230) if not primary else (210, 210, 210)
    rect(d, (x, y, x + w, y + h), fill=fill, width=2)
    # center-ish label
    text(d, (x + 12, y + h // 2 - 8), label, 14, bold=True)


def chrome(d, title, screen_id):
    rect(d, (40, 30, W - 40, H - 30), width=3)
    rect(d, (40, 30, W - 40, 80), fill=(235, 235, 235), width=2)
    text(d, (55, 45), "GMS  |  Dashboard   Membership   PT   Reports          [Gym Owner]", 15, True)
    text(d, (55, 95), title, 20, True)
    text(d, (W - 220, 98), screen_id, 13, fill=MUTED)
    # nav underline
    d.line((40, 80, W - 40, 80), fill=FG, width=2)


def callout(d, x, y, n):
    d.ellipse((x, y, x + 22, y + 22), outline=FG, width=2, fill=(255, 255, 255))
    text(d, (x + 6, y + 2), str(n), 13, True)


def draw_uc05(error=False):
    img, d = new_canvas()
    chrome(d, "REGISTER MEMBERSHIP (at Counter)", "SCR-05" + ("-E" if error else ""))
    callout(d, 420, 95, 1)

    # Customer block
    rect(d, (60, 140, 1040, 290), width=2)
    text(d, (75, 150), "Customer Information", 16, True)
    callout(d, 280, 148, 2)
    input_box(d, 80, 200, 420, 34, "Full Name", "Nguyen Van A")
    input_box(d, 530, 200, 300, 34, "Phone Number", "0901234567")
    button(d, 850, 200, 160, 34, "Search existing")
    input_box(d, 80, 260, 520, 34, "Email", "a.nguyen@email.com")

    # Package
    rect(d, (60, 310, 620, 500), width=2)
    text(d, (75, 320), "Membership Package", 16, True)
    callout(d, 270, 318, 3)
    packages = [
        ("( )  Basic — 1 Month — 500,000 VND", False),
        ("(•)  Premium — 6 Months — 2,000,000 VND", True),
        ("( )  VIP — 12 Months — 3,500,000 VND", False),
    ]
    y = 360
    for label, sel in packages:
        text(d, (90, y), label, 14, bold=sel)
        y += 32

    # Promo + payment
    rect(d, (640, 310, 1040, 500), width=2)
    text(d, (655, 320), "Payment", 16, True)
    callout(d, 740, 318, 4)
    input_box(d, 660, 370, 220, 32, "Promo Code", "SUMMER10" if not error else "OLDCODE")
    button(d, 900, 370, 110, 32, "Apply")
    text(d, (660, 420), "Total Amount:  2,000,000 VND", 15, True)
    callout(d, 900, 418, 5)
    text(d, (660, 455), "Payment Method:  [ Cash ▼ ]", 14)
    text(d, (660, 480), "Ref note: [________________]", 13, fill=MUTED)

    if error:
        rect(d, (60, 520, 1040, 590), outline=ERR, width=3, fill=(255, 240, 240))
        text(d, (80, 540), "ERROR: Payment failed / timeout. Membership kept INACTIVE. [Retry]", 15, True, fill=ERR)
        text(d, (80, 565), "Exception 05.0.E1 — map BR-02 (no ACTIVE until paid)", 13, fill=ERR)
    else:
        text(d, (60, 530), "Wireframe note: low-fidelity · fields only · no colors/logo", 12, fill=MUTED)

    button(d, 680, 620, 140, 44, "Cancel")
    button(d, 850, 620, 190, 44, "Register & Pay", primary=True)
    callout(d, 1045, 630, 6)

    name = "UI_UC-05_RegisterMembership_Error.png" if error else "UI_UC-05_RegisterMembership.png"
    path = OUT / name
    img.save(path, "PNG")
    print("wrote", path)


def draw_uc06(error=False):
    img, d = new_canvas()
    chrome(d, "ACTIVATE MEMBERSHIP", "SCR-06" + ("-E" if error else ""))
    callout(d, 300, 95, 1)

    # Table
    rect(d, (60, 140, 1040, 320), width=2)
    text(d, (75, 150), "Pending memberships (INACTIVE + Paid)", 16, True)
    headers = ["ID", "Customer", "Package", "Amount", "Pay", "Action"]
    xs = [80, 180, 400, 580, 720, 850]
    for h, x in zip(headers, xs):
        text(d, (x, 185), h, 13, True, fill=MUTED)
    d.line((70, 210, 1030, 210), fill=FG, width=1)
    rows = [
        ("M001", "Nguyen Van A", "Premium 6M", "2,000,000", "Paid", "[Select]"),
        ("M002", "Tran Thi B", "Basic 1M", "500,000", "Paid", "[Select]"),
        ("M003", "Le Van C", "VIP 12M", "3,500,000", "Unpaid" if error else "Paid", "[Select]"),
    ]
    y = 225
    for i, row in enumerate(rows):
        for val, x in zip(row, xs):
            text(d, (x, y), val, 13, bold=(i == 0 and not error))
        if i == 0:
            callout(d, 1000, y - 2, 2)
        y += 28

    # Details
    rect(d, (60, 340, 1040, 560), width=2)
    text(d, (75, 350), "Selected membership details", 16, True)
    callout(d, 330, 348, 3)
    details = [
        "Membership ID:  M001",
        "Customer:  Nguyen Van A     Phone: 0901234567",
        "Package:  Premium (6 Months)",
        "Payment Status:  [ Paid ✓ ]" if not error else "Payment Status:  [ UNPAID ✗ ]",
        "Activate date: [10/11/2026]     End date (auto): 10/05/2027   (BR-03)",
    ]
    y = 390
    for line in details:
        text(d, (90, y), line, 14, bold=("UNPAID" in line))
        y += 28

    if error:
        rect(d, (60, 575, 1040, 640), outline=ERR, width=3, fill=(255, 240, 240))
        text(d, (80, 590), "BLOCKED: Cannot activate — outstanding fee (BR-02). Activate disabled.", 15, True, fill=ERR)
        text(d, (80, 615), "Alternative 06.1 / Exception path — show on wireframe as error state", 13, fill=ERR)
        button(d, 700, 660, 120, 40, "Back")
        # disabled look
        rect(d, (840, 660, 1040, 700), fill=(200, 200, 200), width=2)
        text(d, (855, 672), "Generate QR & Activate", 13, fill=MUTED)
    else:
        button(d, 700, 590, 120, 44, "Back")
        button(d, 840, 590, 200, 44, "Generate QR & Activate", primary=True)
        callout(d, 1045, 600, 4)
        text(d, (60, 655), "After success: QR preview [####]   [Print]   [Resend SMS]", 14)
        callout(d, 520, 652, 5)

    name = "UI_UC-06_ActivateMembership_Error.png" if error else "UI_UC-06_ActivateMembership.png"
    path = OUT / name
    img.save(path, "PNG")
    print("wrote", path)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    draw_uc05(False)
    draw_uc05(True)
    draw_uc06(False)
    draw_uc06(True)
