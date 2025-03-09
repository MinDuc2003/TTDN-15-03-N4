from odoo import models, fields

class TienIch(models.Model):
    _name = 'tien_ich'
    _description = 'Thiết bị phòng họp'

    name = fields.Char(string="Tên thiết bị", required=True)
    serial_number = fields.Char(string="Số Serial", unique=True)
    loai_thiet_bi = fields.Selection([
        ('may_chieu', 'Máy chiếu'),
        ('micro', 'Micro'),
        ('loa', 'Loa'),
        ('camera', 'Camera'),
        ('khac', 'Khác')
    ], string="Loại thiết bị", default='khac')
    image = fields.Binary(string="Hình ảnh thiết bị")
    trang_thai = fields.Selection([
        ('in_use', 'Đang sử dụng'),
        ('broken', 'Đang hỏng'),
        ('maintenance', 'Đang bảo trì')
    ], string="Trạng thái", default='in_use')

    # Quan hệ với Phòng Họp (Many2one)
    phong_hop_id = fields.Many2one('phong_hop', string="Phòng Họp")
    phong_hoi_nghi_id = fields.Many2one('phong_hoi_nghi', string="Phòng Họp")