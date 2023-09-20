# input

diskon = int(input("berapa diskonnya = "))
harga = int(input("berapa harganya = "))

harga_diskon = (diskon / 100) * harga

harga_akhir = harga - harga_diskon

print("Harga yang harus dibayar adalah Rp.", harga_akhir)

