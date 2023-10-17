# pembuatan dan print element pada dictionary
Training = {
  "hardware": "Raspberry Pi", 
  "software": "Python",
  "topic": "Image Processing", 
  "year": 2019
}
print(Training)
#print element in dictionary 
print("Hardware: " + Training["hardware"])

# Mengubah element dalam dictionary
Training["year"] = 2020
print("Year: " + str(Training["year"]))
Year: 2020

# Iterating dictionary
for item in Training: 
  print (item)

# Mengecek key, length, dan menambahkan item dalam dictionary
# mengecek jika Key telah ada
if "topic" in Training:
  print("terdapat key 'topic' pada dictionary Training");

#Dictionary Length 
print(len(Training))

#add item to dictionary 
Training["level"] = "basic"
print (Training)
