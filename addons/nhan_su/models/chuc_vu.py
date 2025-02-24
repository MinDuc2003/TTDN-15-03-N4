from odoo import models, fields, api


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Chức vụ của nhân viên'

    ma_chuc_vu = fields.Char("Mã Chức Vụ", required=True)
    ten_chuc_vu = fields.Char("Tên Chức Vụ", required=True)
