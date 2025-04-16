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
with st.form("form"):
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
