name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input(
    "kamu tersesat di jalan, dan kamu di beri pilihan untuk menentukan nya, pilih arah nya (kanan/kiri) ? ")

if answer == "kiri":
    answer = input(
         "kamu bisa berjalan di sekitar atau berenang mengelilingi? ketik berjalan untuk berjalan-jalan dan berenang ke berenang menyebrang(berenang/berjalan/tidak ada pilihan) : ")
    
    if answer == "berenang":
        print("kamu berenang menyebrang dan dimakan oleh buaya jahat. ")
    elif answer == "berjalan":
        print("kamu berjalan sejauh beberapa km, kehabisan air dan kamu kehilangan di game itu. ")
    else:
        print('tidak ada pilihan yang valid. kamu kalah. ')

elif answer == "kanan":
    answer = input(
        "kamu datang ke jembatan, kelihatan goyah, kamu ingin menyebranginya atau kembali (menyebrangi/kembali)? ")
    
    if answer == "kembali":
        print("kamu kembali atau kalah. ")
    elif answer == "menyeberang":
        answer = input(
            "kamu menyebrang di jembatan itu dan jumpa seseorang orang asing. apakah kamu berbicara dengan dia (iya/tidak)? ")
        
        if answer == "iya":
            print("kamu berbicara dengan orang asing dan memberi mu emas. kamu MENANG!")
        elif answer == "tidak":
            print("kamu abaikan orang asing itu dan dia tersinggung dan kamu kalah.")
        else:
            print('tidak ada pilihan yang valid. kamu kalah')
    else:
        print('tidak ada pilihan yang valid, kamu kalah, ')

else:
    print('tidak ada pilihan yang valid')

print("terima kasih telah mencoba", name)
