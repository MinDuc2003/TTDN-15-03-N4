from odoo import models, fields, api

class DonMuonPhong(models.Model):
    _name = 'don_muon_phong'
    _description = 'Đơn Mượn Phòng'

    tieu_de = fields.Char(string='Tiêu đề', required=True)
    ten_nguoi_dat_phong = fields.Char(string='Tên người đặt phòng', required=True)
    lich_su_su_dung_ids = fields.One2many('lich_su_su_dung_phong', 'don_muon_phong_id', string='Lịch Sử Sử Dụng')
    phong_hop_id = fields.Many2one('phong_hop', string='Phòng họp', domain="[('trang_thai_phong_hop', '=', 'available')]", required=False)
    phong_hoi_nghi_id = fields.Many2one('phong_hoi_nghi', string='Phòng hội nghị', domain="[('trang_thai', '=', 'available')]", required=False)
    # Thông tin phòng họp (related fields)
    ten_phong_hop = fields.Char(related='phong_hop_id.ten_phong_hop', string='Tên phòng', readonly=True)
    ma_phong_hop = fields.Char(related='phong_hop_id.ma_phong_hop', string='Mã phòng', readonly=True)
    suc_chua_phong_hop = fields.Integer(related='phong_hop_id.suc_chua_phong_hop', string='Sức chứa', store=True)
    dia_diem_phong_hop = fields.Char(related='phong_hop_id.dia_diem_phong_hop', string='Địa điểm', readonly=True)
    trang_thai_phong_hop = fields.Selection(related='phong_hop_id.trang_thai_phong_hop', string='Trạng thái phòng', readonly=True)
    mo_ta_phong_hop = fields.Text(related='phong_hop_id.mo_ta_phong_hop', string='Mô tả', readonly=True)
    hinh_anh_phong_hop = fields.Binary(related='phong_hop_id.hinh_anh_phong_hop', string='Hình ảnh', readonly=True)

    # Thông tin phòng hội nghị (related fields)
    ten_phong = fields.Char(related='phong_hoi_nghi_id.ten_phong', string='Tên phòng', readonly=True)
    ma_phong = fields.Char(related='phong_hoi_nghi_id.ma_phong', string='Mã phòng', readonly=True)
    suc_chua = fields.Integer(related='phong_hoi_nghi_id.suc_chua', string='Sức chứa', store=True)
    dia_diem = fields.Char(related='phong_hoi_nghi_id.dia_diem', string='Địa điểm', readonly=True)
    trang_thai_phong = fields.Selection(related='phong_hoi_nghi_id.trang_thai', string='Trạng thái phòng', readonly=True)
    mo_ta = fields.Text(related='phong_hoi_nghi_id.mo_ta', string='Mô tả', readonly=True)
    hinh_anh = fields.Binary(related='phong_hoi_nghi_id.hinh_anh', string='Hình ảnh', readonly=True)

    thoi_gian_bat_dau = fields.Datetime(string='Thời gian bắt đầu', required=True)
    thoi_gian_ket_thuc = fields.Datetime(string='Thời gian kết thúc', required=True)
    muc_dich = fields.Text(string='Mục đích')
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('cancelled', 'Đã hủy')
    ], string='Trạng thái', default='draft')
    loai_phong = fields.Selection([
        ('phong_hop', 'Phòng Họp'),
        ('phong_hoi_nghi', 'Phòng Hội Nghị')
    ], string='Loại phòng')
    ghi_chu = fields.Text(string='Ghi chú')


@api.model
def create(self, vals):
        """ Khi tạo đơn mượn phòng, tự động tạo bản ghi lịch sử sử dụng phòng """
        record = super(DonMuonPhong, self).create(vals)
        self.env["lich_su_su_dung_phong"].create({
            'don_muon_phong_id': record.id,
            'phong_hop_id': record.phong_hop_id.id if record.phong_hop_id else False,
            'phong_hoi_nghi_id': record.phong_hoi_nghi_id.id if record.phong_hoi_nghi_id else False,
            'thoi_gian_bat_dau': record.thoi_gian_bat_dau,
            'thoi_gian_ket_thuc': record.thoi_gian_ket_thuc,
            'trang_thai_su_dung': record.trang_thai
        })
        return record

def write(self, vals):
        """ Khi cập nhật đơn mượn phòng, tự động cập nhật lịch sử sử dụng phòng """
        res = super(DonMuonPhong, self).write(vals)
        for record in self:
            lich_su = self.env["lich_su_su_dung_phong"].search([('don_muon_phong_id', '=', record.id)], limit=1)
            if lich_su:
                lich_su.write({
                    'phong_hop_id': record.phong_hop_id.id if record.phong_hop_id else False,
                    'phong_hoi_nghi_id': record.phong_hoi_nghi_id.id if record.phong_hoi_nghi_id else False,
                    'thoi_gian_bat_dau': record.thoi_gian_bat_dau,
                    'thoi_gian_ket_thuc': record.thoi_gian_ket_thuc,
                    'trang_thai_su_dung': record.trang_thai
                })
        return res