from odoo import models, fields, api
class ThietBiPhongHop(models.Model):
    _name = 'thiet_bi_phong_hop'
    _description = 'Thiết Bị Phòng Họp'

    ten_thiet_bi = fields.Char(string='Tên thiết bị', required=True)
    ma_thiet_bi = fields.Char(string='Mã thiết bị', required=True)
    #phong_id = fields.Many2one('phong_hop', string='Phòng họp')
    trang_thai = fields.Selection([
        ('available', 'Có sẵn'),
        ('in_use', 'Đang sử dụng'),
        ('broken', 'Hỏng')
    ], string='Trạng thái', default='available')