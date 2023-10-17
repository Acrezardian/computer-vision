# List dapat dibuat seperti membuat variabel biasa, namun nilai variabelnya di isi dengan tanda kurung siku []

# List nama-nama buah
buah = ["apel", "anggur", "mangga", "jeruk"]
# Misanya kita ingin mengambil mangga maka indeknya adalah 2
print (buah[2])

"""
Tedapat Tiga metode (method) atau fungsi yang bisa digunakan untuk menambahkan isi atau item ke List:
prepend(item)       : menambahkan item dari depan, jarang dipakai karena sering mengakibatkan error pada program
append(item)        : menambahkan item dari belakang.
insert(index, item) : menambahkan item dari indeks tertentu
"""

#list mula-mula
buah ["jeruk", "apel", "mangga", "duren"] 
# Tambahkan manggis 
buah.append("manggis")
print (buah)
﻿
#list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
buah.insert(2, "pepaya")
print(buah)

#list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
buah.remove("mangga")
print(buah)

# Index item list & extend
# list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"] 
buah.index("mangga")

# list mula-mula
buah1 = ["jeruk", "apel"] 
buah2 = ["mangga", "duren"]
# Add buah2 to buah1 
buah1.extend(buah2)
print (buah1)

# sum(), len(), min() and max() functions dari List
List = [1, 2, 3, 4, 5]
#sum
print("sum : " + str(sum(List)))
#min
print("min : " + str(min(List)))
#max
print("max : " + str(max(list)))
#Length
print("length : " + str(len(List)))
