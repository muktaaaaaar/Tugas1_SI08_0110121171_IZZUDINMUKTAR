# Nama      : izzudin muktar
# NIM       : 0110121171
# Kelas     : SI08
# Matkul    : DDP

def Valid_email():
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input('Masukkan Email: ')
    if (re.fullmatch(regex, email)): 
        return True
    else:
        print('Email tidak valid. Cobalagi.')
        return Valid_email() 


def Valid_password():
    character = ['@', "#", '$', '!'] 
    password = input("Masukkan password: ")
    if len(password) >= 8: 
        if any(word.isnumeric() for word in password): 
            if any(word.islower() for word in password): 
                if any(word.isupper() for word in password): 
                    if any(word in character for word in password): 
                        return True 
                    else:
                        print("Password tidak valid. Cobalagi.")
                        return Valid_password() 
                else:
                    print("Password tidak valid. Cobalagi.")       
                    return Valid_password() 
            else:
                print("Password tidak valid. Cobalagi.")  
                return Valid_password() 
        else:
            print("Password tidak valid. Cobalagi.")
            return Valid_password() 
    else:
        print("Password tidak valid. Cobalagi.")
        return Valid_password() 


def Valid_player():
    diskon = 0
    peringkat = input("Masukkan peringkat kepersertaan Anda (Silver/Gold/Diamond): ")
    while peringkat != 'Silver' and peringkat != 'Gold' and peringkat != 'Diamond': 
        print("Masukkan tidak valid. Cobalagi.") 
        return Valid_player()
    else:
        if peringkat == 'Silver':
            if barang < 5:
                diskon = REGO* (5/100) 
                print('Selamat! Anda mendapatkan potongan harga 5%') 
            else:
                diskon = REGO* (10/100) 
                print('Selamat! Anda mendapat potongan harga 10%') 
        elif peringkat == 'Gold':
            if barang < 5:
                diskon = REGO* (10/100) 
                print('Selamat! Anda mendapat potongan harga 10%') 
            else:
                diskon = REGO* (15/100) 
                print('Selamat! Anda mendapat potongan harga 15%') 
        elif peringkat == 'Diamond':
            if barang < 5:
                diskon = REGO* (15/100) 
                print('Selamat! Anda mendapat potongan harga 15%') 
            else:
                diskon = REGO* (20/100) 
                print('Selamat! Anda mendapat potongan harga 20%') 
        setelah_diskon = REGO- diskon 
        print('Total Harga yang harus dibayar: ', float(setelah_diskon)) 
        print("Terima kasih telah berbelanja di Toko serba ada kami!")
        print('\n') 
        quit()      
    
print('\n')
barang = 0
Total_harga = 0 
print('Fitur Belanja')
print()
while True:
    Produk = input('Masukkan nama produk yang akan dibeli atau X untuk selesai: ')
    while Produk == "": 
        Produk = input("Tidak valid. Masukkan produk: ") 
    if Produk == 'X' or Produk == 'x':
        if barang > 0: 
            print()
            print('Total produk yang dibeli: ' + str(barang)) 
            print('Total harga produk: ', float(Total_harga)) 
            print()
            Anggota = input('Apakah Anda seorang anggota? (Y/T): ')
            if Anggota == 'T' or Anggota == "t": 
                print('Total harga yang harus dibayar: ', float(Total_harga)) 
                print("Terima kasih telah berbelanja di toko serba ada Kami!") 
                print('\n')
                quit()
            elif Anggota == 'Y' or Anggota == 'y':
                Valid_email() 
                while True: 
                    if Valid_password(): 
                        Valid_player() 
                    else:
                        Valid_password() 
            else:
                quit() 
        elif Produk == "X" or Produk == "x" and barang == 0: 
            print("Terima kasih telah berkunjung di toko Kami. Sampai jumpa!") 
            print('\n')
            quit() 
    else: 
        REGO= int(input('Masukkan harga produk: ')) 
        print('Berhasil menambahkan', Produk, 'dengan harga', float(REGO))
        barang += 1 
        Total_harga += REGO