#  Buatlah GUI dengan Tkinter yang berisi:
#     1 label judul Aplikasi prediksi Prodi Pilihan
#     10 input nilai mata pelajaran
#     1 button bertuliskan Hasil Prediksi
#      1 label luaran hasil produksi
#  Atur posisi GUI sebaik mungkin
#  Fungsi Hasil Prediksi menuliskan prodi Teknologi Informasi apapun input yang diberikan ().


from tkinter import *

def prediksi():
    # Fungsi ini selalu menampilkan "prodi Teknologi Informasi" apapun inputnya
    output_label.config(text="prodi Teknologi Informasi")

# Membuat window utama
root = Tk()
root.title("Aplikasi Prediksi Prodi")
root.geometry("400x500")  # Mengatur ukuran window agar rapi

# Label judul
judul_label = Label(root, text="Aplikasi prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat 10 input nilai mata pelajaran
entries = []
for i in range(10):
    label = Label(root, text=f"Nilai {i+1}:")
    label.grid(row=i+1, column=0, sticky="e", padx=10, pady=5)
    entry = Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries.append(entry)

# Button Hasil Prediksi
prediksi_button = Button(root, text="Hasil Prediksi", command=prediksi, font=("Arial", 12))
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label luaran hasil prediksi
output_label = Label(root, text="", font=("Arial", 12), fg="blue")
output_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
 