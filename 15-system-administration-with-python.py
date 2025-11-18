import os
import subprocess
import time

os.system("ls -a")
# kita tambahkan delay n second untuk mengurangi efek async race
time.sleep(0.5)
print("==============")
subprocess.run(["ls", "-a"])
# capture_output
# python dapat menangkap std output dan std error

# text
# Python dapat secara otomatis melakukan decoding special karakter dari shell ke string

# Perbedaan os dan subprocess:
#     1. OS adalah cara lama untuk berkomunikasi python dengan shell host OS, 
#     digantikan oleh subprocess yang sudah disempurkan secara sistemik
#     2. OS berjalan async, 
#     jadi ketika kita menulis program di bawahnya, terkadang mengalami async race.
#     biasanya menambahkan temporary hold (delay) di baris setelah os di eksekusi
#     3. Subprocess bisa menangkap std error, sehingga handling error lebih mudah
#     4. Bisa melakukan decoding otomatis terhadap special character
    

