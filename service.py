import du_doan_tuyen_sinh
import sys
if (__name__ == '__main__'):
    if (len(sys.argv) != 6):
        print('usage: python3 du_doan_tuyen_sinh.py <nganh_khoi-file> <ket_qua_nam_truoc-file>\
                <ket_qua_nam_nay-file> <chi_tieu_diem_chuan_nam_truoc-file> <chi_tieu_nam_nay-file> ')
        # vd: python3 du_doan_tuyen_sinh.py bk_nganh_khoi.xlsx ketquacacnam.xlsx ketQua_2017.xlsx ct_dc_2016_bk.xlsx ct_dc_2017_bk.xlsx
    nganh_khois = sys.argv[1]
    kq_tuyen_sinh_cu = sys.argv[2]
    kq_tuyen_sinh_moi = sys.argv[3]
    chi_tieu_diem_chuan_cu = sys.argv[4]
    chi_tieu_moi = sys.argv[5]
    output = du_doan(nganh_khois, kq_tuyen_sinh_cu, kq_tuyen_sinh_moi, chi_tieu_diem_chuan_cu, chi_tieu_moi)
    # print(sys.argv)
    print(output)
