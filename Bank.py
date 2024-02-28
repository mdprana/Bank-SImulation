from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem Manajemen Bank")
        self.master.geometry("800x650")
        self.users = {}

        # Tambahkan label untuk menampilkan gambar
        self.image = Image.open("image\logo.png")
        self.image = self.image.resize((110, 100))  # Sesuaikan ukuran gambar
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.master, image=self.photo)
        self.image_label.pack()

        # Tambah label untuk pesan selamat datang
        self.welcome_label = Label(self.master, text="SELAMAT DATANG DI BANK INFORMATIKA UDAYANA", font=("Arial", 14, "bold"), pady=10)
        self.welcome_label.pack()   

        # Buat Frame Pembuatan Akun
        self.frame_buat_akun = Frame(self.master)
        self.frame_buat_akun.pack()
        self.label_nama = Label(self.frame_buat_akun, text="Nama:")
        self.label_nama.grid(row=0, column=0, padx=10, pady=10,)
        self.entry_nama = Entry(self.frame_buat_akun)
        self.entry_nama.grid(row=0, column=1, padx=10, pady=10)
        self.label_umur = Label(self.frame_buat_akun, text="Umur:")
        self.label_umur.grid(row=1, column=0, padx=10, pady=10)
        self.entry_umur = Entry(self.frame_buat_akun)
        self.entry_umur.grid(row=1, column=1, padx=10, pady=10)
        self.label_pendapatan = Label(self.frame_buat_akun, text="Pendapatan:")
        self.label_pendapatan.grid(row=2, column=0, padx=10, pady=10)
        self.entry_pendapatan = Entry(self.frame_buat_akun)
        self.entry_pendapatan.grid(row=2, column=1, padx=10, pady=10)
        self.label_pin = Label(self.frame_buat_akun, text="PIN:")
        self.label_pin.grid(row=3, column=0, padx=10, pady=10)
        self.entry_pin = Entry(self.frame_buat_akun, show="*")
        self.entry_pin.grid(row=3, column=1, padx=10, pady=10)
        self.tombol_buat_akun = Button(self.frame_buat_akun, text="Buat Akun", command=self.buat_akun)
        self.tombol_buat_akun.grid(row=4, column=1, padx=10, pady=10) 

        # Frame Login
        self.frame_login = Frame(self.master, bg="#FFFFFF")
        self.frame_login.pack(pady=20, anchor=CENTER)
        self.label_login_nama = Label(self.frame_login, text="Nama:", font=("Arial", 14), bg="#FFFFFF")
        self.label_login_nama.grid(row=0, column=0, padx=10, pady=10)
        self.entry_login_nama = Entry(self.frame_login, width=30, font=("Arial", 14))
        self.entry_login_nama.grid(row=0, column=1, padx=10, pady=10)
        self.label_login_pin = Label(self.frame_login, text="PIN:", font=("Arial", 14), bg="#FFFFFF")
        self.label_login_pin.grid(row=1, column=0, padx=10, pady=10)
        self.entry_login_pin = Entry(self.frame_login, show="*", width=30, font=("Arial", 14))
        self.entry_login_pin.grid(row=1, column=1, padx=10, pady=10)
        self.tombol_login = Button(self.frame_login, text="Login", command=self.login, font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF', activebackground='#2E8B57', activeforeground='#FFFFFF', relief='raised', borderwidth=0)
        self.tombol_login.grid(row=2, column=1, padx=10, pady=10)
        self.master.bind('<Return>', self.login) # Membolehkan login dengan tombol "Enter" 

        # Frame Detail Pengguna
        self.frame_detail_pengguna = Frame(self.master)

        # Label       
        label_style = {"fg": "green", "font": ("Arial", 14)}
        self.label2_nama = Label(self.frame_detail_pengguna, text="Nama:", **label_style)
        self.label2_nama.grid(row=0, column=1, padx=10, pady=10)
        self.label2_umur = Label(self.frame_detail_pengguna, text="Umur:", **label_style)
        self.label2_umur.grid(row=1, column=1, padx=10, pady=10)
        self.label2_pendapatan = Label(self.frame_detail_pengguna, text="Pendapatan:", **label_style)
        self.label2_pendapatan.grid(row=2, column=1, padx=10, pady=10)
        self.label_saldo_anda = Label(self.frame_detail_pengguna, text="Saldo:", **label_style)
        self.label_saldo_anda.grid(row=3, column=1, padx=10, pady=10)

        # Tombol
        self.tombol_riwayat_transaksi = Button(self.frame_detail_pengguna, text="Riwayat Transaksi", command=self.lihat_riwayat_transaksi, bg="green", fg="white")
        self.tombol_riwayat_transaksi.grid(row=10, column=0, padx=10, pady=20)
        self.tombol_setor_tunai = Button(self.frame_detail_pengguna, text="Setor Tunai", command=self.setor_tunai, bg="yellow", fg="black")
        self.tombol_setor_tunai.grid(row=10, column=1, padx=10, pady=20)
        self.tombol_tarik_tunai = Button(self.frame_detail_pengguna, text="Tarik Tunai", command=self.tarik_tunai, bg="orange", fg="white")
        self.tombol_tarik_tunai.grid(row=10, column=2, padx=10, pady=20)
        self.tombol_logout = Button(self.frame_detail_pengguna, text="Logout", command=self.logout, bg="red", fg="white")
        self.tombol_logout.grid(row=10, column=3, padx=10, pady=20)

        # Inisialisasi data pengguna
        self.nama = ""
        self.umur = ""
        self.pendapatan = ""
        self.pin = ""
        self.saldo_anda = 0
        self.riwayat_transaksi = []

        # Flag untuk melacak visibilitas kata sandi
        self.tampilkan_PIN = False
        self.tombol_tampilkan_PIN = Button(self.frame_login, text="Tampilkan PIN", command=self.sembunyikan_tampilkan_pin)
        self.tombol_tampilkan_PIN.grid(row=1, column=2, padx=10, pady=10)

    # Fungsi untuk membuat akun    
    def buat_akun(self):
        # Input User
        nama = self.entry_nama.get()
        umur = self.entry_umur.get()
        pendapatan = self.entry_pendapatan.get()
        pin = self.entry_pin.get()
        
        # Variabel untuk menyimpan data pengguna
        user_data = {'nama': nama, 'umur': umur, 'pendapatan': pendapatan, 'pin': pin, 'saldo': 0}

        # Menambahkan user ke dalam variabel user_data
        self.users[pin] = user_data
        
        # Validasi input
        if not nama or not umur or not pendapatan or not pin:
            messagebox.showerror("Error", "Semua kolom harus diisi!")
            return
        if not umur.isdigit():
            messagebox.showerror("Error", "Umur harus angka!")
            return
        if not pendapatan.isdigit():
            messagebox.showerror("Error", "Pendapatan harus angka!")
            return
        if not pin.isdigit() or len(pin) != 6:
            messagebox.showerror("Error", "PIN harus terdiri dari 6-digit angka!")
            return
        
        # Menghilangkan text selamat datang setelah login/buat akun
        self.welcome_label.pack_forget()

        # Menyimpan user data
        self.nama = nama
        self.umur = umur
        self.pendapatan = pendapatan
        self.pin = pin
        self.saldo_anda = 0
        self.riwayat_transaksi = []
        
        # Menghilangkan text pada kolom inputan setealah login/buat akun
        self.entry_nama.delete(0, END)
        self.entry_umur.delete(0, END)
        self.entry_pendapatan.delete(0, END)
        self.entry_pin.delete(0, END)
        
        # Menampilkan detail pengguna setelah login/buat akun
        self.label2_nama.config(text="Nama: " + self.nama)
        self.label2_umur.config(text="Umur: " + self.umur)
        self.label2_pendapatan.config(text="Pendapatan: " + self.pendapatan)
        self.label_saldo_anda.config(text="Saldo saat ini: " + str(self.saldo_anda))
        
        # Menampilkan frame detail pengguna
        self.frame_buat_akun.pack_forget()
        self.frame_login.pack_forget()
        self.frame_detail_pengguna.pack()

        # Memanggil tombol cari
        self.tombol_cari()

    # Fungsi untuk login
    def login(self, event=None):
        # Mengambil nama user dan pin dari inputan
        name = self.entry_login_nama.get()
        pin = self.entry_login_pin.get()

        # Mengecek apakah user ada di dalam variabel self.users diatas dan mengecek apakah pin benar
        if name in [user_data['nama'] for user_data in self.users.values()]:
            correct_pin = [user_data['pin'] for user_data in self.users.values() if user_data['nama'] == name][0]
            if pin == correct_pin:

                # Mengatur user data saat ini ke dalam variabel user data
                self.user_data_saat_ini = [user_data for user_data in self.users.values() if user_data['nama'] == name][0]

                # Menampilkan frame detail pengguna dan memperbarui label
                self.frame_detail_pengguna.pack(pady=20)
                self.label2_nama['text'] = f"Nama: {self.user_data_saat_ini['nama']}"
                self.label2_umur['text'] = f"Umur: {self.user_data_saat_ini['umur']}"
                self.label2_pendapatan['text'] = f"Pendapatan: {self.user_data_saat_ini['pendapatan']}"
                self.label_saldo_anda['text'] = f"Saldo Anda: {self.user_data_saat_ini['saldo']}"   

                # Menghilangkan frame login, buat akun, dan pesan selamat datang setelah login
                self.frame_login.pack_forget()
                self.frame_buat_akun.pack_forget()
                self.welcome_label.pack_forget()
            else:
                # Menampilkan pesan error jika PIN salah
                messagebox.showerror("Error", "Username atau PIN salah!")
        else:
            # Menampilkan pesan error jika Username salah atau tidak ada
            messagebox.showerror("Error", "Username atau PIN salah!")
    
    # Fungsi untuk menampilkan atau menyembunyikan PIN
    def sembunyikan_tampilkan_pin(self):
        if self.tampilkan_PIN:
            self.entry_login_pin.config(show="*")
            self.tampilkan_PIN = False
            self.tombol_tampilkan_PIN.config(text="Tampilkan PIN")
        else:
            self.entry_login_pin.config(show="")
            self.tampilkan_PIN = True
            self.tombol_tampilkan_PIN.config(text="Sembunyikan PIN")
    
    # Fungsi untuk melakukan setor tunai
    def setor_tunai(self):
        # Input user
        pin = simpledialog.askstring("Setor Tunai", "Masukkan PIN:")
        
        # Validasi input PIN
        if not pin:
            return
        if pin not in self.users:
            messagebox.showerror("Error", "PIN Invalid!")
            return

        # Konfirmasi PIN yang dimasukkan sesuai dengan PIN pada data pengguna
        if pin == self.users[pin]['pin']:
            # Jika PIN sesuai, lanjutkan dengan proses setor tunai
            jumlah = simpledialog.askstring("Setor Tunai", "Masukkan Jumlah:")
            if not jumlah or not jumlah.isdigit() or int(jumlah) <= 0:
                messagebox.showerror("Error", "Input Invalid!")
                return

        # Menambahkan jumlah ke saldo kita
        self.users[pin]['saldo'] += int(jumlah)

        # Memperbarui label saldo kita
        self.label_saldo_anda.config(text="Saldo saat ini: " + str(self.users[pin]['saldo']))

        # Menambahkan transaksi ke riwayat transaksi
        transaksi = "Setor Tunai: +" + jumlah + ", Saldo Terbaru: " + str(self.users[pin]['saldo'])
        self.riwayat_transaksi.append(transaksi)
        self.users[pin]['transaksis'] = self.riwayat_transaksi

    # Fungsi untuk melakukan tarik tunai
    def tarik_tunai(self):
        # Input user
        pin = simpledialog.askstring("Tarik Tunai", "Masukkan PIN Anda:")
        
        # Validasi input PIN
        if not pin:
            return
        if pin not in self.users:
            messagebox.showerror("Error", "PIN Invalid!")
            return

        # Konfirmasi PIN yang dimasukkan sesuai dengan PIN pada data pengguna
        if pin == self.users[pin]['pin']:
            # Jika PIN sesuai, lanjutkan dengan proses penarikan tunai
            jumlah = simpledialog.askstring("Tarik Tunai", "Masukkan jumlah:")
            if not jumlah or not jumlah.isdigit() or int(jumlah) <= 0:
                messagebox.showerror("Error", "Jumlah Invalid!")
                return
                
            saldo_anda = self.users[pin]['saldo']
            if int(jumlah) > saldo_anda:
                messagebox.showerror("Error", "Saldo tidak mencukupi!")
                return
        
        # Mengurangkan jumlah saldo yang ingin ditarik dari saldo kita
        saldo_anda -= int(jumlah)
        self.users[pin]['saldo'] = saldo_anda

        # Memperbarui label saldo yang kita miliki
        self.label_saldo_anda.config(text="Saldo saat ini: " + str(saldo_anda))

        # Menambahkan transaksi ke riwayat transaksi
        transaksi = "Tarik Tunai: -" + jumlah + ", Saldo Terbaru: " + str(saldo_anda)
        self.riwayat_transaksi.append(transaksi)
        self.users[pin]['transaksis'] = self.riwayat_transaksi

    # Fungsi untuk melihat riwayat transaksi
    def lihat_riwayat_transaksi(self):
        # Membuat window riwayat transaksi
        riwayat_tranasaksi_window = Toplevel(self.master)
        riwayat_tranasaksi_window.title("Riwayat Transaksi")

        # Mengambil PIN pengguna saat ini
        pin = self.entry_login_pin.get()

        # Tambahkan transaksi pengguna ke riwayat transaksi
        if pin in self.users:
            self.users[pin]['transaksis'].extend(self.riwayat_transaksi)

        # Mengatur ukuran window dan posisi agar pas ditengah saat terbuka
        window_width = 400
        window_height = 350
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        riwayat_tranasaksi_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Membuat frame riwayat transaksi
        riwayat_tranasaksi_frame = Frame(riwayat_tranasaksi_window)
        riwayat_tranasaksi_frame.pack(padx=10, pady=10)

        # Membuat label riwayat transaksi
        riwayat_tranasaksi_label = Label(riwayat_tranasaksi_frame, text="Riwayat Transaksi:")
        riwayat_tranasaksi_label.grid(row=0, column=0, padx=10, pady=10)

        # Membuat kotak list untuk riwayat transaksi
        riwayat_tranasaksi_listbox = Listbox(riwayat_tranasaksi_frame, width=50)
        riwayat_tranasaksi_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Ambil dan masukkan semua transaksi ke dalam kotak list riwayat transaksi
        if pin in self.users:
            for transaksi in self.users[pin]['transaksis']:
                riwayat_tranasaksi_listbox.insert(END, transaksi)
        else:
            # Masukkan transaksi kedalam kotak list riwayat transaksi
            for transaksi in self.riwayat_transaksi:
                riwayat_tranasaksi_listbox.insert(END, transaksi)

    # Fungsi untuk logout
    def logout(self):
        # Tampilkan kembali label "Selamat Datang" dan gambar logo setelah logout
        self.image_label.pack()
        self.welcome_label.pack()

        # Mereset kembali user data
        self.nama = ""
        self.umur = ""
        self.pendapatan = ""
        self.pin = ""
        self.saldo_anda = 0
        self.riwayat_transaksi = []

        # Mereset kolom inputan nama
        self.entry_login_nama.delete(0, END)
        
        # Mereset kolom inputan PIN
        self.entry_login_pin.delete(0, END)

        # Menampilkan frame login
        self.frame_detail_pengguna.pack_forget()
        self.frame_buat_akun.pack(pady=20)
        self.frame_login.pack()

    # Algoritma Searching
    def jump_search(self, target_umur):
        # Mengurutkan user data berdasarkan umur
        sorted_users = sorted(self.users.values(), key=lambda x: int(x['umur']) if x['umur'].isdigit() else 0)

        # Mulai melakukan jump search
        block_size = int(len(sorted_users) ** 0.5)
        prev = 0
        while int(sorted_users[min(block_size, len(sorted_users)) - 1]['umur']) < target_umur:
            prev = block_size
            block_size += int(len(sorted_users) ** 0.5)
            if prev >= len(sorted_users):
                return None  # Pengguna tidak ditemukan

        # Mulai melakukan linear search di dalam block yang ditemukan
        for i in range(prev, min(block_size, len(sorted_users))):
            if sorted_users[i]['umur'] == str(target_umur):
                return sorted_users[i]  # Pengguna ditemukan

        return None  # Pengguna tidak ditemukan
    
    # Fungsi untuk mencari user bedasarkan umur
    def cari_berdasarkan_umur(self, umur_untuk_dicari, window_umur):
        # Mengecek apakah inputan sesuai
        if not umur_untuk_dicari.isdigit():
            messagebox.showerror("Error", "Masukkan umur yang sesuai!")
            return

        # Mengkonversi input ke dalam bentuk integer
        umur_untuk_dicari = int(umur_untuk_dicari)

        # Memanggil algoritma jump search untuk mencari user berdasarkan umur
        hasil = self.jump_search(umur_untuk_dicari)
        if hasil:
            # Jika pengguna ditemukan, tampilkan detial user berupa nama dan umur
            messagebox.showinfo("Hasil Pencarian", f"Pengguna ditemukan:\n\n Nama: {hasil['nama']}\n Umur: {hasil['umur']}")
        else:
            messagebox.showinfo("Hasil Pencarian", f"Tidak ada pengguna dengan umur {umur_untuk_dicari}.")

        # Meutup window inputan umur setelah mencari
        window_umur.destroy()

    # Fungsi untuk menampilkan tombol cari setelah 1 akun dibuat dan log out
    def tombol_cari(self):
        # Buat tombol untuk memicu fungsi pencarian berdasarkan umur
        search_button = Button(self.frame_buat_akun, text="Cari Berdasarkan Umur", command=self.buka_window_baru_untuk_input_umur)
        search_button.grid(row=5, column=1, padx=10, pady=10)

    # Fungsi untuk membuka window baru untuk menginputkan pencarian berdasarkan umur
    def buka_window_baru_untuk_input_umur(self):
        # Menentukan lebar window
        window_width = 300
        # Membuat window baru untuk menginputkan umur
        window_umur = Toplevel(self.master)
        window_umur.title("Cari Berdasarkan Umur")

        # Mengatur ukuran window dan posisi agar saat dibuka pas ditengah-tengah layar
        window_height = 100
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        window_umur.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Membuat label dan masukan untuk input umur
        label_umur = Label(window_umur, text="Masukkan umur:")
        label_umur.pack()
        entry_umur = Entry(window_umur)
        entry_umur.pack()

        # Membuat tombol untuk melakukan pencarian
        search_button = Button(window_umur, text="Cari", command=lambda: self.cari_berdasarkan_umur(entry_umur.get(), window_umur))
        search_button.pack()

def main():
    # Buat objek Tk
    root = Tk()

    # Buat sebuah representasi dari kelas BankSystem
    bank_system = BankSystem(root)

    # Mengatur ukuran dan posisi window agar saat dibuka pas ditengah layar
    window_width = 800
    window_height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Hitung koordinat x dan y
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    # Mengatur ukuran window dan posisikan di koordinat yang dihitung
    root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
    root.title("Sistem Managemen Bank")

    # Start
    root.mainloop()

if __name__ == '__main__':
    main()