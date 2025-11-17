# Composite data type: Bisa menyimpan banyak nilai dalam satu variable
# Contoh composite data type: List, Tuple, Dictionary

# 1. List
# List can store multiple value with mixed-various data type. Mutable
myList = ["Jeruk", "Anggur", "Mangga", 50]
print(type(myList))
print(myList) # Memanggil semua nilai
print(myList[1]) # Memanggil anggur
myList[0] = "Jeruk Bali" # Mutating member value
print(myList)

print("====")
# 2. Tuple
# Similar with List but immutable
myTuple = ("Jeruk", "Anggur", "Mangga", 50)
print(type(myTuple))
print(myTuple)
print(myTuple[1])
# myTuple[0] = "Jeruk Bali" # Mutating member value. Error! Cannot mutating
# print(myTuple)


print("====")
# 3. Dictionary
# Similar with list, but we can custom the index. We call it "Key".
myDictionary = {
    "buah1": "Jeruk",
    "buah2": "Anggur",
    "buah3": "Mangga",
    "harga": 50
}
print(type(myDictionary))
print(myDictionary)
print(myDictionary["buah2"])
myDictionary["buah1"] = "Jeruk Bali"
print(myDictionary)




# ===========
# Challenge
# ===========
# 1. Misalkan saya punya list myList = ["python","php","javascript","c#","golang"]
# dengan menggunakan 1 notasi index (satu kotak), panggil C# dan golang sekaligus
myList = ["python","php","javascript","c#","golang"]
# Cara Start : Stop index
print(myList[3:5]) # Approved!
print(myList[3:]) # Approved!
print(myList[-2:]) # Approved!


# 2. Misalkan saya punya complex dictionary.
# myComplexDict = {
#     "nama": "Abdul Basri",
#     "alamat": {
#         "kota": "Jakarta Barat",
#         "provinsi": "DKI Jakarta"
#     }
# }
# Bagiamana saya membuat kalimat "Abdul Basri, Alamat: Jakarta Barat, DKI Jakarta".
# Manfaatkan print() untuk menyelesaikan task ini.

myComplexDict = {
    "nama": "Abdul Basri",
    "alamat": {
        "kota": "Jakarta Barat",
        "provinsi": "DKI Jakarta",
        "desa": {
            "rt": "01",
            "rw": "02",
            "nama": "Tanjung Barat"
        }
    },
    "anak": ["Andi", "Putri", "Rizky"]
}

# Panggil Rizky
print(myComplexDict["anak"][2])

# panggil desa
print(myComplexDict["alamat"]["desa"]["nama"])

print(myComplexDict["nama"],", Alamat: ",myComplexDict["alamat"]["kota"],", ",myComplexDict["alamat"]["provinsi"])
print(myComplexDict['nama'] + ', Alamat: ' +  myComplexDict['alamat']['kota'] + ', ' + myComplexDict['alamat']['provinsi'])
print(f"{myComplexDict['nama']}, Alamat: {myComplexDict['alamat']['kota']}, {myComplexDict['alamat']['provinsi']}")
print("{}. Alamat: {}, {}".format(
    myComplexDict['nama'],
    myComplexDict['alamat']['kota'],
    myComplexDict['alamat']['provinsi']
    ))
 