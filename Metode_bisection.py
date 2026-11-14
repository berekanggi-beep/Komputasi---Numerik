 ==============================================
 Metode Bisection - Komputasi Numerik
 Mencari Akar Persamaan Non Linear
==============================================

import math

 Definisikan fungsi f(x) yang akan dicari akarnya
def f(x):
    return math.exp(-x) - x   f(x) = e^(-x) - x

 Fungsi Metode Bisection
def bisection(a, b, toleransi):
    print("=" * 60)
    print(f"Mencari akar di selang [{a}, {b}] dengan toleransi {toleransi}")
    print("=" * 60)
    print(f"{'Iterasi':<10} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<12}")
    print("-" * 60)
    
    iterasi = 0
    while (b - a) / 2 > toleransi:
        c = (a + b) / 2
        iterasi += 1
        fc = f(c)
        
        print(f"{iterasi:<10} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<12.6f}")
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    akar = (a + b) / 2
    print("=" * 60)
    print(f" Akar persamaan adalah: x = {akar:.6f}")
    return akar

 ==============================================
Jalankan Program
 ==============================================
if __name__ == "__main__":
    a_awal = 0       Batas bawah
    b_awal = 1       Batas atas
    tol = 0.01      Toleransi kesalahan
    
    hasil = bisection(a_awal, b_awal, tol)
