from odoo import models, fields, api
from datetime import timedelta

class ThongKe(models.Model):
    _name = 'thong_ke'
    _description = 'Thống Kê Phòng Họp'

    tong_so_cuoc_hop = fields.Integer(string='Tổng số cuộc họp', compute='_tinh_toan_thong_ke', store=True)
    lich_su_su_dung_ids = fields.One2many('lich_su_su_dung_phong', 'thong_ke_id', string='Lịch Sử Sử Dụng Phòng')
    ty_le_su_dung = fields.Float(string='Tỷ lệ sử dụng (%)', compute='_tinh_toan_thong_ke', store=True)
    so_cuoc_hop_huy = fields.Integer(string='Số cuộc họp bị hủy', compute='_tinh_toan_thong_ke', store=True)
    ngay_thong_ke = fields.Date(string='Ngày thống kê', default=fields.Date.today)
    thoi_luong_tb = fields.Float(string='Thời lượng trung bình (giờ)', compute='_tinh_toan_thong_ke', store=True)
    du_lieu_bieu_do = fields.Binary(string='Biểu đồ')

    @api.depends('lich_su_su_dung_ids')
    def _tinh_toan_thong_ke(self):
     for thong_ke in self:
        # Lấy danh sách lịch sử sử dụng phòng
        danh_sach_lich_su = thong_ke.lich_su_su_dung_ids

        # Tính tổng số cuộc họp chưa bị hủy
        so_cuoc_hop = len(danh_sach_lich_su.filtered(lambda ls: ls.trang_thai_su_dung != 'cancelled'))

        # Tính số cuộc họp bị hủy
        so_cuoc_hop_huy = len(danh_sach_lich_su.filtered(lambda ls: ls.trang_thai_su_dung == 'cancelled'))

        # Tính tổng thời gian họp (giờ)
        tong_thoi_gian = sum(
            ((ls.thoi_gian_ket_thuc - ls.thoi_gian_bat_dau).total_seconds() / 3600)
            for ls in danh_sach_lich_su 
            if ls.thoi_gian_bat_dau and ls.thoi_gian_ket_thuc and ls.trang_thai_su_dung != 'cancelled'
        )

        # Tính thời gian trung bình của cuộc họp (giờ)
        thoi_luong_trung_binh = tong_thoi_gian / so_cuoc_hop if so_cuoc_hop else 0

        # Giả sử tổng số phòng có sẵn là 8
        tong_phong_hop = 8  # Số phòng có sẵn (có thể thay đổi tùy nhu cầu)
        
        # Tính tỷ lệ sử dụng phòng (phần trăm)
        ty_le_su_dung = (so_cuoc_hop / tong_phong_hop) * 100 if tong_phong_hop else 0

        # Cập nhật các giá trị vào các trường trong bản ghi thống kê
        thong_ke.tong_so_cuoc_hop = so_cuoc_hop
        thong_ke.so_cuoc_hop_huy = so_cuoc_hop_huy
        thong_ke.thoi_luong_tb = thoi_luong_trung_binh
        thong_ke.ty_le_su_dung = ty_le_su_dung
