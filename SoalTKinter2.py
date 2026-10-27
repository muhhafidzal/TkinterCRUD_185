import sqlite3
import tkinter as tk
import tkinter.messagebox as msg

def create_db():
    conn = sqlite3.connect("Nilai_Siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT NOT NULL,
        biologi INTEGER NOT NULL,
        fisika INTEGER NOT NULL,
        inggris INTEGER NOT NULL,
        prediksi_fakultas TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def predict(biologi, fisika, inggris):
    if inggris > biologi and inggris > fisika:
        return "Bahasa"
    elif biologi > inggris and biologi > fisika:
        return "Kedokteran"
    elif fisika > inggris and fisika > biologi:
        return "Teknik"
    else:
        return "mending nggak usah sekolah"

def simpan_data(nama, biologi, fisika, inggris, prediksi):
    conn = sqlite3.connect("Nilai_Siswa.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) "
        "VALUES (?, ?, ?, ?, ?)",
        (nama, biologi, fisika, inggris, prediksi))
    conn.commit()
    conn.close()

def submit():
    nama = E_nama.get().strip()
    biologi = E_biologi.get().strip()
    fisika = E_fisika.get().strip()
    inggris = E_inggris.get().strip()
    if not nama or not biologi or not fisika or not inggris:
        msg.showwarning("Data kurang", "Semua kolom harus diisi.")
        return
    if not (biologi.isdigit() and fisika.isdigit() and inggris.isdigit()):
        msg.showwarning("Nilai salah", "Nilai harus berupa angka.")
        return
    biologi = int(biologi)
    fisika = int(fisika)
    inggris = int(inggris)

    hasil = predict(biologi, fisika, inggris)
    simpan_data(nama, biologi, fisika, inggris, hasil)
    var.set("Prediksi Fakultas: " + hasil)
    msg.showinfo("Berhasil", "Data " + nama + " tersimpan.")

    E_nama.delete(0, tk.END)
    E_biologi.delete(0, tk.END)
    E_fisika.delete(0, tk.END)
    E_inggris.delete(0, tk.END)

create_db()

root = tk.Tk()
root.title("Prediksi Fakultas")
tk.Label(root, text="Aplikasi Prediksi Fakultas").pack()

tk.Label(root, text="Nama Siswa").pack()
E_nama = tk.Entry(root, bd=5)
E_nama.pack()

tk.Label(root, text="Nilai Biologi").pack()
E_biologi = tk.Entry(root, bd=5)
E_biologi.pack()

tk.Label(root, text="Nilai Fisika").pack()
E_fisika = tk.Entry(root, bd=5)
E_fisika.pack()

tk.Label(root, text="Nilai Inggris").pack()
E_inggris = tk.Entry(root, bd=5)
E_inggris.pack()

tk.Button(root, text="Submit", command=submit).pack()

var = tk.StringVar()
tk.Label(root, textvariable=var, relief=tk.RAISED).pack()

root.mainloop()