# Mengambil module random
import random

# membuat fungsi charlie
def charlie():
    pretanyaan = ""
    jawaban = ""
    pilihan = ["Yes","No","Maybe"]
    # Kunci untuk bermain
    main = 1
    while main == 1:
        pertanyaan = str(input("Apa Yang Ingin Kamu Tanyakan ?\n"))
        jawaban = random.choice(pilihan)
        main = int(input("Tekan 1 Jika Ingin Bertanya Lagi = "))
    print("Good Bye")

charlie()

