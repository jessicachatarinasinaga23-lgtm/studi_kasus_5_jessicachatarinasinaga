def hitung_biaya_parkir(jenis_kendaraan, jam_masuk, jam_keluar):

    lama_parkir = jam_keluar - jam_masuk

    if lama_parkir < 0:
        lama_parkir += 24

    jenis_kendaraan = jenis_kendaraan.lower()
    if jenis_kendaraan == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan == "motor":
        tarif_per_jam = 3000
    else:
        return "Jenis kendaraan tidak valid!"

    if lama_parkir == 0:
        lama_parkir = 1

    total_biaya = lama_parkir * tarif_per_jam

    return lama_parkir, total_biaya

kendaraan = "Motor"
masuk = 7 
keluar = 16

durasi, total = hitung_biaya_parkir(kendaraan, masuk, keluar)

print(" STRUK BIAYA PARKIR ")
print(f"Jenis Kendaraan : {kendaraan}")
print(f"Jam Masuk       : {masuk}:00")
print(f"Jam Keluar      : {keluar}:00")
print(f"Lama Parkir     : {durasi} jam")
print(f"Total Biaya     : Rp{total:,}")