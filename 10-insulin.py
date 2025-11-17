# # Task 1
# cleaning prepoinsulin-seq.txt dengan cara menghilangkan spasi nya. 
# Pastikan hasil akhir ada 110 karakter

# # Task 2
# pisahkan karakter yang dihasilkan oleh task 1, dengan ketentuan sebagai berikut:
# 1. lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.
# 2. binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.
# 3. cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.
# 4. ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.

# tempatkan semua hasil (file 1-4 di folder result)
import os

# 1. Read file and remove spaces
with open("preproinsulin-seq.txt", "r") as f:
    seq = f.read().replace(" ", "").replace("\n", "").lower()

# Create result folder if not found
result_dir = "result"
os.makedirs(result_dir, exist_ok=True)

# Helper function to save a segment and verify length
def save_segment(filename, segment, expected_len):
    path = os.path.join(result_dir, filename)
    with open(path, "w") as f:
        f.write(segment)
    print(f"{filename}: length = {len(segment)} (expected {expected_len})")

# 2. Extract required segments
lsinsulin = seq[0:24]      # amino acids 1–24
binsulin = seq[24:54]      # amino acids 25–54
cinsulin = seq[54:89]      # amino acids 55–89
ainsulin = seq[89:110]     # amino acids 90–110

# 3. Save files
save_segment("lsinsulin-seq-clean.txt", lsinsulin, 24)
save_segment("binsulin-seq-clean.txt", binsulin, 30)
save_segment("cinsulin-seq-clean.txt", cinsulin, 35)
save_segment("ainsulin-seq-clean.txt", ainsulin, 21)