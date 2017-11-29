from xlrd import open_workbook
import pickle
import sys
import math
import json
def init_dict():
    dic ={}
    for diem in range(30*4):
        dic[diem/4] =0
    return dic
def x_round(x):
    return round(x*4)/4
def getData(wb):
    values = []
    for s in wb.sheets():
        #print 'Sheet:',s.name
        for row in range(1, s.nrows):
            col_names = s.row(0)
            col_value = {}
            i = 0
            for name, col in zip(col_names, range(s.ncols)):
                value  = (s.cell(row,col).value)
                try : value = float(value)
                except : value = value.lower()
                col_value[name.value.lower()]= value
                i+=1
            values.append(col_value)
    return values
class Nganh:
    def __init__(self, maNganh, tenNganh, khoi):
        self.maNganh = maNganh
        self.tenNganh= tenNganh
        self.chi_tieu_cu = 0
        self.chi_tieu_moi = 0
        self.diem_chuan_cu = 30.0
        self.diem_chuan_moi = 30.0
        self.diem_chuan_theo_pho_diem_moi = 30.0
        self.diem_chuan_chac_chan_chi_tieu = 30.0
        self.so_sv_lay = 0
        self.so_sv_lay_chac_chan_chi_tieu = 0
        self.khoi = khoi
        self.dict =  init_dict()
        self.pro_dict = init_dict()
        self.kq_dict = init_dict()
        self.pro = 0.0
        self.tong_sv_khoi_cu = 0
        self.tong_sv_khoi_moi = 0
        self.tong_sv_co_the_dau = 0
# class Khoi:
#     def __init__(self, tenKhoi):
#         self.tenKhoi = tenKhoi
#         self.diem

# khoiA_A1 = Khoi("a,a1")
# khoiB_B1 = Khoi("b,b1")
# khoiD1 = Khoi("d")

def du_doan(nganh_khois, kq_tuyen_sinh_cu, kq_tuyen_sinh_moi, chi_tieu_diem_chuan_cu, chi_tieu_moi):
    def keydiem_valueso_hoc_sinh_2khoi(kq_tuyen_sinh, khoi1, khoi2):
        data ={}
        for diemx4 in range(30*4):
            data[diemx4/4] = kq_tuyen_sinh[diemx4]['khoi_'+khoi1] + kq_tuyen_sinh[diemx4]['khoi_'+khoi2]
        return data
    def keydiem_valueso_hoc_sinh(kq_tuyen_sinh, khoi):
        data ={}
        for diem in range(30*4):
            data[diemx4/4] = kq_tuyen_sinh[diemx4]['khoi_'+khoi1]
        return data
    def tinh_tong_sv(dict):
        sum = 0
        for value in dict.values():
            sum += value
        return sum
    def tinh_sv_co_the_dau(nganh):
        dict = nganh.dict
        sum = 0
        for d in range(int(KHOANG_DIEM_CO_THE_DAU*4)):
            diem = nganh.diem_chuan_cu + d/4
            sum += dict[diem]
        # print(sum)
        if sum ==0:
            return nganh.diem_chuan_cu
        return sum
    def kq_thi_cac_nganh(nganh,kq_tuyen_sinh):
        dict ={}
        if nganh.khoi =="a,a1":
            dict = keydiem_valueso_hoc_sinh_2khoi(kq_tuyen_sinh, 'a', 'a1')
        if nganh.khoi == "b,b1":
            dict = keydiem_valueso_hoc_sinh_2khoi(kq_tuyen_sinh, 'b', 'b1')
        if nganh.khoi == "d":
            dict = keydiem_valueso_hoc_sinh(kq_tuyen_sinh, 'd')
        return dict
    KHOANG_DIEM_CO_THE_DAU = 0.5
    HE_SO = 1
    # doc du lieu nganh, khoi thi cua truong
    nganh_khois = getData(open_workbook(nganh_khois))
    nganhs = []
    for nganh_khoi in nganh_khois:
        nganh = Nganh(nganh_khoi["ma_nhom_nganh"], nganh_khoi["ten_nhom_nganh"], nganh_khoi["khoi_thi"])
        nganhs.append(nganh)
    # print(nganhs[0].khoi)

    kq_tuyen_sinh_cu = getData(open_workbook(kq_tuyen_sinh_cu))
    # print(kq_tuyen_sinh_cu[int(25.5*4)]['khoi_a'])
    kq_tuyen_sinh_moi = getData(open_workbook(kq_tuyen_sinh_moi))
    # print(kq_tuyen_sinh_moi[int(25.5*4)]['khoi_a'])
    chi_tieu_diem_chuan_cu = getData(open_workbook(chi_tieu_diem_chuan_cu))
    # print(chi_tieu_diem_chuan_cu[0]['chi_tieu'])
    chi_tieu_moi = getData(open_workbook(chi_tieu_moi))
    # print(chi_tieu_moi[0]['chi_tieu'])

    # 
    nganh_index = 0
    for nganh in nganhs:
        nganh.chi_tieu_cu = int(float(chi_tieu_diem_chuan_cu[nganh_index]['chi_tieu']))
        nganh.diem_chuan_cu = x_round(float(chi_tieu_diem_chuan_cu[nganh_index]['diem_chuan'])*3)
        nganh.chi_tieu_moi = int(float(chi_tieu_moi[nganh_index]['chi_tieu']))
        nganh.diem_chuan_thuc_te = float(chi_tieu_moi[nganh_index]['diem_chuan'])
        nganh_index += 1
    
    # 
    for nganh in nganhs:
        nganh.dict = kq_thi_cac_nganh(nganh, kq_tuyen_sinh_cu)
        nganh.kq_dict = kq_thi_cac_nganh(nganh, kq_tuyen_sinh_moi)
        nganh.tong_sv_khoi_cu = tinh_tong_sv(nganh.dict)
        # print(nganh.tong_sv_khoi_cu)
        nganh.tong_sv_khoi_moi = tinh_tong_sv(nganh.kq_dict)
        # print(nganh.tong_sv_khoi_moi)
    def thu_tu_diem(diem_chuan, keydiem_valueso_hoc_sinh):
        thu_tu = 0
        for d in range(int((29.75-diem_chuan)*4)):
            diem = diem_chuan + d/4
            thu_tu += keydiem_valueso_hoc_sinh[diem]
        return thu_tu
    def tinh_diem_theo_pho_diem_moi(nganh):
        ti_le_nguoi_dat_diem_chuan_cu_cua_ky_thi_cu = thu_tu_diem(nganh.diem_chuan_cu, nganh.dict)/nganh.tong_sv_khoi_cu
        # print(nganh.dict[nganh.diem_chuan_cu])
        # print(nganh.kq_dict[nganh.diem_chuan_cu])
        # print(ti_le_nguoi_dat_diem_chuan_cu_cua_ky_thi_cu)
        # print(thu_tu_diem(nganh.diem_chuan_cu,nganh.kq_dict)/nganh.tong_sv_khoi_moi)
        # print(nganh.tong_sv_khoi_cu)
        # print(nganh.tong_sv_khoi_moi)
        min = 10
        diem = 0
        for diemx4 in range(30*4):
            ti_le_nguoi_dat_diem_dang_xet_cua_ky_thi_moi = thu_tu_diem(diemx4/4,nganh.kq_dict)/nganh.tong_sv_khoi_moi
            hieu = abs(ti_le_nguoi_dat_diem_chuan_cu_cua_ky_thi_cu - ti_le_nguoi_dat_diem_dang_xet_cua_ky_thi_moi)
            if hieu < min:
                min = hieu
                diem = diemx4/4
        nganh.diem_chuan_theo_pho_diem_moi = diem
        # print("diem_chuan_cu = {}, diem_chuan_theo_pho_diem_moi {}".format(nganh.diem_chuan_cu,diem ))
        # print(ti_le_nguoi_dat_diem_chuan_cu_cua_ky_thi_cu)
        # print(thu_tu_diem(diem,nganh.kq_dict)/nganh.tong_sv_khoi_moi)        
        return diem
                
    def tinh_khoang_cach(diem_chuan_cu_theo_pho_diem_moi, diem):
        return abs(diem - diem_chuan_cu_theo_pho_diem_moi)
    for nganh in nganhs:
        # print(nganh.diem_chuan)
        # nganh.pro = nganh.dict[nganh.diem_chuan]/nganh.tong_sv_khoi_cu
        nganh.tong_sv_co_the_dau = tinh_sv_co_the_dau(nganh)
        nganh.pro = float(nganh.chi_tieu_cu)/nganh.tong_sv_co_the_dau
        # print("pro = {}".format(nganh.pro))
        diem_chuan_cu_theo_pho_diem_moi = tinh_diem_theo_pho_diem_moi(nganh)
        for diemx4 in range(30*4):
            khoang_cach = tinh_khoang_cach(diem_chuan_cu_theo_pho_diem_moi, diemx4/4)
            nganh.pro_dict[diemx4/4] = nganh.pro/math.exp(HE_SO*khoang_cach)
    def tinh_so_sv_lay(diem_xet,nganh):
        so_luong = 0
        for dx4 in range(int((29.75-diem_xet)*4)):
            diem = diem_xet + dx4/4
            so_luong += round(nganh.pro_dict[diem]*nganh.kq_dict[diem])
        return so_luong
    # print("Diem chuan moi:")
    nganh_index = 0
    for nganh in nganhs:
        # print("diem chuan {}, so sinh vien lay theo diem chuan {}".format(nganh.diem_chuan_cu, nganh.pro_dict[nganh.diem_chuan_cu]* nganh.kq_dict[nganh.diem_chuan_cu]))
        # print("diem chuan {}, so sinh vien lay theo diem chuan pho diem moi {}".format(nganh.diem_chuan_cu, nganh.pro_dict[nganh.diem_chuan_theo_pho_diem_moi]* nganh.kq_dict[nganh.diem_chuan_theo_pho_diem_moi]))
        so_sv_lay = 0.0
        diem_chuan_moi = 0
        for d in range(30*4):
            diem = 30.0 - d/4.0 -0.25
            # if nganh.maNganh == "kt22":
                # print("diem {}, so sinh vien {}".format(diem, so_sv_lay + round(nganh.pro_dict[diem]*nganh.kq_dict[diem])))
                # print(so_sv_lay + round(nganh.dict[diem]*nganh.kq_dict[diem]))
                # print(nganh.pro_dict[diem])
            if nganh.chi_tieu_moi < so_sv_lay + nganh.pro_dict[diem]*nganh.kq_dict[diem] :
                diem_chuan_moi = diem + 0.25
                
                break
            else:
                # print(nganh.diem_chuan_moi)
                if round(nganh.pro_dict[diem]*nganh.kq_dict[diem]) != 0:
                    diem_chuan_moi = diem
                so_sv_lay += round(nganh.pro_dict[diem]*nganh.kq_dict[diem])
        nganh.diem_chuan_moi = diem_chuan_moi
        # print(nganh.diem_chuan_moi)
                
                
        nganh.so_sv_lay = so_sv_lay
        # print("Nganh {}, Chi tieu nam ngoai {},Diem chuan nam ngoai: {}, diem chuan theo pho diem moi: {}\
        #  ,Chi tieu nam nay {}, diem chuan du doan: {}, so hoc sinh du doan {}, diem-so hoc sinh du doan\
        #   {}-{}, diem chuan nam nay {}"\
        #  .format(nganh.maNganh,nganh.chi_tieu_cu,nganh.diem_chuan_cu, nganh.diem_chuan_theo_pho_diem_moi\
        #  ,nganh.chi_tieu_moi,nganh.diem_chuan_moi, nganh.so_sv_lay, nganh.diem_chuan_moi -0.25 \
        #  , nganh.so_sv_lay + round(nganh.pro_dict[nganh.diem_chuan_moi - 0.25]*\
        #  nganh.kq_dict[nganh.diem_chuan_moi - 0.25]) , chi_tieu_moi[nganh_index]['diem_chuan']))
        # print(nganh.so_sv_lay)
        nganh_index += 1
    # 
    
    
    # diem_soLuong,append({diem: nganh.diem_chuan_moi - 0.25, diem_chuan_moi: nganh.diem_chuan_moi}) 

    output =[]
    for nganh in nganhs:
        diem_soLuong= []
        for dx4 in range(2*4):
            diem = nganh.diem_chuan_moi - 1 + dx4/4
            so_luong = tinh_so_sv_lay(diem, nganh)
            diem_soLuong.append({'diem': diem, 'so_luong': so_luong})
        print(diem_soLuong)
        output.append({'maNganh': nganh.maNganh, 'tenNganh': nganh.tenNganh, 'chi_tieu_cu': nganh.chi_tieu_cu, \
        'diem_chuan_cu': nganh.diem_chuan_cu, 'diem_chuan_theo_pho_diem_moi': nganh.diem_chuan_theo_pho_diem_moi, \
         'chi_tieu_moi': nganh.chi_tieu_moi, 'diem_chuan_moi': nganh.diem_chuan_moi, 'so_sv_lay': nganh.so_sv_lay, \
         'ds_ketqua': diem_soLuong, 'diem_chuan_thuc_te': nganh.diem_chuan_thuc_te})
    json.dumps(output)
    return (json.JSONEncoder().encode(output))
if (__name__ == '__main__'):
    if (len(sys.argv) != 6):
        print('usage: python3 du_doan_tuyen_sinh.py <nganh_khoi-file> <ket_qua_nam_truoc-file>\
                <ket_qua_nam_nay-file> <chi_tieu_diem_chuan_nam_truoc-file> <chi_tieu_nam_nay-file> ')
        # vd: python3 du_doan_tuyen_sinh.py bk_nganh_khoi.xlsx ketquathicacnam.xlsx ketQua_2017.xlsx ct_dc_2016_bk.xlsx ct_dc_2017_bk.xlsx
    nganh_khois = sys.argv[1]
    kq_tuyen_sinh_cu = sys.argv[2]
    kq_tuyen_sinh_moi = sys.argv[3]
    chi_tieu_diem_chuan_cu = sys.argv[4]
    chi_tieu_moi = sys.argv[5]
    output = du_doan(nganh_khois, kq_tuyen_sinh_cu, kq_tuyen_sinh_moi, chi_tieu_diem_chuan_cu, chi_tieu_moi)

