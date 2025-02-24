from odoo import models, fields, api


class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Bảng chứa thông tin văn bản đến'

    ma_chuc_vu = fields.Char("Mã Chức Vụ", required=True)
    ten_chuc_vu = fields.Char("Tên Chức Vụ", required=True)
