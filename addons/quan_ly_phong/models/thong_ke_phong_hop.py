from odoo import models, fields, api
class ThongKePhongHop(models.Model):
    _name = 'thong_ke_phong_hop'
    _description = 'Thống Kê Phòng Họp'

    tong_so_cuoc_hop = fields.Integer(string='Tổng số cuộc họp')
    phong_id = fields.Many2one('phong.hop', string='Phòng họp')
    ty_le_su_dung = fields.Float(string='Tỷ lệ sử dụng (%)')
    so_nguoi_tham_du_tb = fields.Float(string='Số người tham dự trung bình')
    so_su_co_thiet_bi = fields.Integer(string='Số lần sự cố thiết bị')
    so_cuoc_hop_huy = fields.Integer(string='Số cuộc họp bị hủy')
    nguoi_dat_nhieu_nhat = fields.Many2one('res.users', string='Người đặt nhiều nhất')
    ngay_thong_ke = fields.Date(string='Ngày thống kê')
    thoi_luong_tb = fields.Float(string='Thời lượng trung bình (giờ)')
    du_lieu_bieu_do = fields.Binary(string='Biểu đồ')