from odoo import models, fields, api

class PhongHop(models.Model):
    _name = 'phong_hop'
    _description = 'Phòng Họp'

    ten_phong_hop = fields.Char(string='Tên phòng họp', required=True)
    ma_phong_hop = fields.Char(string='Mã phòng', required=True)
    suc_chua_phong_hop = fields.Integer(string='Sức chứa')
    dia_diem_phong_hop = fields.Char(string='Địa Điểm', required=True)
    #thiet_bi_ids = fields.Many2many('thiet_bi_phong_hop', string='Thiết bị')
    trang_thai_phong_hop = fields.Selection([
        ('available', 'Có sẵn'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available')
    mo_ta_phong_hop = fields.Text(string='Mô tả')
    hinh_anh_phong_hop = fields.Binary(string='Hình ảnh')

    # Quan hệ One2many với Đơn Mượn Phòng
    don_muon_phong_ids = fields.One2many('don_muon_phong', 'phong_hop_id', string='Danh sách đơn mượn')
    lich_su_su_dung_ids = fields.One2many('lich_su_su_dung_phong', 'phong_hop_id', string='Lịch Sử Sử Dụng')