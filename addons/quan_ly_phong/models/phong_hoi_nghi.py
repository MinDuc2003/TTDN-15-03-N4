from odoo import models, fields, api

class PhongHoiNghi(models.Model):
    _name = 'phong_hoi_nghi'
    _description = 'Phòng Hội Nghị'

    ten_phong = fields.Char(string='Tên phòng ', required=True)
    ma_phong = fields.Char(string='Mã phòng', required=True)
    suc_chua = fields.Integer(string='Sức chứa')
    dia_diem = fields.Char(string='Địa Điểm', required=True)
    trang_thai = fields.Selection([
        ('available', 'Có sẵn'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available')
    mo_ta = fields.Text(string='Mô tả')
    hinh_anh = fields.Binary(string='Hình ảnh')

     # Quan hệ One2many với Đơn Mượn Phòng
    don_muon_phong_ids = fields.One2many('don_muon_phong', 'phong_hoi_nghi_id', string='Danh sách đơn mượn')
    lich_su_su_dung_ids = fields.One2many('lich_su_su_dung_phong', 'phong_hoi_nghi_id', string='Lịch Sử Sử Dụng')