

def perbandingan(pertama, kedua):
    if pertama > kedua:
        print("Angka pertama lebih besar dari angka kedua")
                
    elif pertama < kedua:
        print("Angka pertama lebih kecil dari angka kedua")
    
    else:
        print("Angka pertama dan angka kedua sama besar")

angka_pertama = int(input("masukkan angka pertama: "))
angka_kedua = int(input("masukkan angka kedua: "))
perbandingan(angka_pertama, angka_kedua)