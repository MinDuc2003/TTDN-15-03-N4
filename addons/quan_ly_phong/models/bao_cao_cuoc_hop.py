from odoo import models, fields, api
class BaoCaoCuocHop(models.Model):
    _name = 'bao_cao_cuoc_hop'
    _description = 'Báo Cáo Cuộc Họp'

    #cuoc_hop_id = fields.Many2one('dat.phong', string='Cuộc họp', required=True)
    tom_tat = fields.Text(string='Tóm tắt nội dung')
    quyet_dinh = fields.Text(string='Các quyết định')
    phan_hoi_nguoi_tham_du = fields.Text(string='Ý kiến người tham dự')
    tap_tin_dinh_kem = fields.Binary(string='File đính kèm')