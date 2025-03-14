# Files read and write
import sys
sys.stdin = open("./files/input.txt", "r")
sys.stdout = open("./files/output.txt", "w")

# defined function
def compute(x: int, y: int) -> int:
    return x + y

from abc import ABC, abstractmethod

# abstract class
class abdNhanVien(ABC):
    @abstractmethod
    def luongHT(self):
        pass

# Xay dung class
class NhanVien(absNhanVien):
    # **kwargs cho so luong bien khac nhau chua biet truoc
    def __init__(self, ma_nv, **kwargs):
        self._ma_nv = ma_nv
        self._ho_ten = kwargs.get('ho_ten', "N/A")
        self._luong_CB = kwargs.get('luong_CB', 0)
        self._luong_HT = 0
   
    # Overiding 
    def __str__(self):
        return str([
                self._ho_ten,
                self._ma_nv,
                self._luong_CB
                ])
    
    def xuat(self):
        print("Ho va ten: ", self._ho_ten)
        print("Ma nhan vien: ", self._ma_nv)
        print("Luong co ban: ", self._luong_CB)
        print("Luong hang thang: ", self._luong_HT)
        
class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, **kwargs):
        super().__init__(ma_nv, **kwargs)
        self.__so_ngay = kwargs.get('so_ngay', 0)
    
    def getNgay(self):
        return self.__so_ngay
    def setNgay(self, day):
        self.__so_ngay = day
        
    # @setattr
    # def ngay(self, day):
    #     self.__so_ngay = day    
        
    def luongHT(self):
        luong = self._luong_CB + 150000 * self.__so_ngay
        self._luong_HT = luong
        return luong
    
    def xuat(self):
        super().xuat()
        print("So ngay: ", self.__so_ngay) 
        print("\n")

class NVBanHang(NhanVien):
    def __init__(self, ma_nv, **kwargs):
        super().__init__(ma_nv, **kwargs)
        self.__so_san_pham = kwargs.get('so_san_pham', 0)
    
    @property
    def sp(self):
        return self.__so_san_pham
    
    def getSP(self):
        return self.__so_san_pham
    def setSP(self, sp):
        self.__so_san_pham = sp
    
    def luongHT(self):
        luong = self._luong_CB + 18000 * self.__so_san_pham
        self._luong_HT = luong
        return luong
    
    def xuat(self):
        super().xuat()
        print("So san pham: ", self.__so_san_pham)    
        print("\n")
    
class CongTy:
    def __init__(self, ma_ct, **kwargs):
        self.__ma_ct = ma_ct
        self.__ten_ct = kwargs.get('ten_ct', 'N/A')
        self.__danh_sach = []
    
    def nhapDS(self):
        nv1 = NVBanHang(111, ho_ten="Nguyen Van A", luong_CB=5000000, so_san_pham=30)
        nv2 = NVVanPhong(112, ho_ten="Nguyen Van B", luong_CB=8000000, so_ngay=30)
        nv3 = NVBanHang(113, ho_ten="Nguyen Van C", luong_CB=10000000, so_san_pham=300)
        nv4 = NVVanPhong(114, ho_ten="Nguyen Van D", luong_CB=20000000, so_ngay=100)
        self.__danh_sach.extend([nv1, nv2, nv3, nv4])
    
    def xuatDS(self):
        for nv in self.__danh_sach: nv.xuat()   
    
    def tinhLuong(self):
        for nv in self.__danh_sach: nv.luongHT() # dat ten khac nhau thi dung isinstance() de phan biet

if __name__ == '__main__':
    ct = CongTy(1111, ten_ct="ABC")
    ct.nhapDS()
    ct.tinhLuong()
    ct.xuatDS()

            