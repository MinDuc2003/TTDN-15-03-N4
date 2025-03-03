from odoo import models, fields, api

class PhongHop(models.Model):
    _name = 'phong_hop'
    _description = 'Phòng Họp'

    ten_phong = fields.Char(string='Tên phòng họp', required=True)
    ma_phong = fields.Char(string='Mã phòng', required=True)
    suc_chua = fields.Integer(string='Sức chứa')
    dia_diem_id = fields.Many2one('res.partner', string='Địa điểm')
    thiet_bi_ids = fields.Many2many('thiet.bi.phong.hop', string='Thiết bị')
    trang_thai = fields.Selection([
        ('available', 'Có sẵn'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available')
    mo_ta = fields.Text(string='Mô tả')
    hinh_anh = fields.Binary(string='Hình ảnh')