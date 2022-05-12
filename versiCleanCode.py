
# konstanta = 7
# modulus = 13
# bilanganAwal = 5
# bilanganSaatIni = (konstanta * bilanganAwal) % modulus

# for count in range(1,6):
#     bilanganSaatIni = (konstanta * bilanganAwal) % modulus
#     uniform = bilanganSaatIni / modulus

#     print(f"{bilanganSaatIni} \t\t {uniform}")

# konstanta = 7
# modulus = 13
# bilanganAwal = 5

# bilanganSaatIni = (konstanta * bilanganAwal) % modulus

# for count in range(1,6):
#     bilanganSaatIni = (konstanta * bilanganSaatIni) % modulus
#     uniform = bilanganSaatIni / modulus

#     print(f"{bilanganSaatIni} \t\t {uniform}")

def membangkitkanBilanganAcak(konstanta,modulus,bilanganAwal):

    # perhitungan membangkitkan bilangan acak
    
    hasil = (konstanta * bilanganAwal) % modulus

    for count in range(1,6):
        hasil = (konstanta * hasil) % modulus
        uniform = hasil / modulus

        print(f"{bilanganSaatIni} \t\t {uniform}")

    
membangkitkanBilanganAcak(7,13,5)
membangkitkanBilanganAcak(6,13,5)