class Sekolah:
    def __init__ (self,nama_sekolah,jumlah_siswa,akreditasi,tahun_berdiri):
        self.nama_sekolah = nama_sekolah
        self.jumlah_siswa = jumlah_siswa
        self.akreditasi = akreditasi
        self.tahun_berdiri = tahun_berdiri
    
    def menerima_murid(self):
        print('-----------------------------------------------------------------------------')
        print(f'{self.nama_sekolah} telah membuka PPDB tahun pelajaran 2045/2046!')
        print(f'Sekolah ini meimiliki akreditasi {self.akreditasi} dan berdiri sejak tahun {self.tahun_berdiri}')
        print('-----------------------------------------------------------------------------')

    def mengeluarkan_murid(self):
        print(f'Maaf anda telah gagal dalam seleksi untuk memasukki {self.nama_sekolah}')
        print(f'Jumlah perserta didik tahun ini adalah {self.jumlah_siswa}, Semoga bisa menjadi bagian dari {self.nama_sekolah} dikesempatan berikutnya')
        print('-----------------------------------------------------------------------------')

    def merekrut_guru(self):
        print(f'Telah dibuka lowongan guru untuk sekolah {self.nama_sekolah}')
        print('-----------------------------------------------------------------------------')
        print(' ')

sekolah_A = Sekolah('Sekolah Indonesia Emas 45', 245, "A++", 1945)
sekolah_B = Sekolah('STM 47 Kapal Karam', 69, 'N+', '69 SM')

sekolah_A.menerima_murid()
sekolah_A.mengeluarkan_murid()
sekolah_A.merekrut_guru()

sekolah_B.menerima_murid()
sekolah_B.mengeluarkan_murid()
sekolah_B.merekrut_guru()