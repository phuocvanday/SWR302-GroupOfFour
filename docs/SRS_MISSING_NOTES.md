# SRS — phần còn thiếu / cần thành viên bổ sung

> Cập nhật: 11/11/2026 · SRS: `01_SRS_GMS_v1draft.docx` (đóng Word rồi đổi tên thành `01_SRS_GMS.docx` nếu file gốc đang bị khóa)  
> Script: `docs/scripts/build_srs_v1.py`  
> UC: bảng **Field | Content** đồng bộ (UC-11/12 đã chuyển cùng template). Font 13, heading đen.  
> Hình nhúng: **chỉ Visual Paradigm** (CD, UCD Overview, AD-02/03, ERD). Không nhúng UI wireframe / PlantUML.  
> **Chưa đóng zip** (chờ AD-01).

## Blocker chính (đúng tình trạng “mới tới bước 6”)

| # | Thiếu | Ai | Issue | Ảnh hưởng SRS |
|---|-------|----|-------|----------------|
| 1 | **AD-01** Đặt gói PT & thanh toán (swimlane ≥3 + PNG) | **Tuấn** | [#30](https://github.com/phuocvanday/SWR302-GroupOfFour/issues/30) OPEN | §3.4 có placeholder đỏ; checklist bước 6 [#33] chưa đóng |
| 2 | File nháp `docs/step6/tuan_ad01.md` trống | Tuấn | #30 | Không có mô tả lane/decision để dán SRS |

## Thiếu hình / export VP

| # | File | Figure trong SRS | Ai | Ghi chú |
|---|------|----------------|----|---------|
| 3 | `03_Images/SMD_Membership.png` | Figure 3.8 | Thiên | Bảng transition đã có trong SRS + `thien_smd.md` |
| 4 | `03_Images/SMD_PTBooking.png` | Figure 3.9 | Thiên | Như trên |
| 5 | Typo nhãn trên `CD_ContextDiagram.png` | Figure 2.1 | Phước sửa VPP | Góp ý peer review Thiên #42 |

## Hình đã nhúng + chú thích

Xem **Appendix F** trong `01_SRS_GMS.docx` (Figure catalogue). Mỗi ảnh có:
- Caption in đậm: `Figure x.y — tên`
- Dòng ghi chú xám: `Source file: 03_Images/... · owner · UC/BR · ≥150 dpi`

UI wireframe: chèn ở **§3.2** (cạnh từng UC) **và** gallery **§5.1**.

## Nháp thành viên còn trống / chưa xác nhận

| File | Ai | Việc |
|------|----|------|
| `docs/step1/tuan_vision.md` | Tuấn | User class PT + chốt BO-03 (SRS đang dùng Vision chung) |
| `docs/step7/tuan_erd_review.md` | Tuấn | Bổ sung TrainingSession / review SMD-02 vs ERD |
| `docs/step8/tuan_peer_review.md` | Tuấn | Peer review UCD PT / AD-01 / UC-11/12 |

## Đã ghép vào SRS (nguồn)

- §1–2: Vision + Thiên/Huy step1 + CD Phước  
- §3: 8 UC dressed step4 + UI step5 + AD-02/03 + SMD tables  
- §4: ERD Huy + dict tóm tắt  
- §5–6: UI map + NFR Huy  
- Appendix: Glossary, model index, RTM trỏ Excel, Open Issues  

## Lưu ý nhất quán

- **BR canonical = Vision BR-01…12** (khớp UC-05/06/08…).  
  `docs/step3/huy_br_glossary.md` đánh số BR khác → **không trộn ID** khi trace.
- ERD Huy dùng tên `Member` / `Booking` / `Customer_Membership` — SRS có bảng map sang tên Vision.
- AD-02 lấy từ `origin/step-6` (`AD_ApprovePT.jpg` → `.png`).

## Việc Phước làm tiếp (sau khi Tuấn xong AD-01)

1. Chèn Figure AD-01 vào §3.4  
2. Thiên export SMD PNG → chèn Figure SMD  
3. Đổi Revision → **1.0** chính thức  
4. Build lại zip A.3 (không làm ở vòng này)
