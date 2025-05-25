from gtts import gTTS
import streamlit as st
import time

# Menampilkan judul aplikasi Streamlit
st.title("⬆️ Sistem Antrian Pasien di RS Suka Sehat")

# Fungsi untuk generate TTS (Text-to-Speech) dan simpan ke file
def generate_tts(text, filename="antrian.mp3"):
    tts = gTTS(text, lang='id', slow=True)  # Mengubah teks menjadi suara bahasa Indonesia, dengan kecepatan lambat
    tts.save(filename)  # Menyimpan suara dalam file MP3 dengan nama default 'antrian.mp3'
    return filename  # Mengembalikan nama file yang telah disimpan

# Membuat session state untuk menyimpan antrian dan nomor antrian yang sedang dipanggil
if "queue" not in st.session_state:
    st.session_state.queue = []  # Jika belum ada antrian, buat list kosong
if "current" not in st.session_state:
    st.session_state.current = 0  # Jika belum ada nomor antrian yang dipanggil, set ke 0

# Membuat form input untuk memasukkan nomor antrian
with st.form("formclass Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_belakang(self, data):
        node_baru = Node(data)
        if not self.head:
            self.head = node_baru
        else:
            saat_ini = self.head
            while saat_ini.next:
                saat_ini = saat_ini.next
            saat_ini.next = node_baru
        print("To Do List berhasil ditambahkan di belakang!")

    def tambah_depan(self, data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru
        print("To Do List berhasil ditambahkan di depan!")

    def tampil_index(self, index):
        saat_ini = self.head
        i = 0
        while saat_ini:
            if i == index:
                print(f"Data pada index {index} adalah: {saat_ini.data}")
                return
            saat_ini = saat_ini.next
            i += 1
        print("Index tidak ditemukan!")

    def hapus_depan(self):
        if not self.head:
            print("List kosong!")
        else:
            print(f"List '{self.head.data}' dihapus dari depan")
            self.head = self.head.next

    def hapus_belakang(self):
        if not self.head:
            print("List kosong!")
        elif not self.head.next:
            print(f"List '{self.head.data}' dihapus dari belakang")
            self.head = None
        else:
            prev = None
            curr = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            print(f"List '{curr.data}' dihapus dari belakang")
            prev.next = None

    def hapus_index(self, index):
        if not self.head:
            print("List kosong!")
            return
        if index == 0:
            print(f"List '{self.head.data}' dihapus dari index 0")
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        i = 0
        while curr and i != index:
            prev = curr
            curr = curr.next
            i += 1
        if not curr:
            print("Index tidak ditemukan!")
        else:
            print(f"List '{curr.data}' dihapus dari index {index}")
            prev.next = curr.next

    def jumlah(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        print(f"Jumlah To Do List: {count}")

    def tampilkan(self):
        if not self.head:
            print("To Do List kosong.")
        else:
            curr = self.head
            i = 0
            while curr:
                print(f"[{i}] {curr.data}")
                curr = curr.next
                i += 1

def main():
    todo = LinkedList()

    while True:
        print("\n=== MENU TO DO LIST (Linked List) ===")
        print("1. Menambah List dari belakang")
        print("2. Menambah List dari depan")
        print("3. Menampilkan List berdasarkan index")
        print("4. Menghapus List dari depan")
        print("5. Menghapus List dari belakang")
        print("6. Menghapus List berdasarkan index")
        print("7. Mengecek jumlah To Do List")
        print("8. Tampilkan semua To Do List")
        print("9. Keluar")
        pilihan = input("Pilih menu (1-9): ")

        if pilihan == '1':
            data = input("Masukkan data To Do: ")
            todo.tambah_belakang(data)
        elif pilihan == '2':
            data = input("Masukkan data To Do: ")
            todo.tambah_depan(data)
        elif pilihan == '3':
            idx = int(input("Masukkan index yang ingin ditampilkan: "))
            todo.tampil_index(idx)
        elif pilihan == '4':
            todo.hapus_depan()
        elif pilihan == '5':
            todo.hapus_belakang()
        elif pilihan == '6':
            idx = int(input("Masukkan index yang ingin dihapus: "))
            todo.hapus_index(idx)
        elif pilihan == '7':
            todo.jumlah()
        elif pilihan == '8':
            todo.tampilkan()
        elif pilihan == '9':
            print("Terima kasih telah menggunakan To Do List!")
            break
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")

if __name__ == "__main__":
    main()
"):
    nomor = st.text_input("Masukan nomor antrian")  # Input teks untuk nomor antrian
    submit = st.form_submit_button("Tambah")  # Tombol untuk submit form
    if submit and nomor:
        st.session_state.queue.append(nomor)  # Menambahkan nomor antrian ke list antrian
        st.success(f"nomor antrian {nomor} sudah ditambahkan")  # Menampilkan pesan sukses setelah nomor ditambahkan

# Menampilkan daftar antrian
st.subheader("Daftar Antrian")
for i, n in enumerate(st.session_state.queue, 1):
    st.write(f"{i}. {n}")  # Menampilkan daftar nomor antrian yang ada

# Ketika tombol "Panggil Daftar Antrian" ditekan
if st.button("Panggil Daftar Antrian"):
    if st.session_state.queue:
        panggil = st.session_state.queue.pop(0)  # Mengambil nomor antrian pertama
        st.session_state.current += 1  # Meningkatkan nomor antrian yang sedang dipanggil
        teks = f"urutan antrian {st.session_state.current},untuk nomor antrian {panggil} silahkan ke loket 1"  # Teks yang akan dibaca
        st.success(teks)  # Menampilkan teks yang akan dibaca

        # Membuat file audio TTS dari teks
        filename = generate_tts(teks)
        
        # Membaca file audio "dingdong.mp3" dan file TTS
        audio_file = open(filename, "rb")
        audio_fileding = open("dingdong.mp3", "rb")
        audio_bytesding = audio_fileding.read()
        audio_bytes = audio_file.read()
        
        # Memutar suara 'dingdong.mp3'
        st.audio(audio_bytesding, format="audio/mp3", autoplay=True)
        
        # Memberikan delay selama 3 detik agar suara 'dingdong' selesai dulu
        time.sleep(3)
        
        # Memutar suara TTS setelah delay
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    else:
        st.warning("Tidak ada antrian")  # Jika tidak ada antrian dalam daftar
