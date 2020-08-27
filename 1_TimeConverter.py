x = int(input("Masukkan detik (s): "))  # x adalah variabel untuk input nilai dalam satuan seconds
def TimeConverter(x):                   # define sebuah function dgn nama TimeConverter, dengan parameter x
    import math                         # karena akan menggunakan fungsi matematika
    if type(x) != int:                  # kalau tidak bertipe integer, outputnya akan "INVALID INPUT"
        print("Invalid Input !")
    else :
        if x >= 360000:                 # untuk membatasi agar x yang dimasukkan tidak besar dari 360000, kalau lebih besar dari 360000 output akan "INVALID INPUT"
            print("Invalid Input")
        elif x < 0 :
            print("Invalid Input")      # x juga tidak bisa kecil dari 0, kalai kecil dari 0 output akan "INVALID INPUT"
        else :
            HH = math.floor(x/3600)             #untuk mendapatkan nilai HH(jam), dilakukan pembulatan kebawah dari hasil bagi x dengan 3600
            MM = math.floor((x-(HH*3600))/60)   #untuk mendapatkan nilai MM(menit), input dikurangin terhadap HH dikalikan 6, kemudian di bagi 60 agar mendapat nilai MM, kemudian dibulatkan kebawah 
            SS = x-(HH*3600)-(MM*60)            #untuk mendapatkan nilai SS(detik),x akan dikurangi dengan MM dikalikan 60 dan HH dikalikan 3600.
            if HH < 10 and  MM < 10 and SS <10 : 
                print(f"0{HH}:0{MM}:0{SS}")
            elif HH < 10 and MM >=10 and SS <10:
                print(f"0{HH}:{MM}:0{SS}")
            elif HH < 10 and MM < 10 and SS >=10:
                print(f"0{HH}:0{MM}:{SS}")
            elif HH >= 10 and MM < 10 and SS <10:
                print(f"{HH}:0{MM}:0{SS}")
            elif HH >= 10 and MM >= 10 and SS<10:
                print(f"{HH}:{MM}:0{SS}")
            elif HH >= 10 and MM < 10 and SS>=10:
                print(f"{HH}:0{MM}:{SS}")
            elif HH < 10 and MM >= 10 and SS>=10: # semua ini kondisi agar apabila, hasil HH atau MM atau SS nya kecil dari 10, maka akan ada angka 0, agar menjadi 2 digit(cth = 09 :06 :04, bukan malah 9:6:4)
                print(f"0{HH}:{MM}:{SS}")
            else :
                print(f"{HH}:{MM}:{SS}") # HH atau MM atau SS besar sama dengan 10, akan di print biasa
TimeConverter(x)   # menjalankan fungsi TimeConverter
