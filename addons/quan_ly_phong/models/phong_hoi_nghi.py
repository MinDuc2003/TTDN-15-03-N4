from odoo import models, fields, api

class PhongHoiNghi(models.Model):
    _name = 'phong_hoi_nghi'
    _description = 'Phòng Hội Nghị'

    ten_phong = fields.Char(string='Tên phòng họp', required=True)
    ma_phong = fields.Char(string='Mã phòng', required=True)
    suc_chua = fields.Integer(string='Sức chứa')
    dia_diem = fields.Char(string='Địa Điểm', required=True)
    #thiet_bi_ids = fields.Many2many('thiet_bi_phong_hop', string='Thiết bị')
    trang_thai = fields.Selection([
        ('available', 'Có sẵn'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available')
    mo_ta = fields.Text(string='Mô tả')
    hinh_anh = fields.Binary(string='Hình ảnh')