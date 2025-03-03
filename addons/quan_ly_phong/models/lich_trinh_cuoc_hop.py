from odoo import models, fields, api
class LichTrinhCuocHop(models.Model):
    _name = 'lich_trinh_cuoc_hop'
    _description = 'Lịch Trình Cuộc Họp'

    cuoc_hop_id = fields.Many2one('dat.phong', string='Cuộc họp', required=True)
    chu_de = fields.Char(string='Chủ đề', required=True)
    gio_bat_dau = fields.Datetime(string='Giờ bắt đầu', required=True)
    gio_ket_thuc = fields.Datetime(string='Giờ kết thúc', required=True)
    ghi_chu = fields.Text(string='Ghi chú')