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
    text(d, (x + 12, y + h // 2 - 8), label, 14, bold=True)

def chrome(d, title, screen_id):
    rect(d, (40, 30, W - 40, H - 30), width=3)
    rect(d, (40, 30, W - 40, 80), fill=(235, 235, 235), width=2)
    text(d, (55, 45), "GMS  |  Dashboard   Packages   Bookings   Profile          [Personal Trainer / Owner]", 14, True)
    text(d, (55, 95), title, 20, True)
    text(d, (W - 220, 98), screen_id, 13, fill=MUTED)
    d.line((40, 80, W - 40, 80), fill=FG, width=2)

def callout(d, x, y, n):
    d.ellipse((x, y, x + 22, y + 22), outline=FG, width=2, fill=(255, 255, 255))
    text(d, (x + 6, y + 2), str(n), 13, True)

# --- 1. Vẽ UI cho UC-16: Register PT Account ---
def draw_uc16():
    img, d = new_canvas()
    chrome(d, "REGISTER PT ACCOUNT (Personal Trainer)", "SCR-16")
    
    rect(d, (60, 140, 1040, 600), width=2)
    text(d, (75, 150), "Personal Trainer Profile & Credentials Registration", 16, True)
    
    input_box(d, 80, 210, 420, 34, "Full Name", "John Smith")
    input_box(d, 530, 210, 300, 34, "Phone Number", "0912345678")
    
    input_box(d, 80, 280, 520, 34, "Email Address", "john.smith@gym.com")
    input_box(d, 630, 280, 400, 34, "Specialty / Expertise", "Fitness, Bodybuilding, Weight Loss")
    
    text(d, (80, 335), "Certificates & Experience Summary", 13, fill=MUTED)
    rect(d, (80, 355, 1010, 450), fill=FILL_BOX)
    text(d, (90, 365), "- Certified Personal Trainer (NASM - 2021)\n- 5 years experience in professional coaching\n- First Aid & CPR Certified", 14)
    
    button(d, 80, 480, 220, 40, "Upload Certificates (.pdf/.jpg)")
    text(d, (320, 490), "File uploaded: NASM_Certificate.pdf (✓)", 13, fill=MUTED)
    
    button(d, 680, 530, 140, 44, "Cancel")
    button(d, 840, 530, 190, 44, "Submit for Approval", primary=True)

    path = OUT / "UI_UC-16_RegisterPT.png"
    img.save(path, "PNG")
    print("Successfully generated:", path)

# --- 2. Vẽ UI cho UC-17: Approve PT Account ---
def draw_uc17():
    img, d = new_canvas()
    chrome(d, "APPROVE PT ACCOUNT (Gym Owner)", "SCR-17")
    
    # Bảng danh sách PT chờ duyệt
    rect(d, (60, 140, 1040, 320), width=2)
    text(d, (75, 150), "Pending PT Registration Requests", 16, True)
    
    headers = ["ID", "Full Name", "Specialty", "Experience", "Status", "Action"]
    xs = [80, 180, 400, 600, 750, 880]
    for h, x in zip(headers, xs):
        text(d, (x, 185), h, 13, True, fill=MUTED)
    d.line((70, 210, 1030, 210), fill=FG, width=1)
    
    rows = [
        ("PT001", "John Smith", "Fitness", "5 Years", "Pending", "[Select]"),
        ("PT002", "Jane Doe", "Yoga / Pilates", "3 Years", "Pending", "[Select]"),
    ]
    y = 225
    for i, row in enumerate(rows):
        for val, x in zip(row, xs):
            text(d, (x, y), val, 13, bold=(i == 0))
        y += 28

    # Chi tiết hồ sơ PT được chọn
    rect(d, (60, 340, 1040, 580), width=2)
    text(d, (75, 350), "Selected PT Details & Verification", 16, True)
    details = [
        "PT ID: PT001     Name: John Smith     Phone: 0912345678",
        "Email: john.smith@gym.com     Specialty: Fitness",
        "Certificates: NASM_Certificate.pdf (Verified View)",
        "Review Status: [ PENDING APPROVAL ]",
        "Owner Notes: [ Candidate has strong background and verified certificates. ]",
    ]
    y = 390
    for line in details:
        text(d, (90, y), line, 14)
        y += 28

    button(d, 640, 510, 180, 44, "Reject Request", primary=False)
    button(d, 840, 510, 190, 44, "Approve & Activate", primary=True)

    path = OUT / "UI_UC-17_ApprovePT.png"
    img.save(path, "PNG")
    print("Successfully generated:", path)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    draw_uc16()
    draw_uc17()