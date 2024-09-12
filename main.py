print ("")
print ("=====================================")
print ("Aplikasi Pembagi Kelompok Secara Acak (GRATIS) - Dibuat dengan PYTHON")
print ("=====================================")
print ("")
print ("Deskripsi:")
print ("   Aplikasi ini berfungsi untuk mengelompokkan nomor presensi siswa secara acak dan merata sesuai dengan jumlah pembagian kelompok yang dikehendaki tanpa terduplikasi, dan jika ada siswa yang ingin dihilangkan atau tidak ingin dimasukkan ke dalam pembagian kelompok ini, maka hal ini juga bisa dilakukan dengan cara mengisikan nomor-nomor presensi yang ingin dihilangkan.")
print ("")
print ("Cara pakai:") 
print ("   1. Masukkan jumlah siswa yang ingin dimasukkan dalam pembagian kelompok ini, lalu klik Enter / GO")
print ("   2. Anda ingin membaginya menjadi berapa kelompok? Masukkan angkanya, lalu klik Enter / GO")
print ("   3. Masukkan jumlah total siswa dalam 1 kelas sesuai daftar presensi, lalu klik Enter / GO")
print ("   4. a. Nomor presensi yang ingin dihilangkan, silakan diisi disini, dipisahkan dengan tanda koma (contoh: 3,15,27 dst), lalu klik Enter / GO")
print ("   4. b. Atau tekan Enter / GO langsung tanpa mengisi, jika tidak ada nomor presensi yang harus dihilangkan")
print ("   5. Apabila aplikasi berhenti / error / ingin mengulang, silakan klik tombol 'Run' di atas. ")
print ("")
print ("Hasilnya / Outputnya: Pembagian Kelompok akan ditampilkan secara acak, merata, dan tidak terduplikasi")
print ("")
print ("=========================================")
print ("Jika mengalami error atau ada pertanyaan, silakan hubungi nomor WA 085641051211 (Dimas BN / Azhiro)")
print ("=========================================")
print ("")
import random

def generate_random_groups(total_numbers, num_groups, num_range, excluded_numbers):
    if total_numbers > num_range - len(excluded_numbers):
        raise ValueError("Jumlah siswa yang ingin dibagi tidak dapat melebihi total siswa yang tersedia setelah penghilangan nomor.")

    # Hapus angka yang dikecualikan dari range
    available_numbers = [i for i in range(1, num_range + 1) if i not in excluded_numbers]
    
    # Pilih angka acak dari angka yang tersedia
    numbers = random.sample(available_numbers, total_numbers)

    # Bagi angka menjadi kelompok
    groups = [numbers[i::num_groups] for i in range(num_groups)]
    return groups

def main():
    try:
        # Input dari pengguna
        total_numbers = int(input("Masukkan jumlah siswa yang ingin dimasukkan dalam pembagian kelompok ini: "))
        num_groups = int(input("Anda ingin membaginya menjadi berapa kelompok? Masukkan angkanya: "))
        num_range = int(input("Masukkan jumlah total siswa dalam 1 kelas sesuai daftar presensi: "))

        # Input angka yang dikecualikan
        excluded_input = input("Masukkan nomor presensi yang ingin dihilangkan, jika lebih dari 1, bisa dipisahkan dengan koma (contoh: 3,15,27); Atau tekan Enter / GO langsung, untuk melanjutkan tanpa menghilangkan nomor: ")
        
        # Memproses angka yang dikecualikan menjadi list integer
        if excluded_input.strip():
            excluded_numbers = list(map(int, excluded_input.split(',')))
        else:
            excluded_numbers = []

        # Validasi input
        if total_numbers <= 0 or num_groups <= 0 or num_range <= 0:
            raise ValueError("Semua input nomor harus bernilai positif.")

        if total_numbers < num_groups:
            raise ValueError("Jumlah total siswa harus lebih besar atau sama dengan jumlah kelompok.")

        # Generate dan tampilkan kelompok angka
        groups = generate_random_groups(total_numbers, num_groups, num_range, excluded_numbers)

        print("\nHasil Pembagian Kelompok Secara Acak:")
        for i, group in enumerate(groups):
            print(f"Kelompok {i + 1}: {group}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()