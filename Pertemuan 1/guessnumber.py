import random

def tebak(x):
    angka = random.randint(1,x)
    tebak = 0
    while tebak != angka:
        tebak = int(input(f"Tebak Angka Antara 1 sampai {x} \n"))
        if tebak <= angka:
            print("Terlalu rendah, Silahkan Coba lagi")
        elif tebak >= angka:
            print("Terlalu tinggi, silahkan coba lagi\n")
        else:
            print("Selamat Kamu Benar!\n")
tebak(10)