from odoo import models, fields, api

class LichSuSuDungPhong(models.Model):
    _name = "lich_su_su_dung_phong"
    _description = "Lịch Sử Sử Dụng Phòng"

    don_muon_phong_id = fields.Many2one("don_muon_phong", string="Đơn Mượn Phòng")
    phong_hop_id = fields.Many2one("phong_hop", string="Phòng Họp", related="don_muon_phong_id.phong_hop_id", store=True)
    phong_hoi_nghi_id = fields.Many2one("phong_hoi_nghi", string="Phòng Hội Nghị", related="don_muon_phong_id.phong_hoi_nghi_id", store=True)
    thoi_gian_bat_dau = fields.Datetime(related="don_muon_phong_id.thoi_gian_bat_dau", store=True)
    thoi_gian_ket_thuc = fields.Datetime(related="don_muon_phong_id.thoi_gian_ket_thuc", store=True)
    trang_thai_su_dung = fields.Selection(related="don_muon_phong_id.trang_thai", store=True)
    thong_ke_id = fields.Many2one("thong_ke", string="Thống Kê")

    @api.model
    def create(self, vals):
        record = super(LichSuSuDungPhong, self).create(vals)
        if record.thong_ke_id:
            record.thong_ke_id._tinh_toan_thong_ke()
        return record

    def write(self, vals):
        res = super(LichSuSuDungPhong, self).write(vals)
        if self.thong_ke_id:
            self.thong_ke_id._tinh_toan_thong_ke()
        return res

    def unlink(self):
        thong_ke_ids = self.mapped('thong_ke_id')
        res = super(LichSuSuDungPhong, self).unlink()
        for thong_ke in thong_ke_ids:
            thong_ke._tinh_toan_thong_ke()
        return res
    
