from collections import Counter

# 1. Meminta input dari pengguna
input_teks = input("Masukkan angka (pisahkan dengan spasi, contoh: 10 20 20 30 10 5): ")

# 2. Konversi input teks menjadi daftar angka
data = []
for x in input_teks.split():
    num = float(x)
    # Konversi ke int jika angka bulat agar tampilan lebih rapi (misal: 10 bukan 10.0)
    data.append(int(num) if num.is_integer() else num)

if data:
    # 3. Perhitungan statistik dasar
    total = sum(data)
    jumlah_data = len(data)
    rata_rata = total / jumlah_data
    
    # 4. Hitung frekuensi kemunculan setiap angka
    frekuensi = Counter(data)
    
    # Filter angka yang muncul lebih dari 1 kali (duplikat)
    duplikat = {angka: jumlah for angka, jumlah in frekuensi.items() if jumlah > 1}

    # 5. Menampilkan hasil
    print("\n" + "="*45)
    print("          HASIL PERHITUNGAN DATA           ")
    print("="*45)
    print(f"Data Input      : {data}")
    print(f"Banyak Data     : {jumlah_data}")
    print(f"Total           : {total}")
    print(f"Rata-rata       : {rata_rata:.2f}")
    print(f"Nilai Tertinggi : {max(data)}")
    print(f"Nilai Terendah  : {min(data)}")
    print("-" * 45)
    print("ANALISIS DATA GANDA (DUPLIKAT):")
    if duplikat:
        print(f"Jumlah jenis angka duplikat : {len(duplikat)} angka")
        for angka, jumlah in duplikat.items():
            print(f"  • Angka {angka} muncul sebanyak {jumlah} kali")
    else:
        print("  • Tidak ada data yang sama (semua angka unik).")
    print("="*45)
else:
    print("Tidak ada data yang dimasukkan.")