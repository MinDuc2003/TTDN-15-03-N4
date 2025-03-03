from odoo import models, fields, api
class LichSuSuDungPhong(models.Model):
    _name = 'lich_su_su_dung_phong'
    _description = 'Lịch Sử Sử Dụng Phòng '

    #cuoc_hop_id = fields.Many2one('dat_phong', string='Cuộc họp', required=True)
    chu_de = fields.Char(string='Chủ đề', required=True)
    gio_bat_dau = fields.Datetime(string='Giờ bắt đầu', required=True)
    gio_ket_thuc = fields.Datetime(string='Giờ kết thúc', required=True)
    ghi_chu = fields.Text(string='Ghi chú')