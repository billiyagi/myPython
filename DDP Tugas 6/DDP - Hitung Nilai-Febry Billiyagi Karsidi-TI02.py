# Program Penghitung Nilai
# Febry Billiyagi Karsidi - TI02

name = input("Nama: ")
grade = input("Kelas (rombel cth: TI02): ")
score = int(input("Nilai: "))
ket_score = ''

if (score <= 100) and (score >= 90):
    ket_score = "Istimewa"
elif (score <= 89) and (score >= 70):
    ket_score = "Sangat bagus"
elif (score <= 69) and (score >= 60):
    ket_score = "Cukup"
elif score < 60:
    ket_score = "Gagal"
else :
    ket_score = "Angka tidak termasuk ke dalam nilai, mohon coba lagi"

print('================================')
print('name     : ' + name, '\n', 'Kelas     : ' + grade, '\n', 'Nilai      : ' + str(score), '\n', 'Ket        : ' + ket_score)
print('================================')