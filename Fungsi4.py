#fungsi untuk menghitung jumlah angka yang dapat dibagi pemisah
def jumlahan_angka(angka, pemisah):
    jumlah = 0
    for bilangan in angka:
        if bilangan % pemisah == 0:
            jumlah += bilangan
    return jumlah

# Contoh penggunaan fungsi dengan list angka dan angka pemisah yang berbeda
angka_1 = [1, 76, 7, 861, 88]
pemisah_1 = 2
hasil_1 = jumlahan_angka(angka_1, pemisah_1)
print(f"Jumlah angka dalam daftar yang dapat dibagi habis oleh {pemisah_1} adalah {hasil_1}")

angka_2 = [76, 89, 80, 65, 7, 5, 105]
pemisah_2 = 5
hasil_2 = jumlahan_angka(angka_2, pemisah_2)
print(f"Jumlah angka dalam daftar yang dapat dibagi habis oleh {pemisah_2} adalah {hasil_2}")
