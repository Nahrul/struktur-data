import streamlit as st 
from ptmn3 import dataMhs

# Membuat Judul Web app
st.title("👩‍🎓Manajelem Data Mahasiswa👨‍🎓")

# menambah data mahasiswa 
st.subheader("➕  Tambah Data Mahasiswa")
new_nama = st.text_input("Masukan Nama Mahasiswa")
new_nim = st.text_input("Masukan NIM Mahasiswa")
new_prodi = st.text_input("Masukan Prodi Mahasiswa")
if st.button("Tambahkan Data"):
    dataMhs.append({"nama":new_nama, "NIM":new_nim, "Prodi":new_prodi})
    st.success("✅Data Berhasil Ditambahkan!")
   

# menampilkan data mahasiswa 
st.subheader("📚Data Mahasiswa📚")
no=0
for i in dataMhs:
    no=no+1
    st.write(f"{no}.Nama = {i['nama']} NIM = {i['NIM']}Prodi = {i['Prodi']}")
