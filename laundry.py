from datetime import datetime

pilihan = "c"

while pilihan == "c" :
    print()
    pelanggan=str(input("Masukan Nama: "))
    print("=========================================================")
    print("|\t\t\t LAUNDRY MAHMUD\t\t\t|")
    print("|\t\t\t MENU JASA \t\t\t|")
    print("| \t1. Ekpress \t\t16000 \t\t\t|")
    print("| \t2. Biasa \t\t7000 \t\t\t|")
    print("| \t3. Cuci \t\t10000 \t\t\t|")
    print("| \t4. Setrika \t\t5000 \t\t\t|")
    print("| \t5. Cuci+Setrika \t12000 \t\t\t|")
    
    print("=========================================================")
    print()

    jasa = int(input("Silahkan Pilih Jasa? (Masukkan angka) = "))
    print()
    jumlah = int(input("Berapa jumlah berat baju? (Masukkan angka) = "))

    if jasa == 1:
        jasa = ("Ekpress")
        harga = 16000*jumlah
    elif jasa == 2:
        jasa = ("Biasa")
        harga = 7000*jumlah
    elif jasa == 3 : 
       jasa= ("Cuci")
       harga = 10000*jumlah
    elif jasa == 4 : 
        jasa = ("Setrika")
        harga = 5000*jumlah
    elif jasa == 5 : 
        jasa= ("Cuci+Setrika")
        harga = 12000*jumlah

    diskon = 0

    if jumlah >= 5:
        diskon = 5/100*harga
    elif jumlah >= 7: 
        diskon = 10/100*harga
    else:
        pass

    semua = harga-diskon
    
    print("Harga yang harus dibayar semua = Rp.",semua)
    
    masuk = str(input("Masukkan tanggal masuk: "))

    uang = int(input("Uang Tunai Pembeli: Rp."))
    kembalian = uang-semua
    print("Kembalian : Rp.",kembalian)
    #keluar = str(input("Masukkan tanggal keluar: "))
    tanggal_saat_ini = datetime.date.today()
        
    print("\n=========================================")

    print("======= S T R U K   PEMBAYARAN ===============")
    print("==========================")
    print(" Nama         :",pelanggan)
    print(" Berat        :", jumlah)
    print(" Bayar        :",harga)
    print(" Diskon       :", diskon)
    print(" Tagihan      : Rp.",semua)
    print(" Tanggal Masuk  : ", masuk)
    print(" Tanggal Diambil:", tanggal_saat_ini)
    print(" Uang         : Rp.",uang)
    print(" Kembalian    : Rp.",kembalian)
    print("===========================================")
    print("===========================================")
    break
