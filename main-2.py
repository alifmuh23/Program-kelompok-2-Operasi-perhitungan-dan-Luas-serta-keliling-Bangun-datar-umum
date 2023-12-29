import numpy as np
import math
import os , sys

#Rumus
def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def pangkat(a,b):
    return a**b

def bagi(a,b):
    if b != 0:
        return a/b
    else:
        return "Angka tidak bisa dibagi boleh 0"
    
def akar(a):
    if a != 0:
      return np.sqrt(a)
    else:
        return " Bilangan kompleks"

def persen(a,b):
    return (a/b)*100
    
def logaritma(x):
    return math.log(x)

def logaritmab10(x):
    return math.log10(x)

def log_dengan_basis(x,y):
    return math.log(x,y)

def luasLingkaran(r):
    luas = math.pi*r**2
    return luas

def kelilingLingkaran(r):
    return 2*math.pi*r

def luasPersegi(s):
    return s*s

def kelilingPersegi(s):
    return s*4

def luasPersegiPanjang(p,l):
    return p*l

def kelilingPersegiPanjang(p,l):
    return 2*(p+l)

def luasSegitigaSS(a,t):
    return 1/2*(a*t)

def kelilingSegitigaSS(a,b,c):
    return a+b+c

def main():
    os.system("cls")
    while True:
        print("-"*47)
        print("|"+"Selamat datang di Perhitungan sederhana ".center(45)+"|")
        print("-"*47)
        print("|"+"1."+"|"+"Perhitungan Sederhana"+"|".rjust(22))
        print("|"+"2."+"|"+"Akar Dan Logaritma"+"|".rjust(25))
        print("|"+"3."+"|"+"Menghitung luas dan keliling bangun datar"+"|".rjust(2))
        print("|"+"4."+"|"+"Exit"+"|".rjust(39))
        print("-"*47)

        pilih = int(input("\nMasukkan pilihan Anda (1/2/3/4): "))

        if pilih == 1:
            os.system("cls")
            print("-"*47)
            print("|"+"Perhitungan Sederhana"+"|".rjust(25))
            print("-"*47)
            print("|"+"1."+"|"+"Tambah"+"|".rjust(37))
            print("|"+"2."+"|"+"Kurang"+"|".rjust(37))
            print("|"+"3."+"|"+"Kali"+"|".rjust(39)) 
            print("|"+"4."+"|"+"Bagi"+"|".rjust(39))       
            print("|"+"5."+"|"+"Pangkat"+"|".rjust(36))
            print("|"+"6."+"|"+"Persen"+"|".rjust(37))
            print("|"+"0."+"|"+"Kembali"+"|".rjust(36))
            print("-"*47)
                
            pilihan = int(input("Masukkan pilihan Anda(1/2/3/4/5/6/0) : "))
            if pilihan == 1:
                print("Perhitungan Tambah")
                angka1 = float(input("Masukkan angka pertama : "))
                angka2 = float(input("Masukkan angka kedua : "))
                hasil = tambah(angka1,angka2)
                print("Hasil : ",hasil)
                
            elif pilihan == 2:
                print("Perhitungan Kurang")
                angka1 = float(input("Masukkan angka pertama : "))
                angka2 = float(input("Masukkan angka kedua : "))
                hasil = kurang(angka1,angka2)
                print("Hasil : ",hasil)
                
            elif pilihan == 3:
                print("Perhitungan Kali")
                angka1 = float(input("Masukkan angka pertama : "))
                angka2 = float(input("Masukkan angka kedua sebagai pengali: "))
                hasil = kali(angka1,angka2)
                print("Hasil : ",hasil)
                
            elif pilihan == 4:
                angka1 = float(input("Masukkan angka : "))
                angka2 = float(input("Masukkan pembagi angka : "))
                hasil = bagi(angka1,angka2)
                print("Hasil : ",hasil)
                
            elif pilihan == 5:
                angka1 = float(input("Masukkan angka yang ingin di pangkatkanfd: "))
                angka2 = float(input("Masukan pangkat : "))
                hasil = pangkat(angka1,angka2)
                print("Hasil : ",hasil)
             
            elif pilihan == 6:
                angka1 = float(input("Masukkan Angka yang ingin di persekan: "))
                angka2 = float(input("Masukkan persen: "))
                hasil = persen(angka1,angka2)
                print(f"Hasil dari {angka1} di persenkan {angka2}:{hasil:2f}")

            elif pilihan == 0:
                continue
                
            kembali_ke_menu = input("Kembali ke menu utama? (y/n) : ")
            if kembali_ke_menu != "y":
                break

            else:
                print("Masukkan angka yg benar..")
            os.system("cls")
        
        elif pilih == 2:
            os.system("cls")
            print("-"*47)
            print("|"+" Akar dan Logaritma"+"|".rjust(27))
            print("-"*47)         
            print("|"+"1."+"|"+"Akar"+"|".rjust(39))        
            print("|"+"2."+"|"+"Logaritma Natural"+"|".rjust(26)) 
            print("|"+"3."+"|"+"Logaritma Basis10"+"|".rjust(26))
            print("|"+"4."+"|"+"Logaritma dengan Basis"+"|".rjust(21))
            print("|"+"0."+"|"+"Kembali"+"|".rjust(36))
            print("-"*47)       
            
            pilihan = int(input("\nMasukkan Pilihan Anda (1/2/3/4/0) : "))
            if pilihan == 1:
                angka = float(input("Akar dari : "))
                hasil = akar(angka)
                print(f"hasil : {hasil:.2f}")
            elif pilihan == 2:
                angka = float(input("log dari : "))
                hasil = logaritma(angka)
                print(f"hasil : {hasil:.2f}")
            elif pilihan == 3:
                angka = float(input("log10 dari : "))
                hasil = logaritmab10(angka)
                print(f"hasil : {hasil:.2f}")
            elif pilihan == 4:
                angka1 = float(input("log : "))
                angka2 = float(input("Dengan Basis : "))
                hasil = log_dengan_basis(angka1,angka2)
                print(f"hasil : {hasil:.2f}")
            elif pilihan == 0:
                continue
            else:
                print("Masukkan angka yg benar..")
            
            kembali_ke_menu = input("Kembali ke menu utama? (y/n) : ")
            if kembali_ke_menu != "y":
                break
            os.system("cls")

        elif pilih == 3:
            os.system("cls")
            print("-"*47)
            print("|"+"Menghitung luas dan keliling bangun datar cm"+"|".rjust(2))
            print("-"*47)
            print("|"+"1."+"|"+"Luas Lingkaran"+"|".rjust(29))
            print("|"+"2."+"|"+"Keliling Lingkaran"+"|".rjust(25))
            print("|"+"3."+"|"+"Luas Persegi"+"|".rjust(31))
            print("|"+"4."+"|"+"Keliling Persegi"+"|".rjust(27))       
            print("|"+"5."+"|"+"Luas Persegi Panjang"+"|".rjust(23))
            print("|"+"6."+"|"+"Keliling Persegi Panjang"+"|".rjust(19))
            print("|"+"7."+"|"+"Luas Segitiga"+"|".rjust(30))
            print("|"+"8."+"|"+"Keliling Segitiga"+"|".rjust(26))
            print("|"+"0."+"|"+"Kembali"+"|".rjust(36))
            print("-"*47)

            pilihan = int(input("\nMasukkan Pilihan Anda (1/2/3/4/5/6/7/8/0) : "))
            if pilihan == 1:
                print("Luas Lingkaran")
                jari_jari = float(input("masukkan jari2 lingkaran : "))
                hasil = luasLingkaran(jari_jari)
                print(f"luas lingkaran : {hasil:.2f} cm**2")
            elif pilihan == 2:
                print("Keliling Lingkaran")
                jari_jari = float(input("masukkan jari2 lingkaran : "))
                hasil = kelilingLingkaran(jari_jari)
                print(f"keliling lingkaran : {hasil:.2f} cm")
            elif pilihan == 3:
                print("Luas Persegi")
                sisi = float(input("masukkan sisi persegi : "))
                hasil = luasPersegi(sisi)
                print(f"luas persegi : {hasil:.2f} cm**2")
            elif pilihan == 4:
                print("Keliling Persegi")
                sisi = float(input("masukkan sisi persegi : "))
                hasil = kelilingPersegi(sisi)
                print(f"Keliling Persegi : {hasil:.2f} cm")
            elif pilihan == 5:
                print("Luas Persegi Panjang dalam cm") 
                panjang = float(input("masukkan panjang persegi : "))
                lebar = float(input("masukkan lebar persegi : "))
                hasil = luasPersegiPanjang(panjang,lebar)
                print(f"Luas Persegi Panjang : {hasil:.2f} cm**2")
            elif pilihan == 6:
                print("Keliling Persegi Panjang") 
                panjang = float(input("masukkan panjang persegi : "))
                lebar = float(input("masukkan lebar persegi : "))
                hasil = kelilingPersegiPanjang(panjang,lebar)
                print(f"Keliling Persegi Panjang : {hasil:.2f} cm")
            elif pilihan == 7:
                print("Luas Segitiga ") 
                alas = float(input("masukkan alas segitiga : "))
                tinggi = float(input("masukkan tinggi segitiga: "))
                hasil = luasSegitigaSS(alas,tinggi)
                print(f"Luas Segitiga  : {hasil:.2f} cm**2")
            elif pilihan == 8:
                print("Keliling Segitiga ") 
                sisi1 = float(input("masukkan panjang sisi 1 : "))
                sisi2 = float(input("masukkan panjang sisi 2 : "))
                sisi3 = float(input("masukkan panjang sisi 3 : "))
                hasil = kelilingSegitigaSS(sisi1,sisi2,sisi3)
                print(f"Keliling Segitiga  : {hasil:.2f} cm")
            elif pilihan == 0:
                continue
            else:
                print("Masukkan angka yg benar..")
            
            kembali_ke_menu = input(" Kembali ke menu utama? (y/n) : ")
            if kembali_ke_menu != "y":
                break
            os.system("cls")

        elif pilih == 4:
            print("Terima kasih Telah menggunakan Program Kami :) ")
            sys.exit()

        else:
            os.system("cls")
            print("masukkssan pilihan yg benar")


main()