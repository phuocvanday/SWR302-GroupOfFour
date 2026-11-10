# Bước 2 — Huy (DF + UC Owner / Report / Feedback / Time)

> Issue: #13 · Nhánh: `step2/huy-uc-df`

## Data flows

| ID | From | To | Data |
|----|------|----|------|
| DF-01 | PT | GMS | Thông tin đăng ký tài khoản PT (Họ tên, chứng chỉ, kinh nghiệm) |
| DF-02 | Gym Owner | GMS | Quyết định duyệt/từ chối tài khoản PT |
| DF-03 | GMS | PT | Thông báo kết quả duyệt tài khoản |
| DF-04 | Gym Owner | GMS | Yêu cầu kết xuất báo cáo (Doanh thu, lượt Check-in, PT booking) |
| DF-05 | GMS | Gym Owner | Báo cáo chi tiết & File Excel xuất ra |
| DF-06 | Customer / PT | GMS | Nội dung phản hồi / đóng góp ý kiến (Feedback) |
| DF-07 | GMS | Gym Owner | Danh sách phản hồi cần xử lý |

## Use cases

| UC-ID | Tên | Actor chính | Mô tả ngắn |
|-------|-----|-------------|------------|
| UC-16 | Register PT Account | Personal Trainer | PT đăng ký tài khoản mới lên hệ thống kèm hồ sơ năng lực. |
| UC-17 | Approve PT Account | Gym Owner | Gym Owner xem xét và duyệt/từ chối hồ sơ đăng ký của PT. |
| UC-21 | Generate Reports | Gym Owner | Hệ thống tổng hợp dữ liệu doanh thu, hội viên, lượt tập để hiển thị báo cáo. |
| UC-22 | Export Excel Report | Gym Owner | Xuất dữ liệu báo cáo vận hành ra file định dạng Excel. |
| UC-24 | View Dashboard | Gym Owner | Xem tổng quan các chỉ số vận hành chính (KPIs) trên màn hình Dashboard. |

## Ghi chú
- Các Use Case UC-16 và UC-17 sẽ được thực hiện đặc tả chi tiết (Fully Dressed) ở Bước 4.