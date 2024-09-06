from flask import Flask, render_template, request
import random
from colorama import init

# Inisialisasi colorama (meskipun tidak akan digunakan di web, kita tetap inisialisasi jika ingin menambahkan output di console)
init(autoreset=True)

app = Flask(__name__)

# Fungsi untuk menghasilkan angka acak dan mengelompokkan
def generate_random_groups(total_numbers, num_groups, num_range):
    if total_numbers > num_range:
        raise ValueError("Total angka yang dihasilkan tidak boleh melebihi range angka yang ditentukan.")

    numbers = random.sample(range(1, num_range + 1), total_numbers)
    groups = [numbers[i::num_groups] for i in range(num_groups)]
    return groups

# Route untuk menampilkan form input
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk memproses hasil setelah form di-submit
@app.route('/result', methods=['POST'])
def result():
    try:
        total_numbers = int(request.form['total_numbers'])
        num_groups = int(request.form['num_groups'])
        num_range = int(request.form['num_range'])

        if total_numbers <= 0 or num_groups <= 0 or num_range <= 0:
            raise ValueError("Semua nilai input harus positif.")

        if total_numbers < num_groups:
            raise ValueError("Jumlah angka harus lebih besar atau sama dengan jumlah kelompok.")

        groups = generate_random_groups(total_numbers, num_groups, num_range)

        return render_template('result.html', groups=groups)

    except ValueError as e:
        return render_template('error.html', message=str(e))

if __name__ == "__main__":
    app.run(debug=True)
