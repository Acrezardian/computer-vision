# contoh penulisan yang salah
if lulus == "tidak"
print ("Kamu harus ikut remidi")

# contoh penulisan yang benar
if lulus == "tidak"
   print ("Kamu harus ikut remidi")

# Memahami percabangan untuk membuat logika program
# IF
﻿lulus = input("Apakah kamu lulus? [ya/tidak] : ")
if lulus == "tidak":
   print("Kamu harus ikut ujian")

# IF ELSE
umur = int(input("Berapa umur kamu: "))
if umur >= 18:
   print("Kamu boleh membuat SIM")
else:
   print("Kamu belum boleh membuat SIM")
  
# Nested IF
nilai = int(input("Inputkan nilaimu: "))
if nilai >= 90: 
   grade = "A"
elif nilai >= 80: 
   grade = "B+"
elif nilai >= 70: 
   grade = "B"
elif nilai >= 60: 
   grade = "C+"
elif nilai >= 50: 
   grade = "C"
elif nilai >= 40:
   grade "D"
else:
   grade = "E"
print("Grade: %s" % grade)
