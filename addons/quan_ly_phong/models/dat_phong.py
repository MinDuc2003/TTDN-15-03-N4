from odoo import models, fields, api
class DatPhong(models.Model):
    _name = 'dat_phong'
    _description = 'Đặt Phòng'

    tieu_de = fields.Char(string='Tiêu đề', required=True)
    phong_id = fields.Many2one('phong.hop', string='Phòng họp', required=True)
    thoi_gian_bat_dau = fields.Datetime(string='Thời gian bắt đầu', required=True)
    thoi_gian_ket_thuc = fields.Datetime(string='Thời gian kết thúc', required=True)
    muc_dich = fields.Text(string='Mục đích')
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('cancelled', 'Đã hủy')
    ], string='Trạng thái', default='draft')
    ghi_chu = fields.Text(string='Ghi chú')