import math
def timeConverter(waktu):
    # Kondisi pertama inputan harus di ketahui dulu tipe data wajib integer (int)
    # baru filter kondisi selanjut nya (minus apa bukan dan jangan lebih dari 359999)
    if waktu!=int:                
        print("Invalid Input !")
    elif waktu==float:
        print("Invalid Input!")
    #Jika inputan minus(dibawah nol maka invalid)
    elif waktu<0 :
        print("Invalid Input !")
    # Jika inputan lebih dari 359999 maka invalid
    elif waktu >=359999 :
        print("invalid Input!")
    else :
        #Menentukan Jam
        jam = math.floor(waktu/3600)
        #Menentukan Sisa jam
        menit_detik= waktu%3600
        #menentukan menit dari sisa jam
        menit=math.floor(menit_detik/60)
        #mentukan sisa menit dari sisa jam (menit_detik)
        detik=menit_detik%60
        print(f"Konversi : {jam:02d}:{menit:02d}:{detik:02d}")

waktu=int(input("Masukkan detik:  "))
timeConverter(waktu)
