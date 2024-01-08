print("----------------- Program Kasir Sederhana Radityatama Nugraha -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Baso - Rp 10000")
   print("3. Mie Ayam - Rp 20000")
   print("4. Soto Ayam - Rp 25000")
   print("5. Ayam Geprek - Rp 30000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*10000
       print (porsi," porsi Baso = Rp", totalmkn)
       mkn=("Baso")
   elif nomor==3:
       totalmkn=porsi*20000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   elif nomor==4:
       totalmkn=porsi*25000
       print (porsi, " porsi Soto Ayam = Rp", totalmkn)
       mkn=("Soto Ayam")
   elif nomor==5:
       totalmkn=porsi*30000
       print (porsi, " porsi Ayam Geprek = Rp", totalmkn)
       mkn=("Ayam Geprek")
    
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh manis - Rp 5000")
   print("2. Es jeruk - Rp 6000")
   print("3. Es lemon - Rp 7000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es teh manis = Rp", totalmnm)
       mnm=(" Gelas Es teh manis ")
   elif nomor==2:
       totalmnm=gelas*6000
       print (gelas, " Gelas Es jeruk = Rp", totalmnm)
       mnm=("Es jeruk")
   elif nomor==3:
       totalmnm=gelas*7000
       print (gelas, " Gelas Es lemon = Rp", totalmnm)
       mnm=("Es lemon")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   P E M B E L I A N =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")